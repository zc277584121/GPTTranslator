# GPTTranslator
支持中英文markdown文件的翻译、润色。

## Installation
```shell
pip install -U gpt-translator
```

## Requirements
准备好OpenAI的API Key，并将其添加到环境变量中。
目前支持以下几个LLM模型：
- OpenAI GPT3.5 请配置环境变量 `OPENAI_API_KEY`
- OpenAI GPT4 请配置环境变量 `OPENAI_API_KEY`
- Azure OpenAI GPT3.5 请配置环境变量 `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_DEPLOYMENT`, `OPENAI_API_VERSION`

## Quickstart
- 翻译中文的md为英文的md，并润色。
```shell
gpt_translator path_to_your_md.md
```
默认会在`path_to_your_md`同级目录下生成`path_to_your_md_zh_to_en.md`结果文件和一个未润色的中间文件`path_to_your_md_zh_to_en_raw.md`。

然后可以用对比工具比较翻译前后和润色前后的差异，再手动修改润色后的结果。
![](imgs/comparing_screenshot.png)

## Usage
- 直接翻译中文的md为英文的md，不润色。
```shell
gpt_translator path_to_your_md.md --mode zh_to_en
```

- 直接翻译英文的md为中文的md，不润色。
```shell
gpt_translator path_to_your_md.md --mode en_to_zh
```

- 润色英文md文件。
```shell
gpt_translator path_to_your_md.md --mode refine_en
```

- 润色中文md文件。
```shell
gpt_translator path_to_your_md.md --mode refine_zh
```

## 模型选择
使用mode参数可以选择模型，默认为OpenAI GPT3.5。
比如要切换成gpt4：
```shell
gpt_translator path_to_your_md.md --mode gpt4
```

## 参数说明
```shell
gpt_translator --help
```
```text
usage: gpt_translator [-h] [--mode {ModeType.DEFAULT,ModeType.REFINE_ZH,ModeType.REFINE_EN,ModeType.ZH_TO_EN,ModeType.EN_TO_ZH}] [--llm {LLMType.GPT3_5,LLMType.GPT4,LLMType.AZURE_GPT3_5}] input_file

Translate using GPT Translator

positional arguments:
  input_file            The input file to be translated or be refined

optional arguments:
  -h, --help            show this help message and exit
  --mode {ModeType.DEFAULT,ModeType.REFINE_ZH,ModeType.REFINE_EN,ModeType.ZH_TO_EN,ModeType.EN_TO_ZH}
                        Translation mode, should be one of [<ModeType.DEFAULT: 'default'>, <ModeType.REFINE_ZH: 'refine_zh'>, <ModeType.REFINE_EN: 'refine_en'>, <ModeType.ZH_TO_EN: 'zh_to_en'>,
                        <ModeType.EN_TO_ZH: 'en_to_zh'>]
  --llm {LLMType.GPT3_5,LLMType.GPT4,LLMType.AZURE_GPT3_5}
                        Language model to be used for translation, should be one of [<LLMType.GPT3_5: 'gpt3.5'>, <LLMType.GPT4: 'gpt4'>, <LLMType.AZURE_GPT3_5: 'azure_gpt3.5'>]
```