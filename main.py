from extraction_chain.extraction_chain import extraction_chain
from extraction_chain.data_models import SocialEventAnalysis, SocialNormativeContext
from extraction_chain.prompt_template import prompt_template

import argparse
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some input text.")
    parser.add_argument("--text", type=str, help="Input text prompt for social analysis")
    args = parser.parse_args()

    result = extraction_chain(
        input=args.text,
        data_model=SocialNormativeContext,
        prompt_template=prompt_template,
        reasoning_model="gpt-4o"
    )
    with open("output.json", "w") as f:
        json.dump(result, f, indent=4)

    print(result)