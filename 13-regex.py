#!/usr/bin/env python3

import re

def validate_email(email):
    # Regular expression pattern for validating email addresses
    pattern = r"\b[A-Za-z0-9._+-]+@[A-Za-z0-9]+\.[A-Za-z]{2,}\b"

    # Use re.findall to check if the email matches the pattern
    if re.findall(pattern, email):
        return True  # Return True if the email is valid
    else:
        return False  # Return False if the email is not valid

# Test cases
print(validate_email("support@hack4u.io"))    # Valid email
print(validate_email("support@.io"))           # Invalid email (missing domain)
print(validate_email("support@hack4u.io3"))    # Invalid email (numeric characters in domain)