## MDEval

MDEval is a benchmark for evaluating the _Markdown Awareness_ of large language model (LLM) chatbots' outputs.

## Human Evaluation Arena

To verify the effectiveness of the proposed benchmark, we built a human evaluation arena where we invited human annotators to evaluate the outputs of the LLM chatbots. The arena is available at the following link: [Human Evaluation Arena](https://md-eval-human.pages.dev/).

## Notice

It is recommended to use `virtualenv` to create a virtual environment, and then install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

Before using MDEval, you need to set your API key as an environment variable.

To facilitate calling multiple model APIs with one interface, we used a third-party proxy.

## Example

We provide partial data obtained through MDEval in the `data` folder and some human evaluation data in the `human_data` folder. Additionally, we offer a simple example script, `md_eval.py`, demonstrating the process from obtaining responses to rewriting them and calculating each model's score under the corresponding query using MDEval. Other files contain our accuracy evaluations, Spearman correlation coefficients, and scores for each model in terms of _Markdown Awareness_ derived from the partial data.
