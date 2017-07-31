# -*- coding:utf-8 -*- 
import sys
sys.path.append("/data/home/sszj/data_stat/pb-temp")
import MySQLdb
import google.protobuf
import player_pb2

reload(sys)
sys.setdefaultencoding('utf8')

def query_role_gem():
    print "query task info start!"
    try:
      dest_conn = MySQLdb.connect(host = '103.244.235.249', user = 'sszj', passwd = 'DR9m_wqsgF8a', db = 'data_stat_ss', port = 3306)
      dest_cur = dest_conn.cursor()
      dest_cur.execute('SET NAMES UTF8')
      sql = "select gateway_id, pf_role_id, db_task from char_blob_2"
      dest_cur.execute(sql)
      for row in dest_cur.fetchall():
         gateway_id = row[0]
         role_id = row[1]
         task_str = row[2]
         task_data = player_pb2.PBCharBlob().db_task
         task_data.ParseFromString(task_str)
         for quest_one in task_data.quest_normal:
             quest_id = quest_one.quest_id
             quest_state = quest_one.quest_state
             level = 0
             metier = 0
             ss_camp_type = 0
             combat_power = 0
             game_id = 0
             vip_level = 0
             dest_sql = "insert into stat_runoff_2 values(%d,  %d,  %d, %d, %d,\
             %d, %d, %d, %d, %d, %d)" % (gateway_id, role_id, game_id, create_time, quest_id, quest_state, level, metier, ss_camp_type, combat_power,vip_level)
             dest_cur.execute(dest_sql)

    except MySQLdb.Error, e:
      print "MySQL Error %d:%s" %(e.args[0], e.args[1])

    dest_cur.close()
    dest_conn.commit()
    dest_conn.close()

query_role_gem()
