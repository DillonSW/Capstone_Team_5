create database capstone5;

use capstone5;

create table inventory
( boxNumber numeric(4),
  date_rented datetime,
  date_stored datetime,
  step numeric(3),
  deviceLevel numeric(1),
  primary key(boxNumber)
);

create table students
( id varchar(12),
  email varchar(100),
  student_name varchar(50),
  course varchar(50),
  term varchar(50),
  boxNumber numeric(4),
  primary key(id),
  foreign key(boxNumber) references inventory(boxNumber)
);

select * from students;
select * from inventory;

delete from students;
delete from inventory;