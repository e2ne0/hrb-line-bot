import requests
import json

headers = {"Authorization":"Bearer 6yNy7TqSZDYbYo98fd2M0nZ9tMyXxaeQvtKMWo/+YOroOUwM0ghQgAHqRrDDEwxJ7XvCG2FS/+k4yNev17o5vQFlgQw8qT8rmA6j/us4lw6kHECLAzT/CaboZbTYqumbFnfHMoEWOXVXpeJcP0FiUwdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
    "size": {"width": 2500, "height": 1686},
    "selected": "true",
    "name": "Test Rich Menu",
    "chatBarText": "Test Rich Menu",
    "areas":[
        {
          "bounds": {"x": 0, "y": 0, "width": 833, "height": 843},
          "action": {"type": "message", "text": "收藏職缺"}
        },
        {
          "bounds": {"x": 833, "y": 0, "width": 833, "height": 843},
          "action": {"type": "message", "text": "我的履歷"}
        },
        {
          "bounds": {"x": 1666, "y": 0, "width": 834, "height": 843},
          "action": {"type": "message", "text": "搜尋職缺"}
        },
        {
          "bounds": {"x": 0, "y": 843, "width": 833, "height": 843},
          "action": {"type": "message", "text": "最新職缺"}
        },
        {
          "bounds": {"x": 833, "y": 843, "width": 833, "height": 843},
          "action": {"type": "message", "text": "常見問題"}
        },
        {
          "bounds": {"x": 1666, "y": 843, "width": 834, "height": 843},
          "action": {"type": "message", "text": "申請成為FA"}
        }
    ]
  }


req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)

