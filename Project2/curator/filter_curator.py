from langchain_core.prompts import PromptTemplate
from langchain_core.chains import LLMChain


def get_filter_from_context(context_for_query: str, llm):
    """
    Given context (descriptions of available filters) and a query,
    returns the most relevant filter filename using the LLM.
    """
    with open("filter_prompt.txt", "r", encoding="utf-8") as f:
        base_prompt = f.read()

    prompt = PromptTemplate(input_variables=["context", "query"], template=base_prompt)
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run({"context": context_for_query, "query": query})

    return response.strip()
