from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def home():

    try:

        result = subprocess.check_output(
            ["python","dgt_fetch.py"]
        ).decode("cp949")

        lines = result.split("\n")

        ships = []

        for line in lines:
            if "|" in line:
                ships.append(line)

        return render_template("index.html",ships=ships)

    except Exception as e:

        return f"에러 발생: {e}"


if __name__ == "__main__":
    app.run(debug=True)