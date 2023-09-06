import openai 

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with OpenAI APIs "}])
print(completion['choices'][0]['message']['content'])
