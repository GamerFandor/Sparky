import json

# Get the content of 'bot.json'
def read_bot_data():
    with open(__file__[:-10].replace("\\", "/") + "../databases/bot.json", "r", encoding = "utf8") as f:
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

# Get the content of 'users.json'
def read_users_data():
    with open(__file__[:-10].replace("\\", "/") + "../databases/users.json", "r", encoding = "utf8") as f:
        json_object = json.loads(f.read())
    return json_object

# Returns the index of the user stored in 'users.json'
def find_user(user_id):
    for user in read_users_data()["users"]:
        if user["id"] == user_id:
            return user
    return None

# Adds a unadded user to the database
def add_user_data(user_id, violation_amount):
    user_dict = {"id":user_id, "violations_amount":violation_amount}
    with open(__file__[:-10].replace("\\", "/") + "../databases/users.json", "w", encoding = "utf8") as f:
        f.write(json.dumps(user_dict, indent=2))

# Increses the amount of the violations of the specified user
def violation_happend(user_id):
    if find_user(user_id) == None:
        add_user_data(user_id, 1)
    else:
        pass
    pass

# Sets the violation counter to 0
def reset_user_database(user_id = None):
    if user_id == None:
        #TODO: reset the whole database
        pass
    else:
        #TODO: reset the specified users database
        pass
    
# Delets every information about everyone
def delete_user_database(user_id = None):
    if user_id == None:
        with open(__file__[:-10].replace("\\", "/") + "../databases/users.json", "w", encoding = "utf8") as f:
            f.write(json.dumps({"users":[]}, indent=4))
        pass
    else:
        #TODO: delete the specified users database
        pass

# Test queries locally
if __name__ == "__main__":
    delete_user_database()
    pass
    #add_user_data(124, 3)
    #
    #print("Test user queries")
    #print("------------------------------")
    #print(f"id     -> {find_user(user_id = 123)['id']}")
    #print(f"amount -> {find_user(user_id = 123)['violations_amount']}")
