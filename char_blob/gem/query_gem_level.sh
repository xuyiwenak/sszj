mysql -usszj -pDR9m_wqsgF8a -P3306 data_stat_ss -e "select gateway_id,sheet_id,
count, count(*) as player_count from (select gateway_id, role_id,sheet_id,
count(*) as count from gem_stat group by gateway_id, role_id, sheet_id order by
gateway_id, role_id, sheet_id)a group by gateway_id, sheet_id, count" \
 >./gem_enchase_last_month.txt
