# app/routes.py
from flask import Blueprint, render_template_string
from datetime import datetime

# Create a blueprint for your routes
main = Blueprint('main', __name__)

# Stylish HTML template for the welcome message with rain animation
HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>AMC DEVELOPERS</title>
    <link href="https://fonts.googleapis.com/css2?family=Nova+Square&display=swap" rel="stylesheet"> <!-- Nova Square font -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap" rel="stylesheet"> <!-- Digital font -->
    <style>
        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            position: relative;
            overflow: hidden;
            font-family: 'Roboto Mono', monospace; /* Default font for body */
            background: linear-gradient(135deg, #1e3c72, #2a69ac); /* Gradient background */
            color: #fff; /* White text color */
        }
        h1 {
            font-size: 48px;
            color: #00ff00; /* Green text for the welcome message */
            opacity: 0;
            animation: slideIn 1s forwards 0.5s;
            cursor: pointer;
            font-family: 'Nova Square', cursive; /* Nova Square font for the welcome text */
        }
        .datetime-box {
            margin-top: 20px;
            padding: 20px;
            background: rgba(0, 0, 0, 0.5); /* Semi-transparent black background for better visibility */
            border: 2px solid #fff;
            border-radius: 10px;
            color: #00ff00; /* Green color for digital clock */
            font-size: 32px; /* Larger font size */
            text-align: center;
            opacity: 0;
            animation: fadeIn 1s forwards 1s;
        }

        /* Rain Animation */
        .rain {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            pointer-events: none;
            overflow: hidden;
        }
        .drop {
            position: absolute;
            background: rgba(255, 255, 255, 0.7);
            width: 2px;
            height: 10px;
            animation: fall linear infinite;
        }

        @keyframes slideIn {
            from { transform: translateY(-50px); }
            to { transform: translateY(0); opacity: 1; }
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes fall {
            0% {
                transform: translateY(-100px);
                opacity: 1;
            }
            100% {
                transform: translateY(100vh);
                opacity: 0;
            }
        }
    </style>
</head>
<body>
    <div class="rain" id="rain"></div> <!-- Rain container -->
    <h1 id="welcomeText" onclick="redirectToTelegram()">WELCOME TO\nAMC DEV</h1>
    <div class="datetime-box" id="datetimeBox">
        <div id="currentDate"></div>
        <div id="currentTime"></div>
    </div>

    <script>
        function redirectToTelegram() {
            window.location.href = "https://t.me/amcdev"; // Redirects to Telegram
        }

        function updateDateTime() {
            const now = new Date();
            const options = { year: 'numeric', month: 'long', day: 'numeric', weekday: 'long' };
            const date = now.toLocaleDateString('en-US', options);
            const time = now.toLocaleTimeString('en-US', { hour12: true });
            
            document.getElementById('currentDate').innerHTML = date;
            document.getElementById('currentTime').innerHTML = time;
        }

        function createRain() {
            const rainContainer = document.getElementById('rain');
            const dropsCount = 100; // Number of raindrops

            for (let i = 0; i < dropsCount; i++) {
                const drop = document.createElement('div');
                drop.className = 'drop';
                drop.style.left = Math.random() * 100 + 'vw'; // Randomize horizontal position
                drop.style.animationDuration = Math.random() * 2 + 0.5 + 's'; // Randomize falling speed
                drop.style.animationDelay = Math.random() * 2 + 's'; // Randomize start time
                rainContainer.appendChild(drop);
            }
        }

        setInterval(updateDateTime, 1000); // Update date and time every second
        updateDateTime(); // Initial call to set the date and time immediately
        createRain(); // Start creating raindrops
    </script>
</body>
</html>
'''

@main.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)
