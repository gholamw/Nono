from wtforms import Form, RadioField
from wtforms import StringField, PasswordField, FileField, BooleanField, TextAreaField, IntegerField, DateTimeField, DecimalField,SelectField,SelectMultipleField,DateField,SubmitField,HiddenField,TextField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.fields.html5 import EmailField
from app import models, db
from app.models import User
from wtforms.widgets import Input
from wtforms.widgets.core import html_params
from wtforms.widgets import HTMLString
from wtforms.validators import InputRequired



class InlineButtonWidget(object):
    """
    Render a basic ``<button>`` field.
    """
    input_type = 'button'
    html_params = staticmethod(html_params)

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', self.input_type)
        kwargs.setdefault('value', field.label.text)
        return HTMLString('<button %s>' % self.html_params(name=field.name, **kwargs))


class InlineSubmitField(BooleanField):
    """
    Represents an ``<button type="submit">``.  This allows checking if a given
    submit button has been pressed.
    """
    widget = InlineButtonWidget()




#myChoices = ["Branch 1", "Branch 2"]
myChoices = [('Branch 1','Branch 1'), ('Branch 2','Branch 2')]
myChoices1 = [('فرع كيلو 8','فرع كيلو 8'), ('فرع الجوهرة','فرع الجوهرة')]

#invoiceCategories = ["single"]
#invoiceCategories = ["جملة ", "جملة  الجملة ", "تجزئة "]
#invoiceCategories =[('aim', 'AIM'), ('msn', 'MSN')]
#invoiceCategories =[('', ''), ('', ''), ('', '')]
invoiceCategories =[('Single', 'Single'), ('Bulk', 'Bulk'), ('Bulk Bulk', 'Bulk Bulk')]

invoiceType = [('نقد', 'نقد')]
transactionType = [('خصم','خصم')]
#invoiceType = ["نقد", "دين"]
#transactionType = ["خصم" , "ايداع"]

class LoginForm(Form):
    username = StringField('اسم المستخدم:', validators=[DataRequired()])
    password = PasswordField('الرقم السري:', validators=[DataRequired()])
    submit = SubmitField('تسجيل الدخول')

class AddProductForm(Form):
	name = StringField('اسم الصنف:', validators=[DataRequired()])
	bulk_price = DecimalField('سعر الجملة:', validators=[DataRequired()])
	bulk_bulk_price = DecimalField('سعر جملة الجملة:', validators=[DataRequired()])
	single_price = DecimalField('سعر التجزئة:', validators=[DataRequired()])
	single_expense = DecimalField('تكلفة الصنف التجزئة', validators=[DataRequired()])
	bulk_bulk_expense = DecimalField('تكلفة الصنف جملة الجملة', validators=[DataRequired()])
	bulk_expense = DecimalField('تكلفة الصنف الجملة', validators=[DataRequired()])
	shelf = StringField('رقم الدرج:', validators=[DataRequired()])
	quantity = IntegerField('كمية الصنف:', validators=[DataRequired()])
	submit = SubmitField('اضافة الصنف')

class AddCustomerForm(Form):
	name = StringField('اسم العميل:', validators=[DataRequired()])
	mobile = StringField('رقم الجوال:', validators=[DataRequired()])
	submit = SubmitField('اضافة العميل')

class AmendProductForm(Form):
	id_number = HiddenField('ID:', validators=[DataRequired()])
	name = StringField('اصم الصنف:', validators=[DataRequired()])
	bulk_price = DecimalField('سعر الجملة:', validators=[DataRequired()])
	bulk_bulk_price = DecimalField('سعر جملة الجملة:', validators=[DataRequired()])
	single_price = DecimalField('سعر التجزئة:', validators=[DataRequired()])
	single_expense = DecimalField('تكلفة الصنف التجزئة', validators=[DataRequired()])
	bulk_bulk_expense = DecimalField('تكلفة الصنف جملة الجملة', validators=[DataRequired()])
	bulk_expense = DecimalField('تكلفة الصنف الجملة', validators=[DataRequired()])
	shelf = StringField('Product Shelf:', validators=[DataRequired()])
	quantity = IntegerField('كمية الصنف', validators=[DataRequired()])
	submit = SubmitField('تعديل الصنف')


class SearchForm(Form):
    autocomp = TextField('اختر صنف', id='autocomplete')

class SellCash(Form):
	inv_category = SelectField(u'اختر نوع الفاتورة', choices = invoiceCategories)
	autocompcustomer = TextField('اختر عميل', id='autocompletecustomer')
	autocomp = TextField('اختر صنف', id='autocomplete')
	price = DecimalField('سعر الصنف:', validators=[DataRequired()])
	quantity = IntegerField('كمية الصنف:', validators=[DataRequired()])
	submit = SubmitField('اضافة الصنف')
	clear = SubmitField('مسح جميع الاصناف')
	confirm = SubmitField('انشاء فاتورة')
	get_price = SubmitField('تحقق من سعر الصنف')

