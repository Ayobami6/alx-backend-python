#!/usr/bin/env python3
""" Test utils module
"""

import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import (
    Dict,
    Union,
    Any,
    List,
    Tuple,
    Callable
)


class TestAcessNestedMap(unittest.TestCase):
    test_cases = [
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ]

    @parameterized.expand(test_cases)
    def test_access_nested_map(
            self, nested_map: Dict,
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
    def test_access_nested_map_exception(
            self,
            n_map: Dict,
            path: Tuple[str],
            exception: KeyError) -> None:
        """ Test access nested map exception

        Args:
            n_map (Dict[Any, Union[Dict, int]]): nested map
            path (Tuple[str]): path
        """
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
        # setting the mock object json return value to be the payload
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as mock_res:
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_res.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Test memoize class
    """

    def test_memoize(self) -> None:
        """ Test memoize

        Returns:
            None: None, Just a simulated test
        """
        class TestClass:

            def a_method(self) -> int:
                """ A method """
                return 42

            @memoize
            def a_property(self) -> int:
                """ decorated property method """
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mck_mtd:
            test = TestClass()
            test.a_property
            test.a_property
            mck_mtd.assert_called_once()


if __name__ == "__main__":
    unittest.main()
