from fastapi import APIRouter

from db.get_requests import get_all_requests, get_requests_by_month, get_requests_by_month_limit

app = APIRouter()


@app.get("/all_requests/{partner_name}/{type_model}")
def send_all_requests_pass(partner_name: str, type_model: str):
    db_name = f"requests/{partner_name}/{partner_name}.db"

    if type_model == "front": 
        table = "pass_recognition"
        
        try:
            get_requests = get_all_requests(db_name = db_name, table = table, model_type = "front")
        except:
            return {"error": "Partner name is incorrect"}
        return get_requests
    elif type_model == "back":
        table = "pass_recognition"
        try:
            get_requests = get_all_requests(db_name = db_name, table = table, model_type = "back")
        except:
            return {"error": "Partner name is incorrect"}
        return get_requests
    elif type_model == "verification":
        table = "verification"
        try:
            get_requests = get_all_requests(db_name = db_name, table = table, model_type = "verification")
        except:
            return {"error": "Partner name is incorrect"}
        return get_requests


@app.get("/{year}/{month}/{partner_name}/{type_model}/{limit}")
def send_requests_by_month(year: int, month: int, partner_name: str, type_model: str, limit: str):
    db_name = f"requests/{partner_name}/{partner_name}.db"

    if limit == "all":
        if type_model == "front" or type_model == "back": 
            table = "pass_recognition"
            
            try:
                get_requests = get_requests_by_month(db_name = db_name, table = table, year = year, month = month, model_type = type_model)
            except:
                return {"error": "Partner name is incorrect"}
            return get_requests
        elif type_model == "verification":
            table = "verification"
            
            get_requests = get_requests_by_month(db_name = db_name, table = table, year = year, month = month, model_type = "verification")
            # except:
            #     return {"error": "Partner name is incorrect"}
            return get_requests
    elif limit != "all":
        limit_num = int(limit)
        if type_model == "front" or type_model == "back": 
            table = "pass_recognition"
            try:
                get_requests = get_requests_by_month_limit(db_name = db_name, table = table, year = year, month = month, model_type = type_model, limit = limit_num)
            except:
                return {"error": "Partner name is incorrect"}
            return get_requests
        elif type_model == "verification":
            table = "verification"
            
            get_requests = get_requests_by_month_limit(db_name = db_name, table = table, year = year, month = month, model_type = "verification", limit = limit_num)
            # except:
            #     return {"error": "Partner name is incorrect"}
            return get_requests
