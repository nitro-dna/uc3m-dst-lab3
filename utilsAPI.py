import csv
from flask import Flask, jsonify, request

app = Flask(__name__)

def read_books_from_csv(filename='books.csv'):
    books = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append(row)
    return books