select
    c.contest_id,
    c.hacker_id,
    c.name,
    sum(ss.total_submissions),
    sum(ss.total_accepted_submissions),
    sum(vs.total_views),
    sum(vs.total_unique_views)
from
    contests as c
    left join colleges col on c.contest_id = col.contest_id
    left join challenges cha on col.college_id = cha.college_id
    left join view_stats vs on cha.challenge_id = vs.challenge_id
    left join submission_stats ss on cha.challenge_id = ss.challenge_id
group by
    c.contest_id,
    c.hacker_id,
    c.name
having
    (
        sum(ss.total_submissions) + sum(ss.total_accepted_submissions) + sum(vs.total_views) + sum(vs.total_unique_views)
    ) > 0
order by
    c.contest_id