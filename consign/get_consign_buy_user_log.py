import sys
import MySQLdb
import time

db_host = '10.10.252.15'
db_user = 'root'
db_passwd = 'game'
db_name = 'gamedb_587001'
db_port = 3306

reload(sys)
sys.setdefaultencoding('utf8')

date_str = time.strftime('%Y%m%d',time.localtime(time.time()))
camp_name = {}

def query_role(db_host, db_user, db_passwd, db_name, db_port, gateway_id, game_id):
    print "get consign data start!"
    dest_conn = MySQLdb.connect(host = '103.244.235.249', user = 'sszj', passwd = 'DR9m_wqsgF8a', db = 'data_stat_ss', port = 3306)
    dest_cur = dest_conn.cursor()
    dest_cur.execute('SET NAMES UTF8')
    try:
      conn = MySQLdb.connect(host = db_host, user = db_user, passwd = db_passwd, db = db_name, port = db_port)
      cur = conn.cursor()
      cur.execute('SET NAMES UTF8')
      sql = "select sheet_name, quantity, price, consign_time, owner_pf_role_id, b.user_id, b.game_id, src_roleid, src_playerid, src_gameid from gms_consign_log a, gms_users b, ums_char_property c  where owner_pf_role_id = c.pf_role_id and c.pf_user_id = b.user_id and consign_flag = 1 and b.game_id = 2196"
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
server_sql = "select ss_camp_type, ss_camp_name from conf_camp_info"
server_cur.execute(server_sql)
for row in server_cur.fetchall():
    camp_name[row[0]] = row[1]

server_sql = "select db_host, db_user, db_password, db_name, gateway_id, game_id from conf_server_list"
server_cur.execute(server_sql)
server_count = 0
for row in server_cur.fetchall():
    query_role(row[0], 'sszj', 'DR9m_wqsgF8a', row[3], 3306, row[4], row[5])
    server_count += 1
    print "server %d query finished!\n" % server_count

server_sql = "select ss_camp_type, ss_camp_name from conf_camp_info"
server_cur.execute(server_sql)
for row in server_cur.fetchall():
    camp_name[row[0]] = row[1]    

server_cur.close()

print "get consign data successfully!"
