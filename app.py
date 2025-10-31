from flask import Flask, render_template, request, redirect, url_for
'''
It creates a Flask application instance.
which will be your WSGI (Web Server Gateway Interface) application.
'''
app = Flask(__name__)

@app.route("/")
def Welcome():
    '''
    This function handles requests to the root URL ("/").
    It returns a simple welcome message.
    '''
    return "<h1>Welcome to the Flask Application!</h1>"

@app.route("/home", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        return f"<h2>Hello, {name}!</h2>"
    return render_template("form.html")


@app.route('/marks', methods=['GET', 'POST'])
def marks():
    """Accepts marks for math, science, english and mechanical,
    computes the average (sum/4) and redirects to /successres/<int:score>
    which will present the result.
    """
    if request.method == 'POST':
        try:
            math = float(request.form.get('math', 0))
            science = float(request.form.get('science', 0))
            english = float(request.form.get('english', 0))
            mechanical = float(request.form.get('mechanical', 0))
        except ValueError:
            # If conversion fails, treat invalid inputs as 0
            math = science = english = mechanical = 0.0

        total = math + science + english + mechanical
        average = total / 4.0
        score = int(average)

        # Redirect to the existing successres route with the integer score
        return redirect(url_for('successres', score=score))

    # GET -> render a simple marks submission form
    return render_template('marks_form.html')

# variable rules
# dynamic URL route that accepts an integer parameter 'score'
# jinja2 template to render the result based on the score
'''
{{ result  }} expresion to prinit the result variable passed from the Flask route.
{% if result == "You have passed the exam!" %} conditional statemen, for loops
{% else %} 
{% endif %}
{% for item in items %} loop through a list
{% endfor %} 
{#...#} comments in jinja2
{% extends "base.html" %} template inheritance
'''
@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "You have passed the exam!"   
    else:
        res = "You have failed the exam!"
    
    return render_template("result.html", result=res)

@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score >= 50:
        res = "You have passed the exam!"   
    else:
        res = "You have failed the exam!"
    
    exp = {'score': score, 'res': res}

    return render_template("result1.html", results =exp)



if __name__ == "__main__":
    app.run(debug=True) # Runs the application in debug mode for development purposes