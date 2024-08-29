import requests

headers = {
    'Host': 'vote2.scopeview.cn',
    'xweb_xhr': '1',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b)XWEB/11205',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://servicewechat.com/wx956061469eb12383/66/page-frame.html',
    'accept-language': 'zh-CN,zh;q=0.9',
}

params = {
    'atid': '23',
}

data = {
    'code': '0b3DNxGa1z7m5I0AkKFa19xda90DNxGd',
    'appid': 'wx956061469eb12383',
}

response = requests.post('https://vote2.scopeview.cn/index.php/fanqie/login/home', params=params, headers=headers, data=data)
print(response.text)