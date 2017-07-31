import sys
import MySQLdb
import time
#QUERY_TYPE="dungeon"
reload(sys)
sys.setdefaultencoding('utf8')

# compare time
def compare_time(l_time,start_t,end_t):
    s_time = time.mktime(time.strptime(start_t,'%Y-%m-%d %H:%M:%S')) # get the seconds for specify date
    e_time = time.mktime(time.strptime(end_t,'%Y-%m-%d %H:%M:%S'))
    log_time = time.mktime(time.strptime(l_time,'%Y-%m-%d %H:%M:%S'))
    if (float(log_time) >= float(s_time)) and (float(log_time) <= float(e_time)):
        return True
    return False
# convert table `s name to time

def convert_log_table2time(table_name):
    date = table_name[0:8]  #1-8 date 20170408
    new_time = date[0:4] + '-' + date[4:6] + '-' + date[6:8] + ' ' + '00:00:00'
    return new_time
# convert dbname to gatewayid  
def convert_dbname2gate(dbname):
    gatewayid = filter(str.isdigit, dbname)
    #print gatewayid
    return gatewayid
    
# query  
def online_data2db(DB_HOST, DB_USER, DB_PWD, db_name, DB_NAME):
    dest_conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
    dest_cur = dest_conn.cursor()
    dest_cur.execute('SET NAMES UTF8')
    try:
        conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = DB_NAME, port = 3306)
        cur = conn.cursor()
        cur.execute('SET NAMES UTF8')
        dbsql = "select dbname,dbhost from globalserverdb"
        cur.execute(dbsql)
        for row in cur.fetchall():
            dbname = row[0]
            dbhost = row[1]
            if "logdb_" in dbname:
                gateway_id = convert_dbname2gate(dbname)
                print "connect %s %s \ n" % (dbname ,gateway_id)
                try:
                    row_conn = MySQLdb.connect(host = dbhost, user = DB_USER, passwd = DB_PWD, db = dbname, port = 3306)
                    cur_logdb = row_conn.cursor()
                    cur_logdb.execute('SET NAMES UTF8')
                    log_cur = row_conn.cursor()
                    log_cur.execute('SET NAMES UTF8')
                    #get log table name
                    #cur_logdb.execute("select TABLE_NAME from information_schema.tables where table_schema = %s " %dbname)
                    cur_logdb.execute("select TABLE_NAME from information_schema.TABLES where table_schema = %s",dbname)
                    for table_row in cur_logdb.fetchall():
                        table_name = table_row[0]
                        if "_item" not in table_name:
                            continue
                        date=convert_log_table2time(table_name)
                        bool_in_range=compare_time(date,'2017-04-01 00:00:00','2017-05-01 23:59:59')
                        if  bool_in_range == False:
                            continue
                        print "get table name  %s , gatewayid %s \n" %(table_name,gateway_id)
                        log_cur.execute("select char_id ,map_id ,item_id, sheet_id, quantity, quality,op_type,change_type,bag_type,log_time,%s\
                                    from %s where log_time between unix_timestamp('2017-04-01 00:00:00') and unix_timestamp('2017-05-01 23:59:59')" % ( gateway_id, table_name))
                        log_data = log_cur.fetchall()
                        #print log_data
                        dest_sql = "insert into item_log values(%s, %s, %s, %s, %s, %s ,%s, %s, %s ,%s, %s)"
                        dest_cur.executemany(dest_sql,log_data)
                    dest_conn.commit()
                    log_cur.close()
                    cur_logdb.close()
                    row_conn.close()
                except MySQLdb.Error, e:
                        print "MySQL Error:%s" % str(e)
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "MySQL Error:%s" % str(e)
    dest_cur.close()
    dest_conn.close()

online_data2db("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss', 'globalserverdb')
#convert_log_time2time('20170809_dungeon')
#convert_dbname2gate('logdb_240001')
