import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data
accounts = {
    'admin': 'adminPass',
    'user': 'userPass',
}


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Credetial Stuffing</h1>
<p>A prototype login API to be cracked using credential stuffing.</p>'''


# Login endpoint
@app.route('/login', methods=['GET'])
def api_all():
    query_parameters = request.args

    username = query_parameters.get('username')
    password = query_parameters.get('password')

    print username, password

    # if accounts[username] in accounts.keys() and accounts[username] == ascii(password):
    if username in accounts.keys() and password == accounts[username]:
        print "SUCCESS"
        return "SUCCESS"

    print "FAIL"
    return "FAIL"


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
