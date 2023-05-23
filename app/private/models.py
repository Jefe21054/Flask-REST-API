from app import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    professor = db.Column(db.String(64), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(256), nullable=False)
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Course.query.all()

    @staticmethod
    def get_by_id(id):
        return Course.query.get(id)
