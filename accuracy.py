import json

with open('human_data/human_data.json', 'r', encoding='utf-8') as f:
    human_stats = json.load(f)

with open('data/md_data.json', 'r', encoding='utf-8') as f:
    md_data = json.load(f)

def get_accuracy(human_stats, md_data):
    accuracy = 0
    count = 0

    md_data_index = {}
    for category in md_data.values():
        for item in category:
            question = item['question']
            model = item['model']
            score = item['score']

            if question not in md_data_index:
                md_data_index[question] = {}
            md_data_index[question][model] = score

    for stat in human_stats:
        question = stat['question']
        rank_data = stat['scores']

        model_a, score_a = rank_data[0]['model_name'], rank_data[0]['score']
        model_b, score_b = rank_data[1]['model_name'], rank_data[1]['score']

        # 查找与问题匹配的 md_data
        if question in md_data_index:
            benchmark_score_a = md_data_index[question].get(model_a)
            benchmark_score_b = md_data_index[question].get(model_b)

            if benchmark_score_a is not None and benchmark_score_b is not None:
                if score_a == score_b:
                    continue
                count += 1
                if (score_a > score_b and benchmark_score_a > benchmark_score_b) or \
                        (score_a < score_b and benchmark_score_a < benchmark_score_b):
                    accuracy += 1
    return accuracy / count


accuracy = get_accuracy(human_stats, md_data)

print("Accuracy:", accuracy)