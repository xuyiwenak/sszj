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
                       map_id int(11),\
                       char_level int(11),\
                       total_damage int(11),\
                       death_times int(11),\
                       total_injures int(11),\
                       dungun_type int(11),\
                       creature_killed int(11),\
                       money_gained int(20),\
                       exp_gained int(24),\
                       op_type int(10),\
                       log_time int(11),\
                       gateway_id int(11))\
                       ENGINE=InnoDB DEFAULT CHARSET=utf8' %TABLE_NAME)
    dest_cur.close()
    dest_conn.close()
create_table("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss', 'log_activity')
