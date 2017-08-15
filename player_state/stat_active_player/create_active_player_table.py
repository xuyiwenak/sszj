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
    dest_cur.execute("create table %s \
                       (role_id int(11) unsigned,\
                       char_id bigint(32), \
                       user_id int(11) unsigned,\
                       role int(4) unsigned,\
                       level int(4) unsigned,\
                       ss_camp_type int(4) unsigned,\
                       diamond_blue bigint(22),\
                       diamond_red bigint(22),\
                       unbuond_money bigint(22),\
                       zhenqi bigint(22),\
                       lingqi bigint(11),\
                       daytime char(32),\
                       gateway_id int(11),\
                       game_id int(11),\
                       vip_level int(11),\
                       last_quittime int(20) unsigned,\
                       map_id int(11),\
                       device_info varchar(255),\
                       pvp_honor bigint(11),\
                       renown bigint(22),\
                       exploit bigint(22),\
                       combat_power int(11),\
                       PRIMARY KEY (`char_id`))\
                       ENGINE=InnoDB DEFAULT CHARSET=utf8" %TABLE_NAME)
    dest_cur.close()
    dest_conn.close()
create_table("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss', 'char_property')