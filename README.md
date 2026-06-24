J'ai un projet Flask sur Raspberry Pi qui s'appelle webauth. Voici la version de base du fichier app.py :
pythonfrom flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "changez-cette-cle-secrete"
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
    app.run(host="0.0.0.0", port=5000, debug=True)
Je veux que tu modifies ce projet pour ajouter toutes ces fonctionnalités :

Hachage des mots de passe avec werkzeug (generate_password_hash et check_password_hash)
Afficher la date et l'heure de connexion dans la page welcome (passer login_time au template)
Ajouter un 3ème utilisateur appelé adnane avec le mot de passe fstt2026
Bloquer après 3 tentatives échouées avec un message indiquant le nombre de tentatives restantes
Bonus : stocker les utilisateurs dans un fichier users.json au lieu du dictionnaire codé en dur — créer aussi un script séparé create_users.py qui génère ce fichier avec les mots de passe déjà hachés

Donne-moi :

Le fichier app.py complet et final
Le fichier create_users.py
La ligne à ajouter dans welcome.html pour afficher la date/heure

Le projet utilise Python 3, Flask, et tourne sur Raspberry Pi OS.
