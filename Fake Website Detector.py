from urllib.parse import urlparse

def fake_website_detector(url):
    parsed_url = urlparse(url)
    
    if not parsed_url.scheme == "https":
        return "Website tidak aman"
    
    suspicious_keywords = ["login", "verify", "secure", "bank"]
    if any(keyword in parsed_url.netloc.lower() for keyword in suspicious_keywords):
        return "Website mencurigakan"
    
    return "Website aman"

url_input = input("Masukkan URL: ")
print(fake_website_detector(url_input))
