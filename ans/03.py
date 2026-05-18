"""
問題3: set と dict の使い分け
=============================

ある文章中に出てきた単語のリストがある．
「単語の種類数」 と 「各単語の出現回数」 を求めたい．
それぞれ set と dict のどちらを使うのが適切か答え，コードを書け．

期待する出力:
  ユニークな単語の数: 3
  出現回数: {"apple": 3, "banana": 2, "cherry": 1}
"""

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]


# ---- 解答 ----

# ユニークな単語の数 → set (重複を除く用途)
unique_count = len(set(words))
print("ユニークな単語の数:", unique_count)


# 各単語の出現回数 → dict (キーと値の対応)
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print("出現回数:", counts)


# 解説:
#   set:  「重複を取り除く」「ユニーク数を数える」など，
#          値の存在だけを扱う用途に最適．
#   dict: 「キーごとに値を持たせたい」場合に使う．
#          d.get(key, 0) でキーが無いときの初期値を指定できる
#          (KeyError を避けられる)．
#
#   ※ collections.Counter を使えば Counter(words) の一行で
#      同じ結果が得られるが，dict の基本動作を理解するための問題．
