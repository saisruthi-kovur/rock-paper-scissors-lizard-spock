# rock-paper-scissors-lizard-spock game API

* Because this is a GET function, I use the @app.get() decorator. We're not inserting, updating, or deleting anything from the database, so I use the @app.get() decorator.
* I have a path parameter called arm that feeds into my shoot(arm: str) function. Here, arm has a type annotated which means entered arm should be a string.
* I choose the opponent's arm at random using the random module.
* To make a key, I merge the user's(your) and opponent's arms into a tuple (arm, opponent_weapon). Then I use that key to search my dictionary of all conceivable weapon combinations for the proper message to display.

## Execution
* Install fastapi (pip install 'fastapi[all]')
* Run the app locally with uvicorn app:app --reload
* Navigate to uvicorn’s development URL (http://127.0.0.1:8000) and observe the JSON response {"message":"Connected"}.
* Then navigate to uvicorn’s development URL (http://127.0.0.1:8000/docs) to get the better experiece.
* Choose your arm and check the response for the same.
