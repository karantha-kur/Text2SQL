Create database Uber_Data;
Use Uber_Data;



CREATE TABLE FACT_TABLE(
TRIP_ID int PRIMARY KEY,
VENDORID int, 
DATE_TIME_ID int, 
PASSENGER_COUNT_ID int, 
TRIP_DISTANCE_ID int, 
RATECODE_ID int, 
STORE_AND_FWD_FLAG ENUM('Y', 'N'),
PICKUP_LOC_ID int, 
DROPOFF_LOC_ID int, 
PAYMENT_TYPE_ID int, 
FARE_AMOUNT_ID int);

CREATE TABLE DROPOFF_LOC(
DROPOFF_LOC_ID int PRIMARY KEY,
DROPOFF_LONGITUDE float, 
DROPOFF_LATITUDE float);

CREATE TABLE PICKUP_LOC(
PICKUP_LOC_ID int PRIMARY KEY,
PICKUP_LONGITUDE float, 
PICKUP_LATITUDE float);

CREATE TABLE RATECODE_TABLE(
RATECODE_ID int PRIMARY KEY,
RATECODEID int, 
RATECODE_NAME VARCHAR(50));

CREATE TABLE TRIP_DISTANCE_TABLE(
TRIP_DISTANCE_ID int PRIMARY KEY,
TRIP_DISTANCE float);

CREATE TABLE PAYMENT_TYPE_TABLE(PAYMENT_TYPE_ID int PRIMARY KEY, 
PAYMENT_TYPE int, 
PAYMENT_TYPE_NAME VARCHAR(50));


CREATE TABLE PASSENGER_COUNT_TABLE(
PASSENGER_COUNT_ID int PRIMARY KEY,
PASSENGER_COUNT int);

CREATE TABLE FARE_AMOUNT_TABLE(
FARE_AMOUNT_ID int PRIMARY KEY,
FARE_AMOUNT float, 
EXTRA float, 
MTA_TAX float, 
TIP_AMOUNT float, 
TOLLS_AMOUNT float, 
IMPROVEMENT_SURCHARGE float, 
TOTAL_AMOUNT float);


CREATE TABLE DATE_TIME_TABLE(
DATE_TIME_ID int PRIMARY KEY,
TPEP_PICKUP_DATE_TIME timestamp, 
PICKUP_TIME TIME,
PICKUP_DATE date, 
PICKUP_DAY int, 
TPEP_DROPOFF_DATE_TIME timestamp, 
DROPOFF_TIME TIME,
DROPOFF_DATE date, 
DROPOFF_DAY int);