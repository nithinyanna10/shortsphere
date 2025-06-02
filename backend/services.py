import random
import string
import requests
from backend.storage import log_click_to_file

# 🔁 In-memory key-value store
memory_store = {}

# 🔑 Generate random short codes
def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# 🚀 Store short URL mapping
async def shorten_url(original_url: str):
    code = generate_code()
    memory_store[code] = original_url
    return code

# 🔍 Retrieve original URL by short code
async def get_original_url(code: str):
    return memory_store.get(code)

# 📊 Log click info into logs.json
async def log_click(code: str, ip: str, user_agent: str):
    geo_info = requests.get(f"http://ip-api.com/json/{ip}").json()
    country = geo_info.get("country", "Unknown")
    log_click_to_file({
        "short_code": code,
        "ip": ip,
        "country": country,
        "user_agent": user_agent
    })
