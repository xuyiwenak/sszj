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
                       items_tosave_list MediumBlob,\
                       gem_enchase_list MediumBlob,\
                       mount_info MediumBlob,\
                       pet_info MediumBlob,\
                       wing_train_data MediumBlob,\
                       xinfa_data MediumBlob,\
                       log_time int(22),\
                       PRIMARY KEY (`char_id`))\
                       ENGINE=InnoDB DEFAULT CHARSET=utf8' %TABLE_NAME)
    dest_cur.close()
    dest_conn.close()
create_table("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss', 'char_blob')