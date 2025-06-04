#!/usr/bin/env python3
"""
Unit tests for the client.py module, specifically for GithubOrgClient.
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized

# Assuming client.py is in the same directory or an accessible Python path
# and defines GithubOrgClient.
# Example:
# from client import GithubOrgClient
# For this to run, a client.py file with GithubOrgClient would be needed.
# We'll proceed as if it exists and can be imported.
# If client.py defines `from utils import get_json`, then patching `client.get_json` is correct.
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test suite for the GithubOrgClient class from client.py.
    """

    @parameterized.expand([
        ("google", {"name": "Google", "type": "Organization"}),
        ("abc", {"name": "Alphabet Inc.", "type": "Organization"}),
        # The payloads are examples of what get_json might return for these orgs.
    ])
    @patch('client.get_json')  # Patch 'get_json' as it's used within client.py
    def test_org(
        self,
        mock_get_json: Mock,        # Argument injected by @patch (comes first)
        org_name: str,              # First argument from @parameterized.expand
        expected_payload: dict      # Second argument from @parameterized.expand
    ) -> None:
        """
        Tests that GithubOrgClient.org returns the correct value and that
        the underlying get_json function is called once with the expected URL.
        """
        # Configure the mock_get_json to return the specific payload for this org
        mock_get_json.return_value = expected_payload

        # Instantiate the client with the organization name
        client_instance = GithubOrgClient(org_name)

        # Call the .org() method (assuming it's a method)
        org_data = client_instance.org()

        # Construct the expected URL that get_json should be called with
        # This assumes GithubOrgClient.ORG_URL is defined as "https://api.github.com/orgs/{org}"
        expected_url = f"https://api.github.com/orgs/{org_name}"

        # Assert that get_json was called exactly once with the expected URL
        mock_get_json.assert_called_once_with(expected_url)

        # Assert that the .org() method returned the expected payload
        self.assertEqual(org_data, expected_payload)


if __name__ == '__main__':
    # This allows running the tests directly from this file:
    # python -m unittest test_client.py
    # or simply:
    # python test_client.py
    # if test_client.py is made executable and the shebang is correct.
    unittest.main()
