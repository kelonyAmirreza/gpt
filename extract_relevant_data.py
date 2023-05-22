import json

with open('result.json', 'r') as f:
    data = json.load(f)

relevant_data = []
for item in data:
    if 'relevant_field' in item and item['relevant_field']:
        relevant_data.append(item['relevant_field'])

with open('relevant_data.txt', 'w') as f:
    for item in relevant_data:
        f.write(item + '\n')
