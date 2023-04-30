import requests
from pprint import pprint
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
        req = requests.get(get_photos_url, params={**self.params, **photos_params})
        req_json = req.json()
        files_info_list = []
        if req.status_code == 200:
            for photo_info in req_json['response']['items']:
                files_info_dict = {}
                width_plus_height = 0
                for size in photo_info['sizes']:
                    if (size['height'] + size['width']) >= width_plus_height:
                        files_info_dict['file_name'] = str(photo_info['likes']['count']) + '.jpg'
                        files_info_dict['size'] = size['type']
                        files_info_dict['url'] = size['url']
                        width_plus_height = size['height'] + size['width']
                files_info_list.append(files_info_dict)
            return files_info_list
        else:
            return f'Ошибка http-запроса на копирование фотографий профиля пользователя VK. Код ошибки {req.status_code}'