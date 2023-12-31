class FinancialPlanner:
    def __init__(self, age, salary, savings, debts, expenses, goals, time_to_goal):
        self.age = age
        self.salary = salary
        self.savings = savings
        self.debts = debts
        self.expenses = expenses
        self.goals = goals
        self.time_to_goal = time_to_goal
        self.aggressiveness = 0  # Placeholder, will be calculated

    def calculate_aggressiveness(self):
        # Rule 1: As age increases, aggressiveness decreases
        self.aggressiveness += max(0, 50 - self.age)  # Assuming a linear decrease in aggressiveness with age

        # Rule 2: Long-term goals are less aggressive, short-term goals are more aggressive
        if "Home Buying" in self.goals:
            self.aggressiveness += 20 if self.time_to_goal < 5 else 10  # Adjust values based on your criteria
        elif "Education Fund" in self.goals:
            self.aggressiveness += 10 if self.time_to_goal > 10 else 5  # Adjust values based on your criteria

        # Rule 3: More time to achieve the goal means less aggressiveness
        self.aggressiveness += max(0, 15 - self.time_to_goal)  # Assuming a linear decrease in aggressiveness with time

        # Rule 4: If time left < 3 years, max out aggressiveness
        if self.time_to_goal < 3:
            self.aggressiveness = 100

        # Rule 5: If time left < 15 years, minimum aggressiveness
        elif self.time_to_goal < 15:
            self.aggressiveness = 10

        # Rule 6: More savings, less aggressiveness
        self.aggressiveness += max(0, 10 - (self.savings / 10000))  # Assuming a linear decrease in aggressiveness with savings

        # Rule 7: If debt and goal isn't debt payoff, give a warning
        if self.debts > 0 and "Debt Reduction" not in self.goals:
            print("Warning: You have debts, but your goal doesn't include debt reduction.")

        # Rule 8: If debt and goal is debt payoff, calculate monthly debt payment based on salary
        if self.debts > 0 and "Debt Reduction" in self.goals:
            monthly_debt_payment = self.salary * 0.2  # Placeholder formula, adjust based on your criteria
            print(f"Monthly Debt Payment: {monthly_debt_payment}")

        # Rule 9: If expenses are the same as salary, give a warning to reduce spending
        if self.expenses == self.salary:
            print("Warning: Your expenses are equal to your salary. Consider reducing spending.")

        # Additional rules can be added based on your specific criteria

        return self.aggressiveness


from flask import Flask, request, jsonify

app = Flask(__name__)

class FinancialPlanner:
    def __init__(self, age, salary, savings, debts, expenses, goals, time_to_goal):
        self.age = age
        self.salary = salary
        self.savings = savings
        self.debts = debts
        self.expenses = expenses
        self.goals = goals
        self.time_to_goal = time_to_goal
        self.aggressiveness = 0  # Placeholder, will be calculated

    def calculate_aggressiveness(self):
        # Your existing logic for calculating aggressiveness
        # ...

        return self.aggressiveness

    def get_recommendation(self):
        # Sample recommendation logic for debugging
        print("Received data:", vars(self))  # Print received data for debugging

        # Return a specific response for testing
        return "This is a test response. Check the server logs for received data."

@app.route('/get_recommendation', methods=['POST'])
def get_recommendation():
    data = request.get_json()

    # Extract relevant data from the request
    age = int(data.get('age', 0))
    salary = float(data.get('salary', 0))
    savings = float(data.get('savings', 0))
    debts = float(data.get('debts', 0))
    expenses = float(data.get('expenses', 0))
    goals = data.get('goals', [])
    time_to_goal = int(data.get('timeToGoal', 0))

    # Use FinancialPlanner class to calculate aggressiveness
    planner = FinancialPlanner(age, salary, savings, debts, expenses, goals, time_to_goal)
    planner.calculate_aggressiveness()

    # Get recommendation based on aggressiveness and specific goal
    recommendation = planner.get_recommendation()

    return jsonify({'aggressiveness': planner.aggressiveness, 'recommendation': recommendation})

if __name__ == '__main__':
    app.run(debug=True)
