import requests

# WHO Global Health Observatory API endpoint
url = "https://ghoapi.azureedge.net/api/Indicator"

# Fetch data
r = requests.get(url)
print("Status Code:", r.status_code)

try:
    data = r.json()
except ValueError:
    print("Response is not valid JSON")
    data = None

def print_json(data, indent=0, max_items=10):
    """Recursively print JSON in key: value format."""
    spacing = "    " * indent
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                print(f"{spacing}{key}:")
                print_json(value, indent + 1, max_items)
            else:
                print(f"{spacing}{key}: {value}")
    elif isinstance(data, list):
        for i, item in enumerate(data[:max_items]):  # Limit printing for large lists
            print(f"{spacing}- Item {i+1}:")
            print_json(item, indent + 1, max_items)
        if len(data) > max_items:
            print(f"{spacing}... ({len(data) - max_items} more items)")
    else:
        print(f"{spacing}{data}")

if data:
    print("\n=== WHO API Response (Readable) ===\n")
    print_json(data)
