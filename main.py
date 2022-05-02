from flask import Flask, jsonify,render_template,Response,request,redirect

from heart_failure import decision

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def myRandom():
    return render_template("/index.html")

global sonuc
@app.route('/answer', methods=['GET','POST'])
def post():  
    if(request.method=='POST'):
            global sonuc
            data = request.get_json()
            karar= decision(data=data)
            sonuc=karar
            

    return jsonify({'message': "başarılı"})

@app.route('/result', methods=['GET','POST'])
def result():  
    global sonuc
    print(sonuc)
    return sonuc

if __name__ == '__main__':
    app.run(debug=True, port=5000)