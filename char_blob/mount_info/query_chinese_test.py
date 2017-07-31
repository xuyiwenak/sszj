# -*- coding:utf-8 -*- 
import sys
sys.path.append("/data/home/sszj/data_stat/pb-temp")
import MySQLdb
import google.protobuf
import player_pb2
import codecs

reload(sys)
sys.setdefaultencoding('utf8')

def query_role_gem():
    try:
      dest_conn = MySQLdb.connect(host = '103.244.235.249', user = 'sszj', passwd = 'DR9m_wqsgF8a', db = 'data_stat_ss', port = 3306)
      dest_cur = dest_conn.cursor()
      #dest_cur.execute('SET NAMES UTF8')
      sql = "select a.key, a.value from dictionary a limit 3"
      dest_cur.execute(sql)
      f = open('dictionary_test.txt', "w")
      for row in dest_cur.fetchall():
         key = row[0]
         value = row[1]
         line_str = "%s,%s" % (key, value)
         f.write(line_str)
         f.write('\n')
      f.close()
    except MySQLdb.Error, e:
      print "MySQL Error %d:%s" %(e.args[0], e.args[1])

    dest_cur.close()
    dest_conn.commit()
    dest_conn.close()

query_role_gem()
