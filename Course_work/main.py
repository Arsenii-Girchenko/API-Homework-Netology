from classes import VkUser
from classes import YaUser
from pprint import pprint
import json

with open('tokens.json', 'r') as f:
    tokens = json.load(f)

vk_app_token = tokens['vk_token']
ya_disk_token = tokens['yandex_token']
vk_version = '5.131'
vk_user_id = 2701504

if __name__ == '__main__':
    vk_client = VkUser(vk_app_token, vk_version)
    ya_client = YaUser(ya_disk_token)
    #vk_client.get_profile_photos(vk_user_id, 5)
    #ya_client.create_Yandex_folder('VK_photos')
    #ya_client.get_upload_link()
    for photo in vk_client.get_profile_photos(vk_user_id, 5):
        ya_client.upload_by_url('VK_photos', photo['file_name'], photo[photo['file_name']])
    
    #pprint(vk_client.get_profile_photos(2701504, 5))
    #ya_client = YaUser()