from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import ConfigurableField

from gpt_trans.prompt_template import SYSTEM_PROMPT


def build_prompt(prompt_md: str, prompt_txt: str) -> ChatPromptTemplate:
    prompt = ChatPromptTemplate.from_messages(
        [("system", SYSTEM_PROMPT), ("human", prompt_md)]
    ).configurable_alternatives(
        ConfigurableField(id="prompt"),
        default_key="md",
        txt=ChatPromptTemplate.from_messages(
            [("system", SYSTEM_PROMPT), ("human", prompt_txt)]
        ),
    )
    return prompt
