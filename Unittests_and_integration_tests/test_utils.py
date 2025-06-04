#!/usr/bin/env python3
"""
Unit tests for utils.py
"""
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict, Tuple

# Assuming utils.py is in the same directory or an accessible path
# and contains the access_nested_map function.
# For the purpose of this example, if utils.py is in the same directory:
from utils import access_nested_map
# If utils is a module in a parent directory or installed,
# the import might differ based on project structure.


class TestAccessNestedMap(unittest.TestCase):
    """
    Test suite for the utils.access_nested_map function.
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
        Tests that access_nested_map returns the expected output for various inputs.
        Verifies successful retrieval of values from nested dictionary structures.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_output)


if __name__ == '__main__':
    # This allows running the tests directly from this file
    unittest.main()