class SellLoan(Form):
	inv_category = SelectField(u'اختر نوع الفاتورة', choices = invoiceCategories)
	autocompcustomer = TextField('اختر العميل', id='autocompletecustomer')
	autocomp = TextField('اختر الصنف', id='autocomplete')
	price = DecimalField('سعر الصنف:', validators=[DataRequired()])
	available_quantity = IntegerField('الكمية الموجودة في الفرع:', validators=[DataRequired()])
	quantity = IntegerField('كمية الصنف:', validators=[DataRequired()])
	submit = SubmitField('اضف الصنف')
	clear = SubmitField('مسح جميع الاصناف')
	confirm = SubmitField('انشاء فاتورة')
	get_price = SubmitField('الحصول على سعر الصنف')

class MoveStock(Form):
	autocomp = TextField('اختر الصنف', id='autocomplete')
	checking = TextField('كمية الصنف المتاحة:', validators=[DataRequired()])
	branch = SelectField(u'اختر الفرع', choices = myChoices)
	number = TextField('الكمية المتاحة:', validators=[DataRequired()])
	check = SubmitField('الكمية المتوفر')
	submit = SubmitField('تاكيد المناقلة')


class MoveStockAdmin(Form):
	autocomp = TextField('اختار الدرج', id='autocomplete')
	branch = SelectField(u'اختر الفرع', choices = myChoices1)
	quantity = IntegerField('كمية الصنف:', validators=[DataRequired()])
	submit = SubmitField('تاكيد المناقلة')


class MoveStockAdminShelf(Form):
	autocomp = TextField('ادخل رقم الدرج', id='autocomplete')
	branch = SelectField(u'اختر الفرع', choices = myChoices1)
	products = SelectField(u'اختر الصنف', choices = {})
	quantity = IntegerField('كمية الصنف:', validators=[DataRequired()])
	submit = SubmitField('تاكيد المناقلة')
	check = SubmitField('عرض الاصناف')


class Sadad(Form):
	invoice_id = TextField('رقم الفاتورة', id='autocomplete')
	remianing_balance = DecimalField('المبلغ المتبقي للسداد:', validators=[DataRequired()])
	pay_amount = DecimalField('مبلغ السداد:', validators=[DataRequired()])
	submit = SubmitField('تاكيد السداد')

def my_length_check(form, field):
    print("INSIDE VALIDATION CHECK")
    if len(field.data) <= 0:
        raise ValidationError('Field must be less than 50 characters')


class CreateUser(Form):
	username = StringField('ادخل اسم المستخدم:', validators=[InputRequired(),my_length_check])
	password = TextField('ادخل الرقم السري:', validators=[DataRequired()])
	#example = RadioField('Label', choices=[('value','description'),('value_two','whatever')])
	admin = BooleanField('ادمن', validators=[DataRequired(), ])
	admin_alike = BooleanField('شبه الادمن', validators=[DataRequired(), ])
	warehouse = BooleanField('مستودع', validators=[DataRequired(), ])
	branch1 = BooleanField('الفرع الاول', validators=[DataRequired(), ])
	branch2 = BooleanField('الفرع الثاني', validators=[DataRequired(), ])

	submit = SubmitField('اضافة مستخدم جديد')

class EditVAT(Form):
	percentage = DecimalField('قيمة الضريبة المضافة:', validators=[DataRequired()])
	submit = SubmitField('تعديل قيمة الضريبة المضافة')

class Spendings(Form):
	invoice_type = SelectField(u'اختر نوع الفاتورة', choices = invoiceType) # Cash, Loan
	transaction_type = SelectField(u'اختر نوع العملية', choices = transactionType) # DR, CR
	description = StringField('وصف العملية', validators=[InputRequired(),my_length_check])
	pay_amount = DecimalField('المبلغ', validators=[DataRequired()])
	submit = SubmitField('انشاء العملية ')

class Procurement(Form):
	autocompcustomer = TextField('اختر عميل', id='autocompletecustomer')
	description = StringField('وصف العملية', validators=[InputRequired(),my_length_check])
	pay_amount = DecimalField('المبلغ', validators=[DataRequired()])
	submit = SubmitField('انشاء العملية ')
	invoices = 	SubmitField('اختيار الفواتير')
	invoices_to_choose = SelectField(u'اختر الفواتير', choices=[])


class Refund(Form):
	refund_type = RadioField('نوع الاسترجاع', choices=[('Full','استرجاع كامل الفاتورة'),('Partial','استرجاع جزء من مبلغ الفاتورة')])
	refund_products = SelectField(u'Select Refund Product', choices=[])
	refund_amount = DecimalField('الكمية المراد استرجاعها', validators=[DataRequired()])
	submit = SubmitField('تنفيذ امر استرجاع المبلغ للعميل')

class RevenueAccount(Form):
		balance = DecimalField('الرصيد الحالي', validators=[DataRequired()])

class VATAccount(Form):
		balance = DecimalField('الرصيد الضريبي الحالي ', validators=[DataRequired()])