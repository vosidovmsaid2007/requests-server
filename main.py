
from fastapi import FastAPI
from routes.pass_recognition import app as pass_router
from routes.verification import app as verification_router
from routes.get_requests import app as all_requests
from routes.partners_info import app as partners_info
from routes.add_partner import app as register_partner
import uvicorn

app = FastAPI()

app.include_router(pass_router)
app.include_router(verification_router)
app.include_router(all_requests)
app.include_router(partners_info)
app.include_router(register_partner)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
