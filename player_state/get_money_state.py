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

filename = "/data/home/sszj/logs/role_combat_power_%s.data" % time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
f = open(filename, "w")

date_str = time.strftime('%Y%m%d',time.localtime(time.time()))
camp_name = {}

def query_role(db_host, db_user, db_passwd, db_name, db_port, gateway_id, game_id):
    print "query role combat power start!"
    dest_conn = MySQLdb.connect(host = '103.244.235.249', user = 'sszj', passwd = 'DR9m_wqsgF8a', db = 'data_stat_ss', port = 3306)
    dest_cur = dest_conn.cursor()
    dest_cur.execute('SET NAMES UTF8')
    try:
      conn = MySQLdb.connect(host = db_host, user = db_user, passwd = db_passwd, db = db_name, port = db_port)
      cur = conn.cursor()
      cur.execute('SET NAMES UTF8')
      sql = "select pf_role_id, char_name, pf_user_id, role, level, ss_camp_type, diamond_blue, diamond_red, unbuond_money, zhenqi, lingqi, game_id, vip_level, last_quittime, map_id, device_info, pvp_honor, renown, exploit, combat_power from ums_char_property a, gms_users b where a.pf_user_id = b.user_id;"
      cur.execute(sql)
      for row in cur.fetchall():
         #print row
         #for col in row:
         #    print col
         role_id = row[0]
         char_name = ''
         user_id = row[2]
         role = row[3]
         level = row[4]
         ss_camp_type = row[5]
         diamond_blue = row[6]
         diamond_red = row[7]
         unbound_money = row[8]
         zhenqi = row[9]
         lingqi = row[10]
         game_id = row[11]
         vip_level = row[12]
         last_quittime = row[13]
         map_id = row[14]
         device_info = row[15]
         pvp_honor = row[16]
         renown = row[17]         
         exploit = row[18]
         combat_power = row[19]
         dest_sql = '''insert into money_state values(%d, '%s', %d, %d, %d, %d, %d, %d, %d, %d, %d, '%s', %d, %d, %d, %d, %d, '%s', %d, %d, %d, %d)''' % (role_id, char_name, user_id, role, level, ss_camp_type, diamond_blue, diamond_red, unbound_money, zhenqi, lingqi, date_str, gateway_id, game_id, vip_level, last_quittime, map_id, device_info, pvp_honor, renown, exploit, combat_power)
         dest_cur.execute(dest_sql)
         #combat_power_str = "%d,%d,%d,%s,%d,%d,%s,%d,%s,%d,%d,%s" % (user_game_id, user_id, role_id, char_name, combat_power, guild_id, guild_name, ss_camp_type, camp_name_str, last_quittime, gateway_id, date_str)
         #f.write(combat_power_str)
         #f.write('\n')
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

f.close()
print "role combat power data uploaded successfully!"
