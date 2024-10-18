import json

with open('data/md_data.json', 'r', encoding='utf-8') as f:
    md_data = json.load(f)


def calculate_average_scores(md_data):
    model_scores = {}
    model_counts = {}

    for category in md_data.values():
        for item in category:
            model = item['model']
            score = item['score']

            if model not in model_scores:
                model_scores[model] = 0
                model_counts[model] = 0

            model_scores[model] += score
            model_counts[model] += 1

    average_scores = {}
    for model in model_scores:
        average_scores[model] = model_scores[model] / model_counts[model]

    return average_scores

average_scores = calculate_average_scores(md_data)

sorted_average_scores = sorted(average_scores.items(), key=lambda x: x[1], reverse=True)

for model, avg_score in sorted_average_scores:
    print(f"Model: {model}, Average Score: {avg_score:.3f}")