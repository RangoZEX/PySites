from flask import Flask
import os

app = Flask(__name__)

# Access the BASE_URL from Heroku's environment variables
BASE_URL = os.getenv('BASE_URL')

@app.route('/')
def home():
    return f"Base URL is: {BASE_URL}"

if __name__ == '__main__':
    app.run(debug=True)
