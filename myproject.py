from flask import *
from DBM import addEmp,selectAllEmp,deleteEmp,selectEmpById,updateEmp,userPass
app = Flask(__name__)

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/log",methods=["POST"])
def user_log():
    email=request.form["email"]
    password=request.form["passw"]
    d=userPass()
    if((email,password)in d):
        return redirect("/emplist")
    else:
        return redirect("/reg")
    
@app.route("/home")    
def home():
    return render_template("home.html")


@app.route("/reg")
def register():
    return render_template("register.html")


@app.route("/emplist")
def emplist():
    d=selectAllEmp()
    return render_template("records.html",elist=d)
@app.route("/addEmp" , methods=["POST"])
def add_emp():
    ids=request.form["id"]
    name=request.form["name"]
    contact=request.form["contact"]
    email=request.form["email"]
    passw=request.form["pass"]
    t=(ids,name,contact,email,passw)
    addEmp(t)
    
    return redirect("/home")

@app.route("/deleteEmp")
def delete_emp():
    ids=request.args.get("id")
    deleteEmp(ids)
    return redirect("/emplist")

@app.route("/updateEmp")
def update():
    id=request.args.get('id')
    d=selectEmpById(id)
    return render_template("update.html",u=d)

@app.route("/updateEmp",methods=["POST"])
def update_emp():
    ids=request.form["id"]
    name=request.form["name"]
    contact=request.form["contact"]                 
    email=request.form["email"]                 
    passw=request.form["pass"]

    t=(name,contact,email,passw,ids)
    updateEmp(t)

    return redirect("/emplist")


   
if(__name__=="__main__"):
    app.run(debug=True)
    
