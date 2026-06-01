from flask import Flask, send_file
import json
from collections import Counter

app = Flask(__name__)
@app.route("/download")

def download_logs():

    return send_file(
        "attacker.json",
        as_attachment=True
    )

@app.route("/")
def home():

    logs = []

    # doc file json
    with open("attacker.json", "r") as f:
        for line in f:
            logs.append(json.loads(line))

    # tong so attack
    total_attacks = len(logs)

    # dem top ip
    ips = [log["ip"] for log in logs]
    top_ips = Counter(ips)

    # tao bang html
    table_rows = ""

    for log in logs:

        status = log["status"]

        # mau status
        if status == "Welcome Ubuntu":
            color = "lime"

        elif status == "blocked":
            color = "yellow"

        else:
            color = "red"

        table_rows += f"""
        <tr>

            <td>{log['ip']}</td>
            <td>{log['country']}</td>
            <td>{log['city']}</td>
            <td>{log['isp']}</td>

            <td>{log['username']}</td>
            <td>{log['password']}</td>
            <td>{log['time']}</td>

            <td style="color:{color}">
                {status}
            </td>

        </tr>
        """

    # top ip html
    ip_html = ""

    for ip, count in top_ips.items():

        ip_html += f"""
        <li class="list-group-item bg-dark text-light">
            {ip} → {count} attempts
        </li>
        """

    return f"""

    <html>

    <head>

        <title>Honeypot Dashboard</title>

        <!-- auto refresh -->
        <meta http-equiv="refresh" content="5">

        <!-- bootstrap -->
        <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
        rel="stylesheet">

    </head>

    <body class="bg-dark text-light">

    <div class="container mt-4">

        <h1 class="text-danger">
            Honeypot Dashboard
        </h1>
        <a href="/download" class="btn btn-danger">
            Download Logs
        </a>

        <br><br>
        <hr>

        <h3>
            Total attacks: {total_attacks}
        </h3>

        <hr>

        <h3>Top attacker IP</h3>

        <ul class="list-group">
            {ip_html}
        </ul>

        <br>

        <h3>Attack Logs</h3>

        <table class="table table-dark table-striped table-bordered">

            <thead>

                <tr>
                    <th>IP</th>
                    <th>COUNTRY</th>
                    <th>CITY</th>
                    <th>ISP</th>
                    <th>USERNAME</th>
                    <th>PASSWORD</th>
                    <th>TIME</th>
                    <th>STATUS</th>
                </tr>

            </thead>

            <tbody>

                {table_rows}

            </tbody>

        </table>

    </div>

    </body>

    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)