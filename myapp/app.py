from flask import Flask, jsonify, render_template_string
import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>My Azure App</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Courier New', monospace;
      background: #0a0a0a;
      color: #00ff88;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }
    h1 { font-size: 2.5rem; letter-spacing: 0.3rem; margin-bottom: 1rem; }
    p { color: #888; margin: 0.5rem 0; }
    .badge {
      margin-top: 2rem;
      padding: 0.5rem 1.5rem;
      border: 1px solid #00ff88;
      border-radius: 4px;
      font-size: 0.85rem;
      color: #00ff88;
    }
    .ping { margin-top: 1rem; color: #555; font-size: 0.75rem; }
  </style>
</head>
<body>
  <h1>⚡ LIVE ON AZURE</h1>
  <p>Python + Flask app running.</p>
  <p>Deployed via Azure App Service.</p>
  <div class="badge">Azure for Students ✓</div>
  <p class="ping">GET /api/status — health check endpoint</p>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/api/status")
def status():
    return jsonify({
        "status": "ok",
        "time": datetime.datetime.utcnow().isoformat(),
        "app": "my-azure-python-app"
    })

if __name__ == "__main__":
    app.run(debug=False)
