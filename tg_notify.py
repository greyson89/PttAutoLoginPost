import requests


def send_telegram_message(text: str, token: str, user_id: str) -> bool:
    """發送 Telegram 訊息

    Args:
        text: 要發送的訊息內容
        token: Telegram Bot Token
        user_id: Telegram 使用者 ID

    Returns:
        bool: 發送是否成功
    """
    try:
        api_url = f'https://api.telegram.org/bot{token}/sendMessage'
        response = requests.post(api_url, data={
            'chat_id': user_id,
            'text': text
        }, timeout=10)

        if response.status_code == 200:
            print(f"Telegram 訊息發送成功: {text}")
            return True
        else:
            print(f"Telegram 訊息發送失敗，狀態碼: {response.status_code}")
            return False

    except Exception as e:
        print(f"發送 Telegram 訊息時發生錯誤: {e}")
        return False
