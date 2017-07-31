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
                    cur_db.execute("SELECT A.char_id,A.pf_role_id,A.level,B.db_task, A.create_time,A.pf_user_id, C.game_id, A.char_name, A.role, A.ss_camp_type, A.combat_power, A.vip_level\
                                FROM ums_char_property A,\
                                ums_char_blob_ex B,\
                                gms_users C\
                                WHERE  A.char_id = B.char_id and C.user_id = A.pf_user_id") 
                                #and CAST(A.last_quittime AS SIGNED) - CAST(A.create_time AS SIGNED) < 3600 * 24 * 7 LIMIT 500000")
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
                        create_time = row[4]
                        user_id = row[5] 
                        game_id = row[6]
                        char_name = row[7]
                        metier = row[8]
                        ss_camp_type = row[9]
                        combat_power = row[10]
                        vip_level = row[11]
                        now_time=int(time.time())
                        #print now_time
                        # deal create_time
                        date_str = time.strftime('%Y%m%d',time.localtime(create_time))
                        date_int = int(date_str)
                        print "create_time:%d \n" % date_int
                        if (date_int >= 20170201 and date_int <= 20170210) or (date_int >= 20170501 and date_int <= 20170510) or (date_int >= 20170601 and date_int <= 20170610) or (date_int >= 20170701 and date_int <= 20170710):
                           print "inserting charid %d \ n" % (char_id)
                           dest_sql = "insert into char_blob_runoff values(%d, %d, %d, %d,'%s','%s', %d, %d, %d, %d, %d, %d)" % (char_id,role_id,gateway_id,level,MySQLdb.escape_string(strTask),now_time,create_time, game_id, metier, ss_camp_type, combat_power, vip_level)
                           dest_cur.execute(dest_sql)
                           #dest_sql = "insert into stat_runoff values(%d, %d, %d, '%s', 0, 0, 0, 0, 0, 0, %d, 0, 0, 0, 0, 0, 0)" % (game_id, role_id, user_id, role_name, create_time)
                           #dest_cur.execute(dest_sql)
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

