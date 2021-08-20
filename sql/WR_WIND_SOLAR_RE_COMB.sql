--central solar--
select date_key, sum(day_energy_actual) AS value from reporting_uat.regional_entities_generation where DATE_KEY BETWEEN 20210810 AND 20210819 AND CLASSIFICATION_NAME IN ('RENEWABLE') AND STATION_TYPE_NAME IN ('SOLAR') GROUP BY DATE_KEY ORDER BY DATE_KEY 

--wind central--
select date_key, sum(day_energy_actual) AS wind_central from reporting_uat.regional_entities_generation where DATE_KEY BETWEEN 20210810 AND 20210819 AND CLASSIFICATION_NAME IN ('RENEWABLE') AND STATION_TYPE_NAME IN ('WIND') GROUP BY DATE_KEY ORDER BY DATE_KEY 

--central re comb--
select date_key, sum(day_energy_actual) AS value from reporting_uat.regional_entities_generation where DATE_KEY BETWEEN 20210810 AND 20210819 AND CLASSIFICATION_NAME IN ('RENEWABLE') AND STATION_TYPE_NAME IN ('SOLAR','WIND') GROUP BY DATE_KEY ORDER BY DATE_KEY 

--states solar combined--
SELECT date_key, sum(solar) FROM REPORTING_UAT.state_load_details where state_name IN('MADHYA PRADESH', 'MAHARASHTRA', 'CHHATTISGARH', 'GUJARAT') and date_key BETWEEN 20210810 AND 20210819 GROUP BY DATE_KEY ORDER BY DATE_KEY

--states wind--
SELECT date_key, sum(wind) AS wind_states FROM REPORTING_UAT.state_load_details where state_name IN('MADHYA PRADESH', 'MAHARASHTRA', 'CHHATTISGARH', 'GUJARAT') and date_key BETWEEN 20210810 AND 20210819 GROUP BY DATE_KEY ORDER BY DATE_KEY
 

--wind geneartion wr, combined of states and central--

SELECT  wind_central_tbl.date_key, (wind_central_tbl.wind_central + wind_states_tbl.wind_states) AS wr_wind_comb FROM (select date_key, sum(day_energy_actual) AS wind_central from reporting_uat.regional_entities_generation where DATE_KEY BETWEEN :start_date AND :end_date AND CLASSIFICATION_NAME IN ('RENEWABLE') AND STATION_TYPE_NAME IN ('WIND') GROUP BY DATE_KEY ORDER BY DATE_KEY) wind_central_tbl inner JOIN (SELECT date_key, sum(wind) AS wind_states FROM REPORTING_UAT.state_load_details where state_name IN('MADHYA PRADESH', 'MAHARASHTRA', 'CHHATTISGARH', 'GUJARAT') and date_key BETWEEN :start_date AND :end_date GROUP BY DATE_KEY ORDER BY DATE_KEY) wind_states_tbl ON wind_central_tbl.DATE_KEY=wind_states_tbl.date_key 

-- solar generation wr , combined of states and central --
SELECT  solar_central_tbl.date_key, (solar_central_tbl.solar_central + solar_states_tbl.solar_states) AS wr_solar_comb FROM (select date_key, sum(day_energy_actual) AS solar_central from reporting_uat.regional_entities_generation where DATE_KEY BETWEEN 20210810 AND 20210819 AND CLASSIFICATION_NAME IN ('RENEWABLE') AND STATION_TYPE_NAME IN ('SOLAR') GROUP BY DATE_KEY ORDER BY DATE_KEY) solar_central_tbl inner JOIN (SELECT date_key, sum(solar) AS solar_states FROM REPORTING_UAT.state_load_details where state_name IN('MADHYA PRADESH', 'MAHARASHTRA', 'CHHATTISGARH', 'GUJARAT') and date_key BETWEEN 20210810 AND 20210819 GROUP BY DATE_KEY ORDER BY DATE_KEY) solar_states_tbl ON solar_central_tbl.DATE_KEY=solar_states_tbl.date_key 

-- total RE generation wr , combined of states and central --
SELECT re_central_tbl.date_key, (re_central_tbl.re_central + re_states_tbl.re_states) AS wr_re_comb FROM (select date_key, sum(day_energy_actual) AS re_central from reporting_uat.regional_entities_generation where DATE_KEY BETWEEN :start_date AND :end_date AND CLASSIFICATION_NAME IN ('RENEWABLE') AND STATION_TYPE_NAME IN ('SOLAR', 'WIND') GROUP BY DATE_KEY ORDER BY DATE_KEY) re_central_tbl inner JOIN (SELECT date_key, sum((coalesce(solar ,0) + coalesce(wind ,0))) AS re_states FROM REPORTING_UAT.state_load_details where state_name IN('MADHYA PRADESH', 'MAHARASHTRA', 'CHHATTISGARH', 'GUJARAT') and date_key BETWEEN :start_date AND :end_date GROUP BY DATE_KEY ORDER BY DATE_KEY) re_states_tbl ON re_central_tbl.DATE_KEY=re_states_tbl.date_key 



