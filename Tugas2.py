# Nur Adhwa Zahratul Aini
# 2309076003
# Mengurutkan bilagan

def susun_bilangan():
    bilangan = [23, 45, 76, 24, 56, 98, 69, 16, 54]
    return bilangan

# Ascending(Terkecil ke terbesar)
bilangan = susun_bilangan()
bilangan_terurut = sorted(bilangan)
print("Bilangan setelah disusun secara ascending:", bilangan_terurut)

# Descending (Terbesar ke terkecil)
bilangan_terurut = sorted(bilangan, reverse=True)
print("Bilangan setelah disusun secara descending:", bilangan_terurut)