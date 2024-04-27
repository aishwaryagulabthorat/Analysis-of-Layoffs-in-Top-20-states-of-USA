select * from state_info;
select * from company_info;
select * from employee_attrition;
-- delete from employee_attrition;


## Get Total number of layoffs by states
select s.state,sumViews(c.`Number of Workers`) as 'total_layoffs' from state_info s inner join company_info c
on c.Company=s.Company
group by s.state;

## Get Total number of layoffs by Closure/Layoff Statuses
select `Closure/Layoff`,sum(`Number of Workers`) as 'total_layoffs' from company_info 
where `Closure/Layoff`!= '0' and `Closure/Layoff`!= '0.0'
group by `Closure/Layoff`
having sum(`Number of Workers`)>0
order by total_layoffs desc;

## Get Total number of layoffs by city
select s.city,sum(c.`Number of Workers`) as 'total_layoffs' from state_info s inner join company_info c
on c.Company=s.Company
where s.city regexp '^[A-Za-z]'
group by s.city
having sum(c.`Number of Workers`)>0
order by sum(c.`Number of Workers`) desc;

## Get Total number of layoffs by across years
select year(`WARN Received Date`),sum(`Number of Workers`) as 'total_layoffs' from company_info 
where year(`WARN Received Date`) is not null
group by year(`WARN Received Date`) 
having sum(`Number of Workers`)>0
order by total_layoffs desc;


## Get Total number of layoffs by Temporary/Permanent Status
select `Temporary/Permanent`,sum(`Number of Workers`) as 'total_layoffs' from company_info 
where `Temporary/Permanent` !='nan' and `Temporary/Permanent` not regexp '^[0-9]'
group by `Temporary/Permanent` 
having sum(`Number of Workers`)>0
order by total_layoffs desc;




