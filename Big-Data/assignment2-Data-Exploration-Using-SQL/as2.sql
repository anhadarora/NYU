-- remember to end each query with a semi-colon

-- ********************Q1*******************

SELECT 'Q1' AS ' ';

select count(name) as count from stations;

-- ********************Q2*******************

SELECT 'Q2' AS ' ';

select name as station from stations where line = 'Broadway';

-- ********************Q3*******************

SELECT 'Q3' AS ' ';

select s.name as station, s.lat, s.long, sum(j.ff) as tickets from stations s, fares_jan18 j where s.line = 'Broadway' and j.station = s.name group by station order by sum(j.ff) desc;

-- ********************Q4*******************

SELECT 'Q4' AS ' ';

select f.station as Station, sum(f.ff-j.ff) as increase from fares_feb1 f, fares_jan18 j where f.remote = j.remote and j.station in (select name from stations where line = 'Broadway') group by Station order by increase;

-- ********************Q5*******************

SELECT 'Q5' AS ' ';

select f.station as Station, sum(f.7d-j.7d) as 'Feb1-Jan18 7d', sum(f.30d-j.30d) as 'Feb1-Jan18 30d' from fares_feb1 f, fares_jan18 j where f.remote = j.remote and j.station in (select name from stations where line = 'Broadway') group by Station;

-- ********************Q6*******************

SELECT 'Q6' AS ' ';

select f.station, sum(f.ff-j.ff) as increase from fares_feb1 f, fares_jan18 j where f.remote = j.remote and j.station group by Station order by increase desc limit 1;

-- ********************Q7*******************

SELECT 'Q7' AS ' ';

select f.station, sum(f.ff-j.ff) as increase from fares_feb1 f, fares_jan18 j where f.remote = j.remote and j.station group by Station order by increase asc limit 1;

-- ********************Q8*******************

SELECT 'Q8' AS ' ';

select f.station, sum(f.ff-j.ff) as increase from fares_feb1 f, fares_jan18 j where f.remote = j.remote group by j.station having increase<-1000 order by increase;

-- ********************Q9*******************

SELECT 'Q9' AS ' ';

select avg(average) as average from ( select sum(f.ff-j.ff) as average from fares_feb1 f, fares_jan18 j where f.remote = j.remote and j.station in (select name from stations where line = 'Broadway') group by j.station) as temptable;

-- ********************Q10*******************

SELECT 'Q10' AS ' ';

select sum(ff) as sum from fares_jan18;

-- ********************Q11*******************

SELECT 'Q11' AS ' ';

select s.name as 'F train stations' from stations s where s.lines like '%F' or s.lines like '%F,%';


