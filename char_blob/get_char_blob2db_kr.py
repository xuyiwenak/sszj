import sys
import MySQLdb
import time
sys.path.append("/home/sszj/data_stat/pb-temp")
import player_pb2,db_pet_pb2,msg_wing_pb2,msg_mount_luck_pb2
import create_charblob_table_kr
# get data  
def Get_Blob(DB_HOST, DB_USER, DB_PWD, db_name, conf_server_list):
	dest_conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
	dest_cur = dest_conn.cursor()
	dest_cur.execute('SET NAMES UTF8')
	try:
		conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, db = db_name, port = 3306)
		cur = conn.cursor()
		cur.execute('SET NAMES UTF8')
		dbsql = "select db_name,db_host_ip,gateway_id from %s" %conf_server_list
		cur.execute(dbsql)
		for row in cur.fetchall():
			dbname = row[0]
			dbhost = row[1]
			gateway_id = row[2]
			print "connect %s %s \ n" % (dbname ,gateway_id)
			try:
				row_conn = MySQLdb.connect(host = dbhost, user = DB_USER, passwd = DB_PWD, db = dbname, port = 3306)
				cur_db = row_conn.cursor()
				cur_db.execute('SET NAMES UTF8')
				pbXiuzhenData = player_pb2.PBDBXiuzhenData()
				cur_db.execute("SELECT A.char_id ,A.pf_role_id,A.char_name,A.level,B.xiuzhen_data\
							FROM ums_char_property AS A INNER JOIN ums_char_blob_ex AS B  ON A.char_id = B.char_id \
							WHERE A.level >= 50")
				fetch_value=cur_db.fetchall()
				for row in fetch_value:
					char_id=row[0]
					print char_id
					role_id=row[1]
					#print role_id
					char_name = row[2]
					level  =row[3]
					if row[4] == None:
						continue
					pbXiuzhenData.ParseFromString(row[4])
					if pbXiuzhenData is None :
						print "pbXiuzhenData is None!"
						continue
					strXiuzhenData=pbXiuzhenData.SerializeToString()

					#print len(strXinfa)
					now_time=int(time.time())
					#print now_time
					print "inserting charid %d \ n" % (char_id)
					dest_sql = "insert into char_blob_kr values(%d, %d, %d, %d, '%s', '%s', '%s')" %(char_id,role_id,gateway_id,level,str(char_name),MySQLdb.escape_string(strXiuzhenData),now_time)
					dest_cur.execute(dest_sql)
				dest_conn.commit()
				cur_db.close()
				row_conn.close()
			except MySQLdb.Error, e:
				print "MySQL Error:%s" % str(e)
		cur.close()
		conn.close()
	except MySQLdb.Error, e:
		print "MySQL Error:%s" % str(e)
	dest_cur.close()
	dest_conn.close()
create_charblob_table_kr.create_table("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss' , 'char_blob_kr')
Get_Blob("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','conf_server_list_kr')

