import os
from fastapi import APIRouter, Request
from pydantic import BaseModel
from datetime import datetime
import shutil
from typing import Any, Dict, AnyStr, List, Union

from configs.decoder import decode_text
from db.insert_data import insert_to_pass_recognition
    
app = APIRouter()
JSONObject = Dict[AnyStr, Any]


def rewrite_counter(counter_text, type):
    spl = counter_text.split("\n")
    
    for i in spl:
        if type in i:
            s = i.split(":")[1]
            
    count = int(s)
    return count


def copy_and_rename_db_file(src_path, dest_folder, new_filename):
    
    shutil.copy(src_path, dest_folder)
    
    _, filename = os.path.split(src_path)

    dest_path = os.path.join(dest_folder, new_filename)
    os.rename(os.path.join(dest_folder, filename), dest_path)


class Pass(BaseModel):
    name: str
        
    type: str
    img_size: str
    weight_img: str
    format_img: str
    special_id: str
    find_pass: str
    pass_num: str
    time: str


class DataModel(BaseModel):
    name: str
    type: str
    img_size: str  # Parse as a list of integers
    weight_img: float
    special_id: str
    pass_num: str
    format_img: str
    find_pass: bool
    time: int
    date: int


@app.post("/exe")
async def pass_recognition(data: JSONObject = None):

    encode_name_bank = data["name"]
    print(encode_name_bank)
    try:
        decode_name_bank = decode_text(encode_name_bank)
    except:
        return {"error": "Username is incorrect"}
        
    
    
    if not os.path.exists(f"requests/{decode_name_bank}"):
        os.mkdir(f"requests/{decode_name_bank}")
        
        with open(f"requests/{decode_name_bank}/access.txt", 'w') as f:
            f.write('0')
            
        with open(f"requests/{decode_name_bank}/counter.txt", 'w') as file:
            file.write('front:0\nback:0\nverify:0')


        source_file = "db.db"
        destination_folder = f"requests/{decode_name_bank}"
        new_filename = f"{decode_name_bank}.db"
        copy_and_rename_db_file(source_file, destination_folder, new_filename)

    
    with open(f"requests/{decode_name_bank}/access.txt", 'r') as f:
        access = int(f.read())
        
    with open(f"requests/{decode_name_bank}/counter.txt", 'r') as f1:
        counter = f1.read()
        

    model = data["type"]
    img_size = data["img_size"]
    weight_img = data["weight_img"]
    special_id = data["special_id"]
    pass_num = data["pass_num"]
    format_img = data["format_img"]
    find_pass = data["find_pass"]
    time = data["time"]
    
    
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        re_counter = rewrite_counter(counter, model)
    except:
        return {"error": "You forget send 'type'. Example: {'type': 'front' or 'back'}"}
    with open(f"requests/{decode_name_bank}/counter.txt", 'w') as f1:
        f1.write(counter.replace(f"{model}:" + str(re_counter), f"{model}:" + str(re_counter+1)))


    db_name = f"requests/{decode_name_bank}/{decode_name_bank}.db"

    insert_to_pass_recognition(db_name, re_counter+1, model, img_size, weight_img, format_img, special_id, find_pass, pass_num, time, date)
    
        
        
        
    
    final_data = {
        "name_bank": decode_name_bank, 
        "access": access, 
        "error": "Access Danied!",
        "counter": re_counter+1, 
        "model": model,
        "img_size": img_size,
        "weight_img": weight_img,
        "format_img": format_img,
        "special_id": special_id,
        "find_pass": find_pass,
        "pass_num": pass_num,
        "time": time,
        "date": date
    }
    return final_data