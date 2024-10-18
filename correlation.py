import json
import pandas as pd
from collections import defaultdict
import scipy

with open('human_data/human_data.json', 'r', encoding='utf-8') as f:
    human_stats = json.load(f)

with open('data/md_data.json', 'r', encoding='utf-8') as f:
    md_data = json.load(f)

def get_battles(human_stats):
    battles = []
    for rank_data in human_stats:
        model_a, score_a = rank_data['scores'][0]['model_name'], rank_data['scores'][0]['score']
        model_b, score_b = rank_data['scores'][1]['model_name'], rank_data['scores'][1]['score']

        winner = 'tie' if score_a == score_b else ('model_a' if score_a > score_b else 'model_b')
        battles.append({'model_a': model_a, 'model_b': model_b, 'winner': winner})
    return battles

def compute_elo(battles, K=10, SCALE=400, BASE=10, INIT_RATING=1000):
    rating = defaultdict(lambda: INIT_RATING)
    for battle in battles:
        model_a = battle['model_a']
        model_b = battle['model_b']
        winner = battle['winner']

        ra, rb = rating[model_a], rating[model_b]
        ea = 1 / (1 + BASE ** ((rb - ra) / SCALE))
        sa = 1 if winner == "model_a" else (0 if winner == "model_b" else 0.5)
        rating[model_a] += K * (sa - ea)
        rating[model_b] += K * ((1 - sa) - (1 - ea))
    return rating

def get_model_rankings(md_data):
    rankings = defaultdict(list)
    for category, items in md_data.items():
        for item in items:
            rankings[item['question']].append({
                'model_name': item['model'],
                'score': item['score']
            })
    return rankings

def calculate_correlations(mad_rankings, bootstrap_lu_median):
    spearman_corr, pearson_corr, kendall_corr = 0, 0, 0

    for rank in mad_rankings:
        rank_df = pd.DataFrame(list(rank.items()), columns=["Model", "MD_rank"]).round(3).sort_values(
            by="MD_rank", ascending=False).reset_index(drop=True)
        merged_df = rank_df.merge(bootstrap_lu_median.reset_index(), on="Model")

        spearman_corr += scipy.stats.spearmanr(merged_df["MD_rank"], merged_df["Elo rating"])[0]
        pearson_corr += scipy.stats.pearsonr(merged_df["MD_rank"], merged_df["Elo rating"])[0]
        kendall_corr += scipy.stats.kendalltau(merged_df["MD_rank"], merged_df["Elo rating"])[0]

    return spearman_corr, pearson_corr, kendall_corr

battles = get_battles(human_stats)
bootstrap_elo_lu = [compute_elo(battles) for _ in range(1000)]
bootstrap_lu_median = pd.DataFrame(bootstrap_elo_lu).median().reset_index().set_axis(["Model", "Elo rating"], axis=1)
bootstrap_lu_median["Elo rating"] = (bootstrap_lu_median["Elo rating"] + 0.5).astype(int)
bootstrap_lu_median = bootstrap_lu_median.sort_values(by="Elo rating", ascending=False).reset_index(drop=True)

model_rankings = get_model_rankings(md_data)

mad_rankings = []
for question, models in model_rankings.items():
    id_score_dict = {model['model_name']: model['score'] for model in models}
    mad_rankings.append(id_score_dict)

spearman_corr, pearson_corr, kendall_corr = calculate_correlations(mad_rankings, bootstrap_lu_median)
print("Spearman Correlation:", spearman_corr / len(mad_rankings))
print("Pearson Correlation:", pearson_corr / len(mad_rankings))
print("Kendall Correlation:", kendall_corr / len(mad_rankings))
