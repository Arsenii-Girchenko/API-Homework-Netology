import json

def write_info_to_json(info_list):
    files_info_list_json = []
    for info in info_list:
        info.pop('url')
        files_info_list_json.append(info)
    with open('files_info.json', 'w') as jf:
        json.dump(files_info_list_json, jf, indent=1)      
    return