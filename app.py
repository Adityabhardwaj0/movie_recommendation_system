from flask import Flask, render_template, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)
api = Api(app)

# ... (Rest of the code remains the same)

# Register the API endpoint
api.add_resource(MovieRecommendation, '/api/recommend/<string:movie_title>')

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# ... (Rest of the code remains the same)

if __name__ == '__main__':
    app.run(debug=True)
