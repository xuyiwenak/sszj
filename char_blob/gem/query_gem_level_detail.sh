mysql -usszj -pDR9m_wqsgF8a -P3306 data_stat_ss -e "select gateway_id, role_id,
sheet_id, count(*) from gem_stat group by gateway_id, role_id, sheet_id order
by gateway_id, role_id, sheet_id" > ./gem_enchase_detail_last_month.txt
