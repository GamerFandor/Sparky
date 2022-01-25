import json

def load(filePath, dataID):
    with open(filePath) as j:
        data = json.load(j)
        
    if data[dataID] != None:
        return data[dataID]
    else:
        return None
    
if __name__ == "__main__":
    print(f"prefix -> {load('databases/botdata.json', 'prefix')}")
    print(f"TOKEN  -> {load('databases/botdata.json', 'TOKEN')}")
