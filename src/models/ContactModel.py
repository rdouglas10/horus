from marshmallow import Schema, fields, EXCLUDE
import datetime
from . import db

class ContactModel(db.Model):
  """
  Contact Model
  """

  # table name
  __tablename__ = 'contacts'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(128), nullable=False)
  phone = db.Column(db.String(128), nullable=False)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)
  deleted = db.Column(db.Boolean(), default=False)

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """
    self.name = data.get('name')
    self.phone = data.get('phone')
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()
    self.deleted = False
      

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    # db.session.delete(self)
    self.deleted = True
    db.session.commit()

  @staticmethod
  def get_all_contacts():
    return ContactModel.query.filter_by(deleted=False)

  @staticmethod
  def get_one_contact(id):
    return ContactModel.query.get(id)


  @staticmethod
  def get_one_contact_number(phone_number):
    exists = db.session.query(db.exists().where(ContactModel.phone == phone_number).where(ContactModel.deleted == False)).scalar()
    return exists

  
  def __repr(self):
    return '<id {}>'.format(self.id)


class ContactSchema(Schema):
  """
  Contact Schema
  """
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)
  phone = fields.Str(required=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)
  deleted = fields.Boolean(dump_only=True)

  class Meta:
        unknown = EXCLUDE