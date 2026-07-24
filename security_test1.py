# PatchIQ-iA Security Scan Test File

# 1. Hardcoded Secret Test
api_key = "AIzaSyD-SUPER_SECRET_TOKEN_123456789"

# 2. Unsafe Eval Test
user_input = "print('Checking for vulnerabilities...')"
eval(user_input)

# 3. SQL Injection Test
user_id = 105
db_query = f"SELECT * FROM users WHERE id = {user_id}"
