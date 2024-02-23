from typing import List, TypedDict, Union
import json
from typing import Union

class JsonMatch(TypedDict):
    start: int
    end: int
    json_object: Union[dict, list]

def get_json_if_present(text):
    # Helper function to check if a block of text is a valid JSON object
    
    try:
        result = json.loads(text)
        if (isinstance(result, dict) or isinstance(result, list)):
            return result if isinstance(result, list) and len(result) > 0 else result
        else:
            return None
    except:
        return None
    

def detect_json(text: str) -> Union[List[JsonMatch], None]:
    # Detects if the text contains a JSON object
    
    length = len(text)
    if length < 2:
        return None
    if get_json_if_present(text):
        # The entire text is a JSON object
        return json.loads(text)
    else:
        # The text contains a JSON object
        matches = []
        for i in range(length):
            if text[i] not in ['{', '['] or text[i-1] == '\\':
                continue
            open_bracket = text[i]
            close_bracket = ']' if open_bracket == '[' else '}'
            count = 1
            for j in range(i+1, length):
                if text[j] == open_bracket and text[j-1] != '\\':
                    count += 1
                elif text[j] == close_bracket and text[j-1] != '\\':
                    count -= 1
                if count == 0:
                    block = text[i:j+1]
                    if get_json_if_present(block):
                        matches.append({
                            'start': i,
                            'end': j+1,
                            'json_object': json.loads(block)
                        })
                    i = j
                    break
        return matches
