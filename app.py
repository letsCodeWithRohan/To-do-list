from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = ''
app.config["MYSQL_DB"] = 'posts'

mysql = MySQL(app)

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM tasks ORDER BY created_at DESC")
        data = cursor.fetchall()
        cursor.close()
        return render_template("index.html",data=data)
    else:
        task = request.form["task"]
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO tasks (title) VALUES (%s)",(task,))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for("index"))
    
@app.route("/delete/<int:id>")
def delete(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s",(id,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for("index"))

@app.route("/complete/<int:id>")
def complete(id):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE tasks SET status = 'complete' WHERE id = %s",(id,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for("index"))

@app.route("/pending/<int:id>")
def pending(id):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE tasks SET status = 'pending' WHERE id = %s",(id,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for("index"))

@app.route("/edit/<int:id>/")
def edit(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id,title FROM tasks WHERE id = %s",(id,))
    data = cursor.fetchone()
    cursor.close()
    return render_template("edit.html",data = data)
        
@app.route("/edit_task",methods=["GET","POST"])
def edit_task():
    if request.method == "POST":
        data = request.form
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE tasks SET title = %s WHERE id = %s",(data["task"],data["id"]))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for("index"))
        
        

if __name__ == "__main__":
    app.run(debug=True)