#coding=utf-8
import sys
import MySQLdb
import time
#QUERY_TYPE="dungeon"
reload(sys)
sys.setdefaultencoding('utf8')
def log_time2timestamp(log_time):
    s_time = time.mktime(time.strptime(log_time,'%Y-%m-%d %H:%M:%S'))
    return s_time
# query  
def query_per_day(DB_HOST, DB_USER, DB_PWD, DB_NAME ,time_start,time_end):
    try:
        filename = "%s_%s.txt" % (DB_NAME,time.strftime('%Y%m%d',time.localtime(time.time())))
        f = open(filename, "w")
        conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = DB_NAME, port = 3306)
        cur = conn.cursor()
        s_time_start = log_time2timestamp(time_start)
        s_time_end = log_time2timestamp(time_end)
        time_pre = s_time_start
        time_post= s_time_start
        time_range = 60 * 60 *24
        while time_post < s_time_end:
            time_pre = time_post
            time_post = time_post + time_range
            time_local = time.localtime(time_pre)
            show_time = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
            print show_time
            rowcnt=cur.execute("select a.map_id, count, b.value, a.gateway_id from (select * from (select map_id, count(role_id) as count, gateway_id from log_activity where op_type =1 and log_time between %s and %s group by gateway_id, map_id)\
                                    c) a, dictionary b where INSTR(b.key, concat('common.mapId.',a.map_id)) > 0 group by a.map_id;" %(time_pre ,time_post)) 
            if rowcnt < 1:
               print "none sql!"
            for row in cur.fetchall():
                map_id = row[0]
                count = row[1]
                value = row[2]
                gateway_id = row[3]
                activity_day_log_str = "%d,%d,%s,%s" %(map_id,count,value,show_time)
                f.write(activity_day_log_str)
                f.write('\n')
                cur.execute("insert into stat_activity values (%d, %d, '%s', %d, %d, '%s')" %(map_id, count, show_time, count, gateway_id, value)) 
        cur.close()
        conn.commit()
        conn.close()
        f.close()
    except MySQLdb.Error, e:
        print "MySQL Error:%s" % str(e)

query_per_day("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','2017-08-01 00:00:00','2017-08-31 23:59:59')
print "query_per_day successfully!"
