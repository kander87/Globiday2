# Globiday

**Web application using Python, Javascript, Flask, MySQL, HTML, CSS, and Bootstrap for generating and saving calendars of selected countries' public holidays.**
- Utilized a public API to aggregate and pull various countries holidays in order to supply users with more data
- Created a live search feature with Javascript that would allow a user to search for a countries holidays instead of having to scroll through all available countries
- Built out registration and login complete with password protection using bcrypt and user validations to ensure user security and added functionality for the user to view their own password while typing


## How it Works
![image](https://user-images.githubusercontent.com/120056106/231262837-46b675ac-bffb-4a9f-a361-48f677082caa.png)

1. Create an account
2. Upon successful registration, users will be able to see their current dashboard of saved calendars. 
3. Users can add a calendar by clicking "Add Calendar". 
4. Once in the add celendar section, users can either scroll through all available countries or use the live search bar to narrow down the choices. Users can select as many countries as they would like. 
![image](https://user-images.githubusercontent.com/120056106/231263653-88b949d5-0fc0-4d2b-88d3-06629cecbbe2.png)

5. After clicking the next button, users are asked to verify their selection before generating their custom calendar. 
6. Users are then prompted to add a name to their calendar in order to save the calendar to their dashboard. 
![image](https://user-images.githubusercontent.com/120056106/231263924-4e7a7071-943b-45c3-8227-5aa569982ab2.png)

7. The dashboard allows users to view and delete current calendars. 


## Uses
- Companies with international business can use this application to compile holidays of any of the countries they might work with/for in order to be more prepared for potential changes in schedules and increase their cultural connectivitiy to their partners. 
- Individuals who are travelling can utilize this application to be aware of any upcomig holidays in countries they may be traveling too for both cultural and planning reasons. 

## Built With
- <img src="https://user-images.githubusercontent.com/120056106/231264726-663e7600-b328-4ae5-a43d-efa03edf7b42.png" height="50"> 
- <img src="https://user-images.githubusercontent.com/120056106/231264886-f24f325d-3638-43d5-8895-350543d7b80c.png" height="50">
- <img src="https://user-images.githubusercontent.com/120056106/231265045-8e09789b-c822-40f4-98da-359111396e25.png" height="50">
- <img src="https://user-images.githubusercontent.com/120056106/231265498-a40886cd-8f74-4da6-99b5-8f6ed4fae529.png" height="50">
- <img src="https://user-images.githubusercontent.com/120056106/231265596-4a32886f-ec30-406c-b709-17ba8d26dbeb.png" height="50">
- <img src="https://user-images.githubusercontent.com/120056106/231265636-fc6a8b40-28ad-4676-bc65-72d564dcc9cf.png" height="50">
- <img src="https://user-images.githubusercontent.com/120056106/231265779-cb4a0d52-0ee1-41af-abd4-61503bb95748.png" height="50">
- <img src="https://user-images.githubusercontent.com/120056106/231265823-92406174-252e-4430-924c-22f04b260834.png" height="50">


## Prerequisites 
**Note: installation may vary based on your computer**
```
python -m pipenv install flask PyMySQL flask-bcrypt
```

## Installation
1. Get a free API key at https://date.nager.at/
2. Install pip files
```
pip install pipenv
python -m pipenv install flask PyMySQL flask-bcrypt

```
3. Create an ERD in MySQL and export it so you can upload the text file version when you are deploying the website
4. Add your secret key into the __init__py file
