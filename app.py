from flask import Flask,jsonify,request
from decouple import config
from twilio.rest import Client
from flask_cors import CORS

account_ssid=config('TWILIO_ACCOUNT_SID')
account_auth_token=config('TWILIO_AUTH_TOKEN')




app=Flask(__name__)

CORS(app)


client=Client(account_ssid,account_auth_token)


@app.route('/')
def index():
    return jsonify({"message":"Hello You"})



@app.route('/send',methods=['POST'])
def send():
    data=request.get_json()

    body=data.get('body')

    sender="+15512265357"

    to=data.get('to')

    message=client.messages.create(
            body=body,
            from_=sender,
            to=to)

    print(message.sid)


    return jsonify({"message":"message sent successfully"})






if __name__ == "__main__":
    app.run()
