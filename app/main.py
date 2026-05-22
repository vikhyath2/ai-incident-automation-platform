from fastapi import FastAPI, UploadFile, File, HTTPException
from app.models import IncidentRequest
from app.ai_service import analyze_incident
from app.database import create_table, save_incident, get_all_incidents
from app.alert_service import send_alert

app = FastAPI(title="AI Incident Automation Platform")

create_table()


@app.get("/")
def home():
    return {
        "message": "AI Incident Automation Platform Running"
    }


@app.post("/analyze-incident")
def analyze_incident_api(request: IncidentRequest):
    result = analyze_incident(request.log_text)

    save_incident(request.log_text, result)
    if result.get("severity") == "Critical":
        send_alert(result) 
    return {
        "input_log": request.log_text,
        "analysis": result
    }


@app.post("/analyze-log-file")
async def analyze_log_file(file: UploadFile = File(...)):
    allowed_extensions = [".txt", ".log"]
    if not any(file.filename.endswith(ext) for ext in allowed_extensions):
        raise HTTPException(
            status_code=400,
            detail="Only .txt and .log files are supported"
    )

    contents = await file.read()

    log_text = contents.decode("utf-8")

    result = analyze_incident(log_text)

    save_incident(log_text, result)
    if result.get("severity") == "Critical":
        send_alert(result) 

    return {
        "filename": file.filename,
        "analysis": result
    }

@app.get("/incidents")
def list_incidents():
    incidents = get_all_incidents()

    return {
        "total": len(incidents),
        "incidents": incidents
    }