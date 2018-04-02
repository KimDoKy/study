import gps
import reverse_geocoding

country = input('국가를 입력하세요. ex) ko : ')
api_key = YOUR_API_KEY

photo_path = input('사진을 입력하세요. ')

lat, lng = gps.get_gps(photo_path)
print('lat: ', lat)
print('lng: ', lng)

address = reverse_geocoding.get_address(country, lat, lng, api_key)

print('신주소: ', address[0])
print('구주소: ', address[1])
print('국가: ', address[2])
print('도시: ', address[3])
print('지역: ', address[4])
