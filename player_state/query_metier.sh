mysql -usszj -pDR9m_wqsgF8a -P3306 data_stat_ss -e "select gateway_id, role, count(*) from money_state group by gateway_id, role" > ./metier_20170615.txt
