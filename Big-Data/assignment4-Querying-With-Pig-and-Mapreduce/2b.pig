register piggybank.jar;
define CSVLoader org.apache.pig.piggybank.storage.CSVLoader(); 

tweets = LOAD 'tweets.csv' USING org.apache.pig.piggybank.storage.CSVLoader() AS (tweetid:chararray, content:chararray, user:chararray);
users = LOAD 'users.csv' USING org.apache.pig.piggybank.storage.CSVLoader() AS (login:chararray, name:chararray, state:chararray);
collections = join tweets by user, users by login; 
collections = foreach collections generate user, name, state, tweetid, content;
store collections into '2b.result';