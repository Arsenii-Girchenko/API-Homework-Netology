TOKEN = 'y0_AgAAAAAbP2AbAADLWwAAAADecWQU33lN8lGoT565Zcw_yutO_41FHDc'

import requests



# YANDEX_URL = 'https://cloud-api.yandex.net'
# PREPARE_UPLOAD_URL = f'{YANDEX_URL}/v1/disk/resources/upload'
# params = {'path': '/File_for_Yandex.txt', 'overwrite': 'true'}
# headers = {'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

# file_path = 'File_for_Yandex.txt'

# response = requests.get(PREPARE_UPLOAD_URL, params=params, headers=headers)
# print(response.text)

# put_url = response.json().get('href')
# print(put_url)

# files = {'file': open(file_path, 'rb')}
# response = requests.put(put_url, files=files, headers=headers)
# print(response)