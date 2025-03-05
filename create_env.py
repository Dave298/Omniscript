import os

# Define the environment variables
env_content = """GITHUB_REPO=https://github.com/Dave298/OmniScript.git
WEBSITE_REPO=https://github.com/Dave298/OmniScriptSite.git
TWITTER_API_KEY=sXtaMaJQtWY0JlfbJq0AVafPR
TWITTER_API_SECRET=cheLGxDtZTHutjfgpFxTfIe7PpnB4fmPmg7tTMXVl6Yd7kNerc
TWITTER_BEARER_TOKEN=1897328812301721600-xuMCBLddsgnJUDq7B5N8CTihjS4aFz
PYPI_USERNAME=David.py
PYPI_PASSWORD=Billiondollar@2
EMAIL_SENDER=Davidikejiaku28@gmail.com
EMAIL_PASSWORD=billiondollar@
EMAIL_RECIPIENTS=Ifeomaikejiaku@gmail.com
"""

# Create and write to the .env file
env_file_path = ".env"

if os.path.exists(env_file_path):
    print("⚠️ .env file already exists. Open it and update your credentials.")
else:
    with open(env_file_path, "w") as env_file:
        env_file.write(env_content)
    print("✅ .env file created successfully! Now open it and replace the placeholder values.")

