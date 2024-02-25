from fastapi import APIRouter

from db.get_requests import get_all_requests

app = APIRouter()


@app.get("/all_requests/{partner_name}/{type_model}")
def send_all_requests_pass(partner_name: str, type_model: str):
    db_name = f"requests/{partner_name}/{partner_name}.db"

    if type_model == "pass_recognition": 
        table = "pass_recognition"
        try:
            get_requests = get_all_requests(db_name = db_name, table = table)
        except:
            return {"error": "Partner name is incorrect"}
        return get_requests
    elif type_model == "verification":
        table = "verification"
        try:
            get_requests = get_all_requests(db_name = db_name, table = table)
        except:
            return {"error": "Partner name is incorrect"}
        return get_requests
