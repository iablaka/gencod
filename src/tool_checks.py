import os.path
import json


EXPECTED_TARGETS = ['python', 'api']

def check_root_folder(folder):
    if os.path.exists(folder):
        return True
    else:
        print("Root folder doesn't exist")
        return False    

def check_app_file(dir):
    if not os.path.exists(os.path.join(dir, "app.json")):
        print('App file not found')
        return False
    else:
        with open(os.path.join(dir, "app.json"), 'r') as json_file:
            json_content = json.load(json_file)
            if 'target' not in json_content:
                print('Target entry not found in app file')
                return False
            else:
                if not json_content['target'] in EXPECTED_TARGETS:
                    print(f"target should be one of the following: {EXPECTED_TARGETS}")
                    return False
            if 'rootFolder' not in json_content:
                print('rootFolder entry not found in app file')
                return False
            else:
                if not check_root_folder(json_content['rootFolder']):
                    return False
            if 'project' not in json_content:
                print('Project entry not found in app file')
                return False
            return json_content


