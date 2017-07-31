import sys
import MySQLdb
import time
#QUERY_TYPE="dungeon"
reload(sys)
sys.setdefaultencoding('utf8')

filename = "/home/sszj/data_stat/actitity/activity_allgateway.txt"
f = open(filename, "w")

def get_dictionary_str(DB_HOST, DB_USER, DB_PWD, DB_NAME, param):
    try:
        result = 0
        conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = DB_NAME, port = 3306)
        cur = conn.cursor()
        cur.execute('SET NAMES UTF8')
        tmpsql = "select dictionary.key,value from dictionary where dictionary.key like '%%%s%%'" %param
        print tmpsql
        n = cur.execute(tmpsql)
        if n < 1:
            print "fetch %s error!" %param
            return 0
        if n > 1:
            print "fetch %s more than one" %param
            return 0
        for row in cur.fetchall():
            key = row[0]
            result = row[1]
            print result
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "MySQL Error:%s" % str(e)
    return result

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
        time_range = 60 * 60 *24
        while time_post < s_time_end:
            time_pre = time_post
            time_post = time_post + time_range
            time_local = time.localtime(time_pre)
            show_time = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
            print show_time
            cur.execute("select a.map_id, count, b.value from \
                                (select * from (select map_id, count(char_id) as count from activity_log where op_type =1 and log_time between %s and %s group by map_id)\
                                    c) a, dictionary b where INSTR(b.key, concat('common.mapId.','a.map_id')) > 0 order by count desc;" %(time_pre ,time_post)) 
            for row in cur.fetchall():
                map_id = row[0]
                count = row[1]
                value = row[2]
                activity_day_log_str = "%d,%d,%s,%s" %(map_id,count,value,show_time)
                f.write(activity_day_log_str)
                f.write('\n') 
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "MySQL Error:%s" % str(e)

query_per_day("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','2017-04-13 00:00:00','2017-06-12 23:59:59')
f.close()
print "query_per_day successfully!"