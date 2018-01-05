#coding=utf-8
import sys
import MySQLdb
import time
import re
sys.path.append("/home/sszj/data_stat/pb-temp")
import player_pb2,db_pet_pb2

reload(sys)
sys.setdefaultencoding('utf8')
# get data  
def Get_Player_Equip(DB_HOST, DB_USER, DB_PWD, db_name,blob_name,insert_db):
    dest_conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
    dest_cur = dest_conn.cursor()
    try:
        conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
        cur = conn.cursor()
        dbsql = "select pf_role_id,gateway_id,level,pet_info from %s" %blob_name
        cur.execute(dbsql)
        filename = "pet_%s.txt" % time.strftime('%Y%m%d',time.localtime(time.time()))
        f = open(filename, "w")
        for row in cur.fetchall():
            role_id = row[0]
            gateway_id = row[1]
            char_level = row[2]
            pbDBPetInfo = db_pet_pb2.PBDBPetInfo()
            pbDBPetInfo.ParseFromString(row[3])
            #print pbDBPetInfo
            #print len(pbDBPetInfo.pet)
            #中文实验
            for onePet in pbDBPetInfo.pet:
                pet_sheet = onePet.sheet_name
                pet_level = onePet.level
                # 宠物悟性
                pet_savvy = onePet.savvy
                # 宠物成长
                pet_grow  = onePet.rand_grow_battle
                skill_num = 0
                # 累加技能个数
                for oneskill in onePet.skill_list:
                    tmp=len(oneskill.skill)+len(oneskill.replace_skill)+len(oneskill.renareplace_skill)
                    skill_num=tmp+skill_num
                equip_class_num = 0
                # 宠物装备总等级
                for oneequip in onePet.pet_equip_info:
                    equip_class_num=oneequip.equip_class+equip_class_num
                temp_sql = "select value from dictionary b where INSTR(b.key, '%s')" % pet_sheet
                rowcnt = dest_cur.execute(temp_sql)
                if rowcnt != 1:
                   print "sheetid %s not found!" %pet_sheet
                   continue
                data_result = dest_cur.fetchone()
                sheet2name = data_result[0]
                print pet_sheet
                    #print equip_level
                dest_sql = "insert into %s values( %d, %d, %d, '%s','%s', %d, %d, %d, %d , %d)" %(insert_db,role_id,gateway_id,char_level,str(pet_sheet),str(sheet2name),pet_level,pet_savvy,pet_grow,skill_num,equip_class_num)
                dest_cur.execute(dest_sql)
                activity_day_log_str = "%d, %d, %d, %s ,%s, %d, %d, %d, %d , %d" %(role_id,gateway_id,char_level,str(pet_sheet),str(sheet2name),pet_level,pet_savvy,pet_grow,skill_num,equip_class_num)
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
#Get_Player_Equip("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_first_month','pet_info')
#Get_Player_Equip("103.244.235.249", 'sszj', 'DR9m_wqsgF8a','data_stat_ss', 'char_blob_middle_month','pet_info')
#Get_Player_Equip("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_last_month','pet_info')
Get_Player_Equip("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob','char_pet')
