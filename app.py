from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Hello, Azure Workshop 2025!</h1>
    <h2>Najciekawsze filmy o GitHub Copilot na YouTube</h2>
    <ul style="list-style:none;">
        <li>
            <a href="https://www.youtube.com/watch?v=SGUCcjHTmGY" target="_blank">
                <img src="https://img.youtube.com/vi/SGUCcjHTmGY/0.jpg" alt="GitHub Copilot: Your AI Pair Programmer" width="200"><br>
                GitHub Copilot: Your AI Pair Programmer
            </a>
        </li>
        <li>
            <a href="https://www.youtube.com/watch?v=4KqUvG8HPYo" target="_blank">
                <img src="https://img.youtube.com/vi/4KqUvG8HPYo/0.jpg" alt="How to use GitHub Copilot - Full Demo" width="200"><br>
                How to use GitHub Copilot - Full Demo
            </a>
        </li>
        <li>
            <a href="https://www.youtube.com/watch?v=0RCbYgSsn5I" target="_blank">
                <img src="https://img.youtube.com/vi/0RCbYgSsn5I/0.jpg" alt="GitHub Copilot: Is it worth it?" width="200"><br>
                GitHub Copilot: Is it worth it?
            </a>
        </li>
        <li>
            <a href="https://www.youtube.com/watch?v=8yLlwITMRDE" target="_blank">
                <img src="https://img.youtube.com/vi/8yLlwITMRDE/0.jpg" alt="GitHub Copilot - AI Code Completion" width="200"><br>
                GitHub Copilot - AI Code Completion
            </a>
        </li>
        <li>
            <a href="https://www.youtube.com/watch?v=3XzLwmI3-1M" target="_blank">
                <img src="https://img.youtube.com/vi/3XzLwmI3-1M/0.jpg" alt="GitHub Copilot: Productivity Boost or Security Risk?" width="200"><br>
                GitHub Copilot: Productivity Boost or Security Risk?
            </a>
        </li>
    </ul>
    """

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