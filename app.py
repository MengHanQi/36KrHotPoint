from flask import Flask
from flask import jsonify
from flask import render_template
from analysis import *

data_lst = read_data()
companies = get_company()
places = get_place()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/company')
def company():
    data = get_company_occur_count(data_lst, companies)
    data = sorted(data.items(), key=lambda x:x[1], reverse = True)
    names = [item[0] for item in data]
    values = [item[1] for item in data]
    return jsonify({"names":names, "values": values})

@app.route('/place')
def place():
    data = get_place_occur_count(data_lst, places)
    data = sorted(data.items(), key=lambda x:x[1], reverse = True)
    names = [item[0] for item in data]
    values = [item[1] for item in data]
    return jsonify({"names":names, "values": values})

@app.route('/date')
def date():
    data = count_by_date(data_lst)
    sorted_data = sorted(data.items(), key=lambda x:x[0])
    days = [item[0] for item in sorted_data]
    values = [item[1] for item in sorted_data]
    return jsonify({"days":days, "values":values})

if __name__ == '__main__':
    app.debug = True
    app.run()