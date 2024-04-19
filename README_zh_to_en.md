# GPTTranslator

Supports the translation and polishing of Chinese and English markdown files.

## Installation
```shell
# Create and activate a virtual environment (optional)
python -m venv .gpt_trans_env && source .gpt_trans_env/bin/activate

# Install gpt_trans
pip install gpt_trans
```

## Requirements
Prepare the API Key for OpenAI and add it to the environment variables.
Currently supported LLM models include:
- OpenAI GPT3.5 and GPT4: configure the environment variable `OPENAI_API_KEY`
- Azure OpenAI GPT3.5: configure the environment variables `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_DEPLOYMENT`, `OPENAI_API_VERSION`


## Quickstart
- Translate Chinese markdown to English markdown and polish.
```shell
gpt_trans path_to_your_md.md
```
By default, a `path_to_your_md_zh_to_en.md` result file and an unpolished intermediate file `path_to_your_md_zh_to_en_raw.md` will be generated in the same directory as `path_to_your_md`. You can then use a diff tool to compare the differences between the original and translated versions, as well as the polished results, and manually modify the polished result. 
![](imgs/comparing_screenshot.png)


## Usage
- Directly translate Chinese markdown to English markdown without polishing.
```shell
gpt_trans path_to_your_md.md --mode zh_to_en
```  
- Directly translate English markdown to Chinese markdown without polishing.
```shell
gpt_trans path_to_your_md.md --mode en_to_zh
```  
- Polish English markdown file.
```shell
gpt_trans path_to_your_md.md --mode refine_en
```  
- Polish Chinese markdown file.
```shell
gpt_trans path_to_your_md.md --mode refine_zh
```  

## Model selection
The model can be selected using the `llm` parameter, with the default being OpenAI GPT3.5.
For example, to switch to GPT-4:
```shell
gpt_trans path_to_your_md.md --llm gpt4
```


## Parameter Description

```shell
gpt_trans --help
```

```text
usage: gpt_translator [-h] [--mode {ModeType.DEFAULT,ModeType.REFINE_ZH,ModeType.REFINE_EN,ModeType.ZH_TO_EN,ModeType.EN_TO_ZH}] [--llm {LLMType.GPT3_5,LLMType.GPT4,LLMType.AZURE_GPT3_5}] input_file

Translate using GPT Translator

positional arguments:
input_file            The input file to be translated or refined

optional arguments:
-h, --help            show this help message and exit
--mode {ModeType.DEFAULT,ModeType.REFINE_ZH,ModeType.REFINE_EN,ModeType.ZH_TO_EN,ModeType.EN_TO_ZH}
Translation mode, should be one of [<ModeType.DEFAULT: 'default'>, <ModeType.REFINE_ZH: 'refine_zh'>, <ModeType.REFINE_EN: 'refine_en'>, <ModeType.ZH_TO_EN: 'zh_to_en'>,
<ModeType.EN_TO_ZH: 'en_to_zh'>]
--llm {LLMType.GPT3_5,LLMType.GPT4,LLMType.AZURE_GPT3_5}
Language model to be used for translation, should be one of [<LLMType.GPT3_5: 'gpt3.5'>, <LLMType.GPT4: 'gpt4'>, <LLMType.AZURE_GPT3_5: 'azure_gpt3.5'>]
```