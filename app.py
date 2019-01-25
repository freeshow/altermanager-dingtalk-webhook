from flask import Flask, request

app = Flask(__name__)


@app.route('/node_alert', methods=['POST', 'GET'])
def node_alert():
    if request.method == 'POST':
        post_json = request.get_json()
        print(post_json)
        return 'success'
    else:
        return 'weclome to use prometheus alertmanager dingtalk webhook server!'


@app.route('/pod_alert', methods=['POST', 'GET'])
def pod_alert():
    if request.method == 'POST':
        post_json = request.get_json()
        print(post_json)
        return 'success'
    else:
        return 'weclome to use prometheus alertmanager dingtalk webhook server!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555)
