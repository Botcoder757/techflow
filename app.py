from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/robots.txt')
def robots():
    content = """User-agent: *
Disallow: /admin
Disallow: /private

# backup-key: Q1VSU09Se2I4MzYxZDgyNThhNzdmYzQ2OGY1ZjI2ZTUzMTEzZDQ3fQ==
"""
    return Response(content, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)