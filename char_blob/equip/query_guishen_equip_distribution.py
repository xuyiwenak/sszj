#coding=utf-8
import sys
import MySQLdb
import time
import re
sys.path.append("/home/sszj/data_stat/pb-temp")
import player_pb2

reload(sys)
sys.setdefaultencoding('utf8')
#31XXXXX71.sitem guishen equip
#1-2bit :equip 3-4bit:zhiye 5-7:level 8-9 pinjie  
# get data  
def Get_Player_Equip(DB_HOST, DB_USER, DB_PWD, db_name,blob_name):
    dest_conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
    dest_cur = dest_conn.cursor()
    filename = "guishen_equip_log_%s.txt" % time.strftime('%Y%m%d',time.localtime(time.time()))
    f = open(filename, "w")
    try:
        conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
        cur = conn.cursor()
        dbsql = "select pf_role_id,gateway_id,level,items_tosave_list from %s" %blob_name
        cur.execute(dbsql)
        #patt = '^31.*?71.sitem$'
        for row in cur.fetchall():
            role_id = row[0]
            gateway_id = row[1]
            char_level = row[2]
            pbItemList = player_pb2.PBItemList()
            pbItemList.ParseFromString(row[3])
            #print pbItemList
            #print len(pbItemList.items_tosave)
            for oneItem in pbItemList.items_tosave:
                now_sheet = oneItem.sheetid
                if now_sheet[0:2] == '31' and now_sheet[7:9] == '71':
                    temp_sql = "select value from dictionary b where INSTR(b.key, '%s')" % now_sheet
                    rowcnt = dest_cur.execute(temp_sql)
                    if rowcnt != 1:
                        print "sheetid %s not found!" %now_sheet
                        continue
                    data_result = dest_cur.fetchone()
                    sheet_name = data_result[0]
                    equip_level=now_sheet[4:7]
                    print now_sheet
                    #print equip_level
                    dest_sql = "insert into char_equip values( %d, %d, '%s', '%s', '%s')" %(role_id,gateway_id,int(equip_level),str(now_sheet),str(sheet_name))
                    dest_cur.execute(dest_sql)
                    activity_day_log_str = "%d, %d, %d, %s, %s" %(role_id,gateway_id,int(equip_level),str(now_sheet),str(sheet_name))
                    f.write(activity_day_log_str)
                    f.write('\n') 
            dest_conn.commit()
        f.close()
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "MySQL Error:%s" % str(e)
    dest_cur.close()
    dest_conn.close()
#Get_Player_Equip("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_first_month')
#Get_Player_Equip("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_middle_month')
#Get_Player_Equip("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_last_month')
Get_Player_Equip("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob')
