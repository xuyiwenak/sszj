#!/bin/bash
DB_IP="103.244.235.249"
DB_USER="sszj"
DB_PWD="DR9m_wqsgF8a"
DB_NAME="globalserverdb"
sql_result=`mysql -N -h${DB_IP} -u${DB_USER} -p${DB_PWD} -D${DB_NAME} -e "select dbname,dbhost from globalserverdb"`
echo $sql_result