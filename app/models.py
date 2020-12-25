from app import db
from wtforms import Form, StringField, TextAreaField, PasswordField, DateField, validators, DateTimeField
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship, backref
from flask_login import login_user, logout_user, current_user, login_required, LoginManager



#Many-To-Many
#users_in_mailing_list = db.Table('emails_in_mailing_list',
#    db.Column('user', db.Integer, db.ForeignKey('user.id')),
#    db.Column('mailing_list', db.Integer, db.ForeignKey('mailing_list.id'))
#)

#association_table = db.Table('items_users',
#    db.Column('user', db.Integer, db.ForeignKey('user.id')),
#    db.Column('mailing_list', db.Integer, db.ForeignKey('mailing_list.id'))
#)

#keep save
#class Recipient(db.Model):
#    __tablename__ = 'recipient'
#    user_id = db.Column( db.Integer, db.ForeignKey('user.id'), primary_key=True)
#    mailing_list_id = db.Column( db.Integer, db.ForeignKey('mailing_list.id'), primary_key=True)
#    user = db.relationship("User")

def to_dict(obj, with_relationships=True):
    d = {}
    for column in obj.__table__.columns:
        if with_relationships and len(column.foreign_keys) > 0:
             # Skip foreign keys
            continue
        d[column.name] = getattr(obj, column.name)

    if with_relationships:
        for relationship in inspect(type(obj)).relationships:
            val = getattr(obj, relationship.key)
            d[relationship.key] = to_dict(val) if val else None
    return d


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    hashed_password = db.Column(db.String(128), nullable=False)
    admin = db.Column(db.Boolean, default = False)
    admin_alike = db.Column(db.Boolean, default = False)
    warehouse = db.Column(db.Boolean, default = False)
    branch1 = db.Column(db.Boolean, default = False)
    branch2 = db.Column(db.Boolean, default = False)
    name = db.Column(db.String(25), index=True)
    phone = db.Column(db.String(16))
    branch = db.Column(db.Integer)
    #mailing_list = relationship('Mailing_list', secondary=association_table, lazy='dynamic', backref=backref('user', lazy='dynamic'))
    #mailing_list = relationship("Mailing_list", secondary="users_mailing_list")
    #users_in_mailing_list = db.relationship('Mailing_list', secondary=users_in_mailing_list,
        #backref=db.backref('user'))

    @property
    def is_authenticated(self):
        return True

    def is_active(self):   
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % (self.username)

# Customer - Invoice is one to many relationship, customer can have many invoices but invoice can only be assigned to one customer. 

# Invoice - Product is many to many relationship, invoice can have many products, and product can be assigned to many invoices. produces middleware table can be
# invoice_identifier [Done]  

# Invoice - Transaction is one to one relationship, each invoice is associated with only one transaction(CR,DR, or Non-financial treatment).[Done]

# Column balance to be added in Transaction table [Done]
# Column pay type (p_type) [cash or loan] to be added in Transaction table [Done]
# Column is_modifies to be added to invoice table. It identifies if someone has modified certain invoice or not (Defalut is NO) [Done]



invoice_identifier = db.Table('invoice_identifier',
    db.Column('invoice_id', db.Integer, db.ForeignKey('invoices.invoice_id')),
    db.Column('product_id', db.Integer, db.ForeignKey('products.product_id'))
)

class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True,unique=True)
    bulk_price = db.Column(db.Float)
    bulk_bulk_price = db.Column(db.Float)
    single_price = db.Column(db.Float)
    single_expense = db.Column(db.Float)
    bulk_bulk_expense = db.Column(db.Float)
    bulk_expense = db.Column(db.Float)
    shelf = db.Column(db.String(64))
    quantity = db.Column(db.Integer)
    invoices = db.relationship("Invoice",
                               secondary=invoice_identifier)
    def __init__(self,name,bulk_price,bulk_bulk_price,single_price, shelf, quantity,invoices = []):
        self.name = name
        self.bulk_price = bulk_price
        self.bulk_bulk_price = bulk_bulk_price
        self.single_price = single_price
        self.shelf = shelf
        self.quantity = quantity
        self.invoices = invoices

class Invoice(db.Model):
    __tablename__ = 'invoices'
    invoice_id = db.Column(db.Integer, primary_key=True)
    is_modified = db.Column(db.Boolean, default=False)
    products = db.relationship("Product",
                               secondary=invoice_identifier)
    #transaction = db.Column(db.Integer, db.ForeignKey("transaction.id"))
    #transaction = relationship("Transaction", uselist=False, backref="invoice")

    def __init__(self,products = []):
        self.products = products


"""
 
inv_identifier = db.Table('inv_identifier',
    db.Column('invoice_id', db.Integer, db.ForeignKey('invoices.invoice_id')),
    db.Column('product_id', db.Integer, db.ForeignKey('products.product_id'))
)

class Inv(db.Model):
    __tablename__ = 'invoices'
    invoice_id = db.Column(db.Integer, primary_key=True)
    products = db.relationship("Prod",
                               secondary=inv_identifier)


class Prod(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True,unique=True)
    price = db.Column(db.Float)
    shelf = db.Column(db.String(64))
    quantity = db.Column(db.Integer)
    invoices = db.relationship("Inv",
                               secondary=inv_identifier)
                               """




