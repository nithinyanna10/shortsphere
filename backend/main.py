from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from backend.services import shorten_url, get_original_url, log_click  # ✅ if services.py is in same dir


app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/shorten")
async def create_short_url(data: URLRequest):
    code = await shorten_url(data.url)
    return {"short_url": f"http://localhost:8000/{code}"}

@app.get("/{code}")
async def redirect(code: str, request: Request):
    result = await get_original_url(code)
    if not result:
        raise HTTPException(status_code=404, detail="URL not found")
    ip = request.client.host
    ua = request.headers.get("user-agent")
    await log_click(code, ip, ua)
    return RedirectResponse(result)

from fastapi.responses import JSONResponse
from backend.storage import get_logs_for_code

@app.get("/analytics/{code}")
async def get_analytics(code: str):
    logs = get_logs_for_code(code)
    if not logs:
        raise HTTPException(status_code=404, detail="No analytics found for this code")

    total_clicks = len(logs)
    
    # Aggregate by country
    country_counts = {}
    user_agents = {}
    for log in logs:
        country = log.get("country", "Unknown")
        ua = log.get("user_agent", "Unknown")
        country_counts[country] = country_counts.get(country, 0) + 1
        user_agents[ua] = user_agents.get(ua, 0) + 1

    return JSONResponse({
        "short_code": code,
        "total_clicks": total_clicks,
        "countries": country_counts,
        "user_agents": user_agents,
        "raw_logs": logs  # Optional for CSV export in frontend
    })

