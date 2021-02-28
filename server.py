from flask import Flask, render_template, request, redirect
import csv
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

# Route with a variable name
# Setting username=None is simply a way of specifying a default value
@app.route('/user/<username>')
def show_welcome_page(username=None):
    return render_template('welcome.html', name=username)

# @app.route('/favicon.ico')
# def render_favicon():
#     return render_template('favicon.ico')

# @app.route('/blog')
# def display_blog():
#     return 'This is my blog'

# @app.route('/blog/<int:post_id>')
# def display_post(post_id=None):
#     return render_template('post.html', postid=post_id)

# @app.route('/blog/2020/dogs')
# def display_blog_post():
#     return 'This is my dog'


# Handle requests for all of our static pages
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# Handle form submissions
@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        # save_data_file(data)
        write_data_to_csv(data)
        return redirect('thankyou.html')
    else:
        return 'An error occurred'
        

# Save form data to a file
def save_data_file(data):
    with open("form_data2.txt", mode='a+') as my_file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        my_file.write(f"\n{email},{subject},{message}")


# Save form data to a csv
def write_data_to_csv(data):
    with open("data.csv", newline='', mode='a+') as my_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        csv_writer = csv.writer(my_csv,delimiter=",", quoting=csv.QUOTE_NONE)
        csv_writer.writerow([email,subject,message])