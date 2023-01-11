# q-learning-email-summarizer


Using Q-Learning, this project implements an email summary and headline generator. Using an email as an input, the app preprocesses the message and extracts key information. Based on a Q-learning algorithm, the app generates a headline summarizing the main topic of the email. Using the Q-function, the features of the email are translated into a set of expected rewards for each possible headline. Moreover, the application has a reward feature, which assigns a numerical reward value to the agent's actions based on the relevance of the headlines. The agent's goal is to maximize the expected reward over time. As part of the exploration strategy, the agent uses an epsilon-greedy strategy, whereby it chooses a random action with a probability of epsilon, followed by the action with the highest Q-value with a probability of (1 - epsilon).

Installing the following libraries is required for the project, which is built in Python:

email library for parsing emails

numpy library for numerical calculations

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

The app can be used by running the script main.py and following the instructions.

The repo includes the following files:

`main
