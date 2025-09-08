from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

votes = {"Python": 0, "Java": 0, "Go": 0}

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', votes=votes)

@app.route('/vote', methods=['POST'])
def vote():
    language = request.form.get('language')
    if language in votes:
        votes[language] += 1
    return redirect(url_for('home'))

@app.route('/reset', methods=['POST'])
def reset():
    for key in votes:
        votes[key] = 0
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
