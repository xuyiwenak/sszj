#!/usr/bin/python
#coding=utf-8
import MySQLdb
import sys
import os
import time
import string
import re

reload(sys)
sys.setdefaultencoding('utf-8')
# 外网通用密码
srcUser = "root"
srcPasswd = "game"
# 配置文件名称
cfg = "transconfig.cfg"
# 服务器列表数据库名称和表名
server_list_db_ip = "10.10.252.15"
server_list_dbname = "test"
server_list_tbname = 'conf_server_list_2'
# ums_char_property 表需要迁移的数据(默认配置是最全的，随版本字段增加在后面添加)
list_property_field = ["race","role","level","exp","acc_exp","hp","mp","unbuond_money","lingqi","charm_point","zhenqi","send_flower_socre","exploit","can_equip_hornor","killer","energy"]
# 有些字段废弃了
# 不需要迁移的字段 "shortcut","cdtime","niuer_info","black_list","delete_friend_info","guild_state","team_info","tmp_shard_iu_info","friend_data",\
# 			 "original_closthes","marriage_data","hold_data","mute","span_imbattle_data","spanteam_data","guild_liveness_data",	"clothes_styleid_default",\
#			 "hair_style_id","hair_sheet_id"
# ums_char_blob_ex 表需要迁移的数据(默认配置是最全的，随版本字段增加在后面添加) 如果老版本有些字段不存在从下面的列表找到报错的地方去掉就可以了
list_field = ["bag",\
			"items_tosave_list",\
			"mission_done_tosave_list",\
			"counter_info_tosave_list",\
			"dungeon",\
			"lottery_list",\
			 "gem_enchase_list",\
			 "char_title",\
			 "offline_exp_info",\
			 "buy_backs",\
			 "mount_info",\
			 "db_task",\
			 "char_gameop_list",\
			 "func_open_info",\
			 "magicweapon_info",\
			 "skill_info",\
			 "pet_info",\
			 "activities_data",\
			 "guild_skill_list",\
			 "climb_tower",\
			 "shop_info",\
			 "sign_activity",\
			 "all_buff_data",\
			 "justice_data",\
			 "newserver_data",\
			 "newserver_recharge",\
			 "xiu_xian_data",\
			 "consume_record_list",\
			 "last_guild_skill",\
			 "single_data",\
			 "exchange_shop",\
			 "quest_data",\
			 "gm_mail_list",\
			 "cornucopia",\
			 "repertory",\
			 "excuting_treasure_incidents",\
			 "newroleact",\
			 "offline_exp_data",\
			 "change_camp_data",\
			 "lottery_status_data",\
			 "luck_data",\
			 "boating_data",\
			 "potential_data",\
			 "wardrobe_data",\
			 "pet_pve_battle_array",\
			 "wing_train_data",\
			 "pet_pvp_battle_array",\
			 "login_gifts_data",\
			 "onearmbandit_data",\
			 "xinfa_data",\
			 "oldplayer_back_data",\
			 "xiuzhen_data",\
			 "magic_pet_data",\
			 "player_bind_vip_data"] 
def importBlobData(srchost, srcdb, dsthost, dstdb, srcRoleId, destRoleId):
	log_data_str = ""
	srcHost  = srchost
	srcDB	= srcdb
	host	=  dsthost
	dbname  =  dstdb
	try:
		conn = MySQLdb.connect(srcHost, srcUser, srcPasswd, srcDB);
		cursor = conn.cursor()
		tmpSelectSql = 'select '
		list_len = len(list_field)
		count = 0
		for field in list_field:
			if (list_len-1)==count:
				tmpSelectSql += '%s' % field
			else:
				tmpSelectSql += '%s, ' % field
			count = count + 1
		tmpSelectSql += (' from ums_char_blob_ex where pf_role_id=%s') % (srcRoleId)
		#print "importBlobData", tmpSelectSql
		log_data_str += tmpSelectSql
		log_data_str += '\n'
		cursor.execute(tmpSelectSql)
		tmpSql = 'update ums_char_blob_ex set '
		isSuccess = False
		for result in cursor:
			index = 0
			isSuccess = True
			for field in list_field:
				tmpSql += field
				if (list_len-1) == index:
					tmpSql += " = '%s' " % MySQLdb.escape_string(result[index])
				else:
					tmpSql += " = '%s', " % MySQLdb.escape_string(result[index])
				index = index+1
				
			tmpSql += ' where pf_role_id=%s' % destRoleId
			break
		#print "importBlobData", tmpSql
		cursor.close()
		conn.close()
		
		#update
		conn = MySQLdb.connect(dsthost, srcUser,srcPasswd, dstdb)
		cursor = conn.cursor()
		if isSuccess==True:
			print '=====>table name ums_char_blob_ex update from %s to %s start!' % (srcRoleId,destRoleId)
			cursor.execute(tmpSql)
			log_data_str += tmpSql
			log_data_str += '\n'
			conn.commit()
			print '=====>table name ums_char_blob_ex update rom %s to %s success!' % (srcRoleId,destRoleId)
		cursor.close()
		conn.close()
	except BaseException, e:
		print 'importBlobData : %s' % str(e)
	return log_data_str

