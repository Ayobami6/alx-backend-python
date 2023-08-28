#!/usr/bin/env python3
""" Test utils module
"""

import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json
from parameterized import parameterized
from typing import (
    Dict,
    Union,
    Any,
    List,
    Tuple,
)


class TestAcessNestedMap(unittest.TestCase):

    """ Module Test Class

    Attributes:
        test_cases (TYPE): Description
    """

    test_cases = [
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ]

    @parameterized.expand(test_cases)
    def test_access_nested_map(self, nested_map: Dict[Any, Union[Dict, int]],
                               path: Tuple[str],
                               expect: Union[Dict, int]) -> None:
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
    def test_access_nested_map_exception(self, n_map:
                                         Dict[Any, Union[Dict, int]],
                                         path: Tuple[str]) -> None:
        with self.assertRaises(KeyError):
            access_nested_map(n_map, path)


class TestGetJson(unittest.TestCase):

    test_cases = [
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ]

    @parameterized.expand(test_cases)
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """ Test get json

        Args:
            test_url (str): Url
            test_payload (Dict): Payload
        """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as mock_res:
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_res.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
