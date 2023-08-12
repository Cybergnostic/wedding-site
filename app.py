from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        save_to_csv(name)
    return render_template('index.html')

# Function to save data to CSV file
def save_to_csv(name):
    with open('guests.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name])

if __name__ == '__main__':
    app.run(host="192.168.100.60", port="777", debug=True)
