from flask import Flask, render_template, url_for

app = Flask(__name__)
# Optional: Load configuration from config.py if you have one
# app.config.from_object('config.DevelopmentConfig')

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

# Example of a route with a dynamic parameter
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'

if __name__ == '__main__':
    app.run(debug=True) # debug=True allows automatic reloading and provides a debugger