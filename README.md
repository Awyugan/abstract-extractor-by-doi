# abstract-extractor-by-doi
A tool that uses doi to obtain paper abstracts and import them into zotero

## 安装

使用`git clone git@github.com:Awyugan/abstract-extractor-by-doi.git`

安装需要的库pip安装：`pip install -r requirements.txt`
pip3安装：`pip3 install -r requirements.txt
`

## 使用步骤

### 1. 获得文献DOI号和bib文件

选中需要获取的文献，导出csv、bib两个文件到py文件同目录
从csv中复制doi号，注意不要标题。如图所示,一行一个单独的DOI号，放进txt文件中，命名为doi_list.txt
![XQ2LtI.png](https://imgtu.com/i/XQ2LtI)

### 2. 根据DOI号文件获取摘要
将如下Python代码[doi2paper_abstract.py](doi2paper_abstract.py)和doi_list.txt放到同一个目录下，并执行，获得doi_abstract.csv
根据电脑的性能速度略有不同，参考获取速度：67秒/83条

### 3. 翻译（英语好的可以忽略）

两个选项

1. 将得到的doi_abstract.csv转为xlsx，然后上传到Google Translate翻译，在doi_abstract.csv中，将英文原文和翻译结果用excel函数公式拼接,列名依然为ABSTRACT（注意DOI以及ABSTRACT这两个列名不能重复)。

2. 使用[zotero-pdf-translate](https://github.com/windingwind/zotero-pdf-translate)翻译标题和摘要

### 4. 获取新的bib文件导入zotero

将需要补充摘要的Zotero条目导出为BibTex格式，命名为old.bib,执行[abstract2bib.py](abstract2bib.py)，选择需要变更的bib文件得到{name}-new.bib
![XQRRbQ.png](https://imgtu.com/i/XQRRbQ)

