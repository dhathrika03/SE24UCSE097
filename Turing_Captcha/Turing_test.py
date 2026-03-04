import random

# Simple bot responses
bot_responses = [
    "Hello! How are you today?",
    "That's interesting. Tell me more.",
    "I like learning new things.",
    "Why do you think that?",
    "Can you explain that again?"
]

print("TURING TEST SIMULATION")
print("You are chatting with an unknown entity.")
print("After 3 messages, guess if it is Human or Bot.\n")

for i in range(3):
    user_input = input("You: ")
    response = random.choice(bot_responses)
    print("Entity:", response)

guess = input("\nDo you think it was a Human or Bot? ")

if guess.lower() == "bot":
    print("Correct! It was a bot.")
else:
    print("Incorrect. It was actually a bot.")

print("Turing Test Simulation Complete.")