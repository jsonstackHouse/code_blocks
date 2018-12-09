import requests
from flask import request, Response, jsonify
import random

def payload_handler(payload):
    # Create buttons message attachment and send message to Slack
    button_builder = {
        "text" : "Pick Option one or Option two",
        "attachments" : [
            {
                "fallback" : "Something went wrong",
                "callback_id" : "buttons",
                "attachment_type" : "default",
                "actions" : [
                    {
                        "name" : "Option One",
                        "text" : "Option One",
                        "type" : "button",
                        "value": "Option One"
                    },
                    {
                        "name" : "Option Two",
                        "text" : "Option Two",
                        "type" : "button",
                        "value": "Option Two"
                    }
                ]
            }
        ]
    }
    url = payload['response_url']
    response = requests.request("POST", url=url, json=button_builder)

def actions_payload_handler(payload):
    ##Un-comment to see payload
    # print(payload)

    # Check the action is related to button clicks. Callback_id is the switcher for this
    if payload["callback_id"] == 'buttons':
        ## Get value of button clicked
        instruction = payload["actions"][0].get("value")
        ## Create log of the button clicked
        log_output = {
        "text" : "You chose " + str(instruction)
        }
        url = payload["response_url"]
        response = requests.request("POST", url=url, json=log_output)
        return(""), 200
    else:
        return("You didn't choose correctly"), 400

