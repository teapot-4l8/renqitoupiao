import requests

headers = {
    'Host': 'vote2.scopeview.cn',
    'xweb_xhr': '1',
    'x-requested-with': 'XMLHttpRequest',
    'authorization': 'fanqie eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvdm90ZTIuc2NvcGV2aWV3LmNuIiwiYXVkIjoiaHR0cHM6XC9cL3ZvdGUyLnNjb3Bldmlldy5jbiIsImRhdGEiOnsiaWQiOiI1MDIyIiwib3BlbmlkIjoib1Btd1o1VDJRc1lPWlNYd1JtaDRyUHIxVFAzUSIsIm5pY2tuYW1lIjoiZnFfMTcyNDgyNTYwMzMiLCJhdmF0YXIiOiIiLCJhZGRfdGltZSI6IjE3MjQ4MjU2MDMiLCJhZGRfaXAiOiIxMjAuMjMwLjEwMS41MCIsImxhc3RfaXAiOiIxMjAuMjMwLjEwMS41MCIsImxhc3RfdGltZSI6IjE3MjQ4MjU2MDMiLCJzdGF0dXMiOiIxIiwidHlwZSI6IjAiLCJtb2JpbGUiOiIiLCJ1c2VybmFtZSI6IiJ9LCJpYXQiOjE3MjQ5MzI0NzgsImV4cCI6MTcyNDkzOTY3OH0.LJ3zugantEhqObWFPiht6kapetMrKfbfG3OnbyR22Yc',
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
    'id': '494',
}

response = requests.post('https://vote2.scopeview.cn/index.php/fanqie/vote/start', params=params, headers=headers, data=data)
print(response.text)
