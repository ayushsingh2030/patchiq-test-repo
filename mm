import os
import pickle
import subprocess

# Hardcoded secret
API_KEY = "sk_test_123456789abcdef"

# Command injection
user_input = input("Enter command: ")
os.system(user_input)

# Insecure deserialization
data = input("Enter serialized data: ")
obj = pickle.loads(data)

# Another command injection example
filename = input("Enter filename: ")
subprocess.run(f"cat {filename}", shell=True)
