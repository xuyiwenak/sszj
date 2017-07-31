import sys
import MySQLdb
sys.path.append("/home/sszj/dbtools/server_info")
import query_server_info
import create_server_info2db

table_name = "conf_server_list_vn"
host = '103.244.235.249'
user = 'sszj'
passwd = 'DR9m_wqsgF8a'
db = 'data_stat_ss' 
port = 3306
# create server table
create_server_info2db.create_table(host, user, passwd, db,table_name)
     

