from .json_detector import detect_json

class ConvertFromJson:
    def __init__(self, text):
        self.text = text
        self.json_objects = detect_json(text)
        
    def split_text(self):
        ## Splits the text into a list of strings delimited by the JSON objects
        split_text = []
        if self.json_objects == None:
            return [self.text]
        for i in range(len(self.json_objects)):
            split_text.append(self.text[self.json_objects[i]['start']:self.json_objects[i]['end']])
        return split_text
        
    def json_to_yaml(self, json_object):
        ## Converts a JSON object to a YAML object
        if isinstance(json_object, dict):
            yaml_object = ''
            for key in json_object:
                yaml_object += f'{key}: {json_object[key]}\n'
            return yaml_object
        elif isinstance(json_object, list):
            yaml_object = ''
            for item in json_object:
                yaml_object += f'- {item}\n'
            return yaml_object
        else:
            return None

    def convert(self):
        ## Replaces the JSON strings in the text with YAML objects in markdown code blocks.
        if self.json_objects == None:
          return self.text
        split_text = self.split_text()
        converted_text = ''
        for i in range(len(split_text)):
            ## if there are code block delimiters (either with hint of "json" or no hint) on the lines before and after the JSON object, we remove them
            if i > 0 and i < len(self.json_objects):
                if split_text[i-1].strip() == '```json' and split_text[i+1].strip() == '```':
                    converted_text += f'{split_text[i-1]}\n'
                    converted_text += f'{split_text[i+1]}\n'
                    continue
                elif split_text[i-1][-1] != '\n' or split_text[i+1][0] != '\n':
                    converted_text += '\n'
            if i < len(self.json_objects):
                converted_text += f'```yaml\n{self.json_to_yaml(self.json_objects[i]["json_object"])}\n```\n'
            converted_text += split_text[i]

                  
        return self.text