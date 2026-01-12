# SocialBench

Small harness for running a LangChain-powered extraction chain against a prompt and returning structured output via Pydantic models.

## Setup

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key (loaded via python-dotenv):

   ```bash
   echo "OPENAI_API_KEY=your_key_here" > .env
   ```

   Or export it in your shell:

   ```bash
   export OPENAI_API_KEY=your_key_here
   ```

## Run the extraction chain (CLI)

```bash
python main.py "A short text prompt describing a scene"
```

By default this runs `extraction_chain` with:
- `SocialEventAnalysis` as the Pydantic schema
- `prompt_template` as the prompt
- `gpt-4o` as the model

## Call the extraction chain from Python

```python
from extraction_chain.extraction_chain import extraction_chain
from extraction_chain.data_models import SocialEventAnalysis
from extraction_chain.prompt_template import prompt_template

result = extraction_chain(
    input="A short text prompt describing a scene",
    data_model=SocialEventAnalysis,
    prompt_template=prompt_template,
    reasoning_model="gpt-4o",
)

```

## Notes

- The chain returns a Python `dict` parsed from the model's JSON output.
- Swap `reasoning_model` if you want to use a different OpenAI model.
