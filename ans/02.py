"""
問題2: タプルのアンパック
=========================

次のコードを実行したとき，a, b, c にはそれぞれ何が代入されるか．
また，最後の行はなぜエラーになるか説明せよ．
"""


def get_info():
    return "Alice", 22, "Tokyo"


a, b, c = get_info()
print(a, b, c)


# 次の行はエラーになる
a, b = get_info()


# ---- 解答 ----
# a = "Alice", b = 22, c = "Tokyo"
#
# 最後の行は ValueError: too many values to unpack (expected 2)
# get_info() が返すのは要素3つのタプル ("Alice", 22, "Tokyo")．
# アンパックは左辺と右辺の要素数が一致する必要があるため，
# 2つの変数では3要素を受け取れない．

# 関数の複数戻り値はタプルとして返ってくる点もポイント．
