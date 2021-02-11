import requests
import datetime
import os.path


year = str(datetime.date.today().year)

# api-endpoint
def api_endpoint():
    return "https://www.londonprayertimes.com/api/times/?format=json&key=70bb0d1d-7d54-4d3e-868e-264ac8b88f91&24hours=true&year=" + year

def timetable_exists():
    return os.path.isfile("./yearlyCalendarOutput/Calendar" + year + ".json")

def download_json(api_endpoint):
    json_file = requests.get(api_endpoint)
    open("./yearlyCalendarOutput/Calendar" + year + ".json", 'wb').write(json_file.content)
