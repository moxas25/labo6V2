# hello.py
import random
import string

# Function that has a security vulnerability detected by Bandit (SAST)
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# This function contains a secret key that will be detected by Gitleaks
def hardcoded_secret():
    secret_key = "12345-my-secret-key"  # This will trigger Gitleaks
    return secret_key

# Example function with an assert statement that will be detected by Bandit (SAST)
def test_addition():
    assert 1 + 1 == 3  # This will trigger Bandit's assert_used check

# A basic function that uses a vulnerable dependency (request library in the requirements.txt)
import requests

def get_data_from_api():
    response = requests.get("https://httpbin.org/get")
    return response.json()

if __name__ == "__main__":
    print("Hello, World!")
    print(generate_random_string())
    print(hardcoded_secret())
    test_addition()
    print(get_data_from_api())
