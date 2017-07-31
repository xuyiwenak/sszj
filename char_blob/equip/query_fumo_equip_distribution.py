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
def Get_Player_Equip(DB_HOST, DB_USER, DB_PWD, db_name):
    dest_conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
    dest_cur = dest_conn.cursor()
    filename = "equip_fumo_%s.txt" % time.strftime('%Y%m%d',time.localtime(time.time()))
    f = open(filename, "w")
    try:
        conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
        cur = conn.cursor()
        #cur.execute('SET NAMES UTF8')
        dbsql = "select pf_role_id,gateway_id,level,items_tosave_list\
                from char_blob_last_month"
        cur.execute(dbsql)
        for row in cur.fetchall():
            role_id = row[0]
            gateway_id = row[1]
            char_level = row[2]
            pbItemList = player_pb2.PBItemList()
            pbItemList.ParseFromString(row[3])
            #print pbItemList
            #print len(pbItemList.items_tosave)
            #中文实验
            if char_level > 100:
                for oneItem in pbItemList.items_tosave:
                    now_sheet = oneItem.sheetid[0:9]
                    attach  =   oneItem.attach_pro
                    #print now_sheet[0:2]
                    #print now_sheet[7:9]
                    if len(attach.properties) != 0 and now_sheet[0:2] == '31':
                        temp_sql = "select value from dictionary b where INSTR(b.key, '%s')" % now_sheet
                        #dest_cur.execute('SET NAMES UTF8')
                        rowcnt = dest_cur.execute(temp_sql)
                        if rowcnt != 1:
                            print "sheetid %s not found!" %now_sheet
                            continue
                        data_result = dest_cur.fetchone()
                        sheet_name = data_result[0]
                        equip_level=now_sheet[4:7]
                        star_num = ["0","0","0"]
                        pinjie_num = ["0","0","0"]
                        index_cnt=0
                        print now_sheet
                        for oneProperty in attach.properties:
                            star_num[index_cnt] = oneProperty.quality
                            pinjie_num[index_cnt] = oneProperty.prop_class
                            index_cnt = index_cnt + 1
                        #print equip_level
                        #dest_sql = "insert into char_equip_fumo values( %d, %d, %d, '%s', '%s', %d, %d)" %(role_id,gateway_id,int(equip_level),str(now_sheet),str(sheet_name),star_num[0],pinjie_num[0],star_num[1],pinjie_num[1],star_num[2],pinjie_num[2])
                        #dest_cur.execute(dest_sql)
                        txt_str = "%d, %d, %d, %s, %s, %d, %d, %d, %d, %d, %d" % (role_id,gateway_id,int(equip_level),str(now_sheet),str(sheet_name),star_num[0],pinjie_num[0],star_num[1],pinjie_num[1],star_num[2],pinjie_num[2])
                        f.write(txt_str)
                        f.write('\n')
            dest_conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "MySQL Error:%s" % str(e)
    dest_cur.close()
    dest_conn.close()
    f.close()
Get_Player_Equip("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss')

