from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(message="Invalid email address."), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(message='Field must be at least 8 characters long'), Length(min=8)])
    submit = SubmitField(label="Log In")

app = Flask(__name__)
app.secret_key = "Kurban"  # adding some secret random key
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html", form=login_form)
        else:
            return render_template("denied.html", form=login_form)
        # return render_template('success.html', form=login_form)
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)

