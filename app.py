from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary to store registered user credentials
user_credentials = {
    'user1': 'password1',
    'user2': 'password2'
}

# Dictionary to store user information
user_info = {}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if the username exists in the user_credentials dictionary
    if username in user_credentials and user_credentials[username] == password:
        return redirect(url_for('user_info_page'))

    return redirect(url_for('invalid_user_pass'))

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def process_signup():
    username = request.form['username']
    password = request.form['password']

    # Save the new user credentials in the user_credentials dictionary
    user_credentials[username] = password

    # Redirect to the login page
    return redirect(url_for('index'))

@app.route('/user_info')
def user_info_page():
    return render_template('user_info.html', user_info=user_info)

@app.route('/user_info', methods=['POST'])
def process_user_info():
    name = request.form['name']
    address = request.form['address']
    dob = request.form['dob']
    country = request.form['country']

    # Save the user information
    user_info['name'] = name
    user_info['address'] = address
    user_info['dob'] = dob
    user_info['country'] = country

    # Redirect to the profile page
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    return render_template('profile.html', user_info=user_info)

@app.route('/settings', methods=['GET', 'POST'])
def settings_page():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        dob = request.form['dob']
        country = request.form['country']

        # Update the user information
        user_info['name'] = name
        user_info['address'] = address
        user_info['dob'] = dob
        user_info['country'] = country

    return render_template('settings.html', user_info=user_info)

@app.route('/change_credentials', methods=['POST'])
def change_credentials():
    new_username = request.form['new_username']
    new_password = request.form['new_password']

    # Update the user credentials in the user_credentials dictionary
    if new_username in user_credentials:
        user_credentials[new_username] = new_password

    # Redirect to the profile page
    return redirect(url_for('profile'))

@app.route('/logout')
def logout():
    user_info.clear()
    return redirect(url_for('index'))

@app.route('/invalid_user_pass')
def invalid_user_pass():
    return render_template('invalid_user_pass.html')

if __name__ == '__main__':
    app.run(debug=True)
