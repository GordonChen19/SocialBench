# from langchain.chains import TransformChain
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from extraction_chain.image_perception import chat_completion


def extraction_chain(input, data_model, prompt_template, reasoning_model):
    """
    input: user-provided prompt
    """

    # using langchain's default message to enforce GPT to output structured info
    parser = PydanticOutputParser(pydantic_object=data_model)

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["input"],
        partial_variables={"format_instructions": parser.get_format_instructions()})
    

    # puts the 1) input (user-provided input), 2) system message, 3) format instructions into one single string
    prompt_str = prompt.invoke({"input":input}).to_string()

    response = chat_completion(prompt_str, reasoning_model)
    
    return parser.invoke(response).dict()