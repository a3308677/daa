from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('1SmGKlg59CG8VNJQFGSRoHhUbbbtYnyoePC0S3DfEbZkYS0kKfueCEYNQz6L/zPbywLbATf1H6BAWnr+K2Ii5U8Bf5JddLN8LklJ/E74wgS6LP3I4cYTEeNVIPE2vu79qBdsaIwxRfzlkFocAWmIzAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9f40c12980e63edb3732a2f7aa4ea7a2')


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text=='吃屎':    
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=str(multiprocessing.cpu_count())))
        return 0
   
    
import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
