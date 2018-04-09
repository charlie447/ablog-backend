from flask import Flask, url_for,json,Response,request

app = Flask(__name__)
user = {
        'username':'admin',
        'password':'admin123'
        }
@app.route('/api/user/getUser',methods = ['POST','GET'])
def getUser():

    data = json.dumps(user)
    resp = Response(data, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin']= '*'
    resp.headers['Access-Control-Allow-Method']= 'POST,GET'
    return resp

@app.route('/api/user/validation',methods = ['POST'])
def valiadteUser():
    data = request.data
    # data = user
    print(data)
    resp = Response(data, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin']= '*'
    resp.headers['Access-Control-Allow-Method']= 'POST,GET'
    
    return resp

if __name__ == '__main__':
    app.run(debug=True)