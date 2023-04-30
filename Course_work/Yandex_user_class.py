import requests
from pprint import pprint
import json
import datetime
from CreateInfoJson import write_info_to_json

class YaUser:
    ya_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    
    def __init__(self, token):
        self.token = token
        
    def get_headers(self):
        return {
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}' 
        }
    
    def create_Yandex_folder(self, folder_name: str):
        folder_path = '/' + folder_name
        params = {'path': folder_path}
        response = requests.put(self.ya_url, params=params, headers=self.get_headers())
        # pprint(response.json())
        if response.status_code == 200 or response.status_code == 201:
            # return response.json()
            return response
        else:
            return pprint(f'Ошибка при созданни папки. Код ошибки {response.status_code}. {response.json()}')
    
    def get_upload_link(self, upload_folder_name, file_name):
        ya_upload_url = f'{self.ya_url}/upload'
        upload_path = '/' + upload_folder_name + '/' + file_name
        params = {'path': upload_path, 'overwrite': 'true'}
        response = requests.get(ya_upload_url, params=params, headers=self.get_headers())
        if response.status_code == 200 or response.status_code == 'default':
            return response
        else:
            return pprint(f'Ошибка при получении ссылки на загрузку. Код ошибки {response.status_code}. {response.json()}')
        
    def upload_info_file(self, upload_folder_name, file_name):
        upload_response = self.get_upload_link(upload_folder_name, file_name) 
        # upload_url = upload_response.get('href')
        upload_url = upload_response.json().get('href')
        with open(file_name, 'rb') as f:
            response = requests.put(upload_url, files={'file': f}, headers=self.get_headers())
        if response.status_code == 200 or response.status_code == 'default' or response.status_code == 201:
            return response
        else:
            return pprint(f'Ошибка при загрузке файла. Код ошибки {response.status_code}. {response.json()}')
    
    def upload_by_url(self, upload_folder_name, file_name, file_url):
        upload_response = self.get_upload_link(upload_folder_name, file_name)     
        upload_path = '/' + upload_folder_name + '/' + file_name
        ya_upload_url = f'{self.ya_url}/upload'
        params = {'path': upload_path, 'url': file_url}
        response = requests.post(ya_upload_url, params=params, headers=self.get_headers())
        if response.status_code == 200 or response.status_code == 202:
            return response
        else:
            return pprint(f'Ошибка {response.status_code}. {response.json()}')