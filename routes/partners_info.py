from fastapi import APIRouter
import os

app = APIRouter()


def get_partner_status(partner_name):
	f = open(f'requests/{partner_name}/access.txt')
	txt = f.read()
	f.close()

	return txt.replace("\n", "")


def get_partner_data_requests(partners_name):
	f = open(f'requests/{partners_name}/counter.txt')
	txt = f.read().replace("\n", " ").split()
	f.close()

	d={}
	d['front'] = txt[0].split(':')[1]
	d['back'] = txt[1].split(':')[1]
	d['verify'] = txt[2].split(':')[1]
	return d

@app.get("/partners_info")
def partners_info():
	partners_name = os.listdir("requests/")

	res = []
	
	for i in range(len(partners_name)):
		data = {}
		data['partner_id'] = i+1
		data['partner_name'] = partners_name[i]
		data['partner_status'] = get_partner_status(partners_name[i])
		data['partner_data'] = get_partner_data_requests(partners_name[i])
		res.append(data)


	return {"partners_amount": len(partners_name), "partners_name": partners_name, "partner_data": res}

