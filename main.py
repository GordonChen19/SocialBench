from extraction_chain.extraction_chain import extraction_chain
from extraction_chain.data_models import SocialEventAnalysis, SocialNormativeContext
from extraction_chain.prompt_template import prompt_template
from db import DEFAULT_DB_PATH, store_scene

import argparse
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some input text.")
    parser.add_argument("--text", type=str, help="Input text prompt for social analysis")
    parser.add_argument(
        "--scene-id",
        type=str,
        help="Scene identifier to store with the output (required if the output schema lacks scene_id)",
    )
    parser.add_argument(
        "--db",
        type=str,
        default=str(DEFAULT_DB_PATH),
        help="Path to SQLite database for storing outputs",
    )
    parser.add_argument(
        "--no-db",
        action="store_true",
        help="Skip writing the output to the database",
    )
    args = parser.parse_args()

    result = extraction_chain(
        input=args.text,
        data_model=SocialNormativeContext,
        prompt_template=prompt_template,
        reasoning_model="gpt-4o"
    )
    if not args.no_db:
        store_scene(result, args.db, scene_id=args.scene_id)

    with open("output.json", "w") as f:
        json.dump(result, f, indent=4)

    print(result)
