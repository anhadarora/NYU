register piggybank.jar;
define CSVLoader org.apache.pig.piggybank.storage.CSVLoader(); 

tweets = LOAD 'tweets.csv' USING org.apache.pig.piggybank.storage.CSVLoader() AS (tweetid:chararray, content:chararray, user:chararray);
favorite = filter tweets by content matches '.*favorite.*';
lastfavorite = order favorite by tweetid;
store lastfavorite into '1b.result';