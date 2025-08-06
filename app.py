from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

# Step 1: Login/Register Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        username = request.form['username']
        password = request.form['password']
        # Authenticate user (placeholder)
        session['user'] = username
        return redirect(url_for('main'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic here
        username = request.form['username']
        password = request.form['password']
        # Save user (placeholder)
        return redirect(url_for('login'))
    return render_template('register.html')

# Step 2: Main Page (Input + Suggestions)
@app.route('/', methods=['GET', 'POST'])
def main():
    suggestions = ['Python', 'Web Development', 'Data Science']
    if request.method == 'POST':
        prompt = request.form['prompt']
        return redirect(url_for('analyze', prompt=prompt))
    return render_template('main.html', suggestions=suggestions)

# Step 3: Fetch 3 things from prompt
@app.route('/analyze')
def analyze():
    prompt = request.args.get('prompt', '')
    # Dummy analysis (replace with actual logic)
    course_name = prompt
    preferred_language = 'English'
    course_duration = 'Short'
    return redirect(url_for('generate_course', 
                            course_name=course_name, 
                            language=preferred_language, 
                            duration=course_duration))

# Step 4: Generate course modules with embedded YouTube links
@app.route('/generate_course')
def generate_course():
    course_name = request.args.get('course_name', '')
    language = request.args.get('language', '')
    duration = request.args.get('duration', '')
    # Dummy modules and YouTube links
    modules = [
        {'title': 'Introduction', 'youtube': 'https://youtube.com/embed/dummy1'},
        {'title': 'Basics', 'youtube': 'https://youtube.com/embed/dummy2'},
    ]
    return render_template('course.html', 
                           course_name=course_name, 
                           language=language, 
                           duration=duration, 
                           modules=modules)

if __name__ == '__main__':
    app.run(debug=True)