from flask import Flask,jsonify 

app = Flask(__name__)

@app.route('/')
def get_articles():
    return jsonify({"hello":"world"})

if __name__ == "__main__" : 
    app.run(debug=True)
