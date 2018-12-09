import requests


oauth_access_token = ""
bot_token = ""

def send_method():
    headers = {
        "Content-type" : "application/json",
        "Authorization" : "Bearer " + bot_token
        }
    json = {
     "text" : "",
     "channel" : "C9ZDU9PK7",
     "as_user" : True
    }
    method = "chat.postMessage"
    url = "https://slack.com/api/" + method
    send_request = requests.request("POST", url=url, headers=headers, json=json)
    ## Un-comment to check response
    #print(send_request.text)
    return

send_method()