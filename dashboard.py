from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def home():

    logs = []

    with open("attacker.json", "r") as f:
        for line in f:
            logs.append(json.loads(line))

    html = ""

    for log in logs:

        html += f"""
        <div style="
            border:1px solid gray;
            padding:10px;
            margin:10px;
            background:#222;
            color:white;
        ">

        <p>IP: {log['ip']}</p>
        <p>USERNAME: {log['username']}</p>
        <p>PASSWORD: {log['password']}</p>
        <p>TIME: {log['time']}</p>
        <p>STATUS: {log['status']}</p>

        </div>
        """

    return f"""
    <html>

    <head>
        <title>Honeypot Dashboard</title>
    </head>

    <body style="background:black">

        <h1 style="color:red">
            Honeypot Dashboard
        </h1>

        {html}

    </body>

    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
