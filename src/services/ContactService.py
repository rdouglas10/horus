from flask import request, g, Blueprint, json, Response
from ..models.ContactModel import ContactModel, ContactSchema
contact_schema = ContactSchema()

class ContactService():

  def create_contact(req_data):
    
    data = contact_schema.load(req_data)
    
    if "name" not in req_data:
      return {"data": "Enter your name.", "status":400}

    if "phone" not in req_data:
      return {"data": "Enter a contact number.", "status":400}

    phone_exist = ContactModel.get_one_contact_number(req_data['phone'])

    if phone_exist == True:
      return {"data": "This phone already exists.", "status":400}

    contact = ContactModel(data)
    contact.save()
    data = contact_schema.dump(contact)
    return {"data":data, "status":200}


  def get_all_contact():
    contacts = ContactModel.get_all_contacts()
    data = contact_schema.dump(contacts, many=True)
    return {"data":data, "status":200}


  def get_one_contact(contact_id):
    contact = ContactModel.get_one_contact(contact_id)
	  
    if not contact or contact.deleted == True:
      return {"data": "Contact not found", "status":404}
    data = contact_schema.dump(contact)
    return {"data":data, "status":200}


  def update_contact(contact_id, req_data):
    contact = ContactModel.get_one_contact(contact_id)

    if not contact or contact.deleted == True:
      return {"data": "Contact not found", "status":404}

    data = contact_schema.load(req_data, partial=True)

    if req_data['phone'] == "" or req_data['phone'] == None:
    	return {"data": "Enter a contact number.", "status":400}	

    if req_data['phone'] == contact.phone:
      return {"data": "This phone already exists.", "status":400}		

    contact.update(data)

    data = contact_schema.dump(contact)
    return {"data":data, "status":200}


  def delete_contact(contact_id):
    contact = ContactModel.get_one_contact(contact_id)

    if not contact:
      return {"data": "contact not found", "status":404}

    data = contact_schema.dump(contact)
	 
    contact.delete()
    return {"data": "deleted contact!", "status":204}
