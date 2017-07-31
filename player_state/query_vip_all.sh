mysql -usszj -pDR9m_wqsgF8a -P3306 data_stat_ss -e "select vip_level, count(*) from money_state group by vip_level" > ./vip_level_all_20170615.txt
