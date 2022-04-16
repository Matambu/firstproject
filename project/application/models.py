from application import db



class ForceUsers(db.Model):
    
    __tablename__ = "ForceUsers"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    power = db.Column(db.String(100), nullable = False)
    masters = db.relationship('Masters', backref = 'mastersbr')
    
    


class Masters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    side = db.Column(db.String(100), nullable = False)
    forceusers_id = db.Column(db.Integer, db.ForeignKey('ForceUsers.id'), nullable = True)
    

    



    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
