import json
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def saved_list(path: Path):
    l = []
    yield l

    with open(path, "wt") as f:
        json.dump(l, f)

path = Path("d:/tmp.json")

with saved_list(path) as my_list:
    assert my_list == []
    my_list.append(1)
    my_list.append(2)

with open(path, "rt") as f:
    assert json.load(f) == [1, 2]
