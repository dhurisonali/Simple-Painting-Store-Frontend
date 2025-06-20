from flask import Flask, render_template

app = Flask(__name__)

# Sample painting data
paintings = [
    {"id": 1, "title": "Sunset Bliss", "price": "$120", "img": "sunset.jpg"},
    {"id": 2, "title": "Ocean Whisper", "price": "$90", "img": "ocean.jpg"},
    {"id": 3, "title": "Golden Forest", "price": "$150", "img": "forest.jpg"},
]

@app.route('/')
def home():
    return render_template("index.html", paintings=paintings)

@app.route('/product/<int:pid>')
def product(pid):
    painting = next((p for p in paintings if p["id"] == pid), None)
    return render_template("product.html", painting=painting)

if __name__ == '__main__':
    app.run(debug=True)
