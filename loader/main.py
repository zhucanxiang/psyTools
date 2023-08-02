from chinese_text_splitter import ChineseTextSplitter
from langchain.document_loaders import UnstructuredFileLoader, TextLoader, CSVLoader

from zh_title_enhance import zh_title_enhance
from pdf_loader import UnstructuredPaddlePDFLoader
import os


def load_file(filepath, sentence_size=100, using_zh_title_enhance=True):

    if filepath.lower().endswith(".md"):
        loader = UnstructuredFileLoader(filepath, mode="elements")
        docs = loader.load()
    elif filepath.lower().endswith(".txt"):
        loader = TextLoader(filepath, autodetect_encoding=True)
        textsplitter = ChineseTextSplitter(pdf=False, sentence_size=sentence_size)
        docs = loader.load_and_split(textsplitter)
    elif filepath.lower().endswith(".pdf"):
        # 暂且将paddle相关的loader改为动态加载，可以在不上传pdf/image知识文件的前提下使用protobuf=4.x
        loader = UnstructuredPaddlePDFLoader(filepath)
        textsplitter = ChineseTextSplitter(pdf=True, sentence_size=sentence_size)
        docs = loader.load_and_split(textsplitter)
    else:
        loader = UnstructuredFileLoader(filepath, mode="elements")
        textsplitter = ChineseTextSplitter(pdf=False, sentence_size=sentence_size)
        docs = loader.load_and_split(text_splitter=textsplitter)
    if using_zh_title_enhance:
        docs = zh_title_enhance(docs)
    write_check_file(filepath, docs)
    return docs

def write_check_file(filepath, docs):
    folder_path = os.path.join(os.path.dirname(filepath), "tmp_files")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    fp = os.path.join(folder_path, 'load_file.txt')
    with open(fp, 'a+', encoding='utf-8') as fout:
        fout.write("filepath=%s,len=%s" % (filepath, len(docs)))
        fout.write('\n')
        for i in docs:
            fout.write(str(i))
            fout.write('\n')
        fout.close()

load_file("/Users/zhucanxiang/Desktop/psy_resources/icd-11.pdf", 100, True)