# -*- coding:utf-8 -*- 
import sys
sys.path.append("/data/home/sszj/data_stat/pb-temp")
import MySQLdb
import google.protobuf
import player_pb2

reload(sys)
sys.setdefaultencoding('utf8')

def query_role_gem():
    print "query gem data start!"
    try:
      dest_conn = MySQLdb.connect(host = '103.244.235.249', user = 'sszj', passwd = 'DR9m_wqsgF8a', db = 'data_stat_ss', port = 3306)
      dest_cur = dest_conn.cursor()
      dest_cur.execute('SET NAMES UTF8')
      sql = "select gateway_id, pf_role_id, gem_enchase_list from\
      char_blob_last_month"
      dest_cur.execute(sql)
      for row in dest_cur.fetchall():
         gateway_id = row[0]
         role_id = row[1]
         gem_str = row[2]
         gem_data = player_pb2.PBCharBlob().gem_enchase_list
         gem_data.ParseFromString(gem_str)
         count = len(gem_data.gem_enchase)
         #for gem_chase in gem_data:
         #    print(gem_chase.equip_type)
         for i in range(count):
             #print(gem_data.gem_enchase[i].equip_type)
             #print(gem_data.gem_enchase[i].slot_index)
             #print(gem_data.gem_enchase[i].slot_enable)
             sheet_id = gem_data.gem_enchase[i].gem_sheetid
             #中文注释
             #建立宝石类型和sheetid的映射，取出宝石类型
             #1 到dictionary中查到道具名 2 根据道具名得到类型
             temp_sql = "select value from dictionary b where INSTR(b.key, '%s')" % sheet_id
             rowcnt = dest_cur.execute(temp_sql)
             if rowcnt != 1:
                continue
             data_result = dest_cur.fetchone()
             #print(data_result[0])
             #sheet_name_list = data_result[0].split('·')
             #sheet_name = sheet_name_list[0]
             #level_list = sheet_name_list[1].split('级')
             #gem_dict = {
             #       '物理攻击水晶':1, '法术攻击水晶':2, '物理防御水晶':3, '法术防御水晶':4, '物理命中眼石':5, '法术命中眼石':6, '物理闪避石':7, '法术闪避石':8, '血宝石':9, 
             #       '法力宝石':10, '眩晕玉髓':11, '沉默玉髓':12,'麻痹玉髓':13, '抗眩晕玉髓':14, '抗沉默玉髓':15, '抗麻痹玉髓':16, '火灵珠':17, '木灵珠':18, '水灵珠':19, 
             #       '雷灵珠':20, '光灵珠':21, '暗灵珠':22, '风灵珠':23, '毒灵珠':24, '圣灵珠':25, '赤玛瑙':26, '绿玛瑙':27, '蓝玛瑙':28, '紫玛瑙':29, '白玛瑙':30, '黑玛瑙':31
             #           }             
             #gem_type = gem_dict.get(sheet_name)
             gem_level = sheet_id[4:6]
    	     gem_type = sheet_id[6:9]
             #print(sheet_name)
             #if gem_type == None:
             #   continue;
             #gem_level = level_list[0]
             dest_sql = "insert into gem_stat values(%d,  %d,  %d, %d,  %d, '%s')" % (gateway_id, role_id, int(gem_type), int(gem_level), 1, data_result[0])
             dest_cur.execute(dest_sql)
    except MySQLdb.Error, e:
      print "MySQL Error %d:%s" %(e.args[0], e.args[1])

    dest_cur.close()
    dest_conn.commit()
    dest_conn.close()

query_role_gem()
