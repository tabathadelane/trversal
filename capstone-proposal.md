# Trversal


## Project Overview
Trversal is an itenerary building app that lets the trip planner input places of interest and save them to each day of their trip in a list view that calculates and provides the travel times between the locations, so the user can get a preview of what will realistically fit into their day. 

## Features

**_"When I prepare a trip, I want a more accurate timeline of places and travel times so that I can make the most realistic plan."_**

**Tasks:**  
Create user models that can save an itenerary.  
Allow the user to list and order the places they want to go in a given day.  
Make a new Model for each day on the trip.  
Implement a map API that calculates route times between location and previous location.  
Display route times and/or timestamps for user to see.  
Allow the user to provide an estimated time to spend at each location.  
Account for this time also for the uer to see.  
Provide a layout of each day with timestamps so the user can track their day.  

**_"If my plans change, I want to be able to edit times and order of locations."_**
**Tasks:**  
Allow the user to rearrange locations if plans change  
Build the app so that the route times automatically recalculate with the location above it  

**_"If I am walking/driving, I want to get accurate travel times based on my method of transportation."_**

**Tasks:**  
Implement the map API travel method feature  
Allow the user to choose which method  

**_"If I am travelling in a group, I want to share the itenerary to save to their accounts, also."_**

**Tasks:**  
Create a Model relationship that allows the day/trip to be saved to that user as well

**_"If I am planning the trip, I don't want my friends to be able to change the schedule."_**
or
**_"If we are planning the trip together, I want others to be able contribute to my itenerary."_**

**Tasks:**  
Give the inteneray creator user permission controls

**_"I like to make use of my entire day, so I want the app to help me check if the place I want to go to dinner will still be open when I plan to arrive."_**

**Tasks:**  
Add a feature that checks the API result for each place with time of arrival/time staying against the OPEN value  
Display a warning if FALSE is returned  

**_"If the weather is nice, I want to go to a park or walk to lunch instead of drive."_**

**Tasks:**  
Implement a weather app   
If the trip is within the forecast range, display weather info to the user  



## Data Model

### Models:  
**TRIP**  
name of trip  
amount of days  
main city for initial map centering  
link to user model  

**DAY**  
link one to Trip model for each day  

**LOCATIONS**  
name/address/LatLang  
duration staying at location  
link to day  

**USERS**  
add a view for trips planned  

**_WEATHER_**  
*major stretch goal, will learn more later*  
weather icon  
temp high  
temp lo  
conditions  
location  
link to day model  

## Schedule

There are 17 class days left in the course as of 06-06-2019. This is a rough timeline of what I plan to do each day.:

*While I work on the weekends, I would like to prevent burnout and will reserve weekend capstone work for only if I begin to fall behind.*

**Day 1**  
Research Google maps API with Python  
Build a basic webpage that loads the map   
Implement the Directions service with two predetermined waypoints  
If I can't get this to work with instructor help, find a new API even though it will give me less features in the end.   

**Day 2**  
Research Vue  

**Day 3**  
Research Django Vue

**Day 4**  
Build a basic app with a map view and user panel  
Allow user input of two locations and calculates route  
display the timestamps of the start and end time and also travel time  

**Day 5-6**  
Make sure Trip, Day and Location models are working and storing information  
preset multiple locations for one day  
Make the map API calculate times and display them  
remove the DirectionsDisplay from showing and add location markers  
or use the multiple WayPoint feature in Google Maps API to display the whole route  
Make all of this work in Vue  
  
**Day 7-8**  
Allow custom location input from user that updates in Vue with new timestamps  
Add up and down arrows and a delete feature  
build a CSS Grid of all the info and buttons  
add a Stay Duration for each location  
Add this to the time and display it.   
  
###### MILESTONE: This is the first very basic working App  
  
**Day 9-10**  
create functionality to add multiple day "cards" to each trip and abilty to arrow between them.   
With the creation of each day, ask for the first Location (hotel name or airport where you will depasrt each morning)  
  
**Day 11-12**  
Expand User and create trips outside of Admin account.   
Add a search for user account to show their trips  

###### MILESTONE: This is my preferred minimum for presentation

**Day 13**
Add a dropdown box for Transportation Method that will change the default in the API  
  
**Day 14-15**  
Allow the addition of other users to each trip  
implement permissions to allow or block edits from new user  
  
###### MILESTONE: This is where I'd realistically like to be for presentation  
  
**Day 16**  
Finalize Styling and Layout and plan presentation content  
  
**Next Milestone**  
Add Weather feature  
  
**Next Milestone**  
Allow the app to track users current position and time from browser geolocation and update the timestamps if they stay at a location past the end of the   original stay duration  
  
**Next Milestone**  
Create my own API from this and build the app to run on it  
  
**Next Milestone**  
Build a new front end for mobile  
I feel this is the best use for this app in the end  

**Next Milestone**  
Learn about Push notifications to alert the user when they are falling behind

**Next Milestone**  
Unknown  
I feel more feature will present themselves over the course of building the app. 





