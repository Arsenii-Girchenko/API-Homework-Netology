TOKEN = ''

from pprint import pprint
import requests

# # Задача №1

# def compare_heroes_by_stat(url, heroes_names: list, stat: str):
#     all_heroes_info = requests.get(url=url).json()
#     comparison_dict = {}
#     for info in requests.get(url=url).json():
#         for hero_name in heroes_names:
#             if hero_name == info["name"]:
#                 comparison_dict[hero_name] = info["powerstats"][stat]
#     return max(comparison_dict, key=comparison_dict.get)


# if __name__ == '__main__':
#     heroes_list = ["Hulk", "Captain America", "Thanos"]
#     stat = 'intelligence'
#     url = "https://akabab.github.io/superhero-api/api/all.json"
#     pprint(f'Hero with the highest {stat} stat is {compare_heroes_by_stat(url, heroes_list, stat)}')
    
    
# # Задача №2

# class YaUploader:
#     def __init__(self, token: str):
#         self.token = token
#         self.yandex_url = "https://cloud-api.yandex.net"
        
#     def get_headers(self):
#         return {
#             'Content-Type': 'application/json',
#             'Authorization': f'OAuth {self.token}'
#         }
        
#     def _get_upload_link(self, disk_file_path):
#         upload_url = f'{self.yandex_url}/v1/disk/resources/upload'
#         headers = self.get_headers()
#         params = {"path": disk_file_path, "overwrite": "true"}
#         response = requests.get(upload_url, headers=headers, params=params)
#         return response.json()   

#     def upload_file_to_disk(self, disk_file_path, filename):
#         href_response = self._get_upload_link(disk_file_path=disk_file_path)
#         href = href_response.get("href", "")
#         response = requests.put(url=href, data=open(filename, 'rb'))
#         response.raise_for_status()
#         if response.status_code == 201:
#             print("Success")

# if __name__ == '__main__':
#     ya = YaUploader(TOKEN)
#     ya.upload_file_to_disk('Netology', "File_for_Yandex.txt")


# № Задача №3

from datetime import datetime, timedelta
import time


def stackoverflow_questions_search(search_word: str):
    start_date = datetime.now() - timedelta(days=2)
    stop_date = datetime.now()
    start_date_unix = int(time.mktime(start_date.timetuple()))
    stop_date_unix = int(time.mktime(stop_date.timetuple()))
    url =  f'https://api.stackexchange.com/2.3/questions?fromdate={start_date_unix}&todate={stop_date_unix}&order=desc&sort=activity&tagged={search_word}&site=stackoverflow'
    questions_info = requests.get(url=url).json()
    pprint(questions_info)
    
if __name__ == '__main__':
    stackoverflow_questions_search('python')