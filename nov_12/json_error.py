import json, datetime

d = {
    "today": datetime.datetime.now()
}

json_str = json.dumps(d)
