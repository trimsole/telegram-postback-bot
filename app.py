from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7901864019:AAESDmULK8q_gUoxwLbr8Sd5iRZv2vcarnI'
CHAT_ID = '458366450'

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=payload)

@app.route('/callback', methods=['POST', 'GET'])
def callback():
    data = request.form if request.method == 'POST' else request.args

    message = f"""📩 Новый постбек:
👤 Trader ID: {data.get("trader_id", "")}
🆔 Click ID: {data.get("click_id", "")}
🌐 Site ID: {data.get("site_id", "")}
📨 Регистрация: {data.get("reg", "")}
✅ Подтверждение email: {data.get("conf", "")}
💳 Первый депозит: {data.get("ftd", "")}
💰 Повторный депозит: {data.get("dep", "")}
💸 Сумма депозита: {data.get("sumdep", "")}
📊 Всего депозитов: {data.get("totaldep", "")}
🔗 Партнёр: {data.get("a", "")}
📋 Кампания: {data.get("ac", "")}
"""
    send_telegram_message(message)
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
