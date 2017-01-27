import requests
import datetime
import locale
locale.setlocale(locale.LC_ALL, '')
import dateutil
import time
from datetime import datetime, date, time
class BaseClient:

     # URL vk api
    BASE_URL = "https://api.vk.com/method/"
    # метод vk api
    method_id = "users.get?user_ids="
    method_friends = "friends.get?user_id="
    # GET, POST, ...
    http_method = "&fields=bdate&v=5.58"

    # Склейка url
    def generate_url(self, method,vkid):
        if method == 1:
            response = (str(self.BASE_URL) + str(self.method_id) + str(vkid) + str(self.http_method))
        else:
            response = (str(self.BASE_URL) + str(self.method_friends) +str(Check_id.vkmethod(self)) + str(self.http_method))

        return response
    # Обработка ответа от VK API
    def response_handler(self, response):
        req = requests.get(response)
        try:
            req.json()['response']
        except KeyError:
            print("Ошибка запроса")
            raise SystemExit(1)

        return response
class Check_id(BaseClient):
    def __init__(self,vk):
        self.vkid = vk
    def show_name(self):
        self.response_handler(BaseClient.generate_url(self, 1, vkid))
        req = requests.get(BaseClient.generate_url(self, 1, vkid))
        name = req.json()['response'][0].get('first_name')
        second_name = req.json()['response'][0].get('last_name')
        print(name, second_name)
    def vkmethod(self):
        self.response_handler(BaseClient.generate_url(self,1,vkid))
        req = requests.get(BaseClient.generate_url(self,1,vkid))
        ans = req.json()['response'][0].get('id')
        return ans

class Check_friend(BaseClient):

    def friends(self):
        self.response_handler(BaseClient.generate_url(self,2,23))
        req = requests.get(BaseClient.generate_url(self,2,23))
        count = req.json()['response'].get('count')

        print()
        print(str(count) + " - количество друзей")
        i = 0
        bArr = []
        while i < count:
            people = req.json()['response']['items'][i].get('last_name')
            bdate = req.json()['response']['items'][i].get('bdate')

            if bdate:
                if len(bdate) > 5:
                    bdate = datetime.strptime(bdate, "%d.%m.%Y")
                    bArr.insert(i, bdate)
            i += 1
        diag = [0 for i in range(116)]
        count1 = len(bArr)
        i = 0
        a = []
        while i < count1:
            result = (datetime.today() - bArr[i]) / 365
            result = str(result).split(' ')
            j = int(result[0])
            diag[j] += 1
            i += 1
        return diag
    def printdiag(self,arr):
        i = 0
        cnt = len(arr)
        while i < cnt:
            if arr[i] != 0:
                j = 0
                print(i, end=" ")
                while j < arr[i]:
                    print('#', end="")
                    j += 1
                print("")
            i += 1

a = BaseClient()
vkid = input("Введите ID пользователя: ")
a1 = Check_id(vkid)
a1.show_name()
a2 = Check_friend()
a2.printdiag(a2.friends())
sleep 180