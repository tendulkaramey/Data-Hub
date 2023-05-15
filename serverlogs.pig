%default TODAYS_DATE `date +%Y-%m-%d`;

server = LOAD '/home/hadoop/hivedjango/server.log' USING PigStorage(' ') as (LOGLEVEL: chararray, DATE: chararray, TIMESTAMP: chararray, METHOD: chararray, API: chararray, STATUS: chararray, USERID: chararray);

server_table = FOREACH server GENERATE API as APINAME, METHOD, STATUS AS STATUSCODE, DATE, TIMESTAMP, USERID, LOGLEVEL;

store server_table into '/home/hadoop/hivedjango/pigoutputs/serverdata/$TODAYS_DATE' using PigStorage(' ');

