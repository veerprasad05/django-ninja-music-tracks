# django-ninja-music-tracks

This project demonstrates a CRUD API using Django Ninja for managing a music tracks database. The API allows users to create, read, update, and delete (CRUD) records of songs stored in a database, initially imported from a JSON file. Additionally, the project includes a feature for uploading documents.

## Features
* **CRUD Operations**
    * **Create:** Add new tracks to the database. 
    * **Read:** Retrieve track details. 
    * **Update:** Modify existing track details. 
    * **Delete:** Remove tracks from the database.
* **File Upload:**
    * Upload documents to the file system.

## Installation and Running
1. **Clone the Repo**
2. **Install Dependencies** \
``` pip install -r requirments.txt```
3. **Run Migrations** \
``` python manage.py makemigrations``` \
``` python manage.py migrate``` 
4. **Load Initial Database** \
``` python manage.py ingest_tracks```
5. **Start the Server** \
``` python manage.py runserver```

## Usage
* **GET:** If the URL entered is "api/tracks" with no data entered, all tracks are outputted. If the URL is "api/tracks/{track_id}, the track with the particular {track_id} is outputted.
* **POST:** When the URL is "api/tracks" with the correctly formatted data passed into the API.
* **PUT:** When the URL is "api/tracks/{track_id} and correctly formatted data is passed into the API, the track with the matching id is changed to reflect the new data.
* **DELETE:** Remove a track by its ID by sending a DELETE request.

## JSON File Import
To import songs into the database from a JSON file, ensure your file is formatted correctly according to your Django model fields. Use Django management commands or a custom script to load the data.