#coding=utf-8
import sys
import MySQLdb
import time
import create_activity_table
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
# query  
def online_data2db(DB_HOST, DB_USER, DB_PWD, db_name, server_list,insert_dbname,time_start,time_end):
    dest_conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
    dest_cur = dest_conn.cursor()
    try:
        conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
        cur = conn.cursor()
        dbsql = "select log_name,log_host_ip,gateway_id from %s" %server_list
        cur.execute(dbsql)
        for row in cur.fetchall():
            dbname = row[0]
            dbhost = row[1]
            gateway_id = row[2]
            if "logdb_" in dbname:
                print "connect %s %s \ n" % (dbname ,gateway_id)
                try:
                    row_conn = MySQLdb.connect(host = dbhost, user = DB_USER, passwd = DB_PWD, db = dbname, port = 3306)
                    cur_logdb = row_conn.cursor()
                    log_cur = row_conn.cursor()
                    cur_logdb.execute("select TABLE_NAME from information_schema.TABLES where table_schema = %s",dbname)
                    for table_row in cur_logdb.fetchall():
                        table_name = table_row[0]
                        if "_dungeon" not in table_name:
                            continue
                        date=convert_log_table2time(table_name)
                        bool_in_range=compare_time(date,time_start,time_end)
                        if  bool_in_range == False:
                            continue
                        print "get table name  %s , gatewayid %s \n" %(table_name,gateway_id)
                        log_cur.execute("select char_id, map_id, char_level, total_damager, totoal_injured, type, creature_killed, money_gained,death_times, exp_gained, op_type ,log_time,%s\
                                    from %s where log_time between unix_timestamp('%s') and unix_timestamp('%s')" % ( gateway_id, table_name,time_start,time_end))
                        log_data = log_cur.fetchall()            
                        #print log_data
                        dest_sql = "insert into log_activity values(%s, %s, %s, %s, %s, %s ,%s, %s, %s ,%s, %s, %s, %s)"
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
create_activity_table.create_table('103.244.235.249', 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss', 'log_activity')
online_data2db("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','conf_server_list_2','log_activity','2017-08-01 00:00:00','2017-08-31 23:59:59')
