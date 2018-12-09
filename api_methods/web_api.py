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
     "channel" : "",
     "as_user" : True
    }
    method = ""
    url = "https://slack.com/api/" + method
    send_request = requests.request("POST", url=url, headers=headers, json=json)
    ## Un-comment to see response
    #print(send_request.text)
    return

#Call function
send_method()