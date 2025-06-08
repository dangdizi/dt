from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = "6766286762:AAHqicKqezqAMRYSgPc7lKzt4RokvDsJxpc"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route('/sendTelegram', methods=['POST'])
def send_telegram():
    data = request.form or request.json
    chat_id = data.get('chat_id')
    text = data.get('text')
    if not chat_id or not text:
        return jsonify({"error": "chat_id và text bắt buộc"}), 400

    payload = {
        'chat_id': chat_id,
        'text': text
    }
    resp = requests.post(TELEGRAM_API_URL, data=payload)
    return jsonify(resp.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
