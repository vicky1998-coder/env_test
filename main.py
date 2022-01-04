import os
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.getenv("EMAIL_ID")
PASSWORD = os.getenv("PASS")

API_KEY = os.getenv("API")

print("------------")
print(EMAIL)
print(PASSWORD)
print(API_KEY)
print("--------------")

