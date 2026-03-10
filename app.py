from flask import Flask, render_template
from dgt_fetch import get_ships

app = Flask(__name__)

@app.route("/")
def home():

    try:

        ships = get_ships()

        return render_template("index.html", ships=ships)

    except Exception as e:

        return f"에러 발생: {e}"


if __name__ == "__main__":
    app.run()