from typing import List, Optional
from ninja import NinjaAPI
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
