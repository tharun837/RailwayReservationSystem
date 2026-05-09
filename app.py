from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    train = request.form['train']
    return render_template('booking.html', name=name, train=train)


@app.route('/confirm', methods=['POST'])
def confirm():
    name = request.form['name']
    train = request.form['train']
    return render_template('confirmation.html', name=name, train=train)


if __name__ == '__main__':
    app.run(debug=True)