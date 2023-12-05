from flask import Flask, render_template, request, redirect
from os import getenv
from views.contacts import contacts
from models import db, Product
from flask_migrate import Migrate
from forms import CreateProductForm

secret_key = getenv('SECRET_KEY', 'development key')

DEFAULT_DB_URI = 'postgresql+psycopg2://otus:otus123@localhost:5432/shop'
database_uri = getenv('SQLALCHEMY_DATABASE_URI', DEFAULT_DB_URI)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

print('SECRET_KEY', secret_key)
print('SQLALCHEMY_DATABASE_URI', database_uri)

app.config['SECRET_KEY'] = secret_key
app.register_blueprint(contacts)
db.init_app(app)
migrate = Migrate(app, db)


@app.cli.command("create-db")
def create_user():
    db.create_all()


@app.route("/")
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)


@app.route('/product/<int:product_id>/')
def product_detail(product_id):
    # product = Product.query.filter_by(id=product_id).first_or_404()
    product = Product.query.get_or_404(product_id)
    # if product is None:
    #     raise NotFound
    return render_template('product.html', product=product)


@app.route('/product/create/', endpoint='create', methods=['GET', 'POST'])
def product_create():
    # if request.method == 'GET':
    #     return render_template('create.html')
    #
    # name = request.form.get('product-name')
    # product = Product(name=name)
    # db.session.add(product)
    # db.session.commit()
    # return redirect('/')
    form = CreateProductForm()
    if form.validate_on_submit():
        name = form.name.data
        product = Product(name=name)
        db.session.add(product)
        db.session.commit()
        return redirect('/')
    return render_template('create.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
