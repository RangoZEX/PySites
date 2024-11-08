import os
from flask import Flask
from dotenv import load_dotenv
from app.routes import main  # Import your blueprint

# Load environment variables from config.env
load_dotenv('config.env')

# Initialize the Flask app
app = Flask(__name__)

# Register the blueprint
app.register_blueprint(main)

# Get BASE_URL and PORT from config.env
BASE_URL = os.getenv('BASE_URL')
PORT = os.getenv('PORT', 5000)  # Default to 5000 if PORT is not set

if __name__ == '__main__':
    # Use the port specified in config.env or default to 5000
    port = int(os.environ.get("PORT", PORT))
    app.run(debug=True, host='0.0.0.0', port=port)
    
