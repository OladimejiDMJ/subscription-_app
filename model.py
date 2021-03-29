from app import db
from datetime import datetime
class User( db.Model):
    __tablename__="users"
    id= db.Column( db.Integer, primary_key=True, autoincrement=True)
    username= db.Column( db.String(), index= False, nullable= False)
    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self, username):
      self.username=username
    def __repr__(self):
      return '' % self.username


class Subscriptions ( db.Model):
    id= db.Column( db.Integer, primary_key=True, unique=True)
    subscribing_user= db.Column( db.String, db.ForeingKey('user.id'))
    subscribed_to_user= db.Column( db.String, db.ForeingKey('user.id'))
    begin_date= db.Column( db.DateTime, nullable= False)
    end_date= db.Column( db.DateTime, nullable= False)
    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,subscribing_user,subscribed_to_user,begin_date,end_date):
      self.subscribing_user=subscribing_user
      self.subscribed_to_user=subscribed_to_user
      self.begin_date=begin_date
      self.end_date=end_date
    def __repr__(self):
      return '' % self.id

db.create_all()
