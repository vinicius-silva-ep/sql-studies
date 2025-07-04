select
    c.company_code,
    c.founder,
    count(distinct lm.lead_manager_code),
    count(distinct sm.senior_manager_code),
    count(distinct m.manager_code),
    count(distinct e.employee_code)
from
    company as c
    left join lead_manager as lm on c.company_code = lm.company_code
    left join senior_manager as sm on c.company_code = sm.company_code
    left join manager as m on c.company_code = m.company_code
    left join employee as e on c.company_code = e.company_code
group by
    c.founder,
    c.company_code
order by
    replace(c.company_code, 'C', '') asc