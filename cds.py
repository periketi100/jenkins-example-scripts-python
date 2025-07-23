import urllib3
import json

bearer_token = "ZWQ4M2U5OTUtNDkyZS00MzY3LTg3YmMtNjFiM2RjZmU0OTVi"

http = urllib3.PoolManager()

url = "https://console.dms.ort.usw2.ficoanalyticcloud.com/com.fico.dmp.manager/rest/dmp/runtime/solutions/d0ny74319/services?env=design&type=kafka"

headers = {
    "Authorization": f"Bearer {bearer_token}"
}

response = http.request(
    "GET",
    url,
    headers=headers
)

# response.data is bytes, decode it
data = json.loads(response.data.decode("utf-8"))

# Pretty print JSON
pretty_json = json.dumps(data, indent=4)
print(pretty_json)
