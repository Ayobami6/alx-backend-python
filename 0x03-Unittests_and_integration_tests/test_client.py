import unittest
from unittest.mock import patch, Mock
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
        """ Test GithubOrgClient.org
        """
        mck_mtd.return_value = expected
        client = GithubOrgClient(org)
        self.assertEqual(client.org, expected)
        mck_mtd.assert_called_once()


if __name__ == '__main__':
    unittest.main()
