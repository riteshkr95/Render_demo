from  flask import Flask ,render_template ,request
import joblib
model=joblib.load("model.pkl")
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/submit" ,methods=["post"])

def sumbit():
    a=eval(request.form.get("%Red Pixel"))
    b=eval(request.form.get("%Green pixel"))
    c=eval(request.form.get("%Blue pixel"))
    d=eval(request.form.get("Hb"))

    prediction=model.predict([[a,b,b,c]])

    if prediction[0]==0:
        return "you are safe"
    else:
        return "you are not safe"




app.run(debug=True)

