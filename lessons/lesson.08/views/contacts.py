from flask import Blueprint, render_template


contacts = Blueprint('contacts', __name__, url_prefix='/contacts')
# contacts = Blueprint('contacts', __name__)

ADMIN_EMAIL = 'admin@admin.com'


@contacts.route("/contacts/")
def contact():
    return render_template('contact.html', admin_email=ADMIN_EMAIL)