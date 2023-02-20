from flask import Flask, redirect, render_template, request, url_for
import openai
app = Flask(__name__)
openai.api_key = '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'

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        description = request.form["description"]
        key = request.form["key"]
        if key == "123":
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=description,
                temperature=0.6,
                max_tokens=2048
            )
            return redirect(url_for("index", result=response.choices[0].text))
        else:
            return redirect(url_for("index", result="Wrong key"))

    result = request.args.get("result")
    return render_template("index.html", result=result)