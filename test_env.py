from dotenv import load_dotenv
import os

load_dotenv()
print("GITHUB_REPO:", os.getenv("GITHUB_REPO"))
print("EMAIL_SENDER:", os.getenv("EMAIL_SENDER"))
