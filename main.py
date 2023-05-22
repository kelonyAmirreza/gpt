from gpt4all import GPT4All
import time
import json

start_time = time.time()

with open('result.json', 'r') as f:
    data = json.load(f)


end_time = time.time()
execution_time = end_time - start_time

gptj = GPT4All("ggml-gpt4all-l13b-snoozy")
messages = [
    {"role": "user", "content": f"analyse this data and give the trend: {data}"}]
gptj.chat_completion(messages)

end_time = time.time()
execution_time = end_time - start_time
print(execution_time)
