import pytest

from activity.main import *

def test_exception():
    bag = {
        "glasses": 1,
        "pens": 2,
        "wallet": 1
        }
    
    with pytest.raises(KeyError):
        key_lookup("key", bag)