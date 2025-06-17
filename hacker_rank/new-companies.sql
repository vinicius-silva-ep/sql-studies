select 
c.company_code,
c.founder,
lm.lead_manager_code
from company as c 
left join lead_manager as lm
 on c.company_code = lm.company_code