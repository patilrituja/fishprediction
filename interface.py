import traceback
from flask import Flask,render_template,jsonify,request
import config
from util import Fish_Market

app = Flask(__name__)

@app.route('/')
def home():

    return render_template("index.html")

@app.route('/prediction')
def prediction():
    try :
        if request.method == "POST":
            data= request.form

            print("User data is :",data)
            
            Length1=eval(data['Length1'])
            Length2=eval(data['Length2'])
            Length3=eval(data['Length3'])
            Height=eval(data['Height'])
            Width=eval(data['Width'])
            Species=data['Species']

            fish_mar=Fish_Market(Length1,Length2,Length3,Height,Width,Species)
            
            weight=fish_mar.get_predicted_weight()
            print(weight)
            #return jsonify ({"Result ": f"Fish Market predicted weight is :{weight}"})
            return render_template('index.html',prediction=weight)
        else :
            data= request.args.get

            print("User data is :",data)

            Length1=eval(data('Length1'))
            Length2=eval(data('Length2'))
            Length3=eval(data('Length3'))
            Height=eval(data('Height'))
            Width=eval(data('Width'))
            Species=data('Species')

            fish_mar=Fish_Market(Length1,Length2,Length3,Height,Width,Species)
            
            weight=fish_mar.get_predicted_weight()
            print(weight)
            #return jsonify ({"Result ": f"Fish Market predicted weight is :{weight}"})
            return render_template('index.html',prediction=weight)


    except :
        print(traceback.print_exc())
        
        return  jsonify({"Message" : "Unsuccessful"})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=config.Port_Number,debug=True)