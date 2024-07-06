import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'universal',
    'url': 'https://sandbox.oxylabs.io/',
    # 'render': 'html', # If page type requires
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('oh ho ', 'hione'), # Your credentials go here
    json=payload,
)

# Instead of response with job status and results url, this will return the
# JSON response with results.
pprint(response.json())