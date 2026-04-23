from flask import Flask, request, redirect, session
from flask_mail import Mail, Message
import random

app = Flask(__name__)
app.secret_key = "secret123"

# cấu hình Gmail gửi mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ht571977@gmail.comN'
app.config['MAIL_PASSWORD'] = 'gpqw emgr ncly imyk'

mail = Mail(app)

# trang nhập email
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        otp = str(random.randint(100000,999999))

        session["otp"] = otp
        session["email"] = email

        msg = Message(
            "Mã OTP đăng nhập",
            sender=app.config['MAIL_USERNAME'],
            recipients=[email]
        )
        msg.body = f"Mã OTP của bạn là: {otp}"

        mail.send(msg)
        return redirect("/verify")

    return '''
    <h2>Đăng nhập bằng Email</h2>
    <form method="post">
        <input name="email" placeholder="Nhập email">
        <button>Gửi OTP</button>
    </form>
    '''

# trang nhập OTP
@app.route("/verify", methods=["GET","POST"])
def verify():
    if request.method == "POST":
        if request.form["otp"] == session.get("otp"):
            return f"Đăng nhập thành công: {session.get('email')} 🎉"
        else:
            return "Sai OTP ❌"

    return '''
    <h2>Nhập OTP</h2>
    <form method="post">
        <input name="otp">
        <button>Xác nhận</button>
    </form>
    '''

app.run(host="0.0.0.0", port=5000)
