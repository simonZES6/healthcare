from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
data = []
arts = []

#class Apotheek(BaseModel):
  #  medicine : str
  #  verval_datum : str


class Doctor(BaseModel):
    doctor_id : int
    doctor_name : str
    hospital : str
  

class HealthCare(BaseModel):
    client_id : int
    name : str
    lastname : str 
    medicine : str
    verval_datum : str
    doctor : Doctor #injection
  

@app.post("/healthcare")
def create_file(healthcare:HealthCare):
    data.append(healthcare)
    return healthcare

@app.get("/healthcare/{client_id}")
def read_client(client_id:int):
    for client in data:
        if client.client_id == client_id:
    
         return client
       
@app.get("/healthcare")
def get_client():
    return data
            
        
@app.put("/healthcare")
def update_file(healthcare:HealthCare):
    for i in data:
        if i.client_id == healthcare.client_id:
             i.client_id = healthcare.client_id
             i.name = healthcare.name
             i.lastname = healthcare.lastname
             i.medicine = healthcare.medicine
             i.verval_datum = healthcare.verval_datum
             i.doctor.doctor_id = healthcare.doctor.doctor_id
             i.doctor.doctor_name = healthcare.doctor.doctor_name
             i.doctor.hospital =healthcare.doctor.hospital
             #i.apotheek.medicine = healthcare.apotheek.medicine
             #i.apotheek.verval_datum = healthcare.apotheek.verval_datum
        
        return i

@app.delete("/healthcare")
def delete_file(healthcare:HealthCare):
    for i in data:
        if i.client_id == healthcare.client_id:
            data.remove (healthcare)

       


