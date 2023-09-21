import os
from twitter_module import authenticate_to_twitter, format_tweet
from dotenv import load_dotenv
from flask import Flask, request, jsonify

# Load the .env file
load_dotenv()

# Fetch the values and store them in Python variables
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Authenticate to Twitter
api = authenticate_to_twitter(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

if api:
    print("Authentication OK")
else:
    print("Error during authentication")

try:
    api.update_status("This is a test tweet from Tweepy.")
    print("Tweet posted successfully!")
except Exception as e:
    print(f"Failed to post tweet: {e}")










# app = Flask(__name__)

# @app.route('/arkham-webhook', methods=['POST'])
# def arkham_listener():
#     data = request.json
#     # Process the data (e.g., send a tweet)
#     return jsonify(status="success"), 200

# if __name__ == '__main__':
#     app.run(port=5000)
