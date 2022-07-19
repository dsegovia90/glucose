import json
import urllib3
from dotenv import dotenv_values

config = dotenv_values(".env")

base_url = config.get('BASE_NIGHTSCOUT_URL')
token = config.get('NIGHTSCOUT_API_TOKEN')
count = 99999
http = urllib3.PoolManager()
request = http.request(
    "GET",
    f"{base_url}?find[dateString][$gte]=2015-08-28&count={count}&token={token}",
    headers={
        "accept": "application/json"
    }
)

data = json.loads(request.data.decode('utf-8'))

sorted_data = sorted(data, key=lambda d: d['date'])
filtered_sorted_data = list(filter(lambda x: x.get('type') == 'sgv', sorted_data))
print(f"data size: {len(filtered_sorted_data)}")
with open("raw_data.json", "w") as outfile:
    outfile.write(json.dumps(filtered_sorted_data))
