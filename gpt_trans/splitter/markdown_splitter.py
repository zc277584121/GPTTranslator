from langchain.text_splitter import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader


def _find_diff(last_metadata, current_metadata):
    different_items = [(key, current_metadata[key]) for key in current_metadata if (
            key in last_metadata and last_metadata[key] != current_metadata[key] or key not in last_metadata)]
    return different_items


def _add_header_to_metadata(split_docs, headers_to_split_on):
    """
    Use metadata information to infer the writing method of the md title before content

    """
    reversed_headers_to_split_on = {
        header: symbol for symbol, header in headers_to_split_on
    }
    last_metadata = {list(split_docs[0].metadata.keys())[0]: ''}#todo 当第一行没有#开头时会报错
    for split_doc in split_docs:
        showing_headers = []
        diff_list = _find_diff(last_metadata, split_doc.metadata)
        for diff in diff_list:
            header, header_content = diff[0], diff[1]
            showing_headers.append((reversed_headers_to_split_on[header], header_content))
        last_metadata = split_doc.metadata
        split_doc.metadata['header_content'] = '\n'.join(
            [showing_header[0] + ' ' + showing_header[1] for showing_header in showing_headers]
        )


def splitter_md_from_file(input_path: str):
    """
    Split a markdown file into multiple documents based on headers.
    """
    loader = TextLoader(input_path)
    data = loader.load()
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
        ("####", "Header 4"),
    ]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    markdown_text = data[0].page_content
    md_header_splits = markdown_splitter.split_text(markdown_text)

    # todo: replace code with placeholder

    chunk_size = 4096
    chunk_overlap = 0
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    split_docs = text_splitter.split_documents(md_header_splits)
    _add_header_to_metadata(split_docs, headers_to_split_on)
    return split_docs