"""
# act as auxiliary table for product and invoice table
product_invoice = db.Table(
    'product_invoice',
    db.Column("product.id", db.Integer, db.ForeignKey("product.id")),
    db.Column("invoice.id", db.Integer, db.ForeignKey("invoice.id"))
)

class Invoice(db.Model):
    __tablename__ = 'invoice'
    id = db.Column(db.Integer, primary_key=True)
    products = db.relationship("Product", secondary=product_invoice)

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True,unique=True)
    price = db.Column(db.Float)
    shelf = db.Column(db.String(64))
    quantity = db.Column(db.Integer)

    """

class BranchOneProduct(db.Model):
    __tablename__ = 'b1product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True,unique=True)
    bulk_price = db.Column(db.Float)
    bulk_bulk_price = db.Column(db.Float)
    single_price = db.Column(db.Float)
    single_expense = db.Column(db.Float)
    bulk_bulk_expense = db.Column(db.Float)
    bulk_expense = db.Column(db.Float)
    shelf = db.Column(db.String(64))
    quantity = db.Column(db.Integer) 

class BranchTwoProduct(db.Model):
    __tablename__ = 'b2product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True,unique=True)
    bulk_price = db.Column(db.Float)
    bulk_bulk_price = db.Column(db.Float)
    single_price = db.Column(db.Float)
    single_expense = db.Column(db.Float)
    bulk_bulk_expense = db.Column(db.Float)
    bulk_expense = db.Column(db.Float)
    shelf = db.Column(db.String(64))
    quantity = db.Column(db.Integer)

class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    t_type = db.Column(db.String(64), index=True) # CR or DR
    total = db.Column(db.Float)
    date = db.Column(db.DateTime)
    description = db.Column(db.String(64))
    balance = db.Column(db.Float)
    p_type = db.Column(db.String(64), index=True) # Cash or Loan
    # relationship
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoices.invoice_id'))

    # define relationship
    invoice = db.relationship('Invoice', backref='invoice')
    #invoice = relationship("Invoice", back_populates="transaction")

    def __init__(self,t_type,total,date, description,balance,p_type):
        self.t_type = t_type
        self.total = total
        self.date = date
        self.description = description
        self.balance = balance
        self.p_type = p_type

class CreditTransaction(db.Model):
    __tablename__ = 'crtransaction'
    id = db.Column(db.Integer, primary_key=True)
    t_type = db.Column(db.String(64), index=True)
    total = db.Column(db.Float)
    date = db.Column(db.DateTime)
    description = db.Column(db.String(64))
    invoice_id = db.Column(db.Integer, db.ForeignKey('inv.id')) 
    current_balance = db.Column(db.Float)  

class DebitTransaction(db.Model):
    __tablename__ = 'drtransaction'
    id = db.Column(db.Integer, primary_key=True)
    t_type = db.Column(db.String(64), index=True)
    total = db.Column(db.Float)
    date = db.Column(db.DateTime)
    description = db.Column(db.String(64))
    invoice_id = db.Column(db.Integer, db.ForeignKey('inv.id'))
    current_balance = db.Column(db.Float)

class Inv(db.Model):
    __tablename__ = "inv"

    id = db.Column(db.Integer, primary_key=True)
    products = db.Column(db.VARCHAR(400))
    vat_value = db.Column(db.Float)
    vat_percentage = db.Column(db.Float)
    total = db.Column(db.Float)
    inv_type = db.Column(db.String(64), index=True) # cash, loan, credit card, or kabs
    status = db.Column(db.String(64), index=True) # paid or not paid
    remaining_balance = db.Column(db.Float)
    is_modified = db.Column(db.Boolean, default=False)
    is_refunded = db.Column(db.Boolean, default=False)
    refund_amount = db.Column(db.Float, default=0.0)
    initiator = db.Column(db.String(64), index=True)
    category = db.Column(db.String(64), index=True) # bulk, bulk bulk, or single
    date = db.Column(db.DateTime)
    is_expense = db.Column(db.Boolean, default=False)
    #customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    #customer = db.relationship("Customer", uselist=False, back_populates="inv")
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'),
        nullable=True)

class Account(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float)
    description = db.Column(db.String(64), index=True,unique=True)


class VAT(db.Model):
    __tablename__ = "vat"
    id = db.Column(db.Integer, primary_key=True)
    vat = db.Column(db.Float)

class Customer(db.Model):
    __tablename__ = "customer"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True,unique=True)
    mobile = db.Column(db.Integer)
    #invoices = db.relationship("Inv", back_populates="customer")
    invoices = db.relationship('Inv', backref='customer', lazy=True)


class Procurement(db.Model):
    __tablename__ = "procurement"
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(64), index=True,unique=True)
    description = db.Column(db.String(64), index=True,unique=True)
    amount = db.Column(db.Float)
    #invoices = db.relationship("Inv", back_populates="customer")    

def init_db():
    print("Initializing DB")
    db.create_all()

    # Create a test user
    #user = User(username="admin", hashed_password="123",admin = True, name = "Abdulrahman Sulimani",
    #phone = "050" , branch = "Kilo 7 Branch")


    #db.session.add(user)
    #db.session.commit()



if __name__ == '__main__':
    init_db()       
