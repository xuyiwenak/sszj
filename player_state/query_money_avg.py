import sys
import MySQLdb
import time

db_host = '103.244.235.249'
db_user = 'sszj'
db_passwd = 'DR9m_wqsgF8a'
db_name = 'data_stat_ss'
db_port = 3306

reload(sys)
sys.setdefaultencoding('utf8')

def query_money_avg():
    dest_conn = MySQLdb.connect(host = db_host, user = db_user, passwd = db_passwd, db = db_name, port = db_port)
    dest_cur = dest_conn.cursor()
    dest_cur.execute('SET NAMES UTF8')
    try:
      sql = "select gateway_id, AVG(diamond_blue), AVG(diamond_red) , AVG(unbuond_money), AVG(zhenqi), AVG(lingqi), AVG(pvp_honor), AVG(renown), AVG(exploit) from char_property  group by gateway_id;"
      dest_cur.execute(sql)
      date_str = time.strftime('%Y%m%d',time.localtime(time.time()))
      for row in dest_cur.fetchall():
         dest_sql = "insert into stat_money values(%d, %d, %d, %d, %d, %d, %d, %d, %d, %d)" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], int(date_str))
         dest_cur.execute(dest_sql)
    except MySQLdb.Error, e:
      print "MySQL Error %d:%s" %(e.args[0], e.args[1])

    dest_cur.close()
    dest_conn.commit()
    dest_conn.close()

query_money_avg()
