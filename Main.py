import requests

R = '\033[31;1m'
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"

class Warrior:
    def __init__(self):
        pass

    def Yahoo(self, email):
        try:
            if '@' in email:
                email = email

                headers = {
                    "User-Agent": "Mozilla/5.0 (Linux; Android 9; ASUS_I003DD Build/PI; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.70 Mobile Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "X-Requested-With": "XMLHttpRequest",
                    "Cookie": "B=6nir0s22dqrd0; A1=d=ARIBBEnXOWYCEA8kg6USZO9xu_WJH1ZhQu0FEgEBCADlOWY7ZtxqyyMA_eMBAAcIoG3dhOBgy2s&S=AQAAAiruxmFBiq-O0p2tXJ0qfyQ; A1S=d=ARIBBEnXOWYCEA8kg6USZO9xu_WJH1ZhQu0FEgEBCADlOWY7ZtxqyyMA_eMBAAcIoG3dhOBgy2s&S=AQAAAiruxmFBiq-O0p2tXJ0qfyQ; WV=\"1:1715066816:1197791112:A:com.yahoo.mobile.client.android.mail:6.13.2:21b6f5f7-884c-4323-95d3-d0abb8ddc573:4:0\"; OA=v=1&nlr=0&let=1715066788&sig=0~Fpln54jhIKRJTf9oW3PwpTuyM8XaoOoHjs68fReWW-Y; A3=d=ARIBBEnXOWYCEA8kg6USZO9xu_WJH1ZhQu0FEgEBCADlOWY7ZtxqyyMA_eMBAAcIoG3dhOBgy2s&S=AQAAAiruxmFBiq-O0p2tXJ0qfyQ; AS=v=1&s=b958X6s9&d=A663b2924|_MBvS2L.2Trj6wbi86t5AfZmNjFUCHfu.pu_fyTEwTdG9QNVEpIgLsRmuHuqjpijPaidj8R3hUusEjhIAPYDVkBZ9aSUkj2MtBQMX7Je818CjIFaP1JTYdK.WDGQNeJOpBNA3m_XgoQ1.YoMxl5f80SUq7FfcSvsx.G5mevPOwwrLXv4SKEAY0x4slSqXRFzs3jtImB1AA19wcCjnNoPhzVbFtATX0qMyCeNPnhk16yqirsVEVfagK0KlVMwEvj200UoB5.EF5FYvLLOlyCNbjnhy4Y9XXHVKJj_G4yohmmxtpj8UetakP6MzhR8ezt0kQ5q_2Du9lXn38bjjP_T_z.nSgkZOIq0C_17D7KKAgjd3ISmACFTde1apS9XeTrHTaq9C.1w0QDIr5_flWC_wZL7I6J2f76yE_SLAQC.mxtdLIAU7Eo1PkZpkHGuFhBW0f.HOsHQpd_eIs7tSEdmPdivcRNMDI__0.qWdkL9mIyT181uH4186mCg_fFA_DQQjFUUJqa8zKu6rKaB2I5uwRtbpBrIu0_xDpz0BlEUqer2cUmsixoUsJoUlAKEgFzRvd49PXNohcXxmPEGWvSKZSxzzR7dSbrzX0L7bS8hBwuKigb8hAa358H1h7Ze6bm8752UxER_aLV6Vm65Zf6Ox3_ZA8iMWTcz1UGGcSH60mEoWgO6MAtS0kJ56bOVAPaMxakIJDPW22IKCdkq4QcqGBBcBqPh_QSUdr04.TV3HzazKyxu5fKX5U2fGpYW3REWX038cp1D0jSf6pgK4Jpf7zrSPgPbCXMmxsu3mYpVphzqpH3NNPkA8dYu8x7CrLH.kBlw5GIzVurhi.khe.PQB5aroFzmh2z0lWbYqWtlVAtJjfgUWkEsDjb0TeCVomuWYBnN0ztdRWySEkWn1AnX6xe_4jE5eqZe3VR0iogdpN1wcqxHKPpSQytob8tk5Tjl9E2jC5JJI7D7L8T7ZWIj9MLWkqY253.kIX0U4lnp2B8kimARsVJ5j2wE4c1gVb6nss1xOw--~A",
                }
                data = {
                    "acrumb": "b958X6s9",
                    "sessionIndex": "QQ--",
                    "firstName": "YOUSIF",
                    "lastName": "AHMED",
                    "userId": email,
                    "password": "Dont Give Up",
                }

                response = requests.post("https://login.yahoo.com/account/module/create?validateField=userId", headers=headers, data=data).json()
                info = response['errors'][0]['name']
                ex = response['errors'][0]['error']

                if 'birthDate' == info:
                    print("{}[{}+{}] {}Email Av {}: {}{}".format(E, H, E, H, R, C, email))
                elif 'IDENTIFIER_EXISTS' == ex:
                    print("{}[{}+{}] {}Email Not Av {}: {}{}".format(E, H, E, R, R, C, email))
                elif 'LENGTH_TOO_SHORT' == ex:
                    print("{}[{}+{}] {}Email Too Short {}: {}{}".format(E, H, E, R, R, C, email))
                elif 'CANNOT_START_WITH_SPECIAL_CHARACTER_OR_NUMBER' == ex:
                    print("{}[{}+{}] {}Email Taken {}: {}{}".format(E, H, E, R, R, C, email))

        except Exception as e:
            self.Yahoo(email=email)

email = input("{}[{}~{}] {}ENTER YOUR {}EMAIL {}: ".format(E, H, E, E, R, R, E))
Warrior().Yahoo(email=email)
