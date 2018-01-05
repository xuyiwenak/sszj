create table stat_mount_info(gateway_id int(11), role_id int(11) unsigned, mount_level int(11), immortal_level int(11), immortal_star int(11), evil_level int(11), evil_star int(11))ENGINE=InnoDB DEFAULT CHARSET=utf8;
create table stat_mount_item(gateway_id int(11), role_id int(11) unsigned, item_type int(11), sheet_id char(32), quantity int(11))ENGINE=InnoDB DEFAULT CHARSET=utf8;

