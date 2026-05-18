"""
問題6: 継承とオーバーライド
===========================

次のコードを実行したときの出力を答えよ．
(実行する前に少し考えてみましょう)
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
