from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)

# Load model and vectorizer
vector = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("phishing.pkl", "rb"))

@app.route("/", methods=['GET', 'POST'])
def index():
    predict = None  # initialize before branching

    if request.method == 'POST':
        url = request.form['url']
        #print(url)

        cleaned_url = re.sub(r'^https?://(www\.)?', '', url)
        #print(cleaned_url)

        predict = model.predict(vector.transform([cleaned_url]))[0]  # get first element if it's an array
        # print(predict)

        if predict == 'bad':
            predict = "The website is Phishing!!"

        elif predict == 'good':
            predict = "The website is Legitimate!!"

        else:
            predict = "Something went wrong!!"



    return render_template("index.html", predict=predict)

if __name__ == "__main__":
    app.run(debug=True)
