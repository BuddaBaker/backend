from flask import Flask, render_template, request

app = Flask(__name__)
app.template_folder = 'templates'

# Define a dictionary to store recommendations for each goal and risk tolerance
goal_recommendations = {
    'Retirement Planning': {
        'Conservative': 'For conservative investors, consider low-risk assets like bonds for your retirement fund. Consult with a financial advisor for more personalized guidance.',
        'Moderate': 'Diversify your retirement investments across various assets like stocks and bonds for balanced growth.',
        'Aggressive': 'Consider high-growth investments like stocks and ETFs for maximizing long-term returns in your retirement fund.'
    },
    'Emergency Fund': {
        'Conservative': 'Build your emergency fund in a stable, low-risk savings account. Aim for at least 3-6 months of living expenses.',
        'Moderate': 'Combine stable savings with moderate-risk investments to grow your emergency fund while maintaining liquidity.',
        'Aggressive': 'Consider moderate-risk investments with quick liquidity for your emergency fund to achieve potential growth.'
    },
    'Wealth Building': {
        'Conservative': 'Start with a diversified portfolio of low to moderate risk to steadily build wealth over time.',
        'Moderate': 'Create a balanced portfolio of diverse assets to grow your wealth and manage risk effectively.',
        'Aggressive': 'Explore high-risk, high-reward investments to accelerate wealth building if you are comfortable with the risk.'
    },
    # Add similar recommendations for other goals...
}

# Weights for different factors
weights = {
    'income': 0.2,
    'company_401k': 0.1,
    'match_percent': 0.1,
    'risk_level': 0.2,
    'inputted_assets': 0.1,
    'spending_amount': 0.1,
    'financial_goal': 0.2,
}

@app.route('/', methods=['GET', 'POST'])
def get_recommendation():
    if request.method == 'POST':
        # Extract user input from the form
        income = float(request.form['income'])
        company_401k = request.form['company_401k']
        match_percent = float(request.form['match_percent'])
        risk_level = int(request.form['risk_level'])
        inputted_assets = float(request.form['inputted_assets'])
        spending_amount = float(request.form['spending_amount'])
        financial_goal = request.form['financial_goal']

        # Calculate a weighted score based on user responses
        score = (
            weights['income'] * income +
            weights['company_401k'] * (1 if company_401k == 'Yes' else 0) +
            weights['match_percent'] * match_percent +
            weights['risk_level'] * risk_level +
            weights['inputted_assets'] * inputted_assets +
            weights['spending_amount'] * spending_amount +
            weights['financial_goal'] * len(financial_goal)  # Consider the length of the financial goal as a proxy for its importance
        )

        # Determine the user's goal based on their input
        user_goal = None  # Set this based on user input (e.g., mapping financial_goal to predefined goals)

        # Get the recommendation based on the user's goal and risk level
        recommendation = goal_recommendations.get(user_goal, {}).get(risk_level, 'No specific recommendation available.')

        return render_template('result.html', recommendation=recommendation)

    return render_template('form.html')

if __name__ == '__main__':
    app.run()
