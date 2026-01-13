class Customer:
    # 各問のコードが期待通り動作するように実装
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age <= 3:
            result = 0
            return result
        elif 3 < self.age < 20:
            result = 1000
            return result
        elif 20 <= self.age < 65:
            result = 1500
            return result
        else:
            result = 1200
            return result

    def info_csv(self):
        name_4 = self.full_name()
        fee_4 = self.entry_fee()
        return f"{name_4},{self.age},{fee_4}"

    def entry_fee_1(self):
        if self.age <= 3:
            result = 0
            return result
        elif 3 < self.age < 20:
            result = 1000
            return result
        elif 20 <= self.age < 65:
            result = 1500
            return result
        elif 65 <= self.age < 75:
            result = 1200
            return result
        else:
            result = 500
            return result

# C-7
    def info_tab(self):
        name_7 = self.full_name()
        fee_7 = self.entry_fee_1()
        return f"{name_7} \t {self.age} \t {fee_7}"

# C-8
    def info_pipe(self):
        name_8 = self.full_name()
        fee_8 = self.entry_fee_1()
        return f"{name_8}|{self.age}|{fee_8}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)  # C-5追加分

# 以降で各問のコードを追加していく

# C-1
print("C-1_answer")
print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力
print(ieyasu.full_name())  # "Ieyasu Tokugawa" という値を出力
# C-2
print("C-2_answer")
print(ken.age)  # 15 という値を出力
print(tom.age)  # 57 という値を出力
print(ieyasu.age)  # 75 という値を出力
# C-3
print("C-3_answer")
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力
# C-4
print("C-4_answer")
print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力
# C-5
print("C-5_answer")
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力
print(michelle.entry_fee())  # 0 という値を出力
# C-6
print("C-6_answer")
print(ken.entry_fee_1())
print(tom.entry_fee_1())
print(ieyasu.entry_fee_1())
print(michelle.entry_fee_1())
# C-7
print("C-7_answer")
print(ken.info_tab())
print(tom.info_tab())
print(ieyasu.info_tab())
print(michelle.info_tab())
# Ken Tanaka      15      1000
# Tom Ford        57      1500
# Ieyasu Tokugawa 75      500
# Michelle Tanner 3       0
# C-8
print("C-8_answer")
print(ken.info_pipe())
print(tom.info_pipe())
print(ieyasu.info_pipe())
print(michelle.info_pipe())
# Ken Tanaka|15|1000
# Tom Ford|57|1500
# Ieyasu Tokugawa|75|500
# Michelle Tanner|3|0
