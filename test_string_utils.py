import pytest
from string_utils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

def test_capitalize_positive(string_utils):
    assert string_utils.capitalize("skypro") == "Skypro"

def test_trim_positive(string_utils):
    assert string_utils.trim("   skypro") == "skypro"

def test_to_list_positive(string_utils):
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]

def test_contains_positive(string_utils):
    assert string_utils.contains("SkyPro", "S") is True

def test_delete_symbol_positive(string_utils):
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"

def test_starts_with_positive(string_utils):
    assert string_utils.starts_with("SkyPro", "S") is True

def test_end_with_positive(string_utils):
    assert string_utils.end


# негативные сценарии 

def test_to_list_negative(string_utils):
    with pytest.raises(TypeError):
        string_utils.to_list(123)

def test_contains_negative(string_utils):
    assert not string_utils.contains("SkyPro", "X")

def test_delete_symbol_negative(string_utils):
    with pytest.raises(TypeError):
        string_utils.delete_symbol(123, "k")
        
        
def test_end_with_negative(string_utils):
    assert string_utils.end
