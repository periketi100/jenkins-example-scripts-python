import requests
import jq
import json

bearer_token = "NjhlNmRkMGUtYmI2OC00NmRkLTg4MzktZTMyYTdlOGVjMjZh"

headers = {"Authorization": "Bearer {}".format(bearer_token)}

response = requests.get(
    "https://console.dms.ort.usw2.ficoanalyticcloud.com/com.fico.dmp.manager/rest/dmp/runtime/solutions/d0ny74319/services?env=design&type=kafka" | jq -r '[ .[] | { id: .id, serviceId: .serviceId} | select(.serviceId | startswith("cds-"))] | .[].id',
    headers=headers,
)

# Get the JSON response as a Python dict
data = response.json()

# Pretty-print JSON with indentation
pretty_json = json.dumps(data, indent=4)

print(pretty_json)


# Load your input data (assume stored in a variable or JSON file)
with open("data.json") as f:
    input_data = json.load(f)

# Define the jq filter (same as the shell version)
jq_filter = '[ .[] | { id: .id, serviceId: .serviceId } | select(.serviceId | startswith("cds-")) ] | .[].id'

# Apply the jq expression
result = jq.compile(jq_filter).input(input_data).all()

# Print the filtered IDs
for id in result:
    print(id)
