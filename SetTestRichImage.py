from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('6yNy7TqSZDYbYo98fd2M0nZ9tMyXxaeQvtKMWo/+YOroOUwM0ghQgAHqRrDDEwxJ7XvCG2FS/+k4yNev17o5vQFlgQw8qT8rmA6j/us4lw6kHECLAzT/CaboZbTYqumbFnfHMoEWOXVXpeJcP0FiUwdB04t89/1O/w1cDnyilFU=')

with open("image/test rich menu.png", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-8a5d727213235686e76240ed2ebecc8e", "image/png", f)
