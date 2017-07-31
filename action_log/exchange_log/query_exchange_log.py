import sys
import MySQLdb
import time
reload(sys)
sys.setdefaultencoding('utf8')
def log_time2timestamp(log_time):
    s_time = time.mktime(time.strptime(log_time,'%Y-%m-%d %H:%M:%S'))
    return s_time
# query  
def query_exchange_log(DB_HOST, DB_USER, DB_PWD, DB_NAME ,time_start,time_end):
    filename = "exchange_log_%s.txt" % time.strftime('%Y%m%d',time.localtime(time.time()))
    f = open(filename, "w")
    try:
        conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = DB_NAME, port = 3306)
        cur = conn.cursor()
        dest_cur = conn.cursor()
        s_time_start = log_time2timestamp(time_start)
        s_time_end = log_time2timestamp(time_end)
        cur.execute("select role_id,sheet_id,gateway_id,log_time as count from action_log where log_type =214 and log_time between %s and %s order by gateway_id" %(s_time_start ,s_time_end)) 
        for row in cur.fetchall():
            role_id = row[0]
            print role_id
            sheet_id = row[1]
            gateway_id = row[2]
            log_time =row[3]
            temp_sql = "select value from dictionary b where INSTR(b.key, '%s')" % sheet_id
            rowcnt = dest_cur.execute(temp_sql)
            if rowcnt != 1:
                print "sheetid %s not found!" %fashion_sheet
                continue
            data_result = dest_cur.fetchone()
            sheet_name = data_result[0]
            activity_day_log_str = "%d,'%s','%s',%d,%d" %(role_id,sheet_id,sheet_name,gateway_id,log_time)
            f.write(activity_day_log_str)
            f.write('\n') 
        f.close()
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "MySQL Error:%s" % str(e)
        
query_exchange_log("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','2017-06-12 00:00:00','2017-07-21 23:59:59')