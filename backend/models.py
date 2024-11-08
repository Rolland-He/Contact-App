from config import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    middle_name = db.Column(db.String(80), unique=False, nullable=True)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    student_number = db.Column(db.Integer, unique=True, nullable=True)

    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "middleName": self.middle_name,
            "lastName": self.last_name,
            "email": self.email,
            "studentNumber": self.student_number
        }
