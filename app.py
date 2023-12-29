from flask import Flask
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome():
    return (
        "<h1>Welcome to the Free Film Stock API Project</h1>"
        + "<p>Hit this endpoint with the filmstockId to get its info in JSON: /stocks/_stockId_</p>"
    )


@app.route("/stocks/<string:stock_id>", methods=["GET"])
def retrieve_stock(stock_id):
    try:
        with open(f"stockdb/{stock_id}.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return json.loads('{"error": "film stock not found"}')
    else:
        return data


if __name__ == "__main__":
    app.run()
