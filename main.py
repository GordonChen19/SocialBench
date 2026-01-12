from extraction_chain.extraction_chain import extraction_chain
from extraction_chain.data_models import SocialEventAnalysis
from extraction_chain.prompt_template import prompt_template

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some input text.")
    parser.add_argument("input", type=str, help="Input text prompt for social analysis")
    args = parser.parse_args()

    result = extraction_chain(
        input=args.input,
        data_model=SocialEventAnalysis,
        prompt_template=prompt_template,
        reasoning_model="gpt-4o"
    )

    print(result)