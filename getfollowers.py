import requests
import json
COOKIE = '''在这里填写你的COOKIE'''
def get_info(mid):
    """
    获取粉丝数量
    :param mid: 用户ID
    :return: 返回关注数量和粉丝数量
    """
    headers = {
        'Connection': 'keep-alive',
        'Cookie': COOKIE,
        'Host': 'api.bilibili.com',
        'Referer': 'https://space.bilibili.com/' + str(mid),
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    url = 'https://api.bilibili.com/x/space/myinfo?jsonp=jsonp'
    try:
        r = requests.get(url, headers = headers, timeout = 60)
        r.raise_for_status()
        status = r.json()
        data = status.get('data')
        if data:
            follower = data.get('follower')
            #粉丝数量
            return follower
    except ConnectionError as e:
        print('ConnectionError', e.args)
def get_followers(mid, pn, ps):
    """
    获取粉丝用户信息
    :param mid: 用户ID
    :param pn: 页数
    :param ps: 每页数量
    """
    headers = {
        'Connection': 'keep-alive',
        'Cookie': COOKIE,
        'Host': 'api.bilibili.com',
        'Referer': 'https://space.bilibili.com/' + str(mid),
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    url = 'https://api.bilibili.com/x/relation/followers?'
    kv = {
        'vmid':str(mid), 
        'pn':str(pn),
        'ps':str(ps), 
        'order':'desc',
        'jsonp':'jsonp'
    }
    try:
        r = requests.get(url, params = kv, headers=headers, timeout=60)
        r.raise_for_status()
        status = r.json()
        data = status.get('data')
        if data:
            for i in data.get('list'):
                result = {
                    'uname': i.get('uname'),
                    'mid': i.get('mid')
                }
                print(result)
    except ConnectionError as e:
        print('ConnectionError', e.args)

def run(mid):
    f = get_info(mid)
    ps = 50
    total_pn = int(f / ps) + 1
    for pn in range (1, total_pn + 1):
	    get_followers(mid, pn, ps)
    
run(29361798) 
