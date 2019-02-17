import compare
from flask import Flask, url_for, render_template, request



app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return("hello ")

@app.route('/home/', methods=["GET", "POST"])
def show_home():
    if request.method == "GET":
        return render_template("home_template.html")
    elif request.method == "POST":
        source_id = request.form["total_payment"]
        print(request.form)
        if request.form["submit"] == "Submit":
            print(source_id)
            return render_template("home_template.html")


@app.route('/template/')
def show_template():
    return(render_template('first_template.html'))


@app.route('/user/<username>/')
def show_user_profile(username):
    # show the user profile for that user
    return('User {0}'.format(username))

@app.route('/next/')
def show_next():
    # show the user profile for that user
    return('Next' )

@app.route('/post/<int:post_id>/')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return('Post {0}'.format(post_id))

with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('show_next'), )
    print(url_for('show_user_profile', username='John Doe'))

if __name__ == "__main__":
    app.run()
