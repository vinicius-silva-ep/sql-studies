select
    h.hacker_id,
    h.name
from
    hackers as h
    join challenges c on h.hacker_id = c.hacker_id