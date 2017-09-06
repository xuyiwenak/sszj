#coding=utf-8
import sys
import MySQLdb
sys.path.append("/home/sszj/dbtools/server_info")
import query_server_info
import create_server_info2db

table_name = "conf_server_list_2"
table_name_kr = "conf_server_list_kr"
host = '103.244.235.249'
user = 'sszj'
passwd = 'DR9m_wqsgF8a'
db = 'data_stat_ss' 
port = 3306
# create server table

# insert db server
def insert2db(host, user, passwd, db, port,table_name,table_name_kr):
    server_conn = MySQLdb.connect(host, user, passwd, db , port)
    server_cur = server_conn.cursor()
    server_count = query_server_info.get_server_count()
    for n in range(server_count):
        gateway_id = query_server_info.get_server_gateway(n)
        ip_addr = query_server_info.get_server_ip(n)
        db_name = query_server_info.get_server_dbname(n)
        if query_server_info.get_server_type(n) != 1:
            continue
        if query_server_info.get_server_type(n) == "韩分":
            server_sql = "insert into %s values('%s', 'server_%s', '%s', '%s', '%s', 0 , 0, 0)" % (table_name_kr, gateway_id, gateway_id, ip_addr, user, db_name)
        else:
            server_sql = "insert into %s values('%s', 'server_%s', '%s', '%s', '%s', 0 , 0, 0)" % (table_name, gateway_id, gateway_id, ip_addr, user, db_name)
        server_cur.execute(server_sql)
    server_conn.commit()    
    for n in range(server_count):
        gateway_id = query_server_info.get_server_gateway(n)
        ip_addr = query_server_info.get_server_ip(n)
        gs_ip = query_server_info.get_server_gsip(n)
        print gs_ip
        if query_server_info.get_server_type(n) == 2:
            if query_server_info.get_server_type(n) == "韩分":
                server_sql = "update %s set log_host_ip = '%s', log_name = 'logdb_%s', server_ip = '%s' where gateway_id = %s" % (table_name_kr,ip_addr,gateway_id,gs_ip,gateway_id)
            else:
                server_sql = "update %s set log_host_ip = '%s', log_name = 'logdb_%s', server_ip = '%s' where gateway_id = %s" % (table_name,ip_addr,gateway_id,gs_ip,gateway_id)
        server_cur.execute(server_sql)
    server_cur.close()
    server_conn.commit()
    server_conn.close()
# 
create_server_info2db.create_table(host, user, passwd, db,table_name)
create_server_info2db.create_table(host, user, passwd, db,table_name_kr)
insert2db(host, user, passwd, db, port,table_name,table_name_kr)

