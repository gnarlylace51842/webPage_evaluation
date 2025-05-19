from flask import Flask, render_template, redirect, request, flash
from bson.objectid import ObjectId
import time
import os
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://dylanashraf56014:F0kXD9K5XZpZ2cdf@cluster0.iigar.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

app = Flask(__name__)
app.secret_key = "random"

db = client.identification
person = db.person

@app.route("/")
def start():
    return render_template("webPage.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = {}
    full_name = request.form.get("full_name", "").strip()
    DateOB = request.form.get("DOB", "").strip()
    email = request.form.get("email", "").strip()
    phone_number = request.form.get("phone_number", "").strip()
    address = request.form.get("address", "").strip()

    data["full_name"]=full_name
    data["DOB"]=DateOB
    data["email"]=email
    data["phone_number"]=phone_number
    data["address"]=address

    if any(value == "" for value in data.values()):
        flash("One of your textboxes is missing information!")
        return redirect("/")
    
    if person.find_one({"email": email}):
        flash("Duplicate detected!")
        return redirect("/")
    
    person.insert_one(dict(request.form))
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True, port=8000)