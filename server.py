from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    form = request.form
    print(form)
    count = int(form['strawberry']) + \
        int(form['raspberry']) + int(form['apple'])
    print(
        f'Charging {form["first_name"]} {form["last_name"]} for {count} fruits')
    return render_template("checkout.html", form=form)


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
