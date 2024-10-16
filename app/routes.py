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
    <link rel="stylesheet" href="{{ url_for('main.static', filename='styles.css') }}">
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
