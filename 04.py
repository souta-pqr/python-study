"""
問題4: 関数とデフォルト引数
===========================

次のコードを実行したとき，それぞれの行は何を出力するか答えよ．
(実行する前に少し考えてみましょう)
"""


def power(base, exp=2):
    return base ** exp


print(power(3))               # ①
print(power(3, 4))            # ②
print(power(exp=3, base=2))   # ③
