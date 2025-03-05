import os
from enum import Enum

from langchain_openai import ChatOpenAI, AzureChatOpenAI


class LLMType(str, Enum):
    GPT3_5 = 'gpt-3.5-turbo'
    GPT4 = 'gpt-4o-mini'
    O1 = 'o1-mini'
    AZURE_GPT3_5 = 'azure_gpt3.5'
    # AZURE_GPT4 = 'azure_gpt4'
    GROQ_LLAMA3 = 'groq_llama3'
    MOONSHOT = 'moonshot'


def select_llm(llm_type: LLMType):
    if llm_type == LLMType.GPT3_5:
        model = ChatOpenAI(model="gpt-3.5-turbo")
    elif llm_type == LLMType.GPT4:
        model = ChatOpenAI(model="gpt-4o-mini")
    elif llm_type == LLMType.O1:
        model = ChatOpenAI(model="o1-mini")
    elif llm_type == LLMType.AZURE_GPT3_5:
        model = AzureChatOpenAI(
            openai_api_version="2023-05-15",
            azure_deployment=os.getenv("AZURE_DEPLOYMENT"),
            model_version="0613",
        )
    elif llm_type == LLMType.GROQ_LLAMA3:
        from langchain_groq import ChatGroq
        model = ChatGroq(temperature=0, model_name="llama3-70b-8192")
    elif llm_type == LLMType.MOONSHOT:
        from langchain_community.llms.moonshot import Moonshot
        model = Moonshot()

    else:  # todo: add azure gpt4
        raise ValueError(f"Unsupported language model: {llm_type}")
    return model