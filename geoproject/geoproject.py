"""Main module."""

import string
import random

def generate_random_string(length):
    characters = string.ascii_letters + string.digits  # Includes both uppercase and lowercase letters, and digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def generate_lucky_number(length=1):
    
    random_string = ''.join(random.choice(string.digits) for _ in range(length))
    return int(random_string)