from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        event = request.form['event']
        return render_template('success.html', name=name, event=event)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5052)