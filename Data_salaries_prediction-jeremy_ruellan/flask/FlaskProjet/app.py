from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
    message = "Welcome to my first flask based web application ... !!!"
    return render_template("home.html", message = message)

@app.route('/getResponseLinearReg',methods=["GET","POST"])
def getResponseLinearReg():
    Title = request.form["Title"]
    Location = request.form["Location"]
    Competences = request.form.getlist('Competences[]')

    experience = False
    anglais = False
    python = False
    sql = False
    azure = False
    spark = False
    dataiku = False
    aws = False
    gcp = False
    spacy = False
    nltk = False
    huggingface = False
    bert = False
    bac1 = False
    bac2 = False
    bac3 = False
    bac4 = False
    bac5 = False
    bac45 = False
    bac34 = False
    tensorflow = False
    torch = False
    pytorch = False
    keras = False
    django = False
    javascript = False
    mongodb = False
    master = False
    postgresql = False
    powerbi = False
    nodejs = False
    node = False
    php = False
    asp = False
    java = False
    c = False
    flutter = False
    dart = False
    flask = False
    mysql = False
    jquery = False
    css = False
    html = False
    xml = False
    sgbd = False
    agile = False
    scrum = False

    for comp in Competences:
        if comp == "Experience":
            experience = True
        elif comp == "Anglais":
            anglais = True
        elif comp == "Python":
            python = True
        elif comp == "SQL":
            sql = True
        elif comp == "Azure":
            azure = True
        elif comp == "Spark":
            spark = True
        elif comp == "Dataiku":
            dataiku = True
        elif comp == "AWS":
            aws = True
        elif comp == "GCP":
            gcp = True
        elif comp == "Spacy":
            spacy = True
        elif comp == "NLTK":
            nltk = True
        elif comp == "HuggingFace":
            huggingface = True
        elif comp == "BERT":
            bert = True
        elif comp == "Bac+1":
            bac1 = True
        elif comp == "Bac+2":
            bac2 = True
        elif comp == "Bac+3":
            bac3 = True
        elif comp == "Bac+4":
            bac4 = True
        elif comp == "Bac+5":
            bac5 = True
        elif comp == "Bac+4/5":
            bac45 = True
        elif comp == "Bac+3/4":
            bac34 = True
        elif comp == "TensorFlow":
            tensorflow = True
        elif comp == "Torch":
            torch = True
        elif comp == "PyTorch":
            pytorch = True
        elif comp == "Keras":
            keras = True
        elif comp == "Django":
            django = True
        elif comp == "Javascript":
            javascript = True
        elif comp == "MongoDB":
            mongodb = True
        elif comp == "Master":
            master = True
        elif comp == "PostgreSQL":
            postgresql = True
        elif comp == "PowerBI":
            powerbi = True
        elif comp == "Nodejs":
            nodejs = True
        elif comp == "Node":
            node = True
        elif comp == "PHP":
            php = True
        elif comp == "ASP":
            asp = True
        elif comp == "Java":
            java = True
        elif comp == "C++":
            c = True
        elif comp == "Flutter":
            flutter = True
        elif comp == "Dart":
            dart = True
        elif comp == "Flask":
            flask = True
        elif comp == "mySQL":
            mysql = True
        elif comp == "Jquery":
            jquery = True
        elif comp == "CSS":
            css = True
        elif comp == "HTML":
            html = True
        elif comp == "XML":
            xml = True
        elif comp == "SGBD":
            sgbd = True
        elif comp == "Agile":
            agile = True
        elif comp == "Scrum":
            scrum = True

    inputList = [float(Title), float(Location), experience, anglais, python, sql, azure, 
                spark, dataiku, aws, gcp, spacy, nltk, huggingface, bert, bac1, bac2, bac3,
                bac4, bac5, bac45, bac34,tensorflow, torch, pytorch, keras, django, javascript,
                mongodb, master, postgresql, powerbi, nodejs, node, php, asp, java, c, flutter,
                dart, flask, mysql, jquery, css, html, xml, sgbd, agile, scrum]

    with open("static/finalized_model_final.sav", 'rb') as file:
            pickle_model = pickle.load(file)
            y_pred_from_pkl = pickle_model.predict([inputList])
    print(y_pred_from_pkl)

    print("Voici le titre == " + Title)
    print("Voici la location == " + Location)
    print("Voici les compétences == " + str(Competences))
    print("Voici la inputList == " + str(inputList))

    return f'[ {str(round(y_pred_from_pkl[0]-3904, 2))} , {str(round(y_pred_from_pkl[0]+3904, 2))} ] € par an'

if __name__ == '__main__':
    app.run(debug=True)