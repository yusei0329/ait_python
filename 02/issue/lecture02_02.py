#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

def lecture02_02() -> None:
    # implement me
    root = ET.Element('book')
    article = ET.SubElement(root, 'article')
    article.set('title', '卒業論文')
    novel = ET.SubElement(root, 'novel')
    
    article_name = ['はじめに', '基礎理論', '実験方法', '結果と考察', 'まとめ', '参考文献']
    article_pages = ['2', '8', '6', '2', '1', '2']

    article＿chapter = []
    for i in range(6):
        chapter = ET.SubElement(article, 'chapter')
        chapter.attrib['id'] = str(i + 1) # cast i from int to str
        chapter.attrib['name'] = article_name[i]
        chapter.attrib['pages'] = article_pages[i]
        article＿chapter.append(chapter)
    
    novel_name = ['1日のはじまり', '朝食', '仕事', '帰宅後', '新しい朝']
    novel_pages = ['2', '8', '6', '2', '1']

    novel_chapter = []
    for i in range(5):
        chapter = ET.SubElement(novel, 'chapter')
        chapter.attrib['id'] = str(i + 1) # cast i from int to str
        chapter.attrib['name'] = novel_name[i]
        chapter.attrib['pages'] = novel_pages[i]
        novel_chapter.append(chapter)


    # write readable xml (have your attention to 'wb')
    with open('./02/lecture02_data.xml', 'wb') as f:
        import xml.dom.minidom as md
        f.write(md.parseString(ET.tostring(root, encoding='utf-8', xml_declaration=True)).toprettyxml(indent='  ',encoding="utf-8"))


if __name__ == '__main__':
    lecture02_02()