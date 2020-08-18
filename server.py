from flask import Flask, render_template, url_for, request, redirect
import smtplib
from email.message import EmailMessage
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def send_to_csv(data):
	with open('database.csv', mode='a', newline='') as database:
		email = data["email"]
		subject = 'Mail from website'
		message = data["message"]
		csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
		csv_writer.writerow([email,subject,message])

# def forward_to_email(data):
# 	email = EmailMessage()
# 	email['from'] = data["email"]
# 	email['to'] = 'edmondshishko@live.se'
# 	email['subject'] = 'Mail from website'
# 	email.set_content(data["message"])

	# with smtplib.SMTP(host='mailcluster.loopia.se', port='587') as smtp:
	# 	smtp.ehlo()
	# 	smtp.starttls()
	# 	smtp.login('contact@edisax.se', 'pranvera1')
	# 	smtp.send_message(email)
	# 	print('All good!')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		print(data)
		# forward_to_email(data)
		send_to_csv(data)
		return redirect('./submitted.html')
	else:
		return 'Something went wrong!'