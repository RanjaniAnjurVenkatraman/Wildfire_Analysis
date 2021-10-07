

from flask import Flask, jsonify
from flask import render_template, request, redirect, url_for, flash



#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """List all available api routes."""
    return render_template('index.html')

@app.route("/data")
def data():
    """List all available api routes."""
    return render_template('data.html')

@app.route("/analysis")
def analysis():
    """List all available api routes."""
    return render_template('pcharts.html')

if __name__ == '__main__':
    app.run(debug=True)
