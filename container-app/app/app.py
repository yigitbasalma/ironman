#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from math import factorial

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index_page():
    if request.method == "POST":
        try:
            return jsonify({
                "result": factorial(int(request.form["number"]))
            })
        except Exception as e:
            return jsonify({
                "error": True,
                "error_info": str(e)
            })
    return render_template('index.html')
