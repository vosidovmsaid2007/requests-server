import sqlite3


def insert_to_pass_recognition(db_name, counter, model, img_size, weight_img, format_img, special_id, find_pass, pass_num, time, date):
  connection = sqlite3.connect(db_name)
  cursor = connection.cursor()

  cursor.execute('INSERT INTO pass_recognition (counter, model, img_size, weight_img, format_img, special_id, find_pass, pass_num, time, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (counter, model, img_size, weight_img, format_img, special_id, find_pass, pass_num, time, date))

  connection.commit()
  connection.close()


def insert_to_verification(db_name, counter, front_img_size, selfi_img_size, format_front, format_selfi, weight_front_img, weight_selfi_img, front_findPass, selfi_findPass, front_passNum, selfi_passNum, front_original, selfi_original, front_len_passnum, selfi_len_passnum, front_special_id, selfi_special_id, pass_match, face_match, distance, explanation_of_reject, is_fake, time, date):
  connection = sqlite3.connect(db_name)
  cursor = connection.cursor()

  cursor.execute('INSERT INTO verification (counter, front_img_size, selfi_img_size, format_front, format_selfi, weight_front_img, weight_selfi_img, front_findPass, selfi_findPass, front_passNum, selfi_passNum, front_original, selfi_original, front_len_passnum, selfi_len_passnum, front_special_id, selfi_special_id, pass_match, face_match, distance, explanation_of_reject, is_fake, time, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (counter, front_img_size, selfi_img_size, format_front, format_selfi, weight_front_img, weight_selfi_img, front_findPass, selfi_findPass, front_passNum, selfi_passNum, front_original, selfi_original, front_len_passnum, selfi_len_passnum, front_special_id, selfi_special_id, pass_match, face_match, distance, explanation_of_reject, is_fake, time, date))

  connection.commit()
  connection.close()
  
