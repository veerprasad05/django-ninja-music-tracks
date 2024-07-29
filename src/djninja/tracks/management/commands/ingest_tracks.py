import json
from datetime import datetime

# settings allows access to Django settings
from django.conf import settings

# 'BaseCommand' is the base class for creating custom management commands in Django
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from tracks.models import Track


class Command(BaseCommand):
    """
    Custom Django management command to import track data from a JSON file
    into the database.

    This command reads a JSON file containing track data, converts date strings
    into timezone-aware datetime objects, and bulk inserts the data into the
    Track model in the database.

    Attributes:
        help (str): Description of the command displayed in the help text.
    """

    help = "Create tracks from JSON file"

    # main method that gets executed when the command is run
    def handle(self, *args, **kwargs):
        # set the path to the datafile
        datafile = settings.BASE_DIR / "data" / "tracks.json"
        assert datafile.exists()

        # load the datafile
        with open(datafile) as f:
            data = json.load(f)

        # create tz-aware datetime object from the JSON string.
        DATE_FMT = "%Y-%m-%d %H:%M:%S"
        for track in data:
            # converts from JSON data into datetime object
            track_date = datetime.strptime(track["last_play"], DATE_FMT)
            # considers current timezone
            track["last_play"] = make_aware(track_date)

        # convert list of dictionaries to list of Track models, and bulk_create
        tracks = [Track(**track) for track in data]

        # inserts all Track instances into database in a single query
        Track.objects.bulk_create(tracks)
