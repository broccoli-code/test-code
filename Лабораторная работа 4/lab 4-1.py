import json

def calculate_sum_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    total_sum = sum(item['score'] * item['weight'] for item in data)

    return round(total_sum, 3)

file_path = 'input.json'  
result = calculate_sum_from_json(file_path)
print(result)