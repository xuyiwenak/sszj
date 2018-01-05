#coding=utf-8
import sys
import MySQLdb
sys.path.append("/home/sszj/data_stat/conf/server_info")
import query_server_info
import create_server_info2db

table_name = "conf_server_list_2"
table_name_kr = "conf_server_list_kr"
table_name_th = "conf_server_list_th"
host = '103.244.235.249'
user = 'sszj'
passwd = 'DR9m_wqsgF8a'
db = 'data_stat_ss' 
port = 3306
# create server table
reload(sys)
sys.setdefaultencoding('utf8')
# insert db server
def insert2db(host, user, passwd, db, port,table_name,table_name_kr,table_name_th):
    server_conn = MySQLdb.connect(host, user, passwd, db , port)
    server_cur = server_conn.cursor()
    server_count = query_server_info.get_server_count()
    for n in range(server_count):
        print n
        gateway_id = query_server_info.get_server_gateway(n)
        if gateway_id == "" :
            continue
        ip_addr = query_server_info.get_server_ip(n)
        db_name = query_server_info.get_server_dbname(n)
        game_channel= query_server_info.get_server_game_channel(n)
        if query_server_info.get_server_type(n) != 1:
            continue
        insert_sql = ""
        if game_channel == "韩分":
            insert_sql = "insert into %s values('%s', 'server_%s', '%s', '%s', '%s', 0 , 0, 0, '%s')" % (str(table_name_kr), str(gateway_id), str(gateway_id), str(ip_addr),str(user), str(db_name), str(game_channel))  
        elif game_channel == "东南亚":
            insert_sql = "insert into %s values('%s', 'server_%s', '%s', '%s', '%s', 0 , 0, 0, '%s')" % (str(table_name_th), str(gateway_id), str(gateway_id), str(ip_addr),str(user), str(db_name), str(game_channel))  
        else:
            insert_sql = "insert into %s values('%s', 'server_%s', '%s', '%s', '%s', 0 , 0, 0, '%s')" % (str(table_name), str(gateway_id), str(gateway_id), str(ip_addr), str(user), str(db_name) , str(game_channel))
        print insert_sql
        server_cur.execute(insert_sql)
        server_conn.commit()    
    for n in range(server_count):
        gateway_id = query_server_info.get_server_gateway(n)
        ip_addr = query_server_info.get_server_ip(n)
        gs_ip = query_server_info.get_server_gsip(n)
        game_channel= query_server_info.get_server_game_channel(n)
        print gs_ip
        update_sql =""
        if query_server_info.get_server_type(n) == 2:
            if game_channel == "韩分":
                update_sql = "update %s set log_host_ip = '%s', log_name = 'logdb_%s', server_ip = '%s' where gateway_id = %s" % (str(table_name_kr),str(ip_addr),str(gateway_id),str(gs_ip),str(gateway_id))
            elif game_channel == "东南亚":
                update_sql = "update %s set log_host_ip = '%s', log_name = 'logdb_%s', server_ip = '%s' where gateway_id = %s" % (str(table_name_th),str(ip_addr),str(gateway_id),str(gs_ip),str(gateway_id))
            else:
                update_sql = "update %s set log_host_ip = '%s', log_name = 'logdb_%s', server_ip = '%s' where gateway_id = %s" % (str(table_name),str(ip_addr),str(gateway_id),str(gs_ip),str(gateway_id))
            print update_sql
        if update_sql =="":
            continue
        server_cur.execute(update_sql)
        server_conn.commit()
    server_cur.close()
    server_conn.close()
# 
create_server_info2db.create_table(host, user, passwd, db,table_name)
create_server_info2db.create_table(host, user, passwd, db,table_name_kr)
create_server_info2db.create_table(host, user, passwd, db,table_name_th)
insert2db(host, user, passwd, db, port,table_name,table_name_kr,table_name_th)

