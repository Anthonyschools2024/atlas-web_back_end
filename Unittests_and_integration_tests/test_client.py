
#!/usr/bin/env python3
"""
Unit tests for the client.py module, specifically for GithubOrgClient,
and integration tests for GithubOrgClient.
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class # Added parameterized_class
from typing import List, Dict, Any

# Assuming client.py is in the same directory or an accessible Python path
from client import GithubOrgClient

# Assuming fixtures.py is in the same directory or an accessible Python path
# and contains: org_payload, repos_payload, expected_repos, apache2_repos
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """
    Test suite for the GithubOrgClient class from client.py (Unit Tests).
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
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient, mocking only external HTTP calls (requests.get).
    Uses fixtures provided by @parameterized_class.
    """
    get_patcher = None  # Class attribute to hold the patcher context manager

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up class by starting a patcher for requests.get.
        The mock will return different payloads based on the URL being accessed.
        Fixtures (org_payload, repos_payload, etc.) are available as class attributes
        thanks to @parameterized_class.
        """

        def side_effect_for_requests_get(url: str) -> Mock:
            """
            Side effect for mocked requests.get.
            Returns a Mock whose json method returns appropriate fixture data based on URL.
            """
            mock_response = Mock()

            # Determine the expected URL for organization details
            # GithubOrgClient.ORG_URL is "https://api.github.com/orgs/{org}"
            # The org name used in tests will be derived from cls.org_payload['login']
            expected_org_url = GithubOrgClient.ORG_URL.format(
                org=cls.org_payload.get('login') # type: ignore
            )

            # Determine the expected URL for repositories list
            # This URL is directly provided in the org_payload fixture
            expected_repos_url = cls.org_payload.get('repos_url') # type: ignore

            if url == expected_org_url:
                mock_response.json.return_value = cls.org_payload
            elif url == expected_repos_url:
                mock_response.json.return_value = cls.repos_payload
            else:
                # Handle unexpected URLs if necessary, e.g., by raising an error
                # or returning a specific error payload. For this setup, we assume
                # only these two URLs will be hit by the methods under test.
                # Defaulting to an empty dict or raising can help debug.
                print(f"Warning: Unhandled URL in mock side_effect: {url}")
                mock_response.json.return_value = {"error": "URL not mocked for integration test"}
            return mock_response

        # The target for patching 'requests.get'. This assumes that 'requests.get'
        # is called by a utility function (e.g., get_json in utils.py) which is
        # imported and used in 'client.py'.
        # Adjust 'utils.requests.get' if the import path or usage is different.
        cls.get_patcher = patch('utils.requests.get') # type: ignore
        mock_requests_get = cls.get_patcher.start() # type: ignore
        mock_requests_get.side_effect = side_effect_for_requests_get

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Tear down class by stopping the patcher to clean up mocks.
        """
        if cls.get_patcher:
            cls.get_patcher.stop() # type: ignore

    # Test methods for integration tests will be added in subsequent tasks.
    # For example:
    # def test_public_repos_integration(self):
    # client = GithubOrgClient(self.org_payload["login"]) # type: ignore
    # actual_repos = client.public_repos()
    # self.assertEqual(actual_repos, self.expected_repos) # type: ignore


if __name__ == '__main__':
    unittest.main()
