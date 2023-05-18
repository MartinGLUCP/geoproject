"""Main module."""

import string
import random

def generate_random_string(length):
    """Generate random string"""
    characters = string.ascii_letters + string.digits  # Includes both uppercase and lowercase letters, and digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def generate_lucky_number(length=1):
    """_summary_

    Args:
        length (int, optional): _description_. Defaults to 1.

    Returns:
        _type_: _description_
    """
    random_string = ''.join(random.choice(string.digits) for _ in range(length))
    return int(random_string)