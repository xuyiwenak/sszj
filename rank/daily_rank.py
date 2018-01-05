#coding=utf-8
import sys
import MySQLdb
import time
import re
import data_pb2
import codecs
import datetime
reload(sys)
sys.setdefaultencoding('utf8')

class GuildMember:
	def __init__(self, gameid, account, guildid, userid, charid, charname, guildpost):
		self.gameid = gameid
		self.account = account
		self.guildid = guildid
		self.userid = userid
		self.charid = charid
		self.charname = charname
		self.guildpost = guildpost
class MyData:
	def __init__(self, guildid, guildname, guildbattle, guildmembers):
		self.guildid = guildid
		self.guildname = guildname
		self.guildbattle = guildbattle
		self.guildmembers = guildmembers

def InsertToList(list, value):
	if(len(list) < 3):
		list.append(value)
		return
	for item in list:
		if(item.guildlevel < value.guildlevel):
			item.guildid = value.guildid
			item.guildname = value.guildname
			item.guildlevel = value.guildlevel
			return
# Get_rank 
def Get_rank(DB_HOST, DB_USER, DB_PWD, db_name , server_conf_list,rank_type,limit_num,sys_path):
	print "get rank data start!"
	dest_conn = MySQLdb.connect(DB_HOST, DB_USER, DB_PWD, db_name, port = 3306)
	dest_cur = dest_conn.cursor()
	dbsql = "select db_name,db_host_ip,gateway_id from %s" %server_conf_list
	dest_cur.execute(dbsql)
	for row in dest_cur.fetchall():
		dbname = row[0]
		dbhost = row[1]
		gateway_id = row[2]
		filename = "%srank_%s_%s_%s.txt" % (sys_path,gateway_id,server_conf_list,time.strftime('%Y%m%d',time.localtime(time.time())))
		f = open(filename, "a")
		title = '排行榜' + str(rank_type) + '网关' + str(gateway_id)
		f.write(str(title))
		f.write('\n')
		index = 'game_id,' + 'account,' + 'pf_user_id,' +'pf_role_id,' +'pf_user_id,' +'char_name,' +'combat_power,' +'level,' +'role,' +'ss_camp_type,' +'pvp_score,' +'charm_point'
		f.write(str(index))
		f.write('\n')
		print "connect %s %s \ n" % (dbname ,gateway_id)
		try:
			row_conn = MySQLdb.connect(dbhost,DB_USER,DB_PWD, dbname, port = 3306)
			cur_db = row_conn.cursor()
			sql = "select A.game_id, A.account, A.pf_user_id, B.pf_role_id, B.char_name,B.combat_power,B.level,B.role,B.ss_camp_type,B.pvp_score,B.charm_point\
							from ums_user_info_ex as A, ums_char_property as B \
							where A.pf_user_id = B.pf_user_id order by B.%s desc limit %d" %(rank_type,limit_num)
			cur_db.execute(sql)
			rows=cur_db.fetchall()
			for one_row in rows:
				print one_row
				game_id = one_row[0]
				account = one_row[1]
				pf_user_id = one_row[2]
				pf_role_id = one_row[3]
				char_name = one_row[4]
				combat_power = one_row[5]
				level = one_row[6]
				role = one_row[7]
				ss_camp_type = one_row[8]
				pvp_score = one_row[9]
				charm_point =  one_row[10]
				txt_str ="%s,%s,%s,%s,%s,%s, %s, %s, %s, %s, %s" %(game_id,str(account),pf_user_id,pf_role_id,str(char_name),combat_power,level,role,ss_camp_type,pvp_score,charm_point)
				f.write(txt_str)
				f.write('\n')
			f.close()
		except MySQLdb.Error, e:
				print "MySQL Error %d:%s" %(e.args[0], e.args[1])
	row_conn.close()
	cur_db.close()
	dest_cur.close()
	dest_conn.close()
# Get_Guild 
def Get_Guild(DB_HOST, DB_USER, DB_PWD, db_name , server_conf_list,limit_num,sys_path):
	print "get Get_Guild start!"
	dest_conn = MySQLdb.connect(DB_HOST, DB_USER, DB_PWD, db_name, port = 3306)
	dest_cur = dest_conn.cursor()
	dbsql = "select db_name,db_host_ip,gateway_id from %s" %server_conf_list
	dest_cur.execute(dbsql)
	for row in dest_cur.fetchall():
		dbname = row[0]
		dbhost = row[1]
		gateway_id = row[2]
		print "connect %s %s \ n" % (dbname ,gateway_id) 
		try:
			row_conn = MySQLdb.connect(dbhost,DB_USER,DB_PWD, dbname, port = 3306)
			cur_db = row_conn.cursor()
			cur_db.execute('SET NAMES UTF8')
			guild_sql = "select guild_data, is_delete from ums_gateway_guild_data"
			cur_db.execute(guild_sql)
			gulid_rows=cur_db.fetchall()
			list = []
			memberlist = []
			for result in gulid_rows:
				if result[0] is None or result[1] == 1:
					continue
				else:
					guild_data = data_pb2.PBGuildData()
					guild_data.ParseFromString(result[0])
					summary = guild_data.guild_summary
					guild_id = summary.guild_id
					guild_name = summary.guild_name
					guild_battle = summary.guild_power
					tmpdata = MyData(guild_id, guild_name, int(guild_battle), guild_data.guild_member)
					list.append(tmpdata)
					list.sort(lambda x, y : cmp(x.guildbattle, y.guildbattle), reverse=True)
			print len(list)
			for i in range(0, len(list)):
				if i > limit_num:
					break
				if list[i] == None:
					continue
				if len(list[i].guildmembers) == 0:
					continue
				for member in list[i].guildmembers:
					guildmember = GuildMember(0, 0, list[i].guildid, 0, member.char_id, member.char_name, member.post)
					memberlist.append(guildmember)
			for member in memberlist:
				sql1 = "select A.game_id, A.account, B.pf_user_id, B.pf_role_id from ums_user_info_ex as A, ums_char_property as B where A.pf_user_id = B.pf_user_id and char_id = " + str(member.charid)
				cur_db.execute(sql1)
				result_sql = cur_db.fetchone()
				member.gameid = result_sql[0]
				member.account = result_sql[1]
				member.userid = result_sql[2]
				member.charid = result_sql[3]
			nowtime = time.strftime('%Y%m%d',time.localtime(time.time()))
			guildfile = sys_path + 'guild_result_' + nowtime + '.txt'
			memberfile = sys_path + 'member_result_' + nowtime + '.txt'
			file = codecs.open(guildfile, 'a+', encoding = 'utf-8')
			for item in list:
				file.write(str(gateway_id) + '\t' +  str(item.guildid) + '\t' + str(item.guildname) + '\t' + str(item.guildbattle) + '\t' + '\n')
			
			file.close()
			file = codecs.open(memberfile, 'a+', encoding = 'utf-8')
			for item in memberlist:
				file.write(str(gateway_id) + '\t' + str(item.gameid) + '\t' +  str(item.guildid) + '\t' + str(item.account) + '\t' + str(item.userid) + '\t' + str(item.charid) + '\t' + str(item.charname) + '\t' + str(item.guildpost) + '\n')
			file.close()
		except MySQLdb.Error, e:
			print "MySQL Error %d:%s" %(e.args[0], e.args[1])
	row_conn.close()
	cur_db.close()
	dest_cur.close()
	dest_conn.close()


Get_rank("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','conf_server_list_th','level',10,'/home/sszj/data_stat/rank/result/')
Get_rank("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','conf_server_list_th','combat_power',10,'/home/sszj/data_stat/rank/result/')
Get_rank("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','conf_server_list_th','charm_point',10,'/home/sszj/data_stat/rank/result/')
Get_rank("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','conf_server_list_th','pvp_score',10,'/home/sszj/data_stat/rank/result/')
print "Get_rank!"
Get_Guild("103.244.235.249", 'sszj', 'DR9m_wqsgF8a', 'data_stat_ss','conf_server_list_th',10,'/home/sszj/data_stat/rank/result/')
print "Get_Guild!"
