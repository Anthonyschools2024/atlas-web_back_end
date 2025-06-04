
#!/usr/bin/env python3
"""
Unit tests for the client.py module, specifically for GithubOrgClient.
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock # Added PropertyMock
from parameterized import parameterized

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
        org_data = client_instance.org() # Assuming org() is a method call
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(org_data, expected_payload)

    def test_public_repos_url(self) -> None:
        """
        Tests the _public_repos_url property of GithubOrgClient.
        It mocks the 'org' property/method to return a known payload and verifies
        that _public_repos_url correctly extracts the 'repos_url' from it.
        """
        # Define a known payload that client_instance.org (mocked as a property) will return
        known_payload = {
            "login": "testorg",
            "repos_url": "https://api.github.com/orgs/testorg/repos"
        }

        # Instantiate the client. The org_name for init doesn't impact this specific
        # test since 'org' is fully mocked.
        client_instance = GithubOrgClient("testorg")

        # Use patch as a context manager to mock 'GithubOrgClient.org'.
        # 'new_callable=PropertyMock' ensures 'org' is treated as a property for mocking.
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org_property:
            # Configure the mocked 'org' property to return our known_payload when accessed
            mock_org_property.return_value = known_payload

            # Access the _public_repos_url property.
            # This should internally access client_instance.org (which is now the mocked property).
            actual_repos_url = client_instance._public_repos_url

            # Assert that the result is the expected 'repos_url' from the payload
            self.assertEqual(actual_repos_url, known_payload["repos_url"])

            # Assert that the 'org' property was accessed once to retrieve the payload
            mock_org_property.assert_called_once()


if __name__ == '__main__':
    unittest.main()
