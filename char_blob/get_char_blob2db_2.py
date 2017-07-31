import sys
import MySQLdb
import time
sys.path.append("/home/sszj/data_stat/pb-temp")
import player_pb2,db_pet_pb2,msg_wing_pb2,msg_mount_luck_pb2

# get data  
def Get_Blob(DB_HOST, DB_USER, DB_PWD, db_name):
    dest_conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
    dest_cur = dest_conn.cursor()
    dest_cur.execute('SET NAMES UTF8')
    try:
        conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
        cur = conn.cursor()
        cur.execute('SET NAMES UTF8')
        dbsql = "select db_name,db_host_ip,gateway_id from conf_server_list_2"
        cur.execute(dbsql)
        for row in cur.fetchall():
            dbname = row[0]
            dbhost = row[1]
            gateway_id = row[2]
            if "gamedb_" in dbname:
                print "connect %s %s \ n" % (dbname ,gateway_id)
                try:
                    row_conn = MySQLdb.connect(host = dbhost, user = DB_USER, passwd = DB_PWD, db = dbname, port = 3306)
                    cur_db = row_conn.cursor()
                    cur_db.execute('SET NAMES UTF8')
                    pbTask = player_pb2.PBDBTask()
                    cur_db.execute("SELECT A.char_id,A.pf_role_id,A.level,B.db_task\
                                FROM ums_char_property AS A INNER JOIN \
                                ums_char_blob_ex AS B  ON A.char_id = B.char_id limit 500000")
                    fetch_value=cur_db.fetchall()
                    for row in fetch_value:
                        char_id=row[0]
                        #print char_id
                        role_id=row[1]
                        #print role_id
                        #print gateway_id
                        level  =row[2]
                        #print level
                        if row[3]:
                           pbTask.ParseFromString(row[3])
                        strTask=pbTask.SerializeToString()
                        now_time=int(time.time())
                        #print now_time
                        print "inserting charid %d \ n" % (char_id)
                        dest_sql = "insert into char_blob_2 values(%d, %d, %d, %d, '%s', '%s')" %(char_id,role_id,gateway_id,level,MySQLdb.escape_string(strTask),now_time)
                        dest_cur.execute(dest_sql)
                        dest_conn.commit()
                    cur_db.close()
                    row_conn.close()
                except MySQLdb.Error, e:
                    print "MySQL Error:%s" % str(e)
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "MySQL Error:%s" % str(e)
    dest_cur.close()
    dest_conn.close()
Get_Blob("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss')

