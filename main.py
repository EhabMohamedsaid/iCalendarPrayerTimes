import api_call
import json_parser

if __name__ == '__main__':
    if not api_call.timetable_exists():
        api_call.download_json(api_call.api_endpoint())
    json_parser.read_json()
