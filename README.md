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
python main.py --text "A short text prompt describing a scene" --scene-id SCENE_001
```

By default this runs `extraction_chain` with:
- `SocialNormativeContext` as the Pydantic schema
- `prompt_template` as the prompt
- `gpt-4o` as the model

It also writes the structured result to `output.json` and stores the output in a local SQLite DB (`eqbench.db`). Use `--no-db` to skip storage or `--db /path/to/file.db` to override the location. If your output schema does not include `scene_id`, pass it explicitly with `--scene-id`.

## Call the extraction chain from Python

```python
from extraction_chain.extraction_chain import extraction_chain
from extraction_chain.data_models import SocialNormativeContext
from extraction_chain.prompt_template import prompt_template

result = extraction_chain(
    input="A short text prompt describing a scene",
    data_model=SocialNormativeContext,
    prompt_template=prompt_template,
    reasoning_model="gpt-4o",
)

```

## Query stored results

Lookup by `scene_id`:

```bash
python db_query.py --scene-id SCENE_001
```

Filter by a JSON field:

```bash
python db_query.py --json-path '$.verdict.judgment' --equals Adherence
```

Run a custom SQL query:

```bash
python db_query.py --sql "SELECT scene_id, json_extract(data_json, '$.verdict.judgment') AS verdict FROM scenes"
```

## Notes

- The chain returns a Python `dict` parsed from the model's JSON output.
- Swap `reasoning_model` if you want to use a different OpenAI model.
- The input prompt is not stored in the database.
- If your schema includes `scene_id` (e.g., `SocialEventAnalysis`), the database writer will use it automatically.
