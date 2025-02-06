from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/system/monitor', methods=['GET'])
def system_monitor():
    return jsonify({"status": "Running smoothly"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
