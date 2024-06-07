from flask import Flask, request
import control_LED

app = Flask(__name__)

@app.route('/led', methods=['POST'])
def control_LED_color():
    """
    LEDを制御するためのエンドポイント
    リクエストボディに 'state' を含める必要があります
    例: { "state": "on" }
    """
    data = request.get_json()
    state = data.get('state')
    if state in ['on', 'off']:
        control_LED.change_color(state)
        return "LED turned {}".format(state), 200
    return "Invalid state", 400

if __name__ == '__main__':
    # サーバーを0.0.0.0:5000で起動
    app.run(host='0.0.0.0', port=5000)

