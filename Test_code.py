import requests

class VK:

   def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

   def users_info(self):
       url = 'https://api.vk.com/method/users.get'
       params = {'user_ids': self.id}
       response = requests.get(url, params={**self.params, **params})
       return response.json()


access_token = 'vk1.a.eoWhezEPdEsupo5V6Ky9XK7yQulhAhmef2H_i-XF6amAWiKvidKftgY060G1qEqZH27aOUA4kz2BTDRfU1jHY-odO4_hGb5xtDzOWaJJBc5IKXzAK6xaHhJv4nw11UsX3gmqz_VB08hPaFxkKTbIBfMX6ZR9NBKtW0MagRrkbWwQb8l4i7Tr5sIqAnvAgmyqrQriz5xSCXWKhVTWba1kOg'
user_id = '2701504'
vk = VK(access_token, user_id)
print(vk.users_info())