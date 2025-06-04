#!/usr/bin/env python3
"""
Unit tests for the client.py module, specifically for GithubOrgClient.
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from typing import List, Dict, Any # Ensure Dict and Any are imported

# Assuming client.py is in the same directory or an accessible Python path
# and defines GithubOrgClient.
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test suite for the GithubOrgClient class from client.py.
    """

    @parameterized.expand([
        ("google", {"name": "Google", "type": "Organization"}),
        ("abc", {"name": "Alphabet Inc.", "type": "Organization"}),
    ])
    @patch('client.get_json')
    def test_org(
        self,
        mock_get_json: Mock,
        org_name: str,
        expected_payload: dict
    ) -> None:
        """
        Tests that GithubOrgClient.org returns the correct value and that
        the underlying get_json function is called once with the expected URL.
        """
        mock_get_json.return_value = expected_payload
        client_instance = GithubOrgClient(org_name)
        org_data = client_instance.org()
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(org_data, expected_payload)

    def test_public_repos_url(self) -> None:
        """
        Tests the _public_repos_url property of GithubOrgClient.
        It mocks the 'org' property to return a known payload and verifies
        that _public_repos_url correctly extracts the 'repos_url' from it.
        """
        known_payload = {
            "login": "testorg",
            "repos_url": "https://api.github.com/orgs/testorg/repos"
        }
        client_instance = GithubOrgClient("testorg")

        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org_property:
            mock_org_property.return_value = known_payload
            actual_repos_url = client_instance._public_repos_url
            self.assertEqual(actual_repos_url, known_payload["repos_url"])
            mock_org_property.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """
        Tests the GithubOrgClient.public_repos method.
        Mocks _public_repos_url (as a property) and get_json (as a function)
        to verify that public_repos processes the data correctly and
        makes the expected calls to its dependencies.
        """
        mock_repos_payload = [
            {"name": "repo-alpha", "license": {"key": "mit"}},
            {"name": "repo-beta", "license": {"key": "apache-2.0"}},
            {"name": "repo-gamma", "license": {"key": "mit"}},
        ]
        mock_get_json.return_value = mock_repos_payload
        mock_target_repos_url = "https://api.example.com/orgs/test_org/repos"
        client_instance = GithubOrgClient("test_org")

        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_public_repos_url_prop:
            mock_public_repos_url_prop.return_value = mock_target_repos_url
            actual_repo_names = client_instance.public_repos()
            expected_repo_names = ["repo-alpha", "repo-beta", "repo-gamma"]
            self.assertEqual(actual_repo_names, expected_repo_names)
            mock_public_repos_url_prop.assert_called_once()
            mock_get_json.assert_called_once_with(mock_target_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict[str, Any], license_key: str, expected: bool) -> None:
        """
        Tests the GithubOrgClient.has_license static method.
        Verifies that it correctly identifies if a repository dictionary
        contains a specific license key.
        """
        # Assuming has_license is a static method on GithubOrgClient
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
