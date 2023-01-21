from flask import Flask
import sys


app = Flask(__name__)
is_healthy = True

@app.route("/myevent", methods=['POST'])
def event():
    print("Hello from binding!", flush=True)

    return "Event Processed!"


@app.route("/crash", methods=['POST'])
def crash():
    print("boom!", flush=True)
    global is_healthy
    is_healthy = False
    return "healthz will hang up"

@app.route("/healthz", methods=['GET'])
def healthz():
    if is_healthy:
        return "ok"
    raise Exception("unhealthy")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
