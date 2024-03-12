import pytest
import json
from jamall.convert_from_json import ConvertFromJson

@pytest.fixture
def fixture_data():
    with open('jamall/fixtures/test_object.json') as f:
        return json.load(f)

@pytest.fixture
def fixture_text():
    with open('jamall/fixtures/complex.md') as f:
        return f.read()

@pytest.fixture
def fixture_result():
    with open('jamall/fixtures/complex_yaml.md') as f:
        return f.read()
    
def test_convert_from_json(fixture_result, fixture_text):
    converter = ConvertFromJson.from_text(fixture_text)
    assert str(converter) == fixture_result
