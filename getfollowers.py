import requests
import json
COOKIE = '''buvid3=3ACCBD53-1E26-41C4-8717-04DEBAF554AA110254infoc; LIVE_BUVID=AUTO4715567244701855; stardustvideo=1; CURRENT_FNVAL=16; rpdid=|(u|Jl)|)mJk0J'ullY~kRY~|; sid=jwdljdqh; _uuid=C2D4A698-4F95-13BC-0F3C-992DC2DD695A47933infoc; fts=1557234273; im_notify_type_39621469=0; _uuid=E5026172-366A-7073-F57A-78F7CA78147A64465infoc; CNZZDATA2724999=cnzz_eid%3D702453138-1557145585-https%253A%252F%252Flive.bilibili.com%252F%26ntime%3D1570444035; laboratory=1-1; DedeUserID=39621469; DedeUserID__ckMd5=66e3dad1d2f507c1; SESSDATA=500cb065%2C1580144451%2C45a6f9c1; bili_jct=3ff3196b653b63b05c08a105fe897ee1; CURRENT_QUALITY=112; INTVER=1; __lfcc=1'''
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
    f = 2000
    ps = 50
    total_pn = int(f / ps) + 1
    for pn in range (1, total_pn + 1):
	    get_followers(mid, pn, ps)
    
run(29361798) 
