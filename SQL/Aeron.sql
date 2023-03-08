CREATE database For_me

use For_me

create table Aeron
(
Enrollment_No bigint,
Name varchar(20),
Address varchar(50),
Mobile_No bigint,
Department varchar(10),
Stream varchar(10),
City varchar(10),
State varchar(10),
Fees bigint
)

insert into Aeron value(1,"Arora","India",8160612345,"Degree","Computer","Nadiad","Gujarat","10000");
insert into Aeron value(2,"Manisha","Russia",1606123456,"Degree","Civil","idk","idk","20000");
insert into Aeron value(3,"Anil","Ukraine",7160655345,"Degree","Computer","idk","idk","50000");
insert into Aeron value(4,"Sagar","India",9160612345,"Degree","Computer","Ahemdavad","Gujarat","15000");
insert into Aeron value(5,"Aman","India",8161234345,"Diploma","Mechanical","Vadodara","Gujarat","100000");
insert into Aeron value(6,"Neel","India",8941246444,"Diploma","Mechanical","Ahemdavad","Gujarat","200000");
insert into Aeron value(7,"Shen","India",8061335421,"Degree","Civil","Vadodara","Gujarat","55555");

select * from Aeron

select Name from Aeron Where City="Vadodara"

select Name, Department from Aeron Where State="Gujarat" and City="Ahemdavad" and Stream="Computer"

set sql_safe_updates=0

Update Aeron set name="kunal" where Enrollment_No=5

alter table aeron
add Hobby varchar(10)

delete from Aeron where Stream="Civil" or Stream="Mechanical"

commit
set autocommit=0

rollback

update Aeron set Hobby="Cricket"

alter table Aeron modify Address varchar(200)