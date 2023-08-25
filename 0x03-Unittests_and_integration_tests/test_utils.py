#!/usr/bin/env python3
""" Test utils module
"""

import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
)


class TestAcessNestedMap(unittest.TestCase):

    """ Module Test Class

    Attributes:
        test_cases (TYPE): Description
    """

    def setUp(self):
        print("Testing the AcessNestedMap method")

    test_cases = [
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ]

    @parameterized.expand(test_cases)
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expect: Any) -> None:
        """ Test access nested map with correct params

        Args:
            nested_map (Mapping): Nested map
            path (Sequence): Sequence of Items
            expect (Any): Any Value
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expect)

    test_cases_2 = [
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ]

    @parameterized.expand(test_cases_2)
    def test_access_nested_map_exception(self, n_map: Mapping, path: Sequence):
        with self.assertRaises(KeyError):
            access_nested_map(n_map, path)


if __name__ == "__main__":
    unittest.main()
