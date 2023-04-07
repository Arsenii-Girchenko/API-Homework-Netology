import requests
import pprint
import json
import datetime

class VkUser:
    vk_url = 'https://api.vk.com/method/'
    
    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_profile_photos(self, user_id=None, photos_amount=5):
        get_photos_url = self.vk_url + 'photos.get'
        photos_params = {
            'owner_id': user_id,
            'album_id': 'profile',
            'rev': 1,
            'extended': 1,
            'photo_sizes': 1,
            'count': photos_amount            
        }
        req = requests.get(get_photos_url, params={**self.params, **photos_params}).json()
        download_path = '/Photos to download'
        size_types_list = ['w', 'z', 'y', 'x', 'm', 's']
        files_info_list = []
        file_info_dict = {}
        for photo_info in req['response']['items']:
            for size in photo_info['sizes']:
                for i in range(len(size_types_list)):
                    if size['type'] == size_types_list[i]:
                        file_info_dict['file_name'] = str(photo_info['likes']['count']) + '.jpg'
                        file_info_dict['size'] = size['type']
                        file_info_dict[file_info_dict['file_name']] = size['url']
                        files_info_list.append(file_info_dict)             
        return files_info_list
        #return json.dumps(files_info_list, indent=2)
             
            #     with open(download_path + '/' + str(photo_info['likes']['count']) + '.jpg', 'wb+') as f:
            #         f.write(size['url'])
            # with open(download_path + '/' + 'files_info.json', 'w') as jf:
            #     jf.write(json.dumps(files_info_list))
            # files_info_list.append(file_info_dict)        
        #return req

class YaUser:
    ya_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    
    def __init__(self, token):
        self.token = token
        
    def get_headers(self):
        return {
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}' 
        }
    
    def create_Yandex_folder(self, folder_path: str):
        self.folder_path = '/' + folder_path
        params = {'path': self.folder_path}
        response = requests.put(self.ya_url, params=params, headers=self.get_headers())
        return response.json()
    
    def get_upload_link(self, upload_path):
        #ya_upload_url = self.create_Yandex_folder(upload_path).get('href')
        self.create_Yandex_folder(upload_path)
        ya_upload_url = f'{self.ya_url}/upload'
        params = {'path': upload_path, 'overwrite': 'true'}
        response = requests.get(ya_upload_url, params=params, headers=self.get_headers())
        return response.json()
    
    def upload_by_url(self, upload_path, filename, file_url):
        upload_response = self.get_upload_link(upload_path)
        ya_upload_url = upload_response.get('href')
        params = {'path': upload_path, 'url': file_url}
        #with open(filename, 'rb') as f:
        response = requests.post(ya_upload_url, params=params, headers=self.get_headers())
        return response.json()
        
        
        # upload_response = self.get_upload_link(upload_path)
        # upload_url = upload_response.get('href')
        # with open(filename, 'rb') as f:
        #     response = requests.put(upload_url, files={'file': f}, headers=self.get_headers())
        # return response.json()
