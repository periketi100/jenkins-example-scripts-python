import httpx
import json

bearer_token = "ZWQ4M2U5OTUtNDkyZS00MzY3LTg3YmMtNjFiM2RjZmU0OTVi"

headers = {"Authorization": f"Bearer {bearer_token}"}

url = "https://console.dms.ort.usw2.ficoanalyticcloud.com/com.fico.dmp.manager/rest/dmp/runtime/solutions/d0ny74319/services?env=design&type=kafka"

response = httpx.get(url, headers=headers)

# Get the JSON response as a Python dict
data = response.json()

# Pretty-print JSON with indentation
pretty_json = json.dumps(data, indent=4)

print(pretty_json)
