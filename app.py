
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

DASHBOARD = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DevOps Control Center</title>
<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #0b1120;
    color: #f1f5f9;
}

header {
    padding: 28px 7%;
    border-bottom: 1px solid #263449;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
}

h1 { margin: 0; font-size: 26px; }

.subtitle {
    color: #94a3b8;
    margin-top: 8px;
}

.pill {
    color: #86efac;
    background: #123324;
    border: 1px solid #226b45;
    padding: 9px 14px;
    border-radius: 30px;
    font-size: 13px;
}

main {
    max-width: 1100px;
    margin: 35px auto;
    padding: 0 22px;
}

h2 {
    font-size: 19px;
    margin-bottom: 18px;
}

.grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 18px;
}

.card {
    background: #141e30;
    border: 1px solid #263449;
    border-radius: 15px;
    padding: 24px;
}

.label {
    color: #94a3b8;
    font-size: 14px;
}

.value {
    font-size: 23px;
    font-weight: bold;
    margin: 13px 0 8px;
}

.green { color: #4ade80; }
.blue { color: #7dd3fc; }
.purple { color: #c4b5fd; }
.yellow { color: #fcd34d; }

.detail {
    color: #94a3b8;
    font-size: 13px;
    line-height: 1.6;
}

.panel { margin-top: 24px; }

.steps {
    display: grid;
    gap: 13px;
}

.step {
    background: #141e30;
    border: 1px solid #263449;
    border-radius: 10px;
    padding: 16px;
    display: flex;
    justify-content: space-between;
    gap: 12px;
}

a {
    color: #7dd3fc;
    text-decoration: none;
}

a:hover { text-decoration: underline; }

footer {
    text-align: center;
    padding: 28px;
    color: #64748b;
    font-size: 12px;
}

@media (max-width: 600px) {
    .grid { grid-template-columns: 1fr; }
    header { padding: 22px; }
    .value { font-size: 21px; }
}
</style>
</head>

<body>

<header>
    <div>
        <h1>⚡ DevOps Control Center</h1>
        <div class="subtitle">
            Flask · Docker · GitHub Actions · AWS EC2
        </div>
    </div>
    <span class="pill">● APPLICATION ONLINE</span>
</header>

<main>
    <h2>Deployment Overview</h2>

    <section class="grid">
        <div class="card">
            <div class="label">Application Status</div>
            <div class="value green">● Healthy</div>
            <div class="detail">Flask web application</div>
        </div>

        <div class="card">
            <div class="label">CI/CD Pipeline</div>
            <div class="value blue">GitHub Actions</div>
            <div class="detail">
                Automated testing and deployment
            </div>
        </div>

        <div class="card">
            <div class="label">Containerization</div>
            <div class="value purple">Docker</div>
            <div class="detail">my-flask-container</div>
        </div>

        <div class="card">
            <div class="label">Cloud Infrastructure</div>
            <div class="value yellow">AWS EC2</div>
            <div class="detail">Application port: 5000</div>
        </div>
    </section>

    <section class="panel">
        <h2>Deployment Pipeline</h2>

        <div class="steps">
            <div class="step">
                <span>01 · Source Code</span>
                <span class="green">GitHub</span>
            </div>

            <div class="step">
                <span>02 · Automated Tests</span>
                <span class="green">pytest</span>
            </div>

            <div class="step">
                <span>03 · Image Build</span>
                <span class="blue">Docker</span>
            </div>

            <div class="step">
                <span>04 · Cloud Deployment</span>
                <span class="purple">AWS EC2</span>
            </div>
        </div>
    </section>

    <section class="card panel">
        <h2>Health Check</h2>

        <p class="detail">
            Verify that the application responds.
        </p>

        <a href="/health" target="_blank">
            Open health check →
        </a>

        <p class="detail">
            Source repository:
            <a
                href="https://github.com/swastikajagtap90-svg/unit-3-mini-project-devops"
                target="_blank">
                View on GitHub →
            </a>
        </p>
    </section>
</main>

<footer>
    UNIT 3 MINI PROJECT · DEVOPS DASHBOARD
</footer>

</body>
</html>
"""


@app.route("/")
def home():
    return jsonify({
        "message": "Hello! My DevOps mini-project is running.",
        "status": "success"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

