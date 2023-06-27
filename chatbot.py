import openai
import yaml

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

api_key = config['bot_api']

openai.api_key = api_key

prompt = ""

while True:
    user_input = input("User: ")

    prompt += user_input + "\n"

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )

    prompt += response.choices[0].text.strip() + "\n"

    print("ChatBot:", response.choices[0].text.strip())


