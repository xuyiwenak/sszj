#coding=utf-8
import sys
import MySQLdb
import time
import re
sys.path.append("/home/sszj/data_stat/pb-temp")
import player_pb2,msg_wing_pb2
import create_char_wing_table
reload(sys)
sys.setdefaultencoding('utf8')
# 时装 衣服36 头部37 翅膀41开头
#31XXXXX71.sitem guishen equip
#1-2bit :equip 3-4bit:zhiye 5-7:level 8-9 pinjie  
# get data  
def Get_Player_Fashion(DB_HOST, DB_USER, DB_PWD, db_name,blob_name,insert_db):
    dest_conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
    dest_cur = dest_conn.cursor()
    try:
        conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
        cur = conn.cursor()
        dbsql = "select pf_role_id,gateway_id,level,wing_train_data from %s" %blob_name
        cur.execute(dbsql)
        for row in cur.fetchall():
            role_id = row[0]
            gateway_id = row[1]
            char_level = row[2]
            pbWing = msg_wing_pb2.PBDBWingTrain()
            pbWing.ParseFromString(row[3])
            star = pbWing.cur_star
            jie = pbWing.cur_jie
            print role_id
            #导入数据
            dest_sql = "insert into %s values( %d, %d, %d, %d)" %(insert_db,role_id,gateway_id,star,jie)
            dest_cur.execute(dest_sql)
        dest_conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "MySQL Error:%s" % str(e)
    dest_cur.close()
    dest_conn.close()
def DB2txt(DB_HOST, DB_USER, DB_PWD, db_name,blob_name,insert_db):
    dest_conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
    dest_cur = dest_conn.cursor()
    filename = "wing_%s.txt" % time.strftime('%Y%m%d',time.localtime(time.time()))
    f = open(filename, "w")
    txtsql = "select * from %s order by gateway_id" %insert_db
    dest_cur.execute(txtsql)
    for row in dest_cur.fetchall():
        role_id=row[0]
        gateway_id=row[1]
        star=row[2]
        jie=row[3]
        txt = "%d, %d, %d, %d"  %(role_id,gateway_id,star,jie)
        f.write(txt)
        f.write('\n')
    f.close()
    dest_cur.close()
    dest_conn.close()
create_char_wing_table.create_table("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_zhenyan')
#Get_Player_Fashion("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_first_month','char_wing')
#Get_Player_Fashion("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_middle_month','char_wing')
Get_Player_Fashion("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_last_month','char_wing')
#DB2txt("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_first_month','char_wing')
#DB2txt("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_middle_month','char_wing')
DB2txt("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_last_month','char_wing')

