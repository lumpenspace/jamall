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
            if len(result) == 0 or \
                isinstance(result, list) and len(result) == 1 and isinstance(result[0], int):
                return None
            return result
        else:
            return None
    except:
        return None
    

def detect_json(text: str) -> List[JsonMatch]:
    # Detects if the text contains a JSON object
    
    length = len(text)
    if length < 2:
        return None
    if result := get_json_if_present(text):
        # The entire text is a JSON object
        return [{
            'start': 0,
            'end': len(text),
            'json_object': result
        }]
    else:
        # The text contains a JSON object
        matches = []
        in_string = False
        i = 0
        while i < length - 1:
            if (text[i] == '"' and text[i-1] != '\\'):
                in_string = not in_string

            if (text[i] not in ['{', '[']) or in_string:
                i += 1
                next

            open_bracket = text[i]
            close_bracket = ']' if open_bracket == '[' else '}'
            count = 1
            if open_bracket == '[':
                print('found array')
    
            for j in range(i+1, length):
                if (text[j] == '"' and text[j-1] != '\\'):
                    in_string = not in_string
                if text[j] == open_bracket and text[j-1] != '\\' and not in_string:
                    count += 1
                elif text[j] == close_bracket and text[j-1] != '\\' and not in_string:
                    count -= 1
                if count == 0:
                    block = text[i:j+1]
                    result = get_json_if_present(block)
                    if result:
                        matches.append({
                            'start': i,
                            'end': j,
                            'json_object': result
                        })
                        i = j
                    break
            i += 1
        if len(matches) == 0:
            return None
        return matches
