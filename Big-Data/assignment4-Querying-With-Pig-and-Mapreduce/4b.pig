register piggybank.jar;
define CSVLoader org.apache.pig.piggybank.storage.CSVLoader(); 

tweets = LOAD 'tweets.csv' USING org.apache.pig.piggybank.storage.CSVLoader() AS (tweetid:chararray, content:chararray, user:chararray);
users = LOAD 'users.csv' USING org.apache.pig.piggybank.storage.CSVLoader() AS (login:chararray, name:chararray, state:chararray);
collections = join users by login full, tweets by user;
groups = group collections by name; 
counts = foreach groups generate group as name, COUNT(collections.tweetid)as number;
finalcount = order counts by number desc;
finalcount = filter finalcount by number==0;
finalname = foreach finalcount generate name;
store finalname into '4b.result';