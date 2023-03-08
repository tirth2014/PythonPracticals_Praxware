create table emp
(
	id int(11) primary key auto_increment,
    uname varchar(20),
    city varchar(30),
    salary int(10),
    dept varchar(20),
	age int(10),
    gender varchar(10)
);
select * from emp
insert into emp(uname,city,salary,dept,age,gender)values("A","Ahmedabad",10000,"SALES",20,"M");
insert into emp(uname,city,salary,dept,age,gender)values("B","Ahmedabad",20000,"SALES",25,"M");
insert into emp(uname,city,salary,dept,age,gender)values("C","Baroda",30000,"Marketing",30,"F");
insert into emp(uname,city,salary,dept,age,gender)values("D","Baroda",30000,"Marketing",25,"M");
insert into emp(uname,city,salary,dept,age,gender)values("E","Mumbai",50000,"Manager",45,"M");
insert into emp(uname,city,salary,dept,age,gender)values("G","Mumbai",80000,"Manager",50,"M");



select COUNT(id),sum(salary),dept,id
from emp
group by dept
order by id DESC;

select COUNT(e1.salary),e1.dept,e1.uname,e1.id
from emp e1 , emp e2
inner join emp on e1.id=e2.id
group by e1.dept;

SELECT SUM(e1.salary),e1.id,e1.uname,e1.dept
FROM emp e1 JOIN emp e2 ON e1.id = e2.id
group by e1.dept
having COUNT(e1.dept)>=3

select * from emp where city like '%d'

SELECT DISTINCT city FROM emp;




