from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def recommend_diet():
    data = request.get_json()

    age = data['age']
    gender = data['gender']
    height_cm = data['height_cm']
    weight_kg = data['weight_kg']
    activity_level = data['activity_level']
    goal = data['goal']

    # BMI
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)

    # BMR
    if gender == 'male':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

    # Activity adjustment
    activity_factors = {
        'sedentary': 1.2,
        'moderate': 1.55,
        'active': 1.725
    }
    calories = bmr * activity_factors.get(activity_level, 1.2)

    # Goal adjustment
    if goal == 'lose':
        calories -= 500
    elif goal == 'gain':
        calories += 500

    # Diet plan
    meals = ['Breakfast', 'Morning Snack', 'Lunch', 'Evening Snack', 'Dinner']
    calories_per_meal = calories / len(meals)

    # Simple meal plan
    sample_meal_plan = {
        'Breakfast': 'Oatmeal with banana and almonds',
        'Morning Snack': 'Greek yogurt with honey',
        'Lunch': 'Grilled chicken with brown rice and veggies',
        'Evening Snack': 'Fruit smoothie or nuts',
        'Dinner': 'Paneer/tofu stir-fry with quinoa'
    }

    return jsonify({
        "BMI": round(bmi, 2),
        "Recommended Calories": int(calories),
        "Calories per Meal": int(calories_per_meal),
        "Diet Plan": sample_meal_plan
    })

if __name__ == '__main__':
    app.run(debug=True)
