# -*- coding:utf-8 -*- 
import sys
sys.path.append("/data/home/sszj/data_stat/pb-temp")
import MySQLdb
import google.protobuf
import player_pb2

reload(sys)
sys.setdefaultencoding('utf8')

def query_role_gem():
    print "query mount info start!"
    try:
      dest_conn = MySQLdb.connect(host = '103.244.235.249', user = 'sszj', passwd = 'DR9m_wqsgF8a', db = 'data_stat_ss', port = 3306)
      dest_cur = dest_conn.cursor()
      dest_cur.execute('SET NAMES UTF8')
      sql = "select gateway_id, pf_role_id, mount_info, luck_data, level from char_blob_last_month"
      dest_cur.execute(sql)
      for row in dest_cur.fetchall():
         gateway_id = row[0]
         role_id = row[1]
         mount_str = row[2]
         luck_str = row[3]
         level = row[4]
         mount_info = player_pb2.PBCharBlob().mount_info
         mount_info.ParseFromString(mount_str)
         luck_info = player_pb2.PBCharBlob().luck_data
         luck_info.ParseFromString(luck_str)
         mount_level = 0
         immortal_level = 0
         immortal_star = 0
         evil_level = 0
         evil_star = 0
         for mount_one in mount_info.mount:
             mount_level = mount_one.level
             # 后续加上剑纹、剑魂的解析
             for rune_item_one in mount_one.RuneSlot.rune_item:
                sheet_id = rune_item_one.item.sheetid
                quantity = rune_item_one.item.quantity
                item_type = 1
                dest_sql = "insert into mount_item_stat values(%d,  %d,  %d, '%s', %d)" % (gateway_id, role_id, item_type, sheet_id, quantity)
                dest_cur.execute(dest_sql)
              
             for soul_item_one in mount_one.soul_star.soul_star_item:
                sheet_id = soul_item_one.item.sheetid
                quantity = soul_item_one.item.quantity
                item_type = 2               
                dest_sql = "insert into mount_item_stat values(%d,  %d,  %d, '%s', %d)" % (gateway_id, role_id, item_type, sheet_id, quantity)
                dest_cur.execute(dest_sql)

         for luck_one in luck_info.db_info:
             if luck_one.type == 0:
                immortal_level = luck_one.cur_level
                immortal_star = luck_one.cur_star
             if luck_one.type == 1:
                evil_level = luck_one.cur_level
                evil_star = luck_one.cur_star
         if level >= 70:
             dest_sql = "insert into mount_info_stat values(%d,  %d,  %d, %d,  %d, %d, %d)" % (gateway_id, role_id, mount_level, immortal_level, immortal_star, evil_level, evil_star)
             dest_cur.execute(dest_sql)
    except MySQLdb.Error, e:
      print "MySQL Error %d:%s" %(e.args[0], e.args[1])

    dest_cur.close()
    dest_conn.commit()
    dest_conn.close()

query_role_gem()
