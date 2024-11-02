from flask import request, jsonify
from config import app, db
from models import Contact


# Request type: GET, POST, PATCH, DELETE
# json: {}

# Response status: 200/success
# json: {}
@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})


# localhost:5000/create_contact
# Create:
# - first_name
# - middle_name
# - last_name
# - email
# - student_number
@app.route("/create_contacts", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    middle_name = request.json.get("middleName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    student_number = request.json.get("studentNumber")

    if not first_name or not last_name or not email:
        return (
            jsonify({
                        "message": "You must include a first name, last name and email"}),
            400,
        )

    new_contact = Contact(first_name=first_name, middle_name=middle_name,
                          last_name=last_name, email=email, student_number=student_number)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "User created!"}), 201


@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404

    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.middle_name = data.get("middleName", contact.middle_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)
    contact.student_number = data.get("studentNumber", contact.student_number)

    db.session.commit()

    return jsonify({"message": "Usr updated."}), 200


@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted!"}), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
