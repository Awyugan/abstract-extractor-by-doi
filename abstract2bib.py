import tkinter as tkfrom tkinter import filedialogimport csvimport os# 初始化Tkinter，用于打开文件选择对话框root = tk.Tk()root.withdraw()  # 不显示Tkinter的主窗口# 获取当前脚本文件的目录current_directory = os.path.dirname(os.path.realpath(__file__))# 设置文件选择对话框的初始目录为当前脚本的目录，弹出文件选择对话框，让用户选择旧的BibTeX文件old_bib_file_path = filedialog.askopenfilename(    title="Select old BibTeX file",    initialdir=current_directory,  # 设置初始目录为脚本所在目录    filetypes=(("BibTeX files", "*.bib"), ("all files", "*.*")))if old_bib_file_path:    # 生成新的BibTeX文件名    new_bib_file_path = old_bib_file_path.replace('.bib', '-new.bib')    # 读取DOI和摘要的对应关系    csv_file_path = filedialog.askopenfilename(title="Select CSV file with DOI and Abstracts", filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))    if csv_file_path:        csv_file = open(csv_file_path, 'r')        csv_reader = csv.DictReader(csv_file)        doi_abstract_dict = {}        for row in csv_reader:            doi_abstract_dict[row['DOI']] = row['ABSTRACT'].replace('\n', '').strip()        csv_file.close()        # 读取旧的BibTeX文件，并将处理后的内容写入新的BibTeX文件        with open(old_bib_file_path, 'r', encoding='utf-8') as f_old, open(new_bib_file_path, 'w', encoding='utf-8') as f_new:            for line in f_old:                f_new.write(line)                if line.strip()[:3] == 'doi':                    bib_doi = line.strip().split(' ')[2].rstrip('},').lstrip('{').strip()                    if doi_abstract_dict.get(bib_doi) is not None:                        new_ab_line = '\tabstract = {' + doi_abstract_dict[bib_doi] + '},\n'                        f_new.write(new_ab_line)        print(f"New file saved: {new_bib_file_path}")    else:        print("No CSV file selected.")else:    print("No BibTeX file selected.")