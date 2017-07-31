mysql -usszj -pDR9m_wqsgF8a -P3306 data_stat_ss -e "load data local infile 'runoff_role_20170413_20170512_146.txt' into table runoff_role CHARACTER SET utf8 FIELDS TERMINATED BY '\t' IGNORE 1 LINES"
