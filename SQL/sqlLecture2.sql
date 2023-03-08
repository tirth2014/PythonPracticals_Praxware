create table employee
(
	id int(11) primary key auto_increment,
    uname varchar(20),
    mobile Bigint(10) unique,
    age int(10) check(age>=18)
);
insert into employee(uname,mobile,age)values("A",9016395600,18);
insert into employee(uname,mobile,age)values("B",7878078780,19);
insert into employee(uname,mobile,age)values("C",9898098980,20);
insert into employee(uname,mobile,age)values("D",8080180801,21);
insert into employee(uname,mobile,age)values("E",9898598985,22);
select * from employee

truncate table employee

create table salary
(
	sid int(11) primary key auto_increment,
    salary int(11) not null,
    eid int(11),
    CONSTRAINT fk_id foreign key(eid)references employee(id)
);

drop table salary
select * from salary

insert into salary(salary,eid)values(10000,1);
insert into salary(salary,eid)values(20000,2);
insert into salary(salary,eid)values(30000,3);
insert into salary(salary,eid)values(40000,4);

select *
from employee
left join salary on employee.id=salary.eid
union
select *
from employee
right join salary on employee.id=salary.eid

select *
from employee e1
join employee e2 on e1.id=e2.id



