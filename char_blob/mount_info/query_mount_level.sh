mysql -usszj -pDR9m_wqsgF8a -P3306 data_stat_ss -e "select gateway_id, mount_level, count(*) as player_count from char_mount_info_tmp group by gateway_id, mount_level" > ./mount_level_last_month.txt
