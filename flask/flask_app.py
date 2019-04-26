from flask import Flask, redirect, url_for, request, render_template
from dcgan_deploy import dcgan

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    text = request.form['text']
    model = dcgan()
    filename = model.get_image(text)
    return render_template('results.html', filename=filename)

if __name__ == '__main__':
#    app.run(debug=True, use_reloader=False)
    app.run(host='0.0.0.0', port=80, debug=True)