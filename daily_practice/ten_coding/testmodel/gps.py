import piexif
from PIL import Image


def get_gps(photo):
    image = Image.open(photo)
    exif_dict = piexif.load(image.info['exif'])
    try:
        gps = exif_dict['GPS']
        latitude = (gps[2][0][0]) + (gps[2][1][0] / 60 + (gps[2][2][0]) / 360000)
        longitude = (gps[4][0][0]) + (gps[4][1][0] / 60 + (gps[4][2][0]) / 360000)
        return round(latitude, 4), round(longitude, 4)
    except KeyError:
         latitude = None
         longitude = None
         return latitude, longitude
