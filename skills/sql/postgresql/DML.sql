create table tutorial.employees(
    id numeric primary key,
    first_name varchar not null,
    last_name varchar not null,
    email varchar,
    hire_date date default current_date,
    department varchar default 'Unassigned'
           );

select  * from tutorial.employees;
ALTER table tutorial.employees add column age INT;
alter table tutorial.employees drop age;

insert into tutorial.employees(id, first_name, last_name, email)
-- enter 3 rows
values (2,'Smith','Deluca','Smith@gmail.com');

SELECT * From tutorial.employees;

update tutorial.employees set first_name = 'Jane', last_name = 'Doe', email='Jane@gmail.com'
where id = 2
