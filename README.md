# Wildfire_Analysis
To deploy interactive Wildfire-Analysis-2021 Dashboard  using JavaScript, Matplotlib, Leaflet, Folium, Python, Flask, HTML,CSS and Bootstrap

#  :fire: Wildfire Analysis :fire:

![image](https://i.pinimg.com/originals/ec/85/10/ec85104066682a9397972283cc5badf5.jpg)

## Table of Contents
   =================

  1. [About This Project](#about-this-project) <br>
	 - [Architectural Diagram](#architectural-diagram)
  	 - [ETL Process](#etl-process)
  2. [Technologies](#Technologies)   
  3. [Visualizations](#visualizations)
  4. [Deployment](#deployment)
  5. [Contributors](#contributors)

## About This Project :point_down:	
As of September 14, 2021, the National Interagency Fire Center (NIFC) reported that 44,647 wildfires in the United States had burned 5.6 million acres of land. We wanted to create an engaging and informative visualization of all wildfires that occurred in various states of USA in 2021, and other relevant data (county, month, and acres burned etc.) 

The data was retrieved from National Interagency Fire Center’s website in a csv format, which has current and very detailed description of all wildfires in the country.The csv file contained over 4000 rows and more then 100 columns. Data was extracted from CSV source, transformed using Python, Pandas and loaded into PostgreSQL. Visualizations was done using JavaScript, Matplotlib, Leaflet, Folium, Python, Flask, HTML, Bootstrap, D3 and CSS. Heroku and Github was used to deploy results to a 2021 wildfire web application. 

The end user for this project includes any business that owns property in wildfire country, as well as fire departments located in the area as well. Due to the millions of dollars lost in properties due to fire damage, we feel this dashboard would help them first and foremost. We also feel that this would draw the attention of any person that enjoys wildlife, because our impact on nature is a direct contribution to these fires.

## Technologies :hammer:	
![image](https://img.shields.io/badge/technologies-Python-orange)
![image](https://img.shields.io/badge/technologies-Pandas-orange)
![image](https://img.shields.io/badge/technologies-SQL-orange)
![image](https://img.shields.io/badge/technologies-PostgreSQL-orange)
![image](https://img.shields.io/badge/technologies-Javascript-orange)
![image](https://img.shields.io/badge/technologies-Flask-orange)
![image](https://img.shields.io/badge/technologies-HTML-orange)
![image](https://img.shields.io/badge/technologies-Bootstrap-orange)
![image](https://img.shields.io/badge/technologies-CSS-orange)
![image](https://img.shields.io/badge/technologies-Folium-orange)
![image](https://img.shields.io/badge/technologies-Leaflet-orange)
![image](https://img.shields.io/badge/technologies-Plotly-orange)
![image](https://img.shields.io/badge/technologies-D3-orange)

## Architectural Diagram :boom:	
<img src="https://i.pinimg.com/564x/c4/ac/2d/c4ac2ded29f79d991d4775a6f96c0653.jpg" width=800 align=center> <br>

## ETL Process 💡	

#### Extract 
2021 Wildfire dataset was extracted from the [National Interagency Fire Center](https://data-nifc.opendata.arcgis.com/datasets/wfigs-2021-wildland-fire-perimeters-to-date/explore?location=0.000000%2C0.000000%2C0.00&showTable=true).

	- Format: CSV
    - Size: MB
	

#### Transform 
Data was transformed and cleaned using Python, Pandas with th Jupyter Notebook. 
Transformations include: 
- Unnecessary columns were deleted, and we renamed existing columns 
- Wildfires with null longitude and latitude were removed and null values in the cause column were changed to “cause not found”
- Country-State column was split into two for further analysis
- Added Fire Duration column by subtracting the end date with the beginning date
- After cleaning up the data, the csv was converted to a geojson file
	

#### Load
The clean data was imported into a pgAdmin Data Base using PostgeSQL from where it can be extracted for future analysis. Imported SQLalchemy dependency in the Jupyter Notebook, an engine was created that connected to the pgAdmin Data Base, called wildfire_db.With pandas, the data frame was exported and stored in 
the wildfire_db data base. 


### Visualizations 📈	
## Top 20 States by Wildfires: <br>
Grouping by state, it can be concluded that majority of wildfires incidents happen in a couple of states, with Montanta, Idaho, and Arizona being on the top of the list. Suprisingly, California comes in fourth, with Montana having more then twice the amount of incidents


<img src="https://i.pinimg.com/236x/93/88/bf/9388bfbd0c8147a957585beea0043228.jpg" width=400 align=center> <br>

## Acres Burned vs Duration: <br>
Wildfires burned more acres the longer the duration of the fire in the beginning stage of the fire. Most of the fires, after around 20 days, were subdued and under control with only a handful still increasing in the size of acres burned. After 100 days, all fires in our dataset were under control with minimal burning.


<img src="https://i.pinimg.com/564x/b7/d0/c7/b7d0c7a71dc28b1d1ffe1f9a3e48285d.jpg" width=600 align=center> <br> 

## Wildfires by Month: <br>
Looking at the data grouped by month, we can clearly see that the number of wildfires in winter is relatively low and that it significantly increases in the summer, especially in June and July

<img src="https://i.pinimg.com/564x/3a/9e/22/3a9e22fde630dc6bf282908f087f71c6.jpg" width=600 align=center> <br> 

## Top Causes: <br>
Tree Map with the top causes of wildfires shows us that the biggest cause of wildfires lighting. For a good chunk of it, the cause of the fire is not known.

<img src="https://i.pinimg.com/originals/83/c8/4d/83c84d102ec307e097a17e299e65bf51.jpg" width=600 align=center> <br> 

## Folium Map for Fire Duration
Plotted folium map shows the states with highestduration of wildfire: bigger the circle. longer the duration. Each marker provides information such as Incident name, duration, state and county.

<img src="https://i.pinimg.com/564x/21/2b/d6/212bd628148bf44c8bc100b7a06cfff7.jpg" width=600 align=center> <br> 

## Deployment 🚀

CSS, Bootstrap and javascript are used to style the webpages. Elevator.js are used for scrolling purpose of the app.
A flask app.py file was created as a micro web framework to deploy the web application. We hosted our application in Heroku as well as on GitHub.

# Page1 : Index 

<img src="https://i.pinimg.com/564x/b4/af/8e/b4af8ee609a65d5b5807fc6353716ebd.jpg" width=600 align=center> <br> 

<img src="https://i.pinimg.com/originals/56/06/fc/5606fc43aeb95410992ac7c5611a8bd2.jpg" width=600 align=center> <br> 

# Page2 : Wildfire Analysis 

<img src="https://i.pinimg.com/originals/c8/58/39/c8583962726c74f7c06e351ffa03c01c.jpg" width=600 align=center> <br> 

# Page3 : Wildfire Data 

<img src="https://i.pinimg.com/564x/b6/31/d7/b631d78415d13e65f7c703a8270cc49a.jpg" width=600 align=center> <br> 

## Unique Javascript :pencil:

In our project we utilized Elevator.js for scrolling purpose. When you click on the elevator icon on the bottom of the page you will be automattically taken to the top with music :wink: 🔊

<img src="https://i.pinimg.com/originals/44/da/4f/44da4f48fe2e5431e8b69e89675248d1.jpg" width=600 align=center> <br>

## Application Link :checkered_flag:

Please be aware that there is a lag when you click on the link because it loads around 2000-3000 custom fire icons on to the main page.

- [Wildfire Dashboard - Github](https://ranjanianjurvenkatraman.github.io/Wildfire_Analysis/)
- [Wildfire Dashboard - Heroku](https://wildfire-2021.herokuapp.com/)

P.S: For some reason heroku is taking long time to load so for checking purpose you can click on github for easy access

## Contributors  👧👦 👩 👨

- [Ranjani Venkatraman](https://github.com/RanjaniAnjurVenkatraman)
- [Novak Radovic](https://github.com/nradovic1)
- [Saiana Darizhapova](https://github.com/Saiana82)
- [David Owens](https://github.com/dowens1186)


	

