# -*- coding:utf-8 -*- 
import sys
sys.path.append("/data/home/sszj/data_stat/pb-temp")
import MySQLdb
import google.protobuf
import player_pb2
import re
import time
filePath = "/home/sszj/data_stat/char_blob/mount_info/mount_soul_star_last_month.txt"
reload(sys)
sys.setdefaultencoding('utf8')

def query_role_channel(host,user,passwd,db_name,table_name,gateway_id,role_id):
    #print "query_role_channel!"
    filename = "role_channel.txt"
    f = open(filename, "w")
    try:
      dest_conn = MySQLdb.connect(host, user, passwd , db_name, port = 3306)
      dest_cur = dest_conn.cursor()
      dest_cur.execute('SET NAMES UTF8')
      sql = "select db_host_ip,db_name from %s where gateway_id = %s" %(table_name,gateway_id)
      rowcnt = dest_cur.execute(sql)
      if rowcnt != 1:
        print "gateway_id %s not found!" %gateway_id
      for row in dest_cur.fetchall():
         db_host_ip = row[0]
         con_db_name = row[1]
         conn = MySQLdb.connect(db_host_ip,user, passwd, con_db_name,3306)
         cur = conn.cursor()
         dbsql = "select A.account,A.game_id from ums_user_info_ex as A left join ums_char_property as B  on A.player_id=B.player_id where pf_role_id=%s" %role_id
         #print dbsql
         cnt =  cur.execute(dbsql)
         if cnt != 1:
            print "role_id %s not found!" %role_id
         data_result = cur.fetchone()
         account = data_result[0]
         role_game_id = data_result[1]
         activity_day_log_str = "%s %s %s" %(role_id,account,role_game_id)
         print activity_day_log_str
         f.write(activity_day_log_str)
         f.write('\n') 
    except MySQLdb.Error, e:
      print "MySQL Error %d:%s" %(e.args[0], e.args[1])
    cur.close()
    conn.commit()
    conn.close()
    dest_cur.close()
    dest_conn.commit()
    dest_conn.close()
    f.close()
def read_from_txt(path):
    splitregex = '\t'
    with open(path,'r') as handle:
        for line in handle:
            items = re.split(splitregex, line)
            #print items[0],items[1]
            query_role_channel('103.244.235.249', 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','conf_server_list_kr',items[0],items[1])
read_from_txt(filePath)

