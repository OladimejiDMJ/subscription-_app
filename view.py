from flask import Flask, request, jsonify, make_response
from .model import User,Subscriptions
@app.route('/subscriptions', methods = ['POST'])
def create_subscriptions():
    data=request.json()
    newSubscription=Subscriptions(data['subscribed_to_user'],data['subscribing_user'],data['begin_date'],data['end_date'])
    db.session.add(newSubscription)
    db.session.commit()
    if db:
        return make_response(jsonify({"Response":"Success"}),200)
    else:
        

@app.route('/subscriptions/<user_id>', methods = ['GET'])
def get_all_subscriptions(user_id):
    user=Subscriptions.query.filter_by(subscribing_user=user_id)
    







