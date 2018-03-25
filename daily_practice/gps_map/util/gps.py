import piexif
from PIL import Image

def get_gps(photo):
    image = Image.open(photo)
    exif_dict = piexif.load(image.info['exif'])
    try:
        gps = exif_dict['GPS']
        lat = (gps[2][0][0]) + (gps[2][1][0] / 60 + (gps[2][2][0]) / 360000)
        lng = (gps[4][0][0]) + (gps[4][1][0] / 60 + (gps[4][2][0]) / 360000)
        return round(lat, 4), round(lng, 4)
    except KeyError:
        lat = None
        lng = None
        return lat, lng
