import json
import re

# Load JSON data
def load_json(file):
    with open(file, encoding='utf-8') as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)

# Store JSON data
response_data = load_json("bot.json")

# Function to get a response based on user input
def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string)
    score_list = []

    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response.get("required_words", [])

        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        if required_score == len(required_words):
            for word in split_message:
                if word in response["user_input"]:
                    response_score += 1

        score_list.append(response_score)

    best_response = max(score_list)
    response_index = score_list.index(best_response)

    if input_string == "":
        return "Please type something so we can chat :("

    if best_response != 0:
        return response_data[response_index]["bot_response"]

while True:
    user_input = input("You: ")
    print("Bot:", get_response(user_input))