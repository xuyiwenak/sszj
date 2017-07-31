mysql -usszj -pDR9m_wqsgF8a -P3306 data_stat_ss -e "select gateway_id, ss_camp_type, count(*) from money_state group by gateway_id, ss_camp_type" > ./ss_camp_type_20170615.txt
