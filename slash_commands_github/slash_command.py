
from flask import Flask, request, Response
import requests
from slash_command_method import payload_handler

## Create Flask server app that will handle and respond to slash command payloads 
app = Flask(__name__)

verif_token = ''

## Create endppoint where Slack sends the payloads for the /command invocation
@app.route('/slash_command', methods=['POST'])
def slash_command_handler():
    ## Check it's coming from Slack
    if request.form.get('token') == verif_token:
        ## Put it in a dictionary format so we can parse it
        incoming_payl = request.form.to_dict()
        ## Send the payload to the payload_handler
        my_response = payload_handler(incoming_payl)
        return Response(''), 200
    else:
        return Response('Invalid token'), 400

## Start app and debugging
if __name__== "__main__":
    app.run(debug=True)

