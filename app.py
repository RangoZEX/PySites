from flask import Flask
from dotenv import load_dotenv
import os
import logging

# Load environment variables from config.env (if it exists)
load_dotenv('config.env')

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Get the BASE_URL from config.env
BASE_URL = os.getenv('BASE_URL')

# Check if BASE_URL is empty and log a message if it is
if BASE_URL == "":
    logging.warning("Missing variable BASE_URL")

@app.route('/')
def home():
    return f"Base URL is: {BASE_URL or 'Not set'}"

if __name__ == '__main__':
    app.run(debug=True)
