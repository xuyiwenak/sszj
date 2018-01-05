#coding=utf-8
import sys
import MySQLdb
import time
import re
reload(sys)
sys.setdefaultencoding('utf8')
# Get_consign 
def Get_consign(DB_HOST, DB_USER, DB_PWD, db_name):
    filename = "kr_consign_%s.txt" % time.strftime('%Y%m%d',time.localtime(time.time()))
    f = open(filename, "w")
    print "get consign data start!"
    dest_conn = MySQLdb.connect(DB_HOST, DB_USER, DB_PWD, db_name, port = 3306)
    dest_cur = dest_conn.cursor()
    dbsql = "select db_name,db_host_ip,gateway_id from conf_server_list_kr"
    dest_cur.execute(dbsql)
    for row in dest_cur.fetchall():
        dbname = row[0]
        dbhost = row[1]
        gateway_id = row[2]
        print "connect %s %s \ n" % (dbname ,gateway_id)
        try:
            row_conn = MySQLdb.connect(dbhost,DB_USER,DB_PWD, dbname, port = 3306)
            cur_db = row_conn.cursor()
            cur_db.execute('SET NAMES UTF8')
            cur_db.execute("select sheet_name, quantity, price, consign_time, owner_pf_role_id from gms_consign_log \
                            where from_unixtime(consign_time) >= '2017-09-01 00:00:00' and from_unixtime(consign_time) < '2017-09-30 23:59:59'")
            fetch_value=cur_db.fetchall()
            for row in fetch_value:
                sheet_name = row[0]
                count = row[1]
                price = row[2]
                consign_time = row[3]
                dest_role_id = row[4]
                txt_str = "%d, %d, %s, %d, %d, %d" % (gateway_id,dest_role_id,str(sheet_name),count,price,consign_time)
                print txt_str
                f.write(txt_str)
                f.write('\n')
        except MySQLdb.Error, e:
               print "MySQL Error %d:%s" %(e.args[0], e.args[1])
    f.close()
    row_conn.close()
    cur_db.close()
    dest_cur.close()
    dest_conn.close()
    
Get_consign("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss')

