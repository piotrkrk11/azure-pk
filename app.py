from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Azure Workshop 2025!"

@app.route('/copilot-videos')
def copilot_videos():
    return """
    <h1>Najciekawsze filmy o GitHub Copilot na YouTube</h1>
    <ul>
        <li><a href="https://www.youtube.com/watch?v=SGUCcjHTmGY" target="_blank">GitHub Copilot: Your AI Pair Programmer</a></li>
        <li><a href="https://www.youtube.com/watch?v=4KqUvG8HPYo" target="_blank">How to use GitHub Copilot - Full Demo</a></li>
        <li><a href="https://www.youtube.com/watch?v=0RCbYgSsn5I" target="_blank">GitHub Copilot: Is it worth it?</a></li>
        <li><a href="https://www.youtube.com/watch?v=8yLlwITMRDE" target="_blank">GitHub Copilot - AI Code Completion</a></li>
        <li><a href="https://www.youtube.com/watch?v=3XzLwmI3-1M" target="_blank">GitHub Copilot: Productivity Boost or Security Risk?</a></li>
    </ul>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)