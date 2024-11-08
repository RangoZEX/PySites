import os
from dotenv import load_dotenv
from app import create_app

# Load environment variables from config.env
load_dotenv('config.env')

# Initialize the Flask app using the create_app function
app = create_app()

# Get BASE_URL and PORT from config.env
BASE_URL = os.getenv('BASE_URL')
PORT = os.getenv('PORT', 5000)  # Default to 5000 if PORT is not set

if __name__ == '__main__':
    # Use the port specified in config.env or default to 5000
    port = int(os.environ.get("PORT", PORT))
    app.run(debug=True, host='0.0.0.0', port=port)
