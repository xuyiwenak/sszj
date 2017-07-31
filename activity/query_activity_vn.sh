#!/bin/bash
#sql = "select map_id, value, show_time, count_char_id from activity_stat  a, dictionary b where INSTR(b.key, concat('common.mapId.',a.map_id) > 0  order by map_id, show_time;"
mysql -usszj -pDR9m_wqsgF8a -P3306 data_stat_ss -e"select map_id, value, show_time, count_char_id, player_times from activity_stat  a, dictionary b where INSTR(b.key, concat('common.mapId.',a.map_id)) > 0  order by map_id, show_time;" > /data/home/sszj/data_stat/actitity/activity_by_mapid.txt
