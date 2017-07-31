mysql -usszj -pDR9m_wqsgF8a -P3306 data_stat_ss -e "select gateway_id, vip_level, count(*) from money_state group by gateway_id, vip_level" > ./vip_level_20170615.txt
