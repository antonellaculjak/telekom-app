from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cjenik")
def rent():
    return render_template("cjenik.html")

@app.route("/naruci", methods=["POST"])
def naruci():
    ime = request.form.get("ime")
    telefon = request.form.get("telefon")
    adresa = request.form.get("adresa")
    mobiteli = request.form.get("mobiteli")
    tarife = request.form.get("tarife")

    return render_template("naruci.html", ime=ime, telefon=telefon, adresa=adresa, jelo=jelo)


if __name__ == '__main__':
    app.run()


