# app/routes.py
from flask import Blueprint, render_template_string

# Create a blueprint for your routes
main = Blueprint('main', __name__)

# Stylish HTML template for the developer bio with animations
HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Welcome to My Site</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #4facfe, #00f2fe);
            color: #fff;
            text-align: center;
            overflow: hidden; /* Prevent scrollbars during animation */
        }
        .door {
            width: 300px;
            height: 400px;
            background: #8B4513; /* Brown color for the door */
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            animation: openDoor 3s forwards; /* Animation to open the door */
            z-index: 1;
        }
        @keyframes openDoor {
            0% { transform: translate(-50%, -50%) rotateY(0); }
            50% { transform: translate(-50%, -50%) rotateY(-120deg); }
            100% { transform: translate(-50%, -50%) rotateY(0); }
        }
        .welcome {
            position: relative;
            z-index: 0; /* Behind the door */
            opacity: 0; /* Hidden initially */
            transition: opacity 1s ease-in 3s; /* Fade in after door opens */
        }
        .welcome.show {
            opacity: 1; /* Show message */
        }
        h1 {
            margin: 20px 0;
            font-size: 3em;
        }
        .section {
            margin: 20px 0;
            padding: 20px;
            border: 2px solid #fff;
            border-radius: 10px;
            background-color: rgba(255, 255, 255, 0.1);
        }
    </style>
</head>
<body>
    <div class="door"></div>
    <div class="welcome" id="welcomeMessage">
        <h1>Welcome to My Site!</h1>
        <div class="section" id="aboutMe">
            <h2>About Me</h2>
            <p>I am a passionate developer with experience in various technologies.</p>
        </div>
        <div class="section" id="contactUs">
            <h2>Contact Us</h2>
            <p>You can reach me at: email@example.com</p>
        </div>
    </div>
    <script>
        // Show the welcome message after the door animation is done
        setTimeout(() => {
            document.getElementById('welcomeMessage').classList.add('show');
        }, 3000); // Time should match the door animation duration
    </script>
</body>
</html>
'''

@main.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)
