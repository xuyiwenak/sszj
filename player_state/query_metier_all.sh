mysql -usszj -pDR9m_wqsgF8a -P3306 data_stat_ss -e "select role, count(*) from money_state group by role" > ./metier_all_20170615.txt
