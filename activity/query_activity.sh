mysql -usszj -pDR9m_wqsgF8a -P3306 data_stat_ss -e"select gateway_id, map_id, map_name, show_time, count_char_id from stat_activity order by gateway_id, map_id, show_time;" > /data/home/sszj/data_stat/activity/stat_activity_20170831.txt