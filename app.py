import pickle

from gensim.models import KeyedVectors
from flask import Flask, request, render_template
from utils import tokenizer, vector_combination_by_sum

app = Flask(__name__, template_folder="templates")


@app.before_request
def load_models():
    global classifier
    global w2v_model

    w2v_dir = "models/skipgram_model.txt"
    classifier_dir = "models/rl_sg.pkl"
    w2v_model = KeyedVectors.load_word2vec_format(w2v_dir)

    with open(classifier_dir, "rb") as f:
        classifier = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    title = next(request.form.values())

    title_tokens = tokenizer(title)
    title_vector = vector_combination_by_sum(title_tokens, w2v_model)
    title_category = classifier.predict(title_vector)

    output = title_category[0].capitalize()

    return render_template(
        "index.html",
        title="Título: {}".format(title),
        category="Categoria: {}".format(output),
    )


if __name__ == "__main__":
    app.run(debug=True)
