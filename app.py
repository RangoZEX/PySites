from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables from config.env (if exists)
load_dotenv('config.env')

app = Flask(__name__)

# Get the BASE_URL from either config.env or Heroku environment variables
BASE_URL = os.getenv('BASE_URL')

@app.route('/')
def home():
    return f"Base URL is: {BASE_URL}"

if __name__ == '__main__':
    app.run(debug=True)
