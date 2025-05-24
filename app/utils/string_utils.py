"""
String Utilities Module
-----------------------

This module provides utility functions for string manipulation.

Current Functions:
- string_to_list: Converts a comma-separated string into a list of substrings,
  safely handling non-string inputs.

Usage:
    Import the desired utility function(s) as needed.

Example:
    >>> from string_utils import string_to_list
    >>> string_to_list("a,b,c")
    ['a', 'b', 'c']
"""

def string_to_list(string):
    """
    Converts a comma-separated string into a list of substrings.

    Parameters:
        string (str): A comma-separated string. If the input is not a string,
                      it will be returned unchanged.

    Returns:
        list: A list of substrings if the input is a string.
        any: The original input if it is not a string.

    Example:
        >>> string_to_list("apple,banana,cherry")
        ['apple', 'banana', 'cherry']

        >>> string_to_list(123)
        123
    """
    if isinstance(string, str):
        return string.split(",")
    return string
