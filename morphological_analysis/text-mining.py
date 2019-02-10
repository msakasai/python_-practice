#!/usr/bin/env python3
# text-mining.py

import sys
import os
import re
import mojimoji

# janomeをインポート
from janome.tokenizer import Tokenizer

# 形態素解析用オブジェクトの生成
# ユーザ辞書（http://mocobeta.github.io/janome/#id7）を使用
t = Tokenizer("simple_userdic.csv", udic_type="simpledic", udic_enc="utf8")

# 引数
args = sys.argv
if len(args) != 2:
    print("ファイル名を指定してください")
    sys.exit()

# 解析対象ファイル
target_file = f"src_text/{args[1]}"
if not os.path.isfile(target_file):
    print("ファイルが存在しません " + args[1])
    sys.exit()

# ファイルの内容を取得
with open(target_file) as f:
    bindata = mojimoji.zen_to_han(f.read().strip().lower(), kana=False)  # 英字は小文字、英数字は半角

# {単語: 出現回数}格納辞書
word_dic = {}

# 1行ずつループ
for line in bindata.splitlines():
    if not line:
        # 空行
        continue

    for token in t.tokenize(line):
        # print(token)

        # 品詞を取得
        ps = token.part_of_speech
        # 名詞のみを対象とします
        if ps.find("名詞") < 0:
            continue

        # 表層系を取得
        surface = token.surface
        # print(surface)

        if surface not in word_dic:
            # 不要なワードが抽出される場合は必要に応じてスキップ処理を追加
            if surface.isdecimal():
                # 数値のみ
                continue
            if re.match("[!\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~└├。]", surface):
                # 記号のみ
                continue
            if re.match("[①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕]", surface):
                # 丸数字
                continue

            # 辞書に入っていなければ格納
            #print(surface)
            word_dic[surface] = 0
        # 出現回数をインクリメント
        word_dic[surface] += 1

#print(word_dic)
print("----- 単語でソート -----")
word_sorted = sorted(word_dic.items())
for word, cnt in word_sorted:
    print(f"{word}: {cnt}")

print("----- 出現回数でソート -----")
cnt_sorted = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word, cnt in cnt_sorted:
    print(f"{word}: {cnt}")
