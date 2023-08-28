#!/usr/bin/env python3
""" Test GithubOrgClient module """

import unittest
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from utils import get_json, memoize


class TestGithubOrgClient(unittest.TestCase):

    # test cases with mocked responses
    test_cases = [
        ("google", {"payload": True}),
        ("abc", {"payload": True})
    ]

    @parameterized.expand(test_cases)
    @patch('client.get_json')
    def test_org(self, org: str, expected: dict, mck_mtd: Mock) -> None:
        """ Test GithubOrgClient.org """
        mck_mtd.return_value = expected
        client = GithubOrgClient(org)
        self.assertEqual(client.org, expected)
        mck_mtd.assert_called_once()

    test_cases_2 = [
        ("google", {"repos_url": "http://test_url"}),
    ]

    @parameterized.expand(test_cases_2)
    def test_public_repos_url(self, org: str, expected: dict) -> None:
        """ Test GithubOrgClient._public_repos_url """

        # mock the org property to return the expected payload
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mck_prop:
            mck_prop.return_value = expected
            client = GithubOrgClient(org)
            self.assertEqual(client._public_repos_url, expected["repos_url"])


if __name__ == '__main__':
    unittest.main()
