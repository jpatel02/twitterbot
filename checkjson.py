import json
from tabnanny import check

with open("tweeted_users.json", 'r+') as file:
    file_data = json.load(file)

    if check in file_data["tweeted_users"]:
        file_data["tweeted_users"].append('asakura11')
    else:
        print("User has already been tweeted.")
    
    file.seek(0)

    json.dump(file_data, file, indent=4)