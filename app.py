from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables from config.env
load_dotenv('config.env')

app = Flask(__name__)

# Access the BASE_URL from environment variables
BASE_URL = os.getenv('BASE_URL')

@app.route('/')
def home():
    return f"Base URL is: {BASE_URL}"

if __name__ == '__main__':
    app.run(debug=True)
