%default TODAYS_DATE `date +%Y-%m-%d`;

advertise = LOAD '/home/hadoop/hivedjango/advertise.log' USING PigStorage(' ') as (DATE: chararray, TIMESTAMP: chararray, USERID: chararray, AGE: chararray, GENDER: chararray, REGION: chararray, MEDIUM: chararray, CAMPAIGN: chararray, SOURCE: chararray, CONVERSION: chararray);

advertise_table = FOREACH advertise GENERATE DATE, TIMESTAMP, USERID, AGE, GENDER, REGION, MEDIUM, CAMPAIGN, SOURCE, CONVERSION;

store advertise_table into '/home/hadoop/hivedjango/pigoutputs/advertisedata/$TODAYS_DATE' using PigStorage(' ');

