from typing import Any, Collection, Dict, Iterator, Tuple
from collections import abc


def iter_leaves(node: Any, prefix: Collection[Any] = ()) -> Iterator[Tuple[Any, Any]]:
    """
    Iterate over the leaf nodes in a tree structure, paired with the path to reach them.

    Instances of abc.Mapping and abc.Collection (excepting strings) are interpreted as
    branches, and all other values are treated as leaves.
    """
    if isinstance(node, abc.Mapping):
        for key, value in node.items():
            yield from iter_leaves(value, prefix + (key,))
    elif isinstance(node, abc.Collection) and not isinstance(
        node, (str, bytes, bytearray)
    ):
        for key, value in enumerate(node):
            yield from iter_leaves(value, prefix + (key,))
    else:
        yield prefix, node


def flatten(obj: Any, separator: str = "/") -> Dict[str, Any]:
    """
    Iterate over the leaf nodes in a tree structure, producing a single flat dictionary
    with string keys and atomic values.
    """
    return {separator.join(map(str, path)): leaf for path, leaf in iter_leaves(obj)}
