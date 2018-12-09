import requests
from flask import request, Response

def payload_handler(payload):
    ## Get the name of the user who invoked the slash command
    username_linked = "<@" + str(payload["user_id"]) + ">"
    ## Get text from payload
    text = payload['text']
    ## Build log message to send back to Slack
    return_message = {
        "text" : "Hello " + str(username_linked) + ", you said... " + "\n" + "\n" + "'"  + text + "'"
    }
    ##Use response URL from payload to respond to slash command directly
    url = payload["response_url"]
    response_to_slack = requests.request("POST", url=url, json=return_message)