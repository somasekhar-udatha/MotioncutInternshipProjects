from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=12):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    if length < 4:
        print("Password length should be at least 4.")
        return

    password = (
        random.choice(uppercase_letters)
        + random.choice(lowercase_letters)
        + random.choice(digits)
        + random.choice(special_characters)
        + ''.join(random.choice(all_characters) for _ in range(length - 4))
    )
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)

    return shuffled_password

def generate_multiple_passwords(num_passwords, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    password_length = int(request.form.get("password_length"))
    num_passwords = int(request.form.get("num_passwords"))
    passwords = generate_multiple_passwords(num_passwords, password_length)
    return render_template("index.html", passwords=passwords)

if __name__ == "__main__":
    app.run(debug=True)
