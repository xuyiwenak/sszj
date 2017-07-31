import sys
import MySQLdb
import time

reload(sys)
sys.setdefaultencoding('utf8')


date_str = time.strftime('%Y%m%d',time.localtime(time.time()))

def query_role(db_host, db_user, db_passwd, db_name, db_port, gateway_id):
    print "get consign data start!"
    dest_conn = MySQLdb.connect(host = '103.244.235.249', user = 'sszj', passwd = 'DR9m_wqsgF8a', db = 'data_stat_ss', port = 3306)
    dest_cur = dest_conn.cursor()
    dest_cur.execute('SET NAMES UTF8')
    try:
      conn = MySQLdb.connect(host = db_host, user = db_user, passwd = db_passwd, db = db_name, port = db_port)
      cur = conn.cursor()
      cur.execute('SET NAMES UTF8')
      sql = "select sheet_name, quantity, price, consign_time, owner_pf_role_id, b.user_id, b.game_id, src_roleid, src_playerid, src_gameid from gms_consign_log a, gms_users b, ums_char_property c  where owner_pf_role_id = c.pf_role_id and c.pf_user_id = b.user_id and consign_flag = 1 and from_unixtime(consign_time) >= '2016-07-01 00:00:00' and from_unixtime(consign_time) < '2017-07-01 00:00:00'"
      cur.execute(sql)
      for row in cur.fetchall():
         #print row
         #for col in row:
         #    print col
         sheet_name = row[0]
         count = row[1]
         price = row[2]
         consign_flag = 1
         consign_time = row[3]
         dest_role_id = row[4]
         dest_user_id = row[5]
         dest_game_id = row[6]
         src_role_id = row[7]
         src_user_id = row[8]
         src_game_id = row[9]
         dest_sql = "insert into consign_log values('%s', %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d)" % (sheet_name, count, price, consign_flag, consign_time, gateway_id, src_role_id, src_user_id, src_game_id, dest_role_id, dest_user_id, dest_game_id)
         dest_cur.execute(dest_sql)
      cur.close()
      conn.close()
    except MySQLdb.Error, e:
      print "MySQL Error %d:%s" %(e.args[0], e.args[1])

    dest_cur.close()
    dest_conn.commit()
    dest_conn.close()
    

server_conn = MySQLdb.connect(host = '103.244.235.249', user = 'sszj', passwd = 'DR9m_wqsgF8a', db = 'data_stat_ss', port = 3306)
server_cur = server_conn.cursor()
server_cur.execute('SET NAMES UTF8')

server_sql = "select db_host_ip, db_user, db_name, gateway_id from conf_server_list_2"
server_cur.execute(server_sql)
server_count = 0
for row in server_cur.fetchall():
    query_role(row[0], row[1], 'DR9m_wqsgF8a', row[2], 3306, row[3])
    server_count += 1
    print "server %d query finished!\n" % server_count

server_cur.close()

print "get consign data successfully!"
