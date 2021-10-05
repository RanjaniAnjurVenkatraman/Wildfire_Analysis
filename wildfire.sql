create table wildfire(
	acres_burned bigint,
	fire_cause text,
	firediscoverydatetime date,
	fireoutdatetime date,
	incidentname text,
	latitude numeric,
	longitude numeric,
	county varchar,
	country varchar,
	state varchar,
	fire_duration bigint,
	month bigint,
	month_name varchar
	
);

 

select * from wildfire;