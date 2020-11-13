from flask import Flask, request, render_template
from webApp import app, forms

@app.route('/',methods=["GET","POST"])
def index():
    myForm = forms.myForm(request.form)
    if request.method == "POST":
        sentence = request.form["text_area"] #input provided by user 

        lang, conf = forms.detectLanguageUserSent(sentence)

        return render_template("answer.html", language = lang, confidence = conf)

    return render_template("search.html", form = myForm)