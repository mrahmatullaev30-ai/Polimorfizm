import os
os.system('cls')

class Talaba:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} ({self.age} yosh)"

class Kurs:
    def __init__(self, kurs_name, kurs_teacher):
        self.kurs_name = kurs_name
        self.kurs_teacher = kurs_teacher
        self.talabalar_soni = 0
        self.talabalar = []

    def add(self, new_student):
        self.talabalar.append(new_student)
        self.talabalar_soni += 1
        print(f"Yangi talaba qo'shildi: {new_student.name}")

    def delete(self, student_name):
        for student in self.talabalar:
            if student.name == student_name:
                self.talabalar.remove(student)
                self.talabalar_soni -= 1
                print(f"Talaba kursdan haydaldi: {student_name}")
                return
        print("Bunday talaba topilmadi.")

    def info_kurs(self):
        print(f"Kurs: {self.kurs_name}")
        print(f"O'qituvchi: {self.kurs_teacher}")
        print(f"Talabalar soni: {self.talabalar_soni}")
        print(f"Talabalar ro'yxati: {self.talabalar}")

python_kurs = Kurs("Python Backend", "Anvar aka")
cyber_kurs = Kurs("Cyber Security", "Sardor aka")

for i in range(1, 11):
    python_kurs.add(Talaba(f"Talaba_Py_{i}", 18 + i))
    cyber_kurs.add(Talaba(f"Talaba_Cyber_{i}", 19 + i))

python_kurs.delete("Talaba_Py_3")
cyber_kurs.delete("Talaba_Cyber_5")

python_kurs.info_kurs()
cyber_kurs.info_kurs()