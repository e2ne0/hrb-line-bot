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
    
    if event.message.text == '線上真人諮詢':
        line_bot_api.reply_message(event.reply_token, onlineHumanContact())

    if event.message.text == '我的履歷':
        line_bot_api.reply_message(event.reply_token, myResume())

    if event.message.text == '瀏覽履歷庫':
        line_bot_api.reply_message(event.reply_token, viewMyResume())

    if event.message.text == 'testflex':
        line_bot_api.reply_message(event.reply_token, testFlex())

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
    
def onlineHumanContact():
    message = TextSendMessage('後台建置中...\n稍待片刻，將由相關人士與您聯絡')
    return message

def myResume():
    message = TemplateSendMessage(
		alt_text='Carousel template',
        template=ButtonsTemplate(
            title='我的履歷',
            text='選擇新增一份律例或挑選現有的履歷',
            actions=[
                URIAction(
                    label='新增新的一份履歷',
                    uri='https://linebot-human-resource.netlify.com/create-resume'
                ),
                MessageAction(
                    label='瀏覽履歷庫',
                    text='瀏覽履歷庫'
                ),
            ]
        )
    )
    return message

def viewMyResume():
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='履歷1',
                    text='Lorem lpsum is simply dummy test',
                    actions=[
						URIAction(
                        	label='編輯履歷',
                        	uri='https://linebot-human-resource.netlify.com/create-resume'
                    	)
					]
                ),
                CarouselColumn(
                    title='履歷2',
                    text='Lorem lpsum is simply dummy test',
                    actions=[
						URIAction(
                        	label='編輯履歷',
                        	uri='https://linebot-human-resource.netlify.com/create-resume'
                    	)
					]
                ),
                CarouselColumn(
                    title='履歷3',
                    text='Lorem lpsum is simply dummy test',
                    actions=[
						URIAction(
                        	label='編輯履歷',
                        	uri='https://linebot-human-resource.netlify.com/create-resume'
                    	)
					]
                )
            ]
        )
    )
    return message

def testFlex():
    message = FlexSendMessage(
        alt_text='hello',
        contents=BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://i.imgur.com/a8MmG2i.png',
                size='full',
                aspect_ratio='1:1',
                aspect_mode='cover',
                action=URIAction(uri='https://imgur.com/gallery/a8MmG2i', label='label')
            )
        )
    )
    return message

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
