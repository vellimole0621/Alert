import googlemaps

lat = 37.224650469991 # 위도 값 Ex) 명지대 위도
lng = 127.18758354347 # 경도 값 Ex) 명지대 경도

API = - # API 값

gmaps = googlemaps.Client(key=API) # api key
reverse_geocode_result = gmaps.reverse_geocode((lat, lng), language='ko')
gps = reverse_geocode_result[1]["formatted_address"]
print(gps)