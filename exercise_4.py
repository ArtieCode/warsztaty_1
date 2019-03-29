from flask import Flask
from flask import request
from flask import render_template



app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def zgadywanka():
    if request.method == 'GET':
        guess = 500
        return render_template("minmax.html", guess=guess, secret_min=1, secret_max=1000)
    else:
        choice = request.form["choice"]
        secret_min = int(request.form["secret_min"])
        secret_max = int(request.form["secret_max"])

        print(choice, secret_min, secret_max)

        old_guess = int((secret_max - secret_min) / 2) + secret_min

        if choice == "za_duzo":
            secret_max = old_guess

        if choice == "za_malo":
            secret_min = old_guess

        if choice == "trafiles":
            return "Hurra! :)"

        new_guess = int((secret_max - secret_min) / 2) + secret_min

        print(choice, new_guess, secret_min, secret_max)

        return render_template("minmax.html",
                               guess=new_guess,
                               secret_min=secret_min,
                               secret_max=secret_max
                               )


app.run()
