import sys
import MySQLdb
sys.path.append("/home/sszj/dbtools/server_info")
import query_server_info

server_conn = MySQLdb.connect(host = '103.244.235.249', user = 'sszj', passwd = 'DR9m_wqsgF8a', db = 'data_stat_ss', port = 3306)
server_cur = server_conn.cursor()
server_cur.execute('SET NAMES UTF8')
server_sql = "delete from conf_server_list_2"
server_cur.execute(server_sql)
server_count = query_server_info.get_server_count()
for n in range(server_count):
     gateway_id = query_server_info.get_server_gateway(n)
     if query_server_info.get_server_type(n) != 1:
          continue
     ip_addr = query_server_info.get_server_ip(n)
     db_name = query_server_info.get_server_dbname(n)
     server_sql = "insert into conf_server_list_2 values(%s, 'server_%s', '%s', 'sszj', '', '%s', 0)" % (gateway_id, gateway_id, ip_addr, db_name)
     server_cur.execute(server_sql)

server_cur.close()
server_conn.commit()
server_conn.close()

     

