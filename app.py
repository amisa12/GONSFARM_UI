# import pymysql
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


from flask import request

@app.route('/registration', methods=['POST', 'GET'])
def registration():

    return render_template('registration.html')


@app.route('/registrationDetails', methods=['POST', 'GET'])
def registrationDetails():
    if request.method == 'POST':
        result = request.form
        print(result)
        first_name = result['first_name']
        last_name = result['last_name'],
        d_o_b = result['d_o_b']
        id_number = result['id_number']
        marital_status = result['marital_status']
        phone_number = result['phone_number']
        farm_size = result['farm_size']
        farm_location = result['farm_location']
        crop = result['crop']
        other_source_of_income = result['other_source_of_income']
        farming_purpose = result['farming_purpose']
        tc_accepted = result['tc_accepted']

        payload = {
                "first_name": first_name,
                "last_name": last_name,
                "d_o_b": d_o_b,
                "id_number": id_number,
                "marital_status": marital_status,
                "phone_number": phone_number,
                "farm_size": farm_size,
                "farm_location": farm_location,
                "crop": crop,
                "other_source_of_income": other_source_of_income,
                "farming_purpose": farming_purpose,
                "salary": 1 if other_source_of_income else 0,
                "tc_accepted": 1 if tc_accepted == 'on' else 0
        }
        print(payload)
        response = requests.post('http://79eee7a3.ngrok.io/api/register', json=payload)
        print(response.status_code)
        return render_template("result.html", result=result)


@app.route('/search', methods=['POST', 'GET'])
def search():

    #     id_number = request.form['id_number']
    #
    #     con = pymysql.connect("localhost", "root", "", "angiedb")
    #     cursor = con.cursor()
    #
    #     sql = "SELECT * FROM registration WHERE id_number = %s"
    #     try:
    #         cursor.execute(sql, (id_number))
    #         rows = cursor.fetchall()
    #         if cursor.rowcount == 0:
    #             return render_template('search.html', msg="No records")
    #         else:
    #             return render_template('search.html', data=rows)
    #     except:
    #         return render_template('search.html', msg="Something went wrong")
    #
    # else:

    return render_template('search.html')


@app.route('/visualize', methods=['POST', 'GET'])
def visualize():
    return render_template('visualization.html')

if __name__ == '__main__':
    app.run()
