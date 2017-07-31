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
        dbsql = "select db_name,db_host_ip,gateway_id from conf_server_list_first_month"
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
                    pbBag = player_pb2.PBItemList()
                    pbGem = player_pb2.PBGemEnchaseList()
                    pbMount = player_pb2.PBMountInfo()
                    pbPet = db_pet_pb2.PBDBPetInfo()
                    pbWing = msg_wing_pb2.PBDBWingTrain()
                    pbXinfa = player_pb2.PBDBXinfaData()
                    pbLucky = msg_mount_luck_pb2.PBDBLuckInfo()
                    pbWardrobe = player_pb2.PBDBWardrobe()
                    backup_time = 0
                    cur_db.execute("select max(last_quittime) from ums_char_property")
                    for row in cur_db.fetchall():
                        backup_time = row[0]  
                    cur_db.execute("SELECT A.char_id ,A.pf_role_id,A.level,B.items_tosave_list,B.gem_enchase_list,B.mount_info,B.pet_info,B.wing_train_data,B.xinfa_data,B.luck_data,B.wardrobe_data\
                                FROM ums_char_property AS A INNER JOIN ums_char_blob_ex AS B  ON A.char_id = B.char_id \
                                WHERE  ABS(%d - A.last_quittime) < 7 * 24 * 3600 AND A.level >= 50" % backup_time)
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
                           pbBag.ParseFromString(row[3])
                        strBag=pbBag.SerializeToString()
                        #print len(strBag)
                        if row[4]:
                           pbGem.ParseFromString(row[4])
                        strGem=pbGem.SerializeToString()
                        #print len(strGem)
                        if row[5]:
                           pbMount.ParseFromString(row[5])
                        strMount=pbMount.SerializeToString()
                        #print len(strMount)
                        if row[6]:
                           pbPet.ParseFromString(row[6])
                        strPet=pbPet.SerializeToString()
                        #print len(strPet)
                        if row[7]:
                           pbWing.ParseFromString(row[7])
                        strWing=pbWing.SerializeToString()
                        #print len(strWing)
                        if row[8]:
                           pbXinfa.ParseFromString(row[8])
                        strXinfa=pbXinfa.SerializeToString()
                        if row[9]:
                           pbLucky.ParseFromString(row[9])
                        strLucky=pbLucky.SerializeToString()
                        if row[10]:
                           pbWardrobe.ParseFromString(row[10])
                        strWardrobe=pbWardrobe.SerializeToString()
                        #print len(strXinfa)
                        now_time=int(time.time())
                        #print now_time
                        print "inserting charid %d \ n" % (char_id)
                        dest_sql = "insert into char_blob_first_month values(%d, %d, %d, %d, '%s', '%s' ,'%s', '%s', '%s' ,'%s', '%s', '%s', '%s')" %(char_id,role_id,gateway_id,level,MySQLdb.escape_string(strBag),MySQLdb.escape_string(strGem),MySQLdb.escape_string(strMount),MySQLdb.escape_string(strPet),MySQLdb.escape_string(strWing),MySQLdb.escape_string(strXinfa),MySQLdb.escape_string(strLucky),MySQLdb.escape_string(strWardrobe),now_time)
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

