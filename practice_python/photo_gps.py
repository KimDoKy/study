from PIL import Image
from PIL.ExifTags import TAGS

filename = str(input("photofilename: "))

try:
    img = Image.open(filename)
    info = img._getexif()
    exif = {}

    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        exif[decoded] = value

    # gps 추출
    exifGPS = exif['GPSInfo']
    latData = exifGPS[2]
    lonData = exifGPS[4]

    # lat / lng 계산
    latDeg = latData[0][0] / float(latData[0][1])
    latMin = latData[1][0] / float(latData[1][1])
    latSec = latData[2][0] / float(latData[2][1])
    lonDeg = lonData[0][0] / float(lonData[0][1])
    lonMin = lonData[1][0] / float(lonData[1][1])
    lonSec = lonData[2][0] / float(lonData[2][1])

    # 방햐에 따른 GPS 계산
    Lat = (latDeg + (latMin + latSec / 60.0) / 60.0)
    Lon = (lonDeg + (lonMin + lonSec / 60.0) / 60.0)
    gps = str(Lat)+","+str(Lon)

finally:
    print(gps)
