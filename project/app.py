from application import app, db
from os import getenv
from flask import Flask, render_template


if __name__ == "__main__":
     
    
    if getenv("CREATE_SCHEMA") != None:
        if getenv("CREATE_SCHEMA").lower() == "true":
            db.drop_all()
            db.create_all()
            
    app.run(debug=True, host="0.0.0.0", port=5000) 