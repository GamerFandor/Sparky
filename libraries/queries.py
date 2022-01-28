import ast
import json

# NOTE: Bot's database functions
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

# NOTE: User's database functions
# Get the content of 'users.json'
def read_users_data():
    with open(__file__[:-10].replace("\\", "/") + "../databases/users.json", "r", encoding = "utf8") as f:
        json_object = json.loads(f.read())
    return json_object

# Set the content of 'users.json'
def write_users_data(data):
    with open(__file__[:-10].replace("\\", "/") + "../databases/users.json", "w", encoding = "utf8") as f:
        f.write(json.dumps(data))

# Returns the index of the user stored in 'users.json'
def find_user(user_id):
    for user in read_users_data()["users"]:
        if user["id"] == user_id:
            return user
    return None

# Adds a unadded user to the database
def add_user_data(user_id, violation_amount):
    user_dict = str({"id":user_id, "violations_amount":violation_amount}, )
    index = str(read_users_data()).find("[") + 1
    new_dict = (str(read_users_data())[:index] + user_dict + str(read_users_data())[index:]).replace("}{", "}, {")
    write_users_data(ast.literal_eval(new_dict))

# Increses the amount of the violations of the specified user
def violation_happend(user_id):
    if find_user(user_id) == None:
        add_user_data(user_id, 1)
    else:
        user = find_user(user_id)
        user["violations_amount"] = user["violations_amount"] + 1
        updated_database = str(read_users_data()).replace(str(find_user(user_id)), str(user))
        write_users_data(ast.literal_eval(updated_database))

# Sets the violation counter to 0
def reset_user_database(user_id = None):
    if user_id == None:
        database = read_users_data()
        for i in range(len(database["users"])):
            database["users"][i]["violations_amount"] = 0
        write_users_data(database)      
    else:
        user = find_user(user_id)
        user["violations_amount"] = 0
        updated_database = str(read_users_data()).replace(str(find_user(user_id)), str(user))
        write_users_data(ast.literal_eval(updated_database))
    
# Delets every information about everyone
def delete_user_database(user_id = None):
    if user_id == None:
        write_users_data({'users':[]})
    else:
        database = str(read_users_data())
        database_replaced = database.replace("{"+"'id': " + str(user_id) + ", 'violations_amount': " + str(find_user(user_id)["violations_amount"]) + "}", "").replace("[, ", "[").replace(", , ", ", ").replace(", ]", "]")
        write_users_data(ast.literal_eval(database_replaced))
