import pytest
import json

@pytest.fixture
def fixture_data():
    with open('jamall/fixtures/test_object.json') as f:
        return json.load(f)

@pytest.fixture
def fixture_text():
    with open('jamall/fixtures/complex.md') as f:
        return f.read()

def test_detect_json(fixture_text):
    from jamall.json_detector import detect_json
    detected_json = detect_json(fixture_text)
    print(json.dumps(detected_json, indent=4))
    assert len(detected_json) == 4
    assert detected_json[0]['start'] == 73
    assert fixture_text[73] == '{'
    assert detected_json[0]['end'] == 365
    assert fixture_text[365] == '}'
    
def test_get_json_if_present(fixture_data):
    from jamall.json_detector import get_json_if_present
    assert get_json_if_present(json.dumps(fixture_data)) == fixture_data
    assert get_json_if_present('{"key": "value"}') == {"key": "value"}
    assert get_json_if_present('["item1", "item2"]') == ["item1", "item2"]
    assert get_json_if_present('{"key": "value"') == None
    assert get_json_if_present('{"key": "value"}garbage') == None
    assert get_json_if_present('garbage{"key": "value"}') == None
    assert get_json_if_present('garbage') == None
    assert get_json_if_present('') == None
    assert get_json_if_present('0') == None
    assert get_json_if_present('0.0') == None
    assert get_json_if_present('0.0e10') == None
    assert get_json_if_present('0.0e-10') == None
    assert get_json_if_present('0.0e+10') == None
    assert get_json_if_present('0.0e10garbage') == None
    assert get_json_if_present('0.0e-10garbage') == None
    assert get_json_if_present('0.0e+10garbage') == None
    assert get_json_if_present('0garbage') == None
    assert get_json_if_present('0.0garbage') == None
    assert get_json_if_present('0.0e10garbage') == None
    assert get_json_if_present('0.0e-10garbage') == None
    assert get_json_if_present('0.0e+10garbage') == None
    assert get_json_if_present('0.0e10') == None
    assert get_json_if_present('0.0e-10') == None
    assert get_json_if_present('0.0e+10') == None
    assert get_json_if_present('0') == None
    assert get_json_if_present('0.0') == None
    assert get_json_if_present('0.0e10') == None
    assert get_json_if_present('0.0e-10') == None
    assert get_json_if_present('0.0e+10') == None