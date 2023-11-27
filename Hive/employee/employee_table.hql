create database if not exists RA;
use RA;
create external table if not exists employee (
  eid int,
  ename string,
  age int,
  jobtype string,
  storeid int,
  storelocation string,
  salary bigint,
  yrsofexp int
)

row format delimited
fields terminated by ','
lines terminated by '\n'
stored as textfile location 'hdfs://namenode:8020/user/hive/warehouse/RA.db/employee';