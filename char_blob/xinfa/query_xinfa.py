# -*- coding:utf-8 -*- 
import sys
sys.path.append("/data/home/sszj/data_stat/pb-temp")
import MySQLdb
import google.protobuf
import player_pb2

reload(sys)
sys.setdefaultencoding('utf8')

def query_role_gem():
    print "query xinfa info start!"
    try:
      dest_conn = MySQLdb.connect(host = '103.244.235.249', user = 'sszj', passwd = 'DR9m_wqsgF8a', db = 'data_stat_ss', port = 3306)
      dest_cur = dest_conn.cursor()
      dest_cur.execute('SET NAMES UTF8')
      sql = "select gateway_id, pf_role_id, xinfa_data from\
      char_blob where level >= 110"
      dest_cur.execute(sql)
      for row in dest_cur.fetchall():
         gateway_id = row[0]
         role_id = row[1]
         xinfa_str = row[2]
         xinfa_data = player_pb2.PBCharBlob().xinfa_data
         xinfa_data.ParseFromString(xinfa_str)
         for xinfa_one in xinfa_data.data_list:
             slot_id = xinfa_one.slot_id
             cur_level = xinfa_one.cur_level
             dest_sql = "insert into char_xinfa values(%d,  %d,  %d, %d)" % (gateway_id, role_id, slot_id, cur_level)
             dest_cur.execute(dest_sql)

    except MySQLdb.Error, e:
      print "MySQL Error %d:%s" %(e.args[0], e.args[1])

    dest_cur.close()
    dest_conn.commit()
    dest_conn.close()

query_role_gem()
