import sys
import MySQLdb
import time
reload(sys)
sys.setdefaultencoding('utf8')

def get_dictionary_str(DB_HOST, DB_USER, DB_PWD, DB_NAME, param):
    try:
        result = 0
        conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = DB_NAME, port = 3306)
        cur = conn.cursor()
        tmpsql = "select value from dictionary b where INSTR(b.key, '%s')" % param
        row = dest_cur.execute(tmpsql)
        if row != 1:
            print "sheet %s not found!" %param
        data_result = cur.fetchone()
        result = data_result[0]
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "MySQL Error:%s" % str(e)
    return result

def log_time2timestamp(log_time):
    s_time = time.mktime(time.strptime(log_time,'%Y-%m-%d %H:%M:%S'))
    return s_time
# query  
def query_tiger_log(DB_HOST, DB_USER, DB_PWD, DB_NAME ,time_start,time_end):
    filename = "tiger_log_%s.txt" % time.strftime('%Y%m%d',time.localtime(time.time()))
    f = open(filename, "w")
    try:
        conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = DB_NAME, port = 3306)
        cur = conn.cursor()
        s_time_start = log_time2timestamp(time_start)
        s_time_end = log_time2timestamp(time_end)
        cur.execute("select role_id, count(role_id),gateway_id as count from action_log where log_type =353 and log_time between %s and %s group by role_id,gateway_id" %(s_time_start ,s_time_end)) 
        for row in cur.fetchall():
            role_id = row[0]
            print role_id
            sum = row[1]
            gateway_id = row[2]
            activity_day_log_str = "%d,%d,%d" %(role_id,sum,gateway_id)
            f.write(activity_day_log_str)
            f.write('\n') 
        f.close()
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "MySQL Error:%s" % str(e)
        
query_tiger_log("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','2017-06-12 00:00:00','2017-07-21 23:59:59')