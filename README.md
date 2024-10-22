# MDEval

Welcome to **MDEval**! This is an innovative benchmark for evaluating the performance of large language model (LLM) chatbots in handling Markdown content. Our goal is to advance research and applications in Markdown Awareness for these models.

## 🚀 Human Evaluation Platform

To validate the effectiveness of our benchmark, we have built a **Human Evaluation Platform** where we invited human reviewers to comprehensively evaluate the outputs of LLM chatbots. Experience our platform here: [Human Evaluation Arena](https://md-eval-human.pages.dev/).

## 🔧 Quick Start

We recommend using `virtualenv` to create an isolated virtual environment. Use the following command to quickly install the required dependencies:

```bash
pip install -r requirements.txt
```

Before using MDEval, make sure to set your API key as an environment variable. To simplify the process of calling multiple model APIs through a single interface, MDEval utilizes a third-party proxy. Normally, if you're not using a proxy and only set the OpenAI API key, you can only access models from OpenAI, like GPT-4 and GPT-4 Turbo. However, with the third-party proxy, you can access models from various providers, such as Google’s Gemini 1.5 Pro and Anthropic’s Claude 3.5 Sonnet, all through the same interface.
## 📂 Sample Data

In the `data` folder, we provide partial data obtained through MDEval, while the `human_data` folder contains some human evaluation data. You can refer to the example script `md_eval.py` to understand how to obtain responses, rewrite them, and calculate scores for each model.


## 📈 Test Results

We randomly selected a subset of data from our overall dataset to display the test results:

- **Accuracy**: The predicted accuracy for MDEval's Markdown Awareness is **0.8240**. You can run `accuracy.py` to check the accuracy for different models.

- **Correlation**: We calculated the following three correlation coefficients to compare MDEval's model rankings with human rankings. Run `correlation.py` to compute the results:
  - **Spearman Correlation**: **0.7313**
  - **Pearson Correlation**: **0.8007**
  - **Kendall Correlation**: **0.6021**

- **Average Scores**: The following are the average scores for the models, calculated on a subset of test data. You can run `md_rank.py` to compute these scores:

| **Model**                         | **Average Score** |
|-----------------------------------|-------------------|
| **deepseek-chat**                 | 0.939             |
| **chatgpt-4o-latest**             | 0.911             |
| **gpt-4o-mini-2024-07-18**        | 0.829             |
| **gemini-1.5-pro**                | 0.795             |
| **gpt-4-turbo-2024-04-09**        | 0.792             |
| **llama3.1:8b**                   | 0.711             |
| **claude-3-5-sonnet-20240620**     | 0.566             |
| **gpt-3.5-turbo**                 | 0.475             |
| **baichuan2-13b-chat-v1**         | 0.164             |

## 📬 Contact Us

For further information or support, please contact us at [223081200004@smail.swufe.edu.cn].
