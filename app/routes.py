# app/routes.py
from flask import Blueprint, render_template_string
from datetime import datetime

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
    <link href="https://fonts.googleapis.com/css2?family=Square+Sans+Serif:wght@700&display=swap" rel="stylesheet">
    <style>
        body {
            display: flex;
            flex-direction: column;
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
        .datetime-box {
            margin-top: 20px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid #fff;
            border-radius: 10px;
            color: #fff;
            font-family: 'Square Sans Serif', sans-serif;
            font-size: 24px;
            text-align: center;
            opacity: 0;
            animation: fadeIn 1s forwards 1s;
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
    <div class="datetime-box" id="datetimeBox">
        <div id="currentDate"></div>
        <div id="currentTime"></div>
    </div>

    <script>
        function redirectToTelegram() {
            window.location.href = "https://t.me/amcdevs"; // Redirects to Telegram
        }

        function updateDateTime() {
            const now = new Date();
            const options = { year: 'numeric', month: 'long', day: 'numeric', weekday: 'long' };
            const date = now.toLocaleDateString('en-US', options);
            const time = now.toLocaleTimeString('en-US', { hour12: true });
            
            document.getElementById('currentDate').innerHTML = date;
            document.getElementById('currentTime').innerHTML = time;
        }

        setInterval(updateDateTime, 1000); // Update date and time every second
        updateDateTime(); // Initial call to set the date and time immediately
    </script>
</body>
</html>
'''

@main.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)
