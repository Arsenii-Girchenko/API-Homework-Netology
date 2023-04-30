from VK_user_class import VkUser
from Yandex_user_class import YaUser
from CreateInfoJson import write_info_to_json
from pprint import pprint
import json

# Введите сюда свои токены ВК и Яндекс.Диск
VK_APP_TOKEN = '' 
YA_DISK_TOKEN = ''

vk_version = '5.131' # версия API ВК
vk_user_id = 2701504 # id пользователя ВК

if __name__ == '__main__':
    vk_client = VkUser(VK_APP_TOKEN, vk_version)
    ya_client = YaUser(YA_DISK_TOKEN)
    info_list = vk_client.get_profile_photos(vk_user_id, 5) #функция зависит от ID пользователя ВК и числа фото профиля, которые надо сохранить
    ya_client.create_Yandex_folder('VK_photos')
    for info in info_list:
            ya_client.upload_by_url('VK_photos', info['file_name'], info['url'])
    write_info_to_json(info_list)
    ya_client.upload_info_file('VK_photos', 'files_info.json')