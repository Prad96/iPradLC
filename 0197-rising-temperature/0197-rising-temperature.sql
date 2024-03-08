# Write your MySQL query statement below
SELECT w1.id
from Weather as w1 join Weather w2

Where w1.temperature>w2.temperature

and DATEDIFF(w1.recordDate,w2.recordDate)=1
;
                    