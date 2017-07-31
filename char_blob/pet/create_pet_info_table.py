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
                       char_level int(11),\
                       pet_sheet char(22),\
                       pet_sheet_name  char(22),\
                       pet_level int(11),\
                       pet_savvy int(11),\
                       pet_grow  int(11),\
                       pet_skill_num int(11),\
                       pet_equip_level_plus int(11))\
                       ENGINE=InnoDB DEFAULT CHARSET=utf8' %TABLE_NAME)
    dest_cur.close()
    dest_conn.close()
create_table("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss', 'pet_info')