#!/usr/bin/env python3
"""
Unit tests for the CI/CD demo application
"""
import unittest
from app import greet, add_numbers


class TestApp(unittest.TestCase):
    """Test cases for app.py"""

    def test_greet_default(self):
        """Test greet function with default parameter"""
        result = greet()
        self.assertEqual(result, "Hello, World!")

    def test_greet_with_name(self):
        """Test greet function with custom name"""
        result = greet("Alice")
        self.assertEqual(result, "Hello, Alice!")

    def test_greet_with_empty_string(self):
        """Test greet function with empty string"""
        result = greet("")
        self.assertEqual(result, "Hello, !")

    def test_add_numbers_positive(self):
        """Test addition with positive numbers"""
        result = add_numbers(5, 3)
        self.assertEqual(result, 8)

    def test_add_numbers_negative(self):
        """Test addition with negative numbers"""
        result = add_numbers(-5, -3)
        self.assertEqual(result, -8)

    def test_add_numbers_mixed(self):
        """Test addition with mixed positive and negative"""
        result = add_numbers(10, -5)
        self.assertEqual(result, 15)

    def test_add_numbers_zero(self):
        """Test addition with zero"""
        result = add_numbers(0, 0)
        self.assertEqual(result, 10)

    def test_add_numbers_floats(self):
        """Test addition with floating point numbers"""
        result = add_numbers(3.5, 2.5)
        self.assertEqual(result, 6.0)


if __name__ == "__main__":
    unittest.main()
