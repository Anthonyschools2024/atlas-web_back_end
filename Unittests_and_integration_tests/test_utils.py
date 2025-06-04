#!/usr/bin/env python3
"""
Unit tests for utility functions and decorators in the 'utils' module.
This test suite covers functionalities such as accessing nested dictionary values,
fetching JSON from URLs (with mocking), and memoization.
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict

# It's assumed that 'utils.py' exists in an importable location
# (e.g., same directory or in PYTHONPATH) and contains the definitions for:
# - access_nested_map(nested_map, path)
# - get_json(url)
# - memoize (decorator)
#
# Example structure for utils.py for these tests to pass:
#
# import requests
# import functools
# from typing import Mapping, Sequence, Any, Dict
#
# def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
# current_value = nested_map
# for key in path:
# if not isinstance(current_value, Mapping):
# raise KeyError(key) # Ensure KeyError for non-mappable intermediate
# try:
# current_value = current_value[key]
# except KeyError:
# raise # Re-raise the original KeyError with the key
# return current_value
#
# def get_json(url: str) -> Dict[Any, Any]:
# response = requests.get(url)
# return response.json()
#
# def memoize(fn):
# attr_name = f"_memoized_result_for_{fn.__name__}"
# @functools.wraps(fn)
# def memoized_wrapper(self, *args, **kwargs):
# if not hasattr(self, attr_name):
# setattr(self, attr_name, fn(self, *args, **kwargs))
# return getattr(self, attr_name)
# return memoized_wrapper
#
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test suite for the utils.access_nested_map function.
    Verifies its ability to correctly access values in nested dictionary structures
    and handle error conditions appropriately.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping,
        path: Sequence,
        expected_output: Any
    ) -> None:
        """
        Tests that access_nested_map returns the expected output for various valid inputs.
        This ensures correct retrieval of values from simple and nested dictionaries.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping,
        path: Sequence,
        expected_key_in_exception: str
    ) -> None:
        """
        Tests that access_nested_map raises a KeyError for invalid or incomplete paths.
        It also verifies that the exception message accurately reflects the problematic key.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{expected_key_in_exception}'")


class TestGetJson(unittest.TestCase):
    """
    Test suite for the utils.get_json function.
    Focuses on mocking external HTTP calls (requests.get) to ensure no actual
    network requests are made during testing, verifying correct URL usage and payload parsing.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')  # Mocks 'requests.get' within the 'utils' module scope
    def test_get_json(
        self,
        mock_requests_get: Mock,    # Argument injected by @patch
        test_url: str,              # First argument from @parameterized.expand
        test_payload: Dict[Any, Any]  # Second argument from @parameterized.expand
    ) -> None:
        """
        Tests that utils.get_json correctly calls requests.get with the provided URL
        and returns the expected JSON payload. External HTTP calls are mocked.
        """
        # Configure the mock for requests.get().return_value (the response object)
        # to have a json() method that returns the test_payload.
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_requests_get.return_value = mock_response

        # Call the function under test
        result = get_json(test_url)

        # Assert that requests.get was called exactly once with the test_url
        mock_requests_get.assert_called_once_with(test_url)

        # Assert that the output of get_json is equal to the test_payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test suite for the utils.memoize decorator.
    Verifies that a method's result is cached after the first call, ensuring
    the underlying logic is not re-executed on subsequent calls for the same instance.
    """

    def test_memoize(self) -> None:
        """
        Tests the memoize decorator by defining an inner class with a method
        and a memoized method. It ensures the underlying method is called only once
        and its result is cached and returned on subsequent invocations.
        """

        class TestClass:
            """
            An example class to demonstrate memoization on one of its methods.
            """

            def a_method(self) -> int:
                """A method that is intended to be called by a_property."""
                # This actual implementation won't be called if mocked properly.
                return 42

            @memoize
            def a_property(self) -> int:
                """
                A memoized method that calls a_method.
                Its result should be cached after the first invocation on an instance.
                """
                return self.a_method()

        test_instance = TestClass()

        # Use patch.object to mock 'a_method' on the 'test_instance'.
        # The mock will allow us to assert how many times it was called
        # and control its return value.
        with patch.object(test_instance, 'a_method', return_value=42) as mock_a_method:
            # Call the memoized method (a_property) twice
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()

            # Assert that a_property returns the correct result for both calls
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Assert that the underlying a_method (now mocked) was called only once
            mock_a_method.assert_called_once()


if __name__ == '__main__':
    # This allows running the tests directly from this file using:
    # python test_utils.py
    unittest.main()
