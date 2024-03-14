from fastapi import APIRouter, HTTPException, status
from pathlib import Path
from pydantic import BaseModel
import os
import shutil


app = APIRouter()

partner_folder = Path("requests")


def copy_and_rename_db_file(src_path, dest_folder, new_filename):
    shutil.copy(src_path, dest_folder)

    _, filename = os.path.split(src_path)

    dest_path = os.path.join(dest_folder, new_filename)
    os.rename(os.path.join(dest_folder, filename), dest_path)


class Partner(BaseModel):
    name: str = None
    status: str = None


@app.post("/register_partner")
def register_partner(partner_data: Partner):

    partner_name = partner_data.name
    partner_status = partner_data.status


    partner_path = partner_folder / partner_name

    if partner_path.exists():
        return {"message": 1}

    partner_path.mkdir(parents=True)
    with open(partner_path / "access.txt", "w") as file:
        file.write(str(partner_status))
    with open(partner_path / "counter.txt", "w") as file1:
        file1.write("front:0\nback:0\nverify:0")

    source_file = "db.db"
    destination_folder = f"requests/{partner_name}"
    new_filename = f"{partner_name}.db"
    copy_and_rename_db_file(source_file, destination_folder, new_filename)

    return {"message": 0}
