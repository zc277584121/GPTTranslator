import argparse
import os
from enum import Enum
from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

from tqdm import tqdm

from gpt_trans.llm import select_llm, LLMType
from gpt_trans.prompt_template import (
    OPTIMIZE_ENGLISH_WITH_RAW_CHINESE_MD,
    OPTIMIZE_ENGLISH_WITH_RAW_CHINESE_TXT,
    OPTIMIZE_ENGLISH_MD,
    OPTIMIZE_ENGLISH_TXT,
    OPTIMIZE_CHINESE_MD,
    OPTIMIZE_CHINESE_TXT,
    TRANSLATE_CHINESE_MD,
    TRANSLATE_CHINESE_TXT,
    TRANSLATE_ENGLISH_MD,
    TRANSLATE_ENGLISH_TXT,
)
from gpt_trans.prompt_template.build_template import build_prompt
from gpt_trans.splitter.markdown_splitter import splitter_md_from_file
from gpt_trans.utils.text_util import is_english_text, infer_prompt_type


class ModeType(str, Enum):
    SMART = "smart"
    REFINE_ZH = "refine_zh"
    REFINE_EN = "refine_en"
    ZH_TO_EN = "zh_to_en"
    EN_TO_ZH = "en_to_zh"


def main_pipeline(
    input_file: str,
    mode: str = ModeType.SMART,
    llm_type=LLMType.GPT4,
    chain_batch_size: int = 1,  # todo confiragable
):
    input_file = os.path.abspath(input_file)
    file_dir = os.path.dirname(input_file)
    file_name = os.path.basename(input_file)
    file_name_no_ext, file_ext = os.path.splitext(file_name)
    llm = select_llm(llm_type=llm_type)
    output_parser = StrOutputParser()
    split_docs = splitter_md_from_file(input_file)
    split_strs = []
    for doc in split_docs:
        if doc.metadata["header_content"]:
            split_strs.append("\n" + doc.metadata["header_content"] + "\n" + doc.page_content)
        else:
            split_strs.append(doc.page_content)


    print(f"Translating {input_file} using mode {mode}")
    if mode == ModeType.SMART:
        if is_english_text('\n'.join(split_strs)):
            mode = ModeType.EN_TO_ZH
        else:
            mode = ModeType.ZH_TO_EN

    if mode == ModeType.REFINE_ZH:
        prompt = build_prompt(OPTIMIZE_CHINESE_MD, OPTIMIZE_CHINESE_TXT)
        chain = (
            {"raw_doc": RunnablePassthrough()}
            | prompt
            | llm
            | {"zh_refined": output_parser}
        )
    elif mode == ModeType.REFINE_EN:
        prompt = build_prompt(OPTIMIZE_ENGLISH_MD, OPTIMIZE_ENGLISH_TXT)
        chain = (
            {"raw_doc": RunnablePassthrough()}
            | prompt
            | llm
            | {"en_refined": output_parser}
        )
    elif mode == ModeType.ZH_TO_EN:
        trans_zh_to_en_chain = build_prompt(TRANSLATE_CHINESE_MD, TRANSLATE_CHINESE_TXT) | llm | output_parser
        refine_zh_chain = (
                build_prompt(OPTIMIZE_ENGLISH_WITH_RAW_CHINESE_MD, OPTIMIZE_ENGLISH_WITH_RAW_CHINESE_TXT) | llm | output_parser
        )
        chain = (
                {"raw_doc": RunnablePassthrough()}
                | RunnablePassthrough.assign(zh_to_en_raw=trans_zh_to_en_chain)
                | RunnablePassthrough.assign(zh_to_en=refine_zh_chain)
        ).pick(["zh_to_en_raw", "zh_to_en"])
    elif mode == ModeType.EN_TO_ZH:
        prompt = build_prompt(TRANSLATE_ENGLISH_MD, TRANSLATE_ENGLISH_TXT)
        chain = (
            {"raw_doc": RunnablePassthrough()}
            | prompt
            | llm
            | {"en_to_zh": output_parser}
        )
    else:
        raise ValueError(f"Unsupported mode: {mode}")
    # print(chain.get_graph().print_ascii())

    result_doc_infos = []
    for i in tqdm(range(0, len(split_strs), chain_batch_size)):
        batch_strs = split_strs[i : i + chain_batch_size]
        prompt_type = infer_prompt_type(batch_strs, input_file)
        batch_res = chain.with_config(
            configurable={"prompt": prompt_type}
        ).batch(batch_strs)
        result_doc_infos.extend(batch_res)
    result_keys = result_doc_infos[0].keys()
    for key in result_keys:
        result_doc = [doc_info[key] for doc_info in result_doc_infos]
        result_md_path = os.path.join(file_dir, f"{file_name_no_ext}_{key}{file_ext}")
        with open(result_md_path, "w", encoding="utf-8") as f:
            f.write("\n\n".join(result_doc))
            print(f"Result saved to {result_md_path}")


def main():
    parser = argparse.ArgumentParser(
        prog="gpt_trans", description="Translate using GPT Translator"
    )
    parser.add_argument(
        "input_file", type=str, help="The input file to be translated or be refined"
    )
    parser.add_argument(
        "--mode",
        choices=list(ModeType),
        default=ModeType.SMART,
        help=f"Translation mode, should be one of {list(ModeType)}",
    )
    parser.add_argument(
        "--llm",
        choices=list(LLMType),
        default=LLMType.GPT4,
        help=f"Language model to be used for translation, should be one of {list(LLMType)}",
    )
    args = parser.parse_args()
    main_pipeline(args.input_file, args.mode, args.llm)


if __name__ == "__main__":
    main()
