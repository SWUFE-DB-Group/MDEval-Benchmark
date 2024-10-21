# MDEval

Welcome to **MDEval**! This is an innovative benchmark for evaluating the performance of large language model (LLM) chatbots in handling Markdown content. Our goal is to advance research and applications in Markdown Awareness for these models.

## 🚀 Human Evaluation Platform

To validate the effectiveness of our benchmark, we have built a **Human Evaluation Platform** where we invited human reviewers to comprehensively evaluate the outputs of LLM chatbots. Experience our platform here: [Human Evaluation Arena](https://md-eval-human.pages.dev/).

## 🔧 Quick Start

We recommend using `virtualenv` to create an isolated virtual environment. Use the following command to quickly install the required dependencies:

```bash
pip install -r requirements.txt
```

Before using MDEval, please ensure to set your API key as an environment variable. To facilitate calling multiple model APIs through a single interface, we used a third-party proxy. For instance, when not using a third-party proxy and setting the OpenAI API key, we can only access models under OpenAI, such as gpt-4o and gpt-4. However, with the third-party proxy, we can call models from various companies, like Google's gemini-1.5-pro and Anthropic's claude-3-5-sonnet.

## 📂 Sample Data

In the `data` folder, we provide partial data obtained through MDEval, while the `human_data` folder contains some human evaluation data. You can refer to the example script `md_eval.py` to understand how to obtain responses, rewrite them, and calculate scores for each model.

## 📈 Output Results

- **Accuracy**: Run `accuracy.py` to check MDEval's predicted accuracy for Markdown Awareness of the models on a subset of test data.
- **Correlation**: Use `correlation.py` to compute the Spearman, Pearson, and Kendall correlation coefficients between MDEval's rankings for Markdown Awareness and human rankings.
- **Average Scores**: Run `md_rank.py` to calculate and output the average scores for each model on a subset of test data.

## 🤝 Contributions

We welcome any form of contributions and feedback! Feel free to submit issues or pull requests to help us improve MDEval.

## 📬 Contact Us

For further information or support, please contact us at [223081200004@smail.swufe.edu.cn].
