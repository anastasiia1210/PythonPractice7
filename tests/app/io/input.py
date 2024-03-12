import pytest
from app.io.input import read_file, read_file_pandas

text = "here is some text"


def test_read_file():
    result = read_file()
    assert isinstance(result, str)
    assert result != ''
    assert result == text


def test_read_file_pandas():
    result = read_file_pandas()
    assert isinstance(result, str)
    assert result != ''
    assert result == text
