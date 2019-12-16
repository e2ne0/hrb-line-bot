import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(
    '6yNy7TqSZDYbYo98fd2M0nZ9tMyXxaeQvtKMWo/+YOroOUwM0ghQgAHqRrDDEwxJ7XvCG2FS/+k4yNev17o5vQFlgQw8qT8rmA6j/us4lw6kHECLAzT/CaboZbTYqumbFnfHMoEWOXVXpeJcP0FiUwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('b28c6adb66067dad7c87c7853cfb32ea')

questNum = 0

tip = 0

start = False

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global questNum
    global tip
    global start
    ans = ['4581', '2486', '5206', '5340', '1235']
    questsURL = [
        'https://imgur.com/osHNXd9.jpg',
        'https://imgur.com/h6YyNbY.jpg',
        'https://imgur.com/RHEUTRx.jpg',
        'https://imgur.com/Ql0wB4b.jpg',
        'https://imgur.com/xXJCZes.jpg'
    ]

    tipsURL = [
        ['https://imgur.com/huqtjzT.jpg', 'https://imgur.com/NB4O7In.jpg'],
        ['https://imgur.com/fGMbFLX.jpg', 'https://imgur.com/OMuYolZ.jpg'],
        ['https://imgur.com/WNqv9rA.jpg', 'https://imgur.com/tp7S2Tn.jpg'],
        ['https://imgur.com/wwOojCl.jpg', 'https://imgur.com/B6Y4FjF.jpg'],
        ['https://imgur.com/SpsRdgy.jpg', 'https://imgur.com/7aMAHiq.jpg']
    ]
    if event.message.text == 'Start':
        questNum = 0
        tip = 0
        message = ImageSendMessage(
            original_content_url = questsURL[questNum],
            preview_image_url = questsURL[questNum]
        )
        line_bot_api.reply_message(event.reply_token, message)
        start = True
        return
    if start:
        if event.message.text == 'tip' or event.message.text == 'Tip':
            if tip < len(tipsURL[questNum]):
                message = ImageSendMessage(
                    original_content_url = tipsURL[questNum][tip],
                    preview_image_url = tipsURL[questNum][tip]
                )
                line_bot_api.reply_message(event.reply_token, message)
                tip += 1
                return
            else:
                message = TextSendMessage(text="已經用了所有提示了，\n再努力想想吧！")
                line_bot_api.reply_message(event.reply_token, message)
                return

        if event.message.text == ans[questNum]:
            if questNum == len(ans) - 1:
                start = False
                questNum = 0
                tip = 0
                message = TextSendMessage(text="答對了，挑戰結束！")
                line_bot_api.reply_message(event.reply_token, message)
                return
            
            tip = 0
            questNum += 1
            message = [TextSendMessage(text="答對了，下一題！"),ImageSendMessage(
            original_content_url = questsURL[questNum],
            preview_image_url = questsURL[questNum]
            )]
            line_bot_api.reply_message(event.reply_token, message)
            return
        for i in range(0,questNum + 1):
            if ans[i] == event.message.text:
                message = TextSendMessage(text="這是別題的答案吧")
                line_bot_api.reply_message(event.reply_token, message)
                return
        
    message = TextSendMessage(text="請輸入Start開始遊戲\n tip獲取提示\n 或是直接輸入答案")
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
