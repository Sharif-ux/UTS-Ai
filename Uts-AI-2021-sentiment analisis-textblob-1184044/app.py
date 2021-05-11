from flask import Flask, render_template, request
from textblob import TextBlob
import re

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def index():
    if request.method == 'POST':
        url = request.form['url']
        remove = url.replace(('-'),' ')
        change = r"https?://(www\.)?"
        text = re.sub(change, ' ', remove)
        sentiment = TextBlob(text).sentiment
        polarty = sentiment.polarity
        subjct = sentiment.subjectivity
        
#polarty   
        if polarty > 0:
            sentiment_polarty = "Positive absolute."
        elif polarty == 0:
            sentiment_polarty = "Netral."
        elif polarty < 0:
            sentiment_polarty = "Negative absolute."
            
#subjct
        if subjct > 0.75:
            sentiment_subjct = "Extremely subjective."
        elif subjct > 0.5:
            sentiment_subjct = "Fairly subjective."
        elif subjct > 0.3:
            sentiment_subjct = "Fairly objective."
        elif subjct > 0.1:
            sentiment_subjct = "Extremely objective."
        elif subjct == 0:
            sentiment_subjct = "Netral."
        else:
            sentiment_subjct = 'no sentiment.' 
        
        return render_template('index.html', url=url, polarty=polarty, sentiment_polarty=sentiment_polarty, sentiment_subjct=sentiment_subjct, subjct=subjct)
    return render_template('layout.html')

if __name__ == "__main__":
    app.run(debug=True)