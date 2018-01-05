# -*- coding:utf-8 -*- 
import sys
sys.path.append("/data/home/sszj/data_stat/pb-temp")
import MySQLdb
import google.protobuf
import player_pb2

reload(sys)
sys.setdefaultencoding('utf8')

def query_role_gem_cutting():
    print "query gem data start!"
    try:
      dest_conn = MySQLdb.connect(host = '103.244.235.249', user = 'sszj', passwd = 'DR9m_wqsgF8a', db = 'data_stat_ss', port = 3306)
      dest_cur = dest_conn.cursor()
      dest_cur.execute('SET NAMES UTF8')
      sql = "select gateway_id, pf_role_id, gem_enchase_list from\
      char_blob"
      dest_cur.execute(sql)
      for row in dest_cur.fetchall():
         gateway_id = row[0]
         role_id = row[1]
         gem_str = row[2]
         gem_data = player_pb2.PBCharBlob().gem_enchase_list
         gem_data.ParseFromString(gem_str)
         count = len(gem_data.gem_cutting)
         for gem_cut_one in gem_data.gem_cutting:
             gem_cut_type = gem_cut_one.cutting_type
             gem_cut_level = gem_cut_one.cutting_level
             dest_sql = "insert into char_gem_cutting values(%d,  %d,  %d, %d)" % (gateway_id, role_id, gem_cut_type, gem_cut_level)
             dest_cur.execute(dest_sql)
    except MySQLdb.Error, e:
      print "MySQL Error %d:%s" %(e.args[0], e.args[1])

    dest_cur.close()
    dest_conn.commit()
    dest_conn.close()


query_role_gem_cutting()
