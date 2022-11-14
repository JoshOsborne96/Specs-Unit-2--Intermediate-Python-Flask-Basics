from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from cupcakes import display_cupcakes, find_cupcake, add_cupcake_dict

@app.route('/')
def home():
    cupcakes = display_cupcakes("cupcakes.csv")

    return render_template('index.html', cupcakes=cupcakes)

@app.route('/cupcakes')
def get_all_cupcakes():
    return render_template('cupcakes.html')

@app.route('/add-cupcake/<name>')
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)
    

    if cupcake:
        add_cupcake_dict("order.csv", cupcake=cupcake)
        return redirect(url_for('home'))
    else: 
        return "Cupcake not found1"


@app.route('/individual-cupcake/<name>')
def individual_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if  cupcake:
        return render_template('individual-cupcake.html', cupcake=cupcake)
    else:
        return "Cupcake not found2"

@app.route('/order')
def order():
    cupcakes = display_cupcakes("order.csv")
    order = display_cupcakes("order.csv")
    order_total = round(sum([float(x["price"]) for x in order]),2)

    cupcakes_set = set()

    for cupcake in cupcakes:
        cupcakes_set.add((cupcake['name'], cupcake['price'], cupcakes.count(cupcake)))
    return render_template("order.html", cupcakes=cupcakes_set, order_total=order_total)



if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, port=8000, host= "localhost")