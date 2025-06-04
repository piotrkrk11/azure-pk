from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <body style="background: linear-gradient(135deg, #24292e 0%, #0366d6 100%); min-height:100vh; color: #fff; font-family: Arial, sans-serif;">
    <div style="text-align:center; padding: 30px 0;">
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo" width="80" style="vertical-align:middle; margin-right:20px;">
        <img src="https://learn.microsoft.com/en-us/media/logos/logo-azure.svg" alt="Azure Logo" width="120" style="vertical-align:middle; margin-right:20px;">
        <img src="https://copilot.github.com/images/copilot-logo.svg" alt="Copilot Logo" width="120" style="vertical-align:middle;">
        <h1 style="margin-top:30px;">Hello, Azure Workshop 2025!</h1>
        <h2>Najciekawsze filmy o GitHub Copilot na YouTube</h2>
    </div>
    <ul style="list-style:none; display:flex; flex-wrap:wrap; justify-content:center; gap:30px; padding:0;">
        <li>
            <a href="https://www.youtube.com/watch?v=SGUCcjHTmGY" target="_blank" style="text-decoration:none; color:#fff;">
                <img src="https://img.youtube.com/vi/SGUCcjHTmGY/0.jpg" alt="GitHub Copilot: Your AI Pair Programmer" width="220" style="border-radius:12px; box-shadow:0 4px 16px #0006;"><br>
                <b>GitHub Copilot: Your AI Pair Programmer</b>
            </a>
        </li>
        <li>
            <a href="https://www.youtube.com/watch?v=4KqUvG8HPYo" target="_blank" style="text-decoration:none; color:#fff;">
                <img src="https://img.youtube.com/vi/4KqUvG8HPYo/0.jpg" alt="How to use GitHub Copilot - Full Demo" width="220" style="border-radius:12px; box-shadow:0 4px 16px #0006;"><br>
                <b>How to use GitHub Copilot - Full Demo</b>
            </a>
        </li>
        <li>
            <a href="https://www.youtube.com/watch?v=0RCbYgSsn5I" target="_blank" style="text-decoration:none; color:#fff;">
                <img src="https://img.youtube.com/vi/0RCbYgSsn5I/0.jpg" alt="GitHub Copilot: Is it worth it?" width="220" style="border-radius:12px; box-shadow:0 4px 16px #0006;"><br>
                <b>GitHub Copilot: Is it worth it?</b>
            </a>
        </li>
        <li>
            <a href="https://www.youtube.com/watch?v=8yLlwITMRDE" target="_blank" style="text-decoration:none; color:#fff;">
                <img src="https://img.youtube.com/vi/8yLlwITMRDE/0.jpg" alt="GitHub Copilot - AI Code Completion" width="220" style="border-radius:12px; box-shadow:0 4px 16px #0006;"><br>
                <b>GitHub Copilot - AI Code Completion</b>
            </a>
        </li>
        <li>
            <a href="https://www.youtube.com/watch?v=3XzLwmI3-1M" target="_blank" style="text-decoration:none; color:#fff;">
                <img src="https://img.youtube.com/vi/3XzLwmI3-1M/0.jpg" alt="GitHub Copilot: Productivity Boost or Security Risk?" width="220" style="border-radius:12px; box-shadow:0 4px 16px #0006;"><br>
                <b>GitHub Copilot: Productivity Boost or Security Risk?</b>
            </a>
        </li>
    </ul>
    <div style="margin: 40px auto 0 auto; max-width: 600px; background: #fff2; border-radius: 16px; box-shadow: 0 4px 24px #0003; padding: 24px; text-align: center;">
        <img src="https://www.trek2summit.com/wp-content/uploads/2022/06/logo-trek2summit.png" alt="Trek2Summit" width="180" style="margin-bottom: 16px;">
        <h2 style="color:#fff; margin-bottom:10px;">Oferta firmy Trek2Summit</h2>
        <p style="color:#fff; font-size:18px;">
            Szukasz wsparcia w chmurze, DevOps lub automatyzacji? <br>
            Trek2Summit to zespół ekspertów Azure, GitHub i AI, który pomoże Twojej firmie wejść na wyższy poziom cyfrowej transformacji.<br>
            <a href="https://trek2summit.com" target="_blank" style="color:#ffd700; font-weight:bold; text-decoration:underline;">Sprawdź ofertę Trek2Summit &rarr;</a>
        </p>
    </div>
    </body>
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