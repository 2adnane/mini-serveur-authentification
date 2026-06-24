from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Clé secrète utilisée pour signer les cookies de session
app.secret_key = "changez-cette-cle-secrete"

# Base d'utilisateurs (à des fins pédagogiques uniquement)
USERS = {
    "admin": "admin123",
    "etudiant": "fstt2026",
}


@app.route("/")
def index():
    if session.get("user"):
        return redirect(url_for("welcome"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if username in USERS and USERS[username] == password:
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            error = "Identifiants invalides. Veuillez reessayer."

    return render_template("login.html", error=error)


@app.route("/welcome")
def welcome():
    if not session.get("user"):
        return redirect(url_for("login"))

    return render_template("welcome.html", user=session["user"])


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    # host=0.0.0.0 : accessible depuis tout le reseau local
    app.run(host="0.0.0.0", port=5000, debug=True)