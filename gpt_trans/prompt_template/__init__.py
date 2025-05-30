SYSTEM_PROMPT = '''
你是一个翻译工具，你只提供翻译的结果，不说其它任何话。You are a translation tool, and you only provide the translation result, WITHOUT ANY OTHER WORDS.
'''

MARKDOWN_ATTENTION = '''如果段落开头有一些"#"，请保留这些符号，因为它们是markdown的标题。'''
TEXT_ATTENTION = ''''''




OPTIMIZE_ENGLISH = '''
下面这段英文是由中文直接翻译过来的，可能有一些写法不地道的地方。如果有，请优化润色成地道的英语表达，如果没有，则返回原文。{{attention}}请直接返回给我最终的结果，不用说其它话。

{raw_doc}

'''

OPTIMIZE_ENGLISH_WITH_RAW_CHINESE = '''
下面我会提供给你【英文译文】和对应的【中文原文】，可能有一些翻译不地道的地方。如果有，请优化润色成地道的英语表达，如果没有，则返回同样的【英文译文】的内容。{{attention}}请直接返回给我最终的结果，不用说其它话。

【英文译文】：
{zh_to_en_raw}

【中文原文】：
{raw_doc}
'''


TRANSLATE_CHINESE = '''将下面这段中文翻译成英文，如果有什么直译过来英文表达不通顺的，可以用地道一点的英文的写法。{{attention}}请直接返回给我翻译后的英文。

{raw_doc}
'''


OPTIMIZE_CHINESE = '''如果下面这段话有一些不通顺的地方，请优化它。如果没有，直接返回给我原文。{{attention}}请直接返回给我最终的结果，不用说其它话。

{raw_doc}
'''

TRANSLATE_ENGLISH = '''将下面这段英文翻译成中文，如果有什么直译过来中文表达不通顺的，可以用地道一点的中文的写法。{{attention}}请直接返回给我翻译后的中文。

{raw_doc}
'''

OPTIMIZE_ENGLISH_MD = OPTIMIZE_ENGLISH.replace("{{attention}}", MARKDOWN_ATTENTION)
OPTIMIZE_ENGLISH_TXT = OPTIMIZE_ENGLISH.replace("{{attention}}", TEXT_ATTENTION)

OPTIMIZE_ENGLISH_WITH_RAW_CHINESE_MD = OPTIMIZE_ENGLISH_WITH_RAW_CHINESE.replace("{{attention}}", MARKDOWN_ATTENTION)
OPTIMIZE_ENGLISH_WITH_RAW_CHINESE_TXT = OPTIMIZE_ENGLISH_WITH_RAW_CHINESE.replace("{{attention}}", TEXT_ATTENTION)

TRANSLATE_CHINESE_MD = TRANSLATE_CHINESE.replace("{{attention}}", MARKDOWN_ATTENTION)
TRANSLATE_CHINESE_TXT = TRANSLATE_CHINESE.replace("{{attention}}", TEXT_ATTENTION)

OPTIMIZE_CHINESE_MD = OPTIMIZE_CHINESE.replace("{{attention}}", MARKDOWN_ATTENTION)
OPTIMIZE_CHINESE_TXT = OPTIMIZE_CHINESE.replace("{{attention}}", TEXT_ATTENTION)

TRANSLATE_ENGLISH_MD = TRANSLATE_ENGLISH.replace("{{attention}}", MARKDOWN_ATTENTION)
TRANSLATE_ENGLISH_TXT = TRANSLATE_ENGLISH.replace("{{attention}}", TEXT_ATTENTION)