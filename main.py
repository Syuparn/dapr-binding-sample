from flask import Flask
import sys


app = Flask(__name__)


@app.route("/myevent", methods=['POST'])
def event():
    print("Hello from binding!", flush=True)

    return "Event Processed!"


@app.route("/crash", methods=['POST'])
def crash():
    print("boom!", flush=True)

    sys.exit(1)

@app.route("/healthz", methods=['GET'])
def healthz():
    return "ok"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
