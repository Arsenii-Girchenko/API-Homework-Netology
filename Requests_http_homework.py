from pprint import pprint

import requests

def compare_heroes_by_stat(url, heroes_names=[], stat=''):
    all_heroes_info = requests.get(url=url).json()
    comparison_dict = {}
    for info in requests.get(url=url).json():
        for hero_name in heroes_names:
            if hero_name == info["name"]:
                comparison_dict[hero_name] = info["powerstats"][stat]
    return max(comparison_dict, key=comparison_dict.get)


if __name__ == '__main__':
    heroes_list = ["Hulk", "Captain America", "Thanos"]
    stat = 'intelligence'
    url = "https://akabab.github.io/superhero-api/api/all.json"
    pprint(f'Hero with the highest {stat} stat is {compare_heroes_by_stat(url, heroes_list, stat)}')