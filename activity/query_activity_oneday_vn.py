import sys
import MySQLdb
import time
#QUERY_TYPE="dungeon"
reload(sys)
sys.setdefaultencoding('utf8')

filename = "/home/sszj/data_stat/actitity/activity.txt"
f = open(filename, "w")

def log_time2timestamp(log_time):
    s_time = time.mktime(time.strptime(log_time,'%Y-%m-%d %H:%M:%S'))
    return s_time
# query  
def query_per_day(DB_HOST, DB_USER, DB_PWD, DB_NAME ,time_start,time_end):
    try:
        conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = DB_NAME, port = 3306)
        cur = conn.cursor()
        cur.execute('SET NAMES UTF8')
        
        s_time_start = log_time2timestamp(time_start)
        s_time_end = log_time2timestamp(time_end)
        time_pre = s_time_start
        time_post= s_time_start
        time_range = 60 * 60 *24 * 7
        while time_post < s_time_end:
            time_pre = time_post
            time_post = time_post + time_range
            time_local = time.localtime(time_pre)
            show_time = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
            print show_time
            cur.execute("select map_id,map_id,count(distinct(char_id)), count(*) from activity_log where op_type =1 and log_time between %s and %s group by map_id" %(time_pre ,time_post)) 
            for row in cur.fetchall():
                gateway_id = 0
                map_id = row[1]
                count_char_id = row[2]
                player_times = row[3]
                activity_day_log_str = "%d,%d,%s" %(map_id,count_char_id,show_time)
                cur.execute("insert into activity_stat values(%d, %d, '%s', %d)" % (map_id, count_char_id, show_time, player_times))
                #f.write(activity_day_log_str)
                #f.write('\n') 
        conn.commit()
	cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "MySQL Error:%s" % str(e)

query_per_day("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','2017-06-03 00:00:00','2017-06-30 23:59:59')
f.close()
print "query_per_day successfully!"