def importPropData(srchost, srcdb, dsthost, dstdb, srcRoleId , destRoleId):
	log_data_str = ""
	srcHost  = srchost
	srcDB	= srcdb
	host	=  dsthost
	dbname  =  dstdb
	try:
		conn = MySQLdb.connect(srcHost, srcUser, srcPasswd,srcDB);
		cursor = conn.cursor()
		tmpSelectSql = 'select '
		list_len = len(list_property_field)
		count = 0
		for field in list_property_field:
			if (list_len-1)==count:
					tmpSelectSql += '%s' % field
			else:
					tmpSelectSql += '%s, ' % field
			count = count + 1
		tmpSelectSql += (' from ums_char_property where pf_role_id=%s') % (srcRoleId)
		log_data_str += tmpSelectSql
		log_data_str += '\n'
		cursor.execute(tmpSelectSql)
		tmpSql = 'update ums_char_property set '
		isSuccess = False
		for result in cursor:
			index = 0
			isSuccess = True
			for field in list_property_field:
					tmpSql += field
					if (list_len-1) == index:
							tmpSql += " = '%s' " % result[index]
					else:
							tmpSql += " = '%s', " % result[index]
					index = index+1

			tmpSql += ' where pf_role_id=%s' % destRoleId
			log_data_str += tmpSql
			log_data_str += '\n'
			break
		cursor.close()
		conn.close()
		#update
		conn = MySQLdb.connect(dsthost, srcUser,srcPasswd, dstdb)
		cursor = conn.cursor()
		if isSuccess==True:
			print '=====>table name ums_char_property update from %s to %s start!' % (srcRoleId,destRoleId)
			cursor.execute(tmpSql)
			conn.commit()
			print '=====>table name ums_char_property update from %s to %s success!' % (srcRoleId,destRoleId)
		cursor.close()
		conn.close()
	except BaseException, e:
			print 'importPropData : %s' % str(e)
			return str
	return log_data_str
def deal_line(line,cfg_line):	
	serial_str = re.split(',', line) #利用正则函数进行分割
	if len(serial_str) != 4:
		print "cfg error! please check transconfig.cfg "
		return 0
	for row in serial_str:
		cfg_line.append(row)
	print cfg_line
def query_gw_info(DB_HOST, DB_USER, DB_PWD, db_name,conf_server_list,cfg_name):
	# 记录日志
	log_time = time.strftime('%Y%m%d',time.localtime(time.time()))
	detail_time = time.strftime('%Y-%m-%d %H:%M:%S %p',time.localtime(time.time()))
	log_name = "log_trans_%s.txt" % log_time
	logfile = open(log_name, "w")
	log_str = ""	
	# 读文件
	f = open(cfg_name)
	file_field = f.readlines()
	for row in file_field:
		cfg_list = []
		deal_line(row,cfg_list)
		
		# 初始化变量
		src_gateway_id = cfg_list[0]
		dest_gateway_id = cfg_list[1]
		src_role_id = cfg_list[2]
		dest_role_id = cfg_list[3]
		src_db_name = ""
		src_db_ip = ""
		dest_db_name = ""
		dest_db_ip = ""
		# 连接服务器列表
		try:
			conn = MySQLdb.connect(DB_HOST, DB_USER, DB_PWD, db_name, 3306)
			cur = conn.cursor()
			srcSql = "select db_name,db_host_ip from %s where gateway_id = %s" %(conf_server_list,src_gateway_id)
			print srcSql
			cur.execute(srcSql)
			src_row = cur.fetchone()
			src_db_name = src_row[0]
			src_db_ip	= src_row[1]
			destSql = "select db_name,db_host_ip from %s where gateway_id = %s" %(conf_server_list,dest_gateway_id)
			print destSql
			cur.execute(destSql)
			dest_row = cur.fetchone()
			dest_db_name = dest_row[0]
			dest_db_ip	= dest_row[1]
			log_str = "%s src_gateway_id = %s,src_role_id = %s,src_db_name = %s,src_db_ip = %s ---------> dest_gateway_id = %s,dest_role_id = %s,dest_db_name = %s,dest_db_ip = %s" \
			%(detail_time,src_gateway_id,src_role_id,src_db_name,src_db_ip,dest_gateway_id,dest_role_id,dest_db_name,dest_db_ip)
			print log_str
			logfile.write(log_str)
			logfile.write('\n')
			# 开始数据迁移
			log_data_str = ""
			log_data_str += importBlobData(src_db_ip, src_db_name, dest_db_ip, dest_db_name, src_role_id,dest_role_id)
			log_data_str += importPropData(src_db_ip, src_db_name, dest_db_ip, dest_db_name, src_role_id,dest_role_id)
			logfile.write(log_data_str)
			logfile.write('\n')
			logfile.close()
			cur.close()
			conn.close()
		except MySQLdb.Error, e:
			print "MySQL Error:%s" % str(e)
	f.close
query_gw_info(server_list_db_ip, srcUser, srcPasswd,server_list_dbname,server_list_tbname,cfg)