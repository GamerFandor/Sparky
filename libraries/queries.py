import json

# Get the content of 'bot.json'
def read_bot_data():
    with open(__file__[:-10].replace("\\", "/") + "../databases/bot.json", "r") as f:
        json_object = json.loads(f.read())
    return json_object
        
# Get the token of the bot from 'bot.json'
def get_token():
    return(read_bot_data()["TOKEN"])

# Get the status type from the 'bot.json'
def get_activity_type():
    return read_bot_data()["ACTIVITY_TYPE"]

# Get the status text from the 'bot.json'
def get_activity_text():
    return read_bot_data()["ACTIVITY_TEXT"]

# Get the deault role's id from 'bot.json'
def get_default_role():
    return(read_bot_data()["NEW_MEMBER_ROLE_ID"])

# Get the welcom channel's id from 'bot.json'
def get_welcome_channel():
    return(read_bot_data()["WELCOME_CHANNEL_ID"])

# Test queries locally
if __name__ == "__main__":
    print("Test queries")
    print("------------------------------")
    print(f"TOKEN              -> {get_token()}")
    print(f"Activity type      -> {get_activity_type()}")
    print(f"Activity text      -> {get_activity_text()}")
    print(f"Welcome channel ID -> {get_welcome_channel()}")
    print(f"Default role       -> {get_default_role()}")
