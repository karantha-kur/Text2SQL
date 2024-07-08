few_shots = [
    {
        'Question' : "What are the total number of records in the table fact table?",
        'SQLQuery' : "SELECT COUNT(trip_id) FROM fact_table;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "1500"
        },
    {
        'Question': "What is the average tip by payment type?",
        'SQLQuery':"SELECT PT.PAYMENT_TYPE_NAME, AVG(FA.TIP_AMOUNT) AS AVG_TIP FROM PAYMENT_TYPE_TABLE PT LEFT JOIN FARE_AMOUNT_TABLE FA ON PT.PAYMENT_TYPE_ID = FA.FARE_AMOUNT_ID GROUP BY 1;",
        'SQLResult': "Result of the SQL query",
        'Answer': "[Credit Card  2.599981753475094, Cash  0, No Charge  0]"
        },
    
    {
        'Question': "what are the number of trips by passenger count?" ,
        'SQLQuery': "SELECT PCT.PASSENGER_COUNT, COUNT(FT.TRIP_ID) FROM FACT_TABLE FT LEFT JOIN PASSENGER_COUNT_TABLE PCT ON FT.TRIP_ID = PCT.PASSENGER_COUNT_ID GROUP BY 1;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "[1  967, 2  200, 3  69, 4  28, 5  142, 6  94]"
        },

    {
        'Question': "Top 5 most number of trips on each day",
        'SQLQuery' : "with cte as(select dtt.pickup_day, count(ft.trip_id), rank() over(order by count(ft.trip_id) desc) as ranking from date_time_table dtt join fact_table ft on dtt.date_time_id = ft.trip_id group by 1) select * from cte where ranking<=5;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "[10 1327 1, 1 173 2]"
    },
    {
        'Question' : "what the the number of trips on each day?",
        'SQLQuery' : "SELECT dtt.pickup_day, COUNT(ft.trip_id) FROM date_time_table dtt JOIN fact_table ft ON dtt.date_time_id = ft.trip_id GROUP BY 1;",
        'SQLResult' : "Result of the SQL query",
        'Answer' : "[10 1327, 1 173]"
    }
]