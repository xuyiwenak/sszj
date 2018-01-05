#coding=utf-8
import sys
import MySQLdb
import time
import re
sys.path.append("/home/sszj/data_stat/pb-temp")
import player_pb2
import create_char_zhenyan_table

reload(sys)
sys.setdefaultencoding('utf8')
#512XXXXXX.sitem 真言 
#1-2bit :equip 3 bit:品阶
# get data  
def Get_Player_Equip(DB_HOST, DB_USER, DB_PWD, db_name,blob_name,insert_db):
    dest_conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
    dest_cur = dest_conn.cursor()
    filename = "zhenyan_%s.txt" % time.strftime('%Y%m%d',time.localtime(time.time()))
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
                equip_sheet = oneItem.sheetid
                equip_rune = oneItem.equip_rune_list
                zhenyan_num = equip_rune.open_num
                if zhenyan_num == 0:
                    continue
                sheet_list=["0","0","0"]
                index_count = 0
                for oneRune in equip_rune.rune_list:
                    rune_sheetid=oneRune.rune_sheet
                    sheetidsql="select b.file_name from sheets_info as b where INSTR(b.sheet_id, '%s')" %rune_sheetid
                    fetch_row = dest_cur.execute(sheetidsql)
                    if fetch_row != 1:
                        print "sheetid %s not found!" %rune_sheetid
                        continue
                    name_result = dest_cur.fetchone()
                    fetch_sheet_name = name_result[0]
                    if fetch_sheet_name[0:2] == '51' or fetch_sheet_name[0:2] == '30':
                        temp_sql = "select value from dictionary b where INSTR(b.key, '%s')" % fetch_sheet_name
                        #print fetch_sheet_name
                        rowcnt = dest_cur.execute(temp_sql)
                        if rowcnt != 1:
                            print "sheetid %s not found!" %fetch_sheet_name
                            continue
                        data_result = dest_cur.fetchone()
                        sheet_name = data_result[0]
                        sheet_list.insert(index_count,sheet_name)
                        index_count=index_count + 1
                print sheet_list
                dest_sql = "insert into %s values( %d, %d, %d, %d, '%s','%s','%s','%s')" %(insert_db,role_id,gateway_id,char_level,zhenyan_num,str(equip_sheet),str(sheet_list[0]),str(sheet_list[1]),str(sheet_list[2]))
                #dest_sql = "insert into char_zhenyan values( %d, %d, %d, %d, '%s',0)" %(role_id,gateway_id,char_level,zhenyan_num,equip_sheet)
                dest_cur.execute(dest_sql)
                activity_day_log_str = "%d, %d, %d, %d, %s,%s,%s,%s" %(role_id,gateway_id,char_level,zhenyan_num,str(equip_sheet),str(sheet_list[0]),str(sheet_list[1]),str(sheet_list[2]))
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
create_char_zhenyan_table.create_table("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_zhenyan')
#Get_Player_Equip("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_first_month','char_zhenyan')
#Get_Player_Equip("103.244.235.249", 'sszj', 'DR9m_wqsgF8a','data_stat_ss','char_blob_middle_month','char_zhenyan')
#Get_Player_Equip("103.244.235.249", 'sszj','DR9m_wqsgF8a','data_stat_ss','char_blob_last_month','char_zhenyan')
Get_Player_Equip("103.244.235.249", 'sszj','DR9m_wqsgF8a','data_stat_ss','char_blob','char_zhenyan')
