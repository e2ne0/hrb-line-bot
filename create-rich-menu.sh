curl -v -X POST https://api.line.me/v2/bot/richmenu \
-H 'Authorization: Bearer 6yNy7TqSZDYbYo98fd2M0nZ9tMyXxaeQvtKMWo/+YOroOUwM0ghQgAHqRrDDEwxJ7XvCG2FS/+k4yNev17o5vQFlgQw8qT8rmA6j/us4lw6kHECLAzT/CaboZbTYqumbFnfHMoEWOXVXpeJcP0FiUwdB04t89/1O/w1cDnyilFU=' \
-H 'Content-Type: application/json' \
-d \
'{
    "size": {
      "width": 2500,
      "height": 843
    },
    "selected": false,
    "name": "richmenu-demo-1",
    "chatBarText": "LINE圖文選單範例",
    "areas": [
      {
        "bounds": {
          "x": 0,
          "y": 0,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "message",
          "label": "文字",
          "text": "Hello, World!"
        }
      },
      {
        "bounds": {
          "x": 833,
          "y": 0,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "uri",
          "label": "網址",
          "uri": "https://www.google.com/"
        }
      },
      {
        "bounds": {
          "x": 1666,
          "y": 0,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "location",
          "label": "位置"
        }
      }
   ]
}'