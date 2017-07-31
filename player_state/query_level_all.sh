mysql -usszj -pDR9m_wqsgF8a -P3306 data_stat_ss -e "select level, count(*) from money_state group by level" > ./ss_level_all_20170622.txt
