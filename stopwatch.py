from flask import Flask, jsonify, request
import time

app = Flask(__name__)

stopwatch = {
    "start_time": None,
    "elapsed_time": 0,
    "running": False,
}

@app.route('/start', methods=['POST'])
def start_stopwatch():
    if not stopwatch["running"]:
        stopwatch["start_time"] = time.time() - stopwatch["elapsed_time"]
        stopwatch["running"] = True
        return jsonify({"message": "Stopwatch started"})
    else:
        return jsonify({"message": "Stopwatch is already running"})

@app.route('/stop', methods=['POST'])
def stop_stopwatch():
    if stopwatch["running"]:
        stopwatch["elapsed_time"] = time.time() - stopwatch["start_time"]
        stopwatch["running"] = False
        return jsonify({"message": "Stopwatch stopped", "elapsed_time": stopwatch["elapsed_time"]})
    else:
        return jsonify({"message": "Stopwatch is not running"})

@app.route('/reset', methods=['POST'])
def reset_stopwatch():
    stopwatch["start_time"] = None
    stopwatch["elapsed_time"] = 0
    stopwatch["running"] = False
    return jsonify({"message": "Stopwatch reset"})

@app.route('/status', methods=['GET'])
def get_status():
    if stopwatch["running"]:
        elapsed_time = time.time() - stopwatch["start_time"]
        return jsonify({"running": True, "elapsed_time": elapsed_time})
    else:
        return jsonify({"running": False, "elapsed_time": stopwatch["elapsed_time"]})

if __name__ == '__main__':
    app.run(debug=True)
