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

f = [True,True,True,False,False]

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

d = ''
#handle postback
@handler.add(PostbackEvent)

def handle_postback(event):

    d = event.postback.data
    if d[d.find('action=')+len('action='):d.rfind('&')] == 'follow':
        num = int(d.split('itemid=')[1])
        global f
        f[num] = not f[num]
        if f[num] == False:
            # line_bot_api.reply_message(event.reply_token, unfollow(d))
            unfollow(d)
    
def unfollow(mydata = None):
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=ButtonsTemplate(
            title='已取消追蹤',
            text='\n',
            actions=[
                PostbackAction(
                    label=followText(0)[1],
                    data='action=follow&itemid='#+mydata.split('itemid=')[1]
                ),
            ]
        )
    )
    return message

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == '收藏職缺':
        line_bot_api.reply_message(event.reply_token, follow())
    
    if event.message.text == '線上真人諮詢':
        line_bot_api.reply_message(event.reply_token, onlineHumanContact())

    if event.message.text == '我的履歷':
        line_bot_api.reply_message(event.reply_token, myResume())

    if event.message.text == '瀏覽履歷庫':
        line_bot_api.reply_message(event.reply_token, viewMyResume())

    if event.message.text == '最新職缺':
        line_bot_api.reply_message(event.reply_token, testFlex())

    if event.message.text == 'testrich':
        testRich(event.source.user_id)
    


def followText(num):
    global f
    if f[num]:
        return ['\n(追蹤中)','取消追蹤']
    else:
        return ['','重新追蹤']


def follow():
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='誠徵java工程師1名',

                    text='地點：捷運市政府站附近'+followText(0)[0],
                    actions=[
                        PostbackAction(
                            label='直接應徵',
                            display_text='履歷投遞...',
                            data='action=buy&itemid=111'
                        ),
                        MessageAction(
                            label='線上真人諮詢',
                            text='線上真人諮詢'
                        ),
                        PostbackAction(
                            label=followText(0)[1],
                            data='action=follow&itemid=0'
                        ),
                    ]
                ),
                CarouselColumn(
                    title='誠徵 資深半導體工程師',
                    text='地點：桃園觀音'+followText(1)[0],
                    actions=[
                        PostbackAction(
                            label='直接應徵',
                            display_text='履歷投遞...',
                            data='action=buy&itemid=111'
                        ),
                        MessageAction(
                            label='線上真人諮詢',
                            text='線上真人諮詢'
                        ),
                        PostbackAction(
                            label=followText(1)[1],
                            data='action=follow&itemid=1'
                        ),
                    ]
                ),
                CarouselColumn(
                    title='誠徵 資深半自動工程師',
                    text='地點：信義101'+followText(2)[0],
                    actions=[
                        PostbackAction(
                            label='直接應徵',
                            display_text='履歷投遞...',
                            data='action=buy&itemid=111'
                        ),
                        MessageAction(
                            label='線上真人諮詢',
                            text='線上真人諮詢'
                        ),
                        PostbackAction(
                            label=followText(2)[1],
                            data='action=follow&itemid=2'
                        ),
                    ]
                ),
                CarouselColumn(
                    title='誠徵 資深java軟體工程師',
                    text='地點：松山區'+followText(3)[0],
                    actions=[
                        PostbackAction(
                            label='直接應徵',
                            display_text='履歷投遞...',
                            data='action=buy&itemid=111'
                        ),
                        MessageAction(
                            label='線上真人諮詢',
                            text='線上真人諮詢'
                        ),
                        PostbackAction(
                            label=followText(3)[1],
                            data='action=follow&itemid=3'
                        ),
                    ]
                ),
                CarouselColumn(
                    title='誠徵 網路管理員',
                    text='地點：新北市'+followText(4)[0],
                    actions=[
                        PostbackAction(
                            label='直接應徵',
                            display_text='履歷投遞...',
                            data='action=buy&itemid=111'
                        ),
                        MessageAction(
                            label='線上真人諮詢',
                            text='線上真人諮詢'
                        ),
                        PostbackAction(
                            label=followText(4)[1],
                            data='action=follow&itemid=4'
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
        alt_text='有一個重要職缺通知',
        contents=BubbleContainer(
            body=BoxComponent(
                layout='vertical',
                contents=[
                    BoxComponent(
                        layout='horizontal',
                        contents=[
                            BoxComponent(
                                layout='vertical',
                                contents=[
                                    ImageComponent(
                                        url='https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png?201912250718',
                                        aspect_mode='cover',
                                        size='full'
                                    )
                                ],
                                corner_radius='100px',
                                width='100px',
                                height='100px'
                            ),
                            BoxComponent(
                                layout='vertical',
                                contents=[
                                    TextComponent(
                                        contents=[
                                            SpanComponent(
                                                text='Apple',
                                                weight='bold',
                                                color='#000000'
                                            ),
                                            SpanComponent(
                                                text='     '
                                            ),
                                            SpanComponent(
                                                text='徵求熟悉Swift Metal Library之人才'
                                            )
                                        ],
                                        size='sm',
                                        wrap=True
                                    )
                                ]
                            )
                        ],
                        spacing='xl',
                        padding_all='20px'
                    )
                ],
                padding_all='0px'
            ),
            footer=BoxComponent(
                layout='vertical',
                contents=[
                    ButtonComponent(
                        style='primary',
                        color='#905c44',
                        action=URIAction(
                            label='我有好友',
                            uri='https://linecorp.com'
                        )
                    )
                ],
                spacing='sm',
                margin='xl'
            )
        )
    )
    return message

def testRich(user_id):
    line_bot_api.link_rich_menu_to_user(user_id, "richmenu-8a5d727213235686e76240ed2ebecc8e")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
