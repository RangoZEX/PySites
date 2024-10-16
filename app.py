from flask import Flask, render_template_string
from dotenv import load_dotenv
import os

# Load environment variables from config.env (if it exists)
load_dotenv('config.env')

app = Flask(__name__)

# Get the BASE_URL from config.env
BASE_URL = os.getenv('BASE_URL')

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
            animation: fadeIn 1s;
        }
        h1 {
            margin-bottom: 20px;
            font-size: 3em;
            animation: slideIn 0.5s ease-in-out forwards;
        }
        .bio {
            margin-top: 30px;
            padding: 20px;
            border: 2px solid #fff;
            border-radius: 10px;
            background-color: rgba(255, 255, 255, 0.1);
            animation: fadeInUp 1s;
        }
        .skills {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .skill {
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: 5px;
            padding: 10px 15px;
            margin: 5px;
            transition: transform 0.3s;
        }
        .skill:hover {
            transform: scale(1.1);
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes slideIn {
            from { transform: translateY(-50px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <h1>Developer Name</h1>
    <div class="bio">
        <p>Hello! I am a passionate developer with experience in various technologies. I love building applications that solve real-world problems and enhance user experiences.</p>
        <p>Current Focus: Full Stack Development, Python, Flask, JavaScript</p>
        <p>Location: Your City</p>
    </div>
    <h2>Skills</h2>
    <div class="skills">
        <div class="skill">HTML</div>
        <div class="skill">CSS</div>
        <div class="skill">JavaScript</div>
        <div class="skill">Python</div>
        <div class="skill">Flask</div>
        <div class="skill">React</div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)
