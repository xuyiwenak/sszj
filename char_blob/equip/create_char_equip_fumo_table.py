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
                       (role_id int(11),\
                       gateway_id int(11),\
                       equip_level int(11),\
                       sheet_id char(11),\
                       sheet_name char(11),\
                       star_num int(11),\
                       pinjie_num int(11))\
                       ENGINE=InnoDB DEFAULT CHARSET=utf8' %TABLE_NAME)
    dest_cur.close()
    dest_conn.close()
create_table("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss', 'char_equip_fumo')
