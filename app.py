from flask import Flask, request, jsonify
import requests

app = Flask (__name__)

BOT_TOKEN = "6766286762:AAHqicKqezqAMRYSgPc7lKzt4RokvDsJxpc"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


@app.route('/', methods=['GET'])
def send_telegram():
        chat_id = "1880412634"
        text = "messager"
        payload = {
                'chat_id': chat_id,
                'text': text
        }
        resp = requests.post(TELEGRAM_API_URL, data=payload)
        return jsonify(resp.json())

        if __name__ == "__main__":
        app.run(host="0.0.0.0", port=10000)
