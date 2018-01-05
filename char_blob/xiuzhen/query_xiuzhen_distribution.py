#coding=utf-8
import sys
import MySQLdb
import time
import re
sys.path.append("/home/sszj/data_stat/pb-temp")
import player_pb2
import create_char_xiuzhen_table
reload(sys)
sys.setdefaultencoding('utf8')

# get data  
def Get_Player_Xiuzhen(DB_HOST, DB_USER, DB_PWD, db_name, blob_name,insert_db):
	dest_conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
	dest_cur = dest_conn.cursor()
	try:
		conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
		cur = conn.cursor()
		dbsql = "select char_id,pf_role_id,gateway_id,level,xiuzhen_data,log_time,char_name from %s" %blob_name
		cur.execute(dbsql)
		for row in cur.fetchall():
			char_id = row[0]
			role_id = row[1]
			gateway_id = row[2]
			char_level = row[3]
			pbXiuzhenData = player_pb2.PBDBXiuzhenData()
			if row[4] is None:
				print "pbXiuzhenData is None!"
				continue
			pbXiuzhenData.ParseFromString(row[4])
			print role_id
			time = row[5]
			char_name = row[6]
			#print pbItemList
			#print len(pbItemList.items_tosave)
			total_zhen = 0
			purple_zhen = 0
			orange_zhen = 0
			for one_xiuzhen in pbXiuzhenData.mai_item_list:
				mai_id = one_xiuzhen.mai_id
				for one_chong in one_xiuzhen.chong_item_list:
					for one_xue in one_chong.xue_item_list:
						xue_id = one_xue.xue_id
						if one_xue.cur_state == 0:
							continue
						total_zhen = total_zhen + 1
						if one_xue.cur_pin < 5 :
							continue
						# 紫色
						elif one_xue.cur_pin == 5:
							print "purple_zhen one_xue = %d" %one_xue.cur_pin
							purple_zhen = purple_zhen + 1
						elif one_xue.cur_pin == 6:
							print "orange_zhen one_xue = %d" %one_xue.cur_pin
							orange_zhen = orange_zhen + 1
					dest_sql = "insert into %s values( %d, %d, %d, %d, %d, '%s',%d, %d, %d)" %(insert_db,time,char_id,role_id,gateway_id,char_level,str(char_name),total_zhen,purple_zhen,orange_zhen)
					dest_cur.execute(dest_sql)
			dest_conn.commit()
		cur.close()
		conn.close()
	except MySQLdb.Error, e:
		print "MySQL Error:%s" % str(e)
	dest_cur.close()
	dest_conn.close()
def DB2txt(DB_HOST, DB_USER, DB_PWD, db_name,insert_db):
	dest_conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
	dest_cur = dest_conn.cursor()
	filename = "xiuzhen_%s.txt" % time.strftime('%Y%m%d',time.localtime(time.time()))
	f = open(filename, "w")
	#txtsql = "select role_id,gateway_id,sheet_id,sheet_name,fashion_type from char_fashion"
	txtsql = "select *,from_unixtime(time) from %s order by gateway_id" %insert_db
	dest_cur.execute(txtsql)
	for row in dest_cur.fetchall():
		local_time = row[0]
		char_id = row[1]
		role_id = row[2]
		gateway_id = row[3]
		char_level = row[4]
		char_name = row[5]
		total_zhen = row[6]
		purple_zhen = row[7]
		orange_zhen = row[8]
		str_time = row[9]
		txt = "'%s', %d, %d, %d, %d, '%s',%d, %d, %d" %(str(str_time),char_id,role_id,gateway_id,char_level,str(char_name),total_zhen,purple_zhen,orange_zhen)
		f.write(txt)
		f.write('\n')
	f.close()
	dest_cur.close()
	dest_conn.close()

create_char_xiuzhen_table.create_table("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss', 'char_xiuzhen')
Get_Player_Xiuzhen("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_blob_kr','char_xiuzhen')
DB2txt("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','char_xiuzhen')

