# Load the environment variables 
from dotenv import load_dotenv
load_dotenv()

# Create API client
from anthropic import Anthropic
client = Anthropic()
model = "claude-sonnet-4-0"

# Append message history to have multi-turn conversations 
# Add user message to the messages list 
def add_user_message(messages, content):
    user_message = {"role":"user", "content": content}
    messages.append(user_message)

# Add assistant message to the messages list 
def add_assistant_message(messages, content):
    assistant_message = {"role":"assistant", "content": content}
    messages.append(assistant_message)

# Call API and return the response from assistant
def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages
    )

    #print(message)
    response = message.content[0].text
    print(response)
    return response 

messages = []

while True:
    prompt = input("Please enter your prompt:")
    add_user_message(messages, prompt)
    assistant_response = chat(messages)
    add_assistant_message(messages, assistant_response)