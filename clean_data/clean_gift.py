# coding=utf-8
import sys
import MySQLdb
import time
import re
sys.path.append("/home/sszj/data_stat/pb-temp")
import player_pb2

reload(sys)
sys.setdefaultencoding('utf8')

def Set_player_data(DB_HOST, DB_USER, DB_PWD, db_name):
    try:
        conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
        cur = conn.cursor()
        dest_cur = conn.cursor()
        cur.execute("SELECT A.char_id ,A.pf_role_id,A.level,B.magic_pet_data FROM ums_char_property AS A INNER JOIN ums_char_blob_ex AS B  ON A.char_id = B.char_id")
        for row in cur.fetchall():
            char_id=row[0]
            role_id=row[1]
            if row[3] == None:
                continue
            print role_id
            pbMagicPetData = player_pb2.PBDBMagicPetData()
            pbMagicPetData.ParseFromString(row[3])
            if len(pbMagicPetData.magic_pet_list) == 0:
                print "pbMagicPetData.magic_pet_list == 0"
                continue
            for oneMagicPet in pbMagicPetData.magic_pet_list:
                sheet_name = oneMagicPet.sheet_name
                gift_level = oneMagicPet.gift_level
                gift_exp  =  oneMagicPet.gift_exp
                if gift_level < 0 :
                    print "found charid = %d roleid = %d sheet_name = %sgiftLevel = %d < 0 \ n" % (char_id,role_id,str(sheet_name), gift_level)
                    oneMagicPet.gift_level = 0
                    oneMagicPet.gift_exp = 0  
            # 写回去
            dest_sql = "update ums_char_blob_ex set magic_pet_data  = '%s' where char_id = %d" %(MySQLdb.escape_string(pbMagicPetData.SerializeToString()),char_id)
            dest_cur.execute(dest_sql)
        conn.commit()
    except MySQLdb.Error, e:
        print "MySQL Error:%s" % str(e)
        cur.close()
        conn.close()
        dest_cur.close()
Set_player_data("103.244.235.198", 'sszj', 'DR9m_wqsgF8a', 'gamedb_155003')
