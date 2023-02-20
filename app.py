from flask import Flask, redirect, render_template, request, url_for
import openai

app = Flask(__name__)
# openai.api_key = 'sk-BMstis98onIYjVWhM7LxT3BlbkFJqvxWxCLJyYX8GiLZ2QJihmk'


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        description = request.form["description"]
        key = request.form["key"]
        api = request.form["api"]
        gen_type = request.form["type"]
        if key == "123":
            if "sk" in api:
                openai.api_key = api
            text_model = request.form["text_model"]
            if gen_type == 'text':
                response = openai.Completion.create(
                    model=text_model,
                    prompt=description,
                    temperature=0.6,
                    max_tokens=2048
                )
                return redirect(url_for("index", result=response.choices[0].text, gen_type=gen_type))
            elif gen_type == 'image':
                img_n = request.form["img_n"]
                img_size = request.form["img_size"]
                response = openai.Image.create(
                    prompt=description,
                    n=img_n,
                    size=img_size
                )
                print("send ok")
                return redirect(url_for("index", result=response.data[0].url, gen_type=gen_type))
        else:
            return redirect(url_for("index", result="Wrong key", gen_type=''))
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
