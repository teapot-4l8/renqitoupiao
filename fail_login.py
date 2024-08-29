import requests

headers = {
    'Connection': 'keep-alive',
    'xweb_xhr': '1',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.3 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1 wechatdevtools/1.06.2209190 MicroMessenger/8.0.5 Language/zh_CN webview/',
    'X-Requested-With': 'XMLHttpRequest',
    'content-type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://servicewechat.com/wx6b6da4e842c89b90/devtools/page-frame.html',
}

params = {
    'atid': '23',
}

data = {
    'code': '0f3Uja1w3EvYp33X6o2w3AIfh54Uja1f',
    'appid': 'wx6b6da4e842c89b90',
}

response = requests.post('https://vote2.scopeview.cn/index.php/fanqie/login/home', params=params, headers=headers, data=data)
print(response.text)