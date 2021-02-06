import requests
import datetime
import os.path

year = str(datetime.date.today().year)
# api-endpoint

def api_endpoint():
    return "https://www.londonprayertimes.com/api/times/?format=json&key=2a99f189-6e3b-4015-8fb8-ff277642561d&24hours=true&year=" + year

def timetable_exists():
    return os.path.isfile("yearlyCalendarOutput/Calendar" + year + ".json")

def download_json(api_endpoint):
    json_file = requests.get(api_endpoint)
    open("yearlyCalendarOutput/Calendar" + year + ".json", 'wb').write(json_file.content)
