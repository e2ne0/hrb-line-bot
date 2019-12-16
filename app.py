import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

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
    if event.message.text == '追蹤中職缺':
        line_bot_api.reply_message(event.reply_token, follow())
    
    

def follow():
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='誠徵java工程師1名',
                    text='地點：捷運市政府站附近\n（追蹤中）',
                    actions=[
                        PostbackAction(
                            label='直接應徵',
                            display_text='履歷投遞...',
                            data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='線上真人諮詢',
                            text='線上真人諮詢'
                        ),
                        PostbackAction(
                            label='取消追蹤',
                            display_text='取消追蹤',
                            data='action=buy&itemid=1'
                        ),
                    ]
                ),
                CarouselColumn(
                    title='誠徵 資深半導體工程師',
                    text='地點：桃園觀音\n（追蹤中）',
                    actions=[
                        PostbackAction(
                            label='直接應徵',
                            display_text='履歷投遞...',
                            data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='線上真人諮詢',
                            text='線上真人諮詢'
                        ),
                        PostbackAction(
                            label='取消追蹤',
                            display_text='取消追蹤',
                            data='action=buy&itemid=1'
                        ),
                    ]
                ),
                CarouselColumn(
                    title='誠徵 資深半自動工程師',
                    text='地點：信義101\n（FA聯繫中）',
                    actions=[
                        PostbackAction(
                            label='直接應徵',
                            display_text='履歷投遞...',
                            data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='線上真人諮詢',
                            text='線上真人諮詢'
                        ),
                        PostbackAction(
                            label='取消追蹤',
                            display_text='取消追蹤',
                            data='action=buy&itemid=1'
                        ),
                    ]
                ),
                CarouselColumn(
                    title='誠徵 資深java軟體工程師',
                    text='地點：松山區',
                    actions=[
                        PostbackAction(
                            label='直接應徵',
                            display_text='履歷投遞...',
                            data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='線上真人諮詢',
                            text='線上真人諮詢'
                        ),
                        PostbackAction(
                            label='取消追蹤',
                            display_text='取消追蹤',
                            data='action=buy&itemid=1'
                        ),
                    ]
                ),
                CarouselColumn(
                    title='誠徵 網路管理員',
                    text='地點：新北市',
                    actions=[
                        PostbackAction(
                            label='直接應徵',
                            display_text='履歷投遞...',
                            data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='線上真人諮詢',
                            text='線上真人諮詢'
                        ),
                        PostbackAction(
                            label='取消追蹤',
                            display_text='取消追蹤',
                            data='action=buy&itemid=1'
                        ),
                    ]
                ),
            ]
        )
    )
    return message
    


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
