from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/check_link")
def index():
    code = request.args.get("code")
    print code
    return code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)