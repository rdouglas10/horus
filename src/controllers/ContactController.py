from flask import request, g, Blueprint, json, Response
from ..services.ContactService import ContactService

contact_api = Blueprint('contact_api', __name__)

@contact_api.route('/', methods=['POST'])
def create():
  """
  Create Contact Function
  """
  output = ContactService.create_contact(request.get_json())
  return custom_response(output['data'],output['status'])

@contact_api.route('/', methods=['GET'])
def get_all():
  """
  Get All Contact
  """
  output = ContactService.get_all_contact()
  return custom_response(output['data'],output['status'])


@contact_api.route('/<int:contact_id>', methods=['GET'])
def get_one(contact_id):
  """
  Get A Contact
  """
  output = ContactService.get_one_contact(contact_id)
  return custom_response(output['data'],output['status'])


@contact_api.route('/<int:contact_id>', methods=['PUT'])
def update(contact_id):
  """
  Update A Contact
  """

  output = ContactService.update_contact(contact_id,request.get_json())
  return custom_response(output['data'],output['status'])
  
  

@contact_api.route('/<int:contact_id>', methods=['DELETE'])
def delete(contact_id):
  """
  Delete A Contact
  """
  output = ContactService.delete_contact(contact_id)
  return output


def custom_response(res, status_code):
    """
  Custom Response Function
  """
    return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )