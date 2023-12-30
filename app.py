from flask import Flask, render_template, request

app = Flask(__name__)
app.template_folder = 'templates'

# Define your goal_recommendations and weights as you did previously

@app.route('/', methods=['GET', 'POST'])
def get_recommendation():
    if request.method == 'POST':
        # Process the form data and calculate the recommendation
        # ...

        return render_template('result.html', recommendation=recommendation)

    return render_template('form.html')

if __name__ == '__main__':
    app.run()
