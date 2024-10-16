# app/routes.py
from flask import Blueprint, render_template_string

# Create a blueprint for your routes
main = Blueprint('main', __name__)

# Stylish HTML template for the developer bio
HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Developer Bio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #4facfe, #00f2fe);
            color: #fff;
            text-align: center;
            padding: 50px;
        }
        h1 {
            margin-bottom: 20px;
            font-size: 3em;
        }
        .bio {
            margin-top: 30px;
            padding: 20px;
            border: 2px solid #fff;
            border-radius: 10px;
            background-color: rgba(255, 255, 255, 0.1);
        }
    </style>
</head>
<body>
    <h1>Developer Name</h1>
    <div class="bio">
        <p>Hello! I am a passionate developer with experience in various technologies.</p>
    </div>
</body>
</html>
'''

@main.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)
    
