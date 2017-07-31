import sys
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf8')
# create tables
def create_table(DB_HOST, DB_USER, DB_PWD ,DB_NAME , TABLE_NAME):
    dest_conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = DB_NAME, port = 3306)
    dest_cur = dest_conn.cursor()
    dest_cur.execute('SET NAMES UTF8')
    dest_cur.execute("DROP TABLE IF EXISTS %s" %TABLE_NAME)
    dest_cur.execute(' create table %s \
                       (char_id bigint(30),\
                       pf_role_id int(11),\
                       gateway_id int(11),\
                       level      int(11),\
                       db_task MediumBlob,\
                       log_time int(22),\
                       create_time int(11),\
                       game_id int(11),\
                       metier int(11),\
                       ss_camp_type int(11),\
                       combat_power int(11),\
                       vip_level int(11),\
                       PRIMARY KEY (`char_id`))\
                       ENGINE=InnoDB DEFAULT CHARSET=utf8' %TABLE_NAME)
    dest_cur.close()
    dest_conn.close()
create_table("103.244.235.249", 'sszj', 'DR9m_wqsgF8a','data_stat_ss','char_blob_runoff')
