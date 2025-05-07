from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy cricket data
cricket_data = {
    "latest_match": {
        "teams": "India vs Australia",
        "winner": "India",
        "score": "India 289/7 (50 overs), Australia 270/9 (50 overs)",
        "top_scorer": "Virat Kohli - 112 runs"
    },
    "next_match": "India vs Pakistan on 12 May 2025"
}

# Chatbot logic
def get_response(user_input):
    user_input = user_input.lower()
    if "who won" in user_input:
        return f"{cricket_data['latest_match']['winner']} won the last match."
    elif "score" in user_input:
        return f"The score was: {cricket_data['latest_match']['score']}."
    elif "next match" in user_input:
        return f"The next match is: {cricket_data['next_match']}."
    elif "top scorer" in user_input:
        return f"The top scorer was: {cricket_data['latest_match']['top_scorer']}."
    else:
        return "Sorry, I didn't understand that. Try asking about the winner, score, next match, or top scorer."

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["query"]
        response = get_response(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
