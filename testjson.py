import urllib.request, urllib.parse, urllib.error
import json
import ssl

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sum=0
while True:
    url = input('Enter location: ')

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = json.loads(data.decode())

    # results = tree.findall('.//count')
    for res in tree["comments"]:
        sum += int(res["count"])
    print(sum)