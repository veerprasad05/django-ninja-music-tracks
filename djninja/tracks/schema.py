from datetime import datetime
from ninja import Schema

class TrackSchema(Schema):
    """
    Schema representing a music track.

    Attributes:
        title (set): A set of strings representing the titles of the track.
        artist (str): The name of the artist or band performing the track.
        duration (float): The duration of the track in minutes.
        last_play (datetime): The datetime when the track was last played.
    """
    title: str
    artist: str
    duration: float
    last_play: datetime
    
class NotFoundSchema(Schema):
    """
    Schema for a not found response (in case the user searches by track id)

    Attributes:
        message (str): A message indicating that the requested resource was not found.
    """
    message:str