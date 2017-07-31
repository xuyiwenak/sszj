mysql -usszj -pDR9m_wqsgF8a -P3306 data_stat_ss -e "select gateway_id,
cutting_type, cutting_level, count(*) as player_count from gem_cutting_stat
group by gateway_id, cutting_type, cutting_level order by
gateway_id,cutting_type, cutting_level" > ./gem_cutting_last_month.txt
