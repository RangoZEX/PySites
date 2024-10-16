# app/routes.py
from flask import Blueprint, render_template_string

# Create a blueprint for your routes
main = Blueprint('main', __name__)

# Stylish HTML template for the welcome message with animation
HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Welcome to AMC Dev</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(to right, #4facfe, #00f2fe);
            overflow: hidden;
            animation: fadeIn 1s ease-in-out;
        }
        h1 {
            font-size: 48px;
            color: #fff;
            opacity: 0;
            animation: slideIn 1s forwards 0.5s;
            cursor: pointer;
        }
        @keyframes slideIn {
            from { transform: translateY(-50px); }
            to { transform: translateY(0); opacity: 1; }
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
</head>
<body>
    <h1 id="welcomeText" onclick="redirectToTelegram()">WELCOME TO AMC DEV</h1>

    <script>
        function redirectToTelegram() {
            window.location.href = "https://t.me/amcdevs"; // Redirects to Telegram
        }
    </script>
</body>
</html>
'''

@main.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)
