from flask import Response
import requests

oatuh_token = ""

def parse_event_data(data):
    ## Un-comment to check payload
    # print(data)
    
    ## Grab the type of event we received
    event = data["event"].get("type")
    ## Check to see if the event was actioned by a bot or non-bot user
    if "bot_id" in data["event"]:
        user = data["event"].get("bot_id")
    else:
        user = data["event"].get("user")
    ## Choose event to listen out for. If it's the correct event we log it to channel CCJ92GUC9
    if event == "reaction_added":
        log_message = {
            "text": "The event " + str(event) + " just occured." + " Actioned by user " + str(user),
            'channel': 'CCJ92GUC9'
        }
        headers = {
            'content-type': 'application/json',
            'Authorization': 'Bearer ' + oauth_token
        }
        url = 'https://slack.com/api/chat.postMessage'
        send_log_to_channel = requests.request("POST", url=url, headers=headers, json=log_message)
        ## Un-comment to check response coming from our app to Slack
        # print(send_log_to_channel.text)
    else: 
    ## If it's not, we log that it wasn't the right event but we got it
        print("We got an event we're not worried about")

