import requests
from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def quote():
    try:
        response = requests.get('https://api.quotable.io/random', verify=False)
        if response.status_code == 200:
            data = response.json()
            quote = data.get('content')
            author = data.get('author')
        else:
            quote = "Couldn't fetch quote at the moment. Please try again later."
            author = ""
    except requests.exceptions.RequestException as e:
        quote = f"An error occurred: {e}"
        author = ""

    return render_template('quote.html', quote=quote, author=author)
