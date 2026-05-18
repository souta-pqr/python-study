"""
問題6: 継承とオーバーライド
===========================

次のコードを実行したときの出力を答えよ．
また，Cat ではオーバーライドした cry が呼ばれ，
Fish では Animal の cry が呼ばれた理由を説明せよ．
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def cry(self):
        return "..."

    def introduce(self):
        return f"{self.name}: {self.cry()}"


class Cat(Animal):
    def cry(self):
        return "ニャー"


class Fish(Animal):
    pass


c = Cat("Tama")
f = Fish("Nemo")

print(c.introduce())   # ①
print(f.introduce())   # ②


# ---- 解答 ----
# ① Tama: ニャー
# ② Nemo: ...
#
# 解説:
#   - Cat は cry をオーバーライドしているので "ニャー" が返る．
#   - Fish は pass だけで何もオーバーライドしていない．
#     継承により Animal の cry がそのまま使われるので "..." が返る．
#   - introduce は親クラス Animal で定義されているが，
#     その中の self.cry() は「そのインスタンスのクラスでの cry」を呼ぶ．
#     c の場合は Cat.cry，f の場合は Animal.cry が呼ばれる．
