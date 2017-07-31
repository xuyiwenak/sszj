mysql -usszj -pDR9m_wqsgF8a -P3306 data_stat_ss -e "select gateway_id, slot_id,
cur_level, count(*) as player_count from xinfa_stat group by gateway_id,
slot_id, cur_level" > ./xinfa_level_middle_month.txt
