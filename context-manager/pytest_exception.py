import pytest as pytest

if __name__ == '__main__':
    with pytest.raises(ValueError):
        int('hello')