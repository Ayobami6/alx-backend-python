#!/usr/bin/env python3
""" Test GithubOrgClient module """

import unittest
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from utils import get_json, memoize
from typing import Dict


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

    test_cases_3 = [
        ("google",
         {"repos_url": "http://test_url",
          "repos": [
              {"name": "test_repo",
               "license": {"key": "my_license"}},
              {"name": "test_repo_2", "license": {
                  "key": "other_license"}},
          ]}),
    ]

    @parameterized.expand(test_cases_3)
    @patch('client.get_json')  # patch get_json to not make external calls
    def test_public_repos(
            self, org: str, expected: dict, mck_mtd: Mock) -> None:
        """ Test GithubOrgClient.public_repos """

        #  make the return of simulated call to get_json return the expected
        mck_mtd.return_value = expected["repos"]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mck_prop:
            mck_prop.return_value = expected.get("repos_url")
            client = GithubOrgClient(org)
            self.assertEqual(client.public_repos(), [
                             "test_repo", "test_repo_2"])
            mck_prop.assert_called_once()
        mck_mtd.assert_called_once()

    test_cases_4 = [
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ]

    @parameterized.expand(test_cases_4)
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """ Test GithubOrgClient.has_license

        Args:
            repo (Dict): response repo
            key (str): license key
            expected (bool): expected result true or false
        """
        result = GithubOrgClient.has_license(repo, key)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
