# Diet-Recommendation-System
This project is a Smart Diet Recommendation System that suggests a basic meal plan based on user input such as age, gender, height, weight, activity level, and fitness goal (maintain, lose, gain). It uses a nutrition dataset and basic health formulas to calculate BMI and recommended daily calories. The final model is deployed using Flask and can be accessed via a simple web form.

🚀 Features
BMI and Calorie calculation

Personalized meal plan (5 meals per day)

User-friendly HTML form input

Flask API for backend processing

Designed for easy deployment via VS Code or PythonAnywhere

📊 Dataset
The system uses a Nutrition dataset (CSV) containing nutritional information such as:

Calories

Total Fat

Saturated Fat

Cholesterol

Sodium

Choline

Folate

Macronutrients

Water content

Make sure your dataset file (e.g., nutrition.csv) is in the same directory as your Flask app.

🛠️ Technologies Used
Python 3.x

Flask

HTML/CSS (for frontend)

Pandas & Numpy (for data processing)

🧪 Setup Instructions
Clone this repository:


git clone https://github.com/your-username/smart-diet-recommender.git
cd smart-diet-recommender
Create a virtual environment:


python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:


pip install -r requirements.txt
Run the Flask app:


python app.py
Open your browser and go to:


http://127.0.0.1:5000/
📂 Project Structure
smart-diet-recommender/
│
├── app.py                    
├── nutrition.csv            
├── templates/
│   └── index.html                       
├── requirements.txt          
└── README.md  

📌 Sample User Inputs
Age: 25

Gender: female

Height: 165 cm

Weight: 60 kg

Activity Level: moderate

Goal: maintain

The API will return a 5-meal diet plan totaling your recommended calorie intake.

🧠 Future Enhancements
Use ML models to personalize meals

Add food preference filters (e.g., vegetarian, diabetic)

Connect to live nutrition databases (e.g., USDA API)

Store user profiles in a database
