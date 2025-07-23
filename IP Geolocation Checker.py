import requests

ip = input("Masukkan IP: ")
response = requests.get(f"https://ipinfo.io/{ip}/json")

data = response.json()
print("Lokasi:", data.get("city"), "-", data.get("region"), "-", data.get("country"))
print("ISP:", data.get("org"))