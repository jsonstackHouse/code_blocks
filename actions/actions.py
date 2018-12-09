
from flask import Flask, request, Response
import requests, json
from actions_methods import payload_handler, actions_payload_handler

app = Flask(__name__)

verif_token = ""
oauth_access_token = ""

## Create endpoint where Slack sends the payloads for the /buttons slash command
@app.route('/buttons', methods=['POST'])
def slash_command_endpoint_handler():
    ## Check it's coming from Slack
    if request.form.get('token') == verif_token:
        #Put it in a dictionary format so it's easier to parse
        incoming_payl = request.form
        #Send it to our payload handler function
        payload_handler(incoming_payl)
        return Response(''), 200
    else:
        return Response('Invalid token'), 400

## Create endpoint for actions payloads
@app.route('/actions', methods=['POST'])
def actions_endpoint_function():
    #Put it in a dictionary format so it's easier to parse
    actions_payl = json.loads(request.form.get("payload"))
    
    #Check the payload is coming from Slack
    if actions_payl["token"] == verif_token:
        #Send it to our actions payload handler
        actions_payload_handler(actions_payl)
    else:
        return("Incorrect token"), 400


## Start app and debugging
if __name__== "__main__":
    app.run(debug=True)
