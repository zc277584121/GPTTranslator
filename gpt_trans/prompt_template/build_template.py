from langchain_core.prompts import ChatPromptTemplate

from gpt_trans.prompt_template import SYSTEM_PROMPT


def build_prompt(prompt_str: str) -> ChatPromptTemplate:
    prompt = ChatPromptTemplate.from_messages([("system", SYSTEM_PROMPT), ("human", prompt_str)])
    return prompt
