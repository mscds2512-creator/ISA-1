from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle form submission logic here
        return redirect(url_for('home'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)