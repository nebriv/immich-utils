import sys
import dotenv
import os

dotenv.load_dotenv()

from immich.configuration import Configuration
from immich.api.album_api import AlbumApi
from immich.models import CreateAlbumDto
from immich.api_client import ApiClient

config = Configuration()
config.host = os.getenv("IMMICH_URL", None)
config.api_key['api_key'] = os.getenv("IMMICH_API_KEY", None)

if not config.host or not config.api_key['api_key']:
    print("Please set the environment variables IMMICH_URL and IMMICH_API_KEY")
    sys.exit(1)


client = ApiClient(configuration=config)
album_api = AlbumApi(api_client=client)


albums_to_delete = []

albums = album_api.get_all_albums()
for album in albums:
    if album.album_name.startswith("Untitled("):
        albums_to_delete.append(album)

if albums_to_delete:
    print("The following albums will be deleted:")
    for album in albums_to_delete:
        print(f"{album.album_name}")

    response = input("Do you want to delete these albums? (y/n): ")
    if response.lower() == "y":
        for album in albums_to_delete:
            album_api.delete_album(album.id)
        print("Albums deleted successfully.")
    else:
        print("Operation cancelled.")

