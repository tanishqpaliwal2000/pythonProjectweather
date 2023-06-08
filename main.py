import requests
import json
while True:

    city=input("enter the name of city-->>\n")
    if city=='no':
        break
    else:
        url=f"https://api.weatherapi.com/v1/current.json?key=632514e167664e62a66112836230406&q={city}"

        r=requests.get(url)

        dict=json.loads(r.text)
        print(dict["current"]["temp_c"])


