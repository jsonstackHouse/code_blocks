from flask import Flask, request, Response
import requests
import json
from events_methods import parse_event_data

oauth_token = ''
verif_token = ''

app = Flask(__name__)

## Create endpoint where we receive event payloads from Slack
@app.route('/events', methods=['POST'])
def events_endpoint_handler():
    # Get it in a dictionary format so we can parse it more easily
    data = json.loads(request.data)
    ## Perform the security handshake to set up events URL with Slack
    if 'challenge' in data:
        return Response(data['challenge']), 200
    #Check each payload is linked to our verification token
    elif data["token"] == verif_token:
        #Check it's an event payload
        if data['type'] == 'event_callback':
        ## Send payload to our event handler function
            parse_event_data(data)
            return Response(''), 200
    else:
        return Response('Not a valid request'), 400



if __name__ == '__main__':
    app.run(debug=True)

