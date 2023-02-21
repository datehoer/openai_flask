from flask import Flask, redirect, render_template, request, url_for
import openai
app = Flask(__name__)
openai.api_key = 'sk-MrN30mBy4fbtfNYTp1FzT3BlbkFJbJ8MVeEDH17jtTwPKk2YHMK'

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        description = request.form["description"]
        key = request.form["key"]
        gen_type = request.form["gen_type"]
        text_model = ['text-ada-001', 'text-babbage-001', 'text-curie-001', 'text-davinci-003']
        text_model_select = request.form["gen_text_module"]
        if key == "123":
            if gen_type == 'text':
                response = openai.Completion.create(
                    model=text_model[int(text_model_select)],
                    prompt=description,
                    temperature=0.6,
                    max_tokens=2048
                )
                return render_template("index.html", result=response.choices[0].text, gen_type=gen_type, title=description)
            else:
                img_size = request.form["gen_img_size"]
                img_n = request.form["gen_img_n"]
                size = {
                    'small': '256x256',
                    'medium': '512x512',
                    'large': '1024x1024',
                }
                response = openai.Image.create(
                  prompt=description,
                  n=int(img_n),
                  size=size[img_size],
                )
                return render_template("index.html", result=response.data[0].url, gen_type=gen_type, title=description)
        else:
            return render_template("index.html", result="Wrong Key", gen_type=gen_type, title=description)

    result = request.args.get("result")
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)