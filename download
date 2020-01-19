If you would like to run trversal on your local server instead of at trversal.com, please follow this guide. 
*You will need a Google API key and the required Credintials listed below need to be turned on or some features will not work
*terminal code snippets are Windows examples


You will need to setup your API Key for the Google services
I will attempt to give a quick guide on this, but the site may change. Also, there are just a lot of tools on the cloud service, but there are a lot of  more in-depth guides available online. (I had to use one the first time!)

https://cloud.google.com/
Sign-in to a Google account and then go your "Console" that is linked in the header.
You will need to start a new project
Once in that project's dashboard, look for 'API's & Services'
Then click "Credentials"
"Create New Credentials"
Select "API Key" to generate a key and select "Restrict this API key"
In the project menu, look for "Library"
Search and 'enable' the following services:

Directions API
Maps JavaScript API
Geocoding API
Places API


This project uses virtual environments with pipenv. With pipenv installed, create the virtual environment:

```bash
pipenv shell
```

'Sync' to install the project's dependencies:

```bash
pipenv sync
```

We need to create a secrets file to hook up the API key

```bash
cd trversalapp

touch secrets.py

nano secrets.py
```
Add the following line of code in the editor. This must be exact or Python won't find the variable. Put **_your api key_** in the quotes:
```python
api_key = "YOUR-KEY"
```

if you are not serving on localhost:8000, the AJAX urls will fail. 
```bash
python manage.py runserver localhost:8000
```

Go to http://localhost:8000/

You can sign into the Demo Account I created:

Username: PortfolioDemo
Password: dem0Password

```bash

```
