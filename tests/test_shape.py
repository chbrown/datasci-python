from datasci.shape import iter_leaves, flatten

example_list = [1, {"b": 2}, [3, {"d": 4}]]

example_dict = {
    "a": 1,
    "b": {"c": 2},
    "d": [3, 4],
}


def test_iter_leaves_on_singletons():
    for singleton in [1, False, None, "a", b"b"]:
        assert list(iter_leaves(singleton)) == [((), singleton)]


def test_iter_leaves_on_examples():
    assert list(iter_leaves(example_list)) == [
        ((0,), 1),
        ((1, "b"), 2),
        ((2, 0), 3),
        ((2, 1, "d"), 4),
    ]

    assert list(iter_leaves(example_dict)) == [
        (("a",), 1),
        (("b", "c"), 2),
        (("d", 0), 3),
        (("d", 1), 4),
    ]


def test_flatten():
    assert flatten(example_list) == {"0": 1, "1/b": 2, "2/0": 3, "2/1/d": 4}

    assert flatten(example_dict) == {"a": 1, "b/c": 2, "d/0": 3, "d/1": 4}
