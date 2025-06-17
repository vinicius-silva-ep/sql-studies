/* Code 1 */
select
    ei.employee_ID,
    ei.name
from
    employee_information ei
    left join last_quarter_bonus as lqb on ei.employee_ID = lqb.employee_ID
where
    division = 'HR'
    and lqb.bonus >= 5000
    /* Code 2 */
select
    pt.stock_code
from
    price_today as pt
    left join price_tomorrow as ptm on pt.stock_code = ptm.stock_code
where
    ptm.price > pt.price