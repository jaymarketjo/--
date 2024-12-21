1.CREATE DATABASE my_database;
use my_database;
CREATE TABLE `学员信息表`(
`学员编号`varchar(12) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
`姓名`varchar(64) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
`年龄`int(12) DEFAULT NULL,
`家庭地址`varchar(200) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
`电话号码`varchar(11) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
PRIMARY KEY(`学员编号`)USING BTREE
)

select * from 学员信息表

use mysql;
SHOW DATABASES;
SHOW grants;

select * from my_database.`1` ;

use my_database;
select * from my_database.`0` 
DROP TABLE IF EXISTS my_database.`0` ;

ALTER TABLE my_database.`1` MODIFY COLUMN 姓名 VARCHAR(255);

SHOW TABLES FROM my_database;

mssql语句
2.SELECT name FROM sys.databases;
按日期降序排列
SELECT * FROM oa.dbo.km_review_main order by fd_last_modified_time DESC 
创建库语句
CREATE DATABASE MyNewDatabase;

#把表1的数据插入到表人员
INSERT INTO my_database.`人员`
SELECT * FROM my_database.`1`;#把表1的数据插入到表人员 
方法1
INSERT INTO my_database.`人员`
SELECT * FROM my_database.`1`;
方法2
INSERT INTO mydatabase.测试(工号,姓名,岗位名称,一级部门,二级部门,三级部门)
SELECT 工号,姓名,岗位名称,一级部门,二级部门,三级部门
FROM my_database.`1`
limit 1000;

use mydatabase;
CREATE TABLE `t1deadlock` (
`id` int(11) NOT NULL,
`name` varchar(100) DEFAULT NULL,
`age` int(11) NOT NULL,
`address` varchar(255) DEFAULT NULL,
PRIMARY KEY (`id`),
KEY `idx_age` (`age`) USING BTREE,
KEY `idx_name` (`name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
Insert into mydatabase.t1deadlock(id,name,age,address) values (1,'刘备',18,'蜀国');
Insert into mydatabase.t1deadlock(id,name,age,address) values (2,'关羽',17,'蜀国');
Insert into mydatabase.t1deadlock(id,name,age,address) values (3,'张飞',16,'蜀国');
Insert into mydatabase.t1deadlock(id,name,age,address) values (4,'关羽',16,'蜀国');
Insert into mydatabase.t1deadlock(id,name,age,address) values (5,'诸葛亮',35,'蜀国');
Insert into mydatabase.t1deadlock(id,name,age,address) values (6,'曹孟德',32,'魏国');

DROP TABLE IF EXISTS t1_deadlock;

update mydatabase.t1deadlock
set name='刘备',address='蜀国'
where id=1;