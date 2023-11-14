from flask import Flask,render_template,request,jsonify
import pymongo

app = Flask("__name__")

@app.route("/",methods = ['GET','POST'])
def homePage():
    return  render_template("index.html")


@app.route('/find', methods = ['POST'])
def search():
   if(request.method=='POST'):
    name = request.form['bookName']
    client = pymongo.MongoClient('mongodb+srv://chiraghira39:Chirag29@cluster0.ihkprpp.mongodb.net/?retryWrites=true&w=majority')
    DataBase = client["Books"]
    coll_book = DataBase['Book_Detail']
    detail = coll_book.find_one({'Book':name})


    return render_template ('Book_Detail.html',id=detail['_id'],name=detail['Book'],Price=detail['Price'],Ava=detail['Stock_Ava'])



if __name__ =="__main__":
     app.run(host = '0.0.0.0')
