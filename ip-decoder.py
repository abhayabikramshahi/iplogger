import requests

def get_ip_location(ip=""):
    try:
        # If no IP is provided, get your public IP
        if not ip:
            ip = requests.get("https://api64.ipify.org?format=json").json().get("ip")

        response = requests.get(f"http://ipinfo.io/{ip}/json")
        data = response.json()

        location_info = {
            "IP": data.get("ip", "N/A"),
            "City": data.get("city", "N/A"),
            "Region": data.get("region", "N/A"),
            "Country": data.get("country", "N/A"),
            "Location": data.get("loc", "N/A"),  # Latitude, Longitude
            "ISP": data.get("org", "N/A")
        }

        return location_info
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    result = get_ip_location()
    
    for key, value in result.items():
        print(f"{key}: {value}")
