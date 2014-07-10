register piggybank.jar;
define CSVLoader org.apache.pig.piggybank.storage.CSVLoader(); 

users = LOAD 'users.csv' USING org.apache.pig.piggybank.storage.CSVLoader() AS (login:chararray, name:chararray, state:chararray);
nyusers = filter users by state == 'NY';
nyuserslogin = foreach nyusers generate login;
store nyuserslogin into '1a.result';