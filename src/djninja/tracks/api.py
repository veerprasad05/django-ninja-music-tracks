from typing import List, Optional
from ninja import NinjaAPI, File
from ninja.files import UploadedFile
from tracks.models import Track
from tracks.schema import TrackSchema, NotFoundSchema

api = NinjaAPI()

#create normal Python functions using api.get()
# similar to Fast-API

# first GET endpoint 
@api.get("/tracks", response=List[TrackSchema])
def tracks(request, title: Optional[str] = None):
    if title:
        return Track.objects.filter(title__startswith=title)
    # list of all Track models
    # will return without any need for a serializer
    return Track.objects.all()

# second GET endpoint
@api.get("/tracks/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def track(request, track_id: int):
    try: 
        track = Track.objects.get(pk = track_id)
        return track
    except Track.DoesNotExist as e:
        return 404, {"message": "Track does not exist"}
    
# POST endpoint (Create)
@api.post("/tracks", response={201: TrackSchema})
def create_track(request, track: TrackSchema):
    Track.objects.create(**track.dict())
    return track

# PUT endpoint (Update)
@api.put("/tracks/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def change_track(request, track_id: int, data: TrackSchema):
    try: 
        # retrieve track using the id
        track = Track.objects.get(pk = track_id)
        # looping over the key-value pairs in the TrackSchema after making it a dict
        for attribute, value in data.dict().items():
            # changes the key-value pairs of track object to new ones sent by user
            setattr(track, attribute, value)
        # new track object saved in database
        track.save()
        
        # respond with 200 status code and the new track
        return 200, track
    except Track.DoesNotExist as e:
        return 404, {"message": "Track does not exist"}
    
# DELETE endpoint (Delete)
@api.delete("/tracks/{track_id}", response={200: None, 404: NotFoundSchema})
def delete_track(request, track_id: int):
    try: 
        # retrieve track using the id
        track = Track.objects.get(pk = track_id)
        # delete track from database and return 200 status code
        track.delete()
        return 200
    except Track.DoesNotExist as e:
        return 404, {"message": "Track does not exist"}

    
@api.post("/upload")
def upload(request, file: UploadedFile = File(...)):
    data = file.read().decode()
    return {
        'name': file.name,
        'data': data
    }

