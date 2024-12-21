import re
from src.main import GetRandomName, GetEpochBasedHash, left, right

def test_random_name():
    name = GetRandomName(left, right)
    assert len(name.split("_")) == 3
    assert re.match(r"[a-z]+_[a-z]+_[a-zA-Z0-9]{4}", name)

def test_epoch_hash():
    epoch_hash = GetEpochBasedHash()
    assert len(epoch_hash) == 32
