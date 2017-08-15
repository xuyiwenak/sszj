#coding=utf-8
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
filename = "jason.txt"
f = open(filename, "w")

url = "http://idb.linekong.com/ZoneConfig.php"

headers = {
    'cache-control': "no-cache",
    'postman-token': "6e5c193a-6cfb-ddb0-22c0-1f5df4987f84"
    }

res = requests.request("GET", url, headers=headers)
jsonData = json.loads(res.content)
#print type(jsonData)
"""
        "id": "1480",
        "strGameName": "蜀山战纪",
        "strProNumber": "1011",
        "strZoneName": "xiaomi_1",
        "strThrTName": "xiaomi",
        "strServiceType": "GameServer",
        "strGatewayId": "241001",
        "strWanIp": "101.251.221.113",
        "strNeiIP": "172.16.12.113",
        "strLogIp": "101.251.221.81",
        "iPensonMax": "3000",
        "strRepCheck": "no",
        "strBackupCheck": "yes",
        "strPensonWarn": "50",
        "strDbName": "gamedb_241001",
        "strTable": "gms_shard_state",
        "strMergeState": "0",
        "strPort": "16201",
        "intGatewayFlag": "0",
        "shardId": null,
        "quxianType": "5",
        "strRemark": "",
        "idc_name": "首都在线",
        "strZoneState": "0",
        "intYunFlag": "1",
        "address": "/home/sszj/server_241001",
        "datetime": null,
        "strPensonDB": ""
"""
count = 0
for oneData in jsonData:
    strData = "%s,%s,%s,%s,%s" %(oneData['id'],oneData['strGatewayId'],oneData['strServiceType'],oneData['strLogIp'],oneData['strDbName'])
    f.write(strData)
    f.write('\n')
    count=count+1
f.close()
print(count)

def get_server_count():
     return len(jsonData)
server_count = get_server_count()
def get_server_type(index):
       if jsonData[index]['strServiceType'] == 'MasterDB':
           return 1
       elif jsonData[index]['strServiceType'] == 'GameServer':
           return 2

def get_server_gateway(index):
       return jsonData[index]['strGatewayId']

def get_server_ip(index):
       if get_server_type(index) == 1:
           return jsonData[index]['strWanIp']
       elif get_server_type(index) == 2:
           return jsonData[index]['strLogIp']

def get_server_dbname(index):
    return jsonData[index]['strDbName']
def get_server_gsip(index):
     if get_server_type(index) == 2:
        #print "server_ip find!"
        return jsonData[index]['strWanIp']
