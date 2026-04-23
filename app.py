from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "kha_secret_key"

# Tạo OTP
def create_otp():
    return str(random.randint(100000, 999999))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        otp = create_otp()
        session["otp"] = otp

        print("OTP của bạn là:", otp)  # không cần Gmail

        return "OTP đã tạo, kiểm tra console/log"

    return render_template("index.html")


@app.route("/verify", methods=["POST"])
def verify():
    user_otp = request.form.get("otp")

    if user_otp == session.get("otp"):
        return "✅ OTP đúng"
    else:
        return "❌ OTP sai"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
