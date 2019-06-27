# Import the framework 
from flask import Flask

# Create an instance of Flask
app = Flask(__name__)

@app.route("/")
def index();

    """Present some documentation"""
    
    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
    