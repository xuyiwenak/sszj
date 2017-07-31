#coding=utf-8
import sys
import MySQLdb
import time
import re
sys.path.append("/home/sszj/data_stat/pb-temp")
import player_pb2

reload(sys)
sys.setdefaultencoding('utf8')
# 时装 衣服36 头部37 翅膀41开头
#31XXXXX71.sitem guishen equip
#1-2bit :equip 3-4bit:zhiye 5-7:level 8-9 pinjie  
# get data  
def Get_Player_Fashion(DB_HOST, DB_USER, DB_PWD, db_name, blob_name,insert_db):
    dest_conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
    dest_cur = dest_conn.cursor()
    try:
        conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
        cur = conn.cursor()
        dbsql = "select pf_role_id,gateway_id,level,items_tosave_list,wardrobe_data from %s" %blob_name
        cur.execute(dbsql)
        #patt = '^31.*?71.sitem$'
        for row in cur.fetchall():
            role_id = row[0]
            gateway_id = row[1]
            char_level = row[2]
            pbItemList = player_pb2.PBItemList()
            pbItemList.ParseFromString(row[3])
            pbDBWardrobe = player_pb2.PBDBWardrobe()
            pbDBWardrobe.ParseFromString(row[4])
            print role_id
            #print pbItemList
            #print len(pbItemList.items_tosave)
            #导入衣橱数据
            for oneWardrobeItem in pbDBWardrobe.data:
                fashion_part = oneWardrobeItem.part
                for oneItem in oneWardrobeItem.bag_slot.item_list:
                    fashion_sheet = oneItem.item.sheetid
                    temp_sql = "select value from dictionary b where INSTR(b.key, '%s')" % fashion_sheet
                    rowcnt = dest_cur.execute(temp_sql)
                    if rowcnt != 1:
                        print "sheetid %s not found!" %fashion_sheet
                        continue
                    data_result = dest_cur.fetchone()
                    sheet_name = data_result[0]
                    dest_sql = "insert into %s values( %d, %d, '%s', '%s', %d)" %(insert_db,role_id,gateway_id,str(fashion_sheet),str(sheet_name),int(fashion_part))
                    dest_cur.execute(dest_sql)
   
            #导入背包数据
            for oneItem in pbItemList.items_tosave:
                now_sheet = oneItem.sheetid
                #print now_sheet[0:2]
                #print now_sheet[7:9]
                if now_sheet[0:2] == '36' or now_sheet[0:2] == '37' or now_sheet[0:2] == '41':
                    #print "%s items_tosave" %role_id
                    temp_sql = "select value from dictionary b where INSTR(b.key, '%s')" % now_sheet
                    rowcnt = dest_cur.execute(temp_sql)
                    if rowcnt != 1:
                        print "sheetid %s not found!" %now_sheet
                        continue
                    data_result = dest_cur.fetchone()
                    sheet_name = data_result[0]
                    fashion_type = 0
                    if now_sheet[0:2] == '36':
                        fashion_type = 2
                    elif now_sheet[0:2] == '37':
                        fashion_type = 1
                    elif now_sheet[0:2] == '41':
                        fashion_type = 3
                    dest_sql = "insert into %s values( %d, %d, '%s', '%s', %d)" %(insert_db,role_id,gateway_id,str(now_sheet),str(sheet_name),int(fashion_type))
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
    filename = "shizhuang_%s.txt" % time.strftime('%Y%m%d',time.localtime(time.time()))
    f = open(filename, "w")
    #txtsql = "select role_id,gateway_id,sheet_id,sheet_name,fashion_type from char_fashion"
    txtsql = "select * from %s order by gateway_id" %insert_db
    dest_cur.execute(txtsql)
    for row in dest_cur.fetchall():
        role_id=row[0]
        gateway_id=row[1]
        now_sheet=row[2]
        sheet_name=row[3]
        fashion_type=row[4]
        txt = "%d, %d, %s, %s, %d" %(role_id,gateway_id,str(now_sheet),str(sheet_name),int(fashion_type))
        f.write(txt)
        f.write('\n')
    f.close()
    dest_cur.close()
    dest_conn.close()
#Get_Player_Fashion("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_first_month','char_fashion')
#Get_Player_Fashion("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_middle_month','char_fashion')
Get_Player_Fashion("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_last_month','char_fashion')
#DB2txt("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_first_month','char_fashion')
#DB2txt("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_middle_month','char_fashion')
DB2txt("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_last_month','char_fashion')

