import os
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
import shutil

from configs.decoder import decode_text
from db.insert_data import insert_to_pass_recognition
from db.insert_data import insert_to_verification
    
app = APIRouter()


def rewrite_counter(counter_text, type="verify"):
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


class Verification(BaseModel):
  name: str = None
  
  front_img_size: str = None
  selfi_img_size: str = None
  
  format_front: str = None
  format_selfi: str = None

  weight_front_img: str = None
  weight_selfi_img: str = None

  front_findPass: str = None
  selfi_findPass: str = None

  front_passNum: str = None
  selfi_passNum: str = None
  
  front_original: str = None
  selfi_original: str = None

  front_len_passnum: str = None
  selfi_len_passnum: str = None

  front_special_id: str = None
  selfi_special_id: str = None

  pass_match: str = None
  face_match: str = None
  distance: str = None

  explanation_of_reject: str = None
  is_fake: str = None

  time: str = None



@app.post("/exe_verify")
def verificaton(item: Verification):
    
    encode_name_bank = item.name
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
        
    if access==0:
        return {"error": "Access Danied!"}
    else:
        front_img_size = item.front_img_size
        selfi_img_size = item.selfi_img_size

        format_front = item.format_front
        format_selfi = item.format_selfi

        weight_front_img = item.weight_front_img
        weight_selfi_img = item.weight_selfi_img

        front_findPass = item.front_findPass
        selfi_findPass = item.selfi_findPass

        front_passNum = item.front_passNum
        selfi_passNum = item.selfi_passNum

        front_original = item.front_original
        selfi_original = item.selfi_original

        front_len_passnum = item.front_len_passnum
        selfi_len_passnum = item.selfi_len_passnum

        front_special_id = item.front_special_id
        selfi_special_id = item.selfi_special_id

        pass_match = item.pass_match
        face_match = item.face_match
        distance = item.distance

        explanation_of_reject = item.explanation_of_reject
        is_fake = item.is_fake
        time = item.time

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        
        re_counter = rewrite_counter(counter)
        with open(f"requests/{decode_name_bank}/counter.txt", 'w') as f1:
            f1.write(counter.replace(f"verify:" + str(re_counter), f"verify:" + str(re_counter+1)))


        db_name = f"requests/{decode_name_bank}/{decode_name_bank}.db"

        insert_to_verification(db_name, re_counter+1, front_img_size, selfi_img_size, format_front, format_selfi, weight_front_img, weight_selfi_img, front_findPass, selfi_findPass, front_passNum, selfi_passNum, front_original, selfi_original, front_len_passnum, selfi_len_passnum, front_special_id, selfi_special_id, pass_match, face_match, distance, explanation_of_reject, is_fake, time, date)
        
        
        
        
    
    final_data = {
      "name_bank": decode_name_bank, 
      "access": access, 
      "counter": re_counter+1, 
      "model": "verify",
      "front_img_size": front_img_size,
      "selfi_img_size": selfi_img_size,

      "format_front": format_front,
      "format_selfi": format_selfi,

      "weight_front_img": weight_front_img,
      "weight_selfi_img": weight_selfi_img,

      "front_findPass": front_findPass,
      "selfi_findPass": selfi_findPass,

      "front_passNum": front_passNum,
      "selfi_passNum": selfi_passNum,

      "pass_match": pass_match,
      "face_match": face_match,
      "distance": distance,

      "front_original": front_original,
      "selfi_original": selfi_original,

      "front_len_passnum":front_len_passnum,
      "selfi_len_passnum":selfi_len_passnum,

      "front_special_id":front_special_id,
      "selfi_special_id":selfi_special_id,

      "explanation_of_reject":explanation_of_reject,
      "is_fake": is_fake,
      "time": time,
      "date": date
    }
    return final_data