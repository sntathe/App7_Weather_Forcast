import requests

api_key = "106cc82d86c6fbcbe7c2aa93fc1768d6"


def get_data(place="london", days=None, option=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}&units=metric"
    response = requests.get(url)
    date_array = []
    temp_array = []
    sky_array = []
    if response.ok:
        data = response.json()
        filtered_data = data["list"]



        for item in filtered_data:
            sky_array.append(item["weather"][0]["main"])
            date_array.append(item['dt_txt'])
            temp_array.append(item['main']['temp'])

    if(option == "sky"):
         return [date_array, sky_array]
    else:
          return [date_array, temp_array]




if __name__ == "__main__":
    print(get_data(place="Tokyo"))
