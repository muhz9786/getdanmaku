import json
import requests
import sys

AID_URL = "http://api.bilibili.com/x/web-interface/archive/stat?bvid="
OID_URL = "https://api.bilibili.com/x/player/pagelist?aid="
DM_URL = "https://api.bilibili.com/x/v1/dm/list.so?oid="
FILE_PATH = "./"

HEADER = {
    "Referer": "https://www.bilibili.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept": "*/*",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-dest": "script",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63",
    "Accept-language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,en-GB;q=0.6,en-US;q=0.5",
}

# 获取视频弹幕池id
def getOid(bid):
    r = requests.get(AID_URL + bid, headers=HEADER)
    aid = str(json.loads(doc.text)["data"]["aid"])
    r = requests.get(OID_URL + aid, headers=HEADER)
    oid = str(json.loads(doc.text)["data"][0]["cid"])
    return oid

# 获取弹幕列表API的url
def getUrl(bid):
    oid = getOid(bid)
    url = DM_URL + oid
    return url

# 获取弹幕列表json文档
def getDoc(bid):
    url = getUrl(bid)
    r = requests.get(url, headers=HEADER)
    return r.text

# 下载弹幕列表json文档
def getFile(bid):
    doc = getDoc(bid)
    f = open(FILE_PATH + bid + ".json", "w")
    f.write(doc)
    f.close

if __name__ == "__main__":
    bid = sys.argv[1]
    getFile(bid)
