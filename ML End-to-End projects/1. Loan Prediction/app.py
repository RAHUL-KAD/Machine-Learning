from flask import Flask, render_template, request
import pickle
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def submit():
    if request.method == 'POST':
        income = int(request.form["income"])
        loan = int(request.form["loan ammount"])
        credit = int(request.form["credit"])
        education = int(request.form["education"])
        employment = int(request.form["employment"])
        married = int(request.form["married"])
        gender = int(request.form["gender"])
        with open('my_model', 'rb') as f:
            model = pickle.load(f)

        result = model.predict(
            [[income, loan, credit, education, employment, married, gender]])
        if result[0] == 'Y':
            return render_template('index.html',
                                   data=['Yes you can get a loan'])
        else:
            return render_template('index.html',
                                   data=['Sorry, you can\'t get a loan'])
    else:
        return 'Something went wrong'


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
