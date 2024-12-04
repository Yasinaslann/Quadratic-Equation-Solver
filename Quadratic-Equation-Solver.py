# Quadratic Equation Solver (2. Dereceden Denklem Çözücü)
# Bu betik, ikinci dereceden bir denklemin köklerini hesaplar.
# This script calculates the roots of a quadratic equation.
# Lütfen sadece tam sayılar giriniz. (Please enter only integers.)
# Kullanıcıdan alınan değerlerin tam sayı olmasına dikkat edilmelidir.
# Make sure that the entered values are integers.

# Kullanıcıdan katsayılar alınır
# Prompt user for coefficients

print("2. Dereceden Denklem Çözücü")
print("Denklem: ax^2 + bx + c")

a = int(input("a katsayısını giriniz (Enter coefficient a): "))
if a == 0:
    print("a katsayısı sıfır olamaz! (Coefficient 'a' cannot be zero!)")
else:
    b = int(input("b katsayısını giriniz (Enter coefficient b): "))
    c = int(input("c katsayısını giriniz (Enter coefficient c): "))

# Diskriminant hesaplama (Calculate the discriminant)
Delta = (b ** 2) - 4 * a * c

if Delta < 0:
    print(f"Denkleminizin diskriminantı negatif: {Delta}")
    print("Gerçek kökler yok, karmaşık kökler oluşur.")
    print("Discriminant is negative. No real roots; complex roots exist.")
else:
    # Köklerin hesaplanması ve gösterimi (Compute and display roots)
    root1 = (-b - (Delta ** 0.5)) / (2 * a)
    root2 = (-b + (Delta ** 0.5)) / (2 * a)
    print(f"Denkleminiz: {a}x^2 + {b}x + {c} = 0")
    print(f"Birinci kök: {root1}")
    print(f"İkinci kök:  {root2}")







