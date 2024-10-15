import json
from openai import OpenAI
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from markdown import markdown
import re
from Levenshtein import distance

client = OpenAI()

MODELS = ["gpt-4o-mini-2024-07-18", "chatgpt-4o-latest"]

all_questions_output = {}

def save_output(filename='output.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(all_questions_output, f, ensure_ascii=False, indent=4)
    print(f"结果已保存为 {filename}")

with open("prompts/prompt_template.txt", 'r', encoding='utf-8') as f:
    prompt_template = f.read()

def convert_math_expressions(md_content):
    md_content = re.sub(r'\\\((.*?)\\\)', r'<math>\1</math>', md_content, flags=re.DOTALL)
    md_content = re.sub(r'\\\[(.*?)\\\]', r'<math>\1</math>', md_content, flags=re.DOTALL)
    md_content = re.sub(r'\$\$(.*?)\$\$', r'<math>\1</math>', md_content, flags=re.DOTALL)
    md_content = re.sub(r'\$(.*?)\$', r'<math>\1</math>', md_content, flags=re.DOTALL)
    return md_content

def convert_md_to_tags(md_content):
    html_content = markdown(md_content)
    html_content = convert_math_expressions(html_content)
    tags = re.findall(r'<[^>]+>', html_content)
    return ' '.join(tags)

def compute_tag_diff(md_content1, md_content2):
    text1 = convert_md_to_tags(md_content1)
    text2 = convert_md_to_tags(md_content2)
    d = distance(text1, text2)
    return 1 - d / max(len(text1), len(text2))

def process_question(question_text, model):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question_text}
        ]
    )
    original_response = response.choices[0].message.content

    prompt = prompt_template.format(content=original_response)

    markdown_reply = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    ).choices[0].message.content

    similarity_score = compute_tag_diff(original_response, markdown_reply)

    return {
        "question": question_text,
        "model": model,
        "response": original_response,
        "rewrite": markdown_reply,
        "score": similarity_score
    }

def main():
    with open('data/partial_queries2.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for category, questions in data.items():
        all_questions_output[category] = []

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(process_question, q, model)
                       for q in questions for model in MODELS]

            for future in tqdm(as_completed(futures), total=len(futures), desc=f"Processing {category}"):
                result = future.result()
                if result:
                    all_questions_output[category].append(result)

    save_output('data/partial_md_data.json')

if __name__ == "__main__":
    main()

