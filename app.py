from flask import Flask, jsonify, render_template, request
from transformers import pipeline, set_seed
import random

app = Flask(__name__)

# Load local AI Model
generator = pipeline('text-generation', model='distilgpt2')
set_seed(42)

categories = {
    "motivation": [
        "Believe you can and you're halfway there.",
        "Push yourself, because no one else is going to do it for you.",
        "Don't stop when you're tired. Stop when you're done."
    ],
    "success": [
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "Don't be afraid to give up the good to go for the great.",
        "Success usually comes to those who are too busy to be looking for it."
    ],
    "happiness": [
        "Happiness is not by chance, but by choice.",
        "Stay close to anything that makes you glad you are alive.",
        "Happiness often sneaks in through a door you didn’t know you left open."
    ],
    "wisdom": [
        "The only true wisdom is in knowing you know nothing.",
        "Turn your wounds into wisdom.",
        "Wisdom is the reward you get for a lifetime of listening."
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quote', methods=['POST'])
def get_quote():
    data = request.json
    category = data.get('category', 'motivation')

    try:
        prompt = f"A {category} quote: "
        response = generator(prompt, max_length=50, num_return_sequences=1)
        quote = response[0]['generated_text'].replace(prompt, "").strip()
        if len(quote) < 5:
            quote = random.choice(categories.get(category, categories['motivation']))
    except Exception as e:
        quote = random.choice(categories.get(category, categories['motivation']))

    return jsonify({'quote': quote})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)