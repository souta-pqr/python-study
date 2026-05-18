"""
問題5: クラスの基本 (属性とメソッド)
====================================

BankAccount クラスを定義せよ．

要件:
  - インスタンス生成時に，所有者名 owner と初期残高 balance を受け取る
  - deposit(amount) メソッド: amount を残高に追加する
  - withdraw(amount) メソッド: amount を残高から引く
                                 (残高不足なら何もせず "残高不足" を返す)

期待する動作:
  a = BankAccount("Alice", 1000)
  a.deposit(500)
  print(a.balance)         # 1500
  print(a.withdraw(2000))  # "残高不足"
  a.withdraw(800)
  print(a.balance)         # 700
"""


# ---- 解答 ----

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "残高不足"
        self.balance -= amount


# 動作確認
a = BankAccount("Alice", 1000)
a.deposit(500)
print(a.balance)          # 1500

print(a.withdraw(2000))   # 残高不足

a.withdraw(800)
print(a.balance)          # 700


# 解説:
#   - __init__ で受け取った引数を self.xxx = xxx の形で属性として保存
#   - メソッドの第1引数は必ず self (そのインスタンス自身)
#   - self.balance のように self. 経由でアクセスすることで，
#     インスタンスごとに別々の残高を保持できる
