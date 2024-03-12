from typing import Union
from pydantic import BaseModel, Field
import yaml
from jamall.json_detector import detect_json

code_block_end = '```'
code_block_start_options = ('```json','```')

def strip_code_block_delimiters(text: str) -> str:
    lines = text.split('\n')
    firstline = text.split('\n')[0]
    lastline = text.split('\n')[-1]
    if firstline.strip() == code_block_end:
        lines = lines[1:]
    if lastline in code_block_start_options:
        lines = lines[:-1]
    return '\n'.join(lines)


class ConvertFromJson(BaseModel):
    original: str = Field(alias='original')
    json_objects: Union[list, None] = Field(default=None, frozen=True)
    converted: Union[str, None] = Field(default=None)

    @classmethod
    def from_text(cls, text: str):
        json_objects = detect_json(text)
        instance = cls(original=text, json_objects=json_objects)
        instance.convert()
        return instance

    @property
    def original(self) -> str:
        return self.original

    def __str__(self) -> Union[str, None]:
        return self.converted
  
    def __repr__(self) -> str:
        return f'ConvertFromJson.from_text(text={self.original})'
    
    @property
    def objects(self) -> Union[list, None]:
        return self.json_objects


    def split_text(self):
        split_text = []
        if self.json_objects == None:
            return [self.original]

        for i in range(len(self.json_objects)):
            if i == 0:
                split_text.append(self.original[:self.json_objects[i]['start']-1].strip())
            elif i < len(self.json_objects) - 1:
                split_text.append(self.original[self.json_objects[i]['end']+1:self.json_objects[i+1]['start']-1].strip())
        split_text.append(self.original[self.json_objects[-1]['end']+1:])

        return split_text
    
    def __json_to_yaml(self, json_object):
        ## Converts a JSON object to a YAML object
        return yaml.dump(json_object, default_flow_style=False, allow_unicode=True)

    
    def __get_yaml_code_block(self, json_object):
        ## Returns a YAML object in a markdown code block
        yaml_object = self.__json_to_yaml(json_object)
        return f'\n```yaml\n{yaml_object}```\n'


    def convert(self) -> str:
        ## Replaces the JSON strings in the text with YAML objects in markdown code blocks.
        if self.json_objects == None:
            return self.original
        split_text = self.split_text()

        converted_text = ''
        for i in range(len(self.json_objects)):
            converted_text += strip_code_block_delimiters(split_text[i])
            json_object = self.json_objects[i]['json_object']
            converted_text += self.__get_yaml_code_block(json_object)
        converted_text += split_text[-1]
        self.converted = converted_text
        return converted_text
    
    
    