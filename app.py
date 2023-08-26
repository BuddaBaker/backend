from flask import Flask, render_template, request

app = Flask(__name__)
app.template_folder = 'templates'

# Define a dictionary to store recommendations for each goal and risk tolerance
# (Insert the goal_recommendations dictionary here)
goal_recommendations = {
    'Retirement Planning': {
        'Conservative': 'Start investing in retirement accounts with low-risk assets like bonds to build a solid retirement fund.',
        'Moderate': 'Diversify your retirement investments across various assets for balanced growth.',
        'Aggressive': 'Consider high-growth investments like stocks and ETFs to maximize long-term returns.'
    },
    'Emergency Fund': {
        'Conservative': 'Save money in a stable, low-risk savings account for your emergency fund.',
        'Moderate': 'Create a mix of stable savings and moderate-risk investments for your emergency fund.',
        'Aggressive': 'Consider moderate-risk investments with quick liquidity for your emergency fund.'
    },
    'Wealth Building': {
        'Conservative': 'Invest in a diversified portfolio with low to moderate risk to steadily build wealth.',
        'Moderate': 'Create a balanced portfolio of diverse assets to grow your wealth over time.',
        'Aggressive': 'Consider high-risk, high-reward investments to accelerate wealth building.'
    },
    'Investing': {
        'Conservative': 'Focus on stable, low-risk assets like bonds and dividend stocks for your investment portfolio.',
        'Moderate': 'Diversify your investment portfolio across different assets for balanced growth.',
        'Aggressive': 'Consider high-growth, high-volatility assets like growth stocks and technology companies.'
    },
    'Home Buying': {
        'Conservative': 'Save money for a down payment in low-risk accounts like a high-yield savings account or CDs.',
        'Moderate': 'Create a balanced saving and investing plan to grow your down payment fund.',
        'Aggressive': 'Consider moderate-risk investments to potentially grow your down payment fund faster.'
    }
}
@app.route('/', methods=['GET', 'POST'])
@app.route('/get_recommendation', methods=['GET', 'POST'])
def get_recommendation():
    if request.method == 'POST':
        user_id = int(request.form['user_id'])
        email = request.form['email']
        password = request.form['password']
        income = float(request.form['income'])
        company_401k = request.form['company_401k']
        company_match = request.form['company_match']
        match_percent = float(request.form['match_percent'])
        match_salary = float(request.form['match_salary'])
        risk_level = int(request.form['risk_level'])
        inputted_assets = float(request.form['inputted_assets'])
        checking_amt = float(request.form['checking_amt'])
        saving_amt = float(request.form['saving_amt'])
        IRA_amt = float(request.form['IRA_amt'])
        comp401k_amt = float(request.form['comp401k_amt'])
        investment_amt = float(request.form['investment_amt'])
        financial_goal = request.form['financial_goal']
        
        # Map risk level to risk tolerance
        risk_tolerances = {
            1: 'Conservative',
            2: 'Moderate',
            3: 'Aggressive'
        }
        risk_tolerance = risk_tolerances.get(risk_level, 'Moderate')  # Default to 'Moderate' if invalid input

        # Use the financial goal and risk tolerance to get the financial recommendation
        if financial_goal in goal_recommendations and risk_tolerance in goal_recommendations[financial_goal]:
            recommendation = goal_recommendations[financial_goal][risk_tolerance]
        elif financial_goal in goal_recommendations:
            recommendation = "No specific risk tolerance provided for this goal. Consider a moderate risk tolerance."
        else:
            recommendation = "No specific recommendation available for this goal."
        
        # Fetch form input data and process it
        # (Insert the form processing code here)
        
        return render_template('result.html', recommendation=recommendation)
    return render_template('form.html')

if __name__ == '__main__':
    app.run()
