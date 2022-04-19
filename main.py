a=5
b=15
liste=[1,3,5,7,9]


print("List içerisinde not in operatörünün kullanımı : \n")
print("Liste : ",liste)
print("Listede a değişkenine karşılık gelmeyen bir değer var mı  ? " ,a not in liste) #a=5 ve 5 değeri listenin içerisinde bulunmaktadır
print("Listede b değişkenine karşılık gelmeyen bir değer var mı  ? ",b not in liste) #b=15 ve 15 değeri listenin içerisinde bulunmamaktadır.

print("\nStringler içerisinde not in operatörü kullanımı : \n")
isim="Mehmet"
x="e"
y="a"
print("isim : ",isim)
print("isim adlı string değişkende e'ye karşılık gelmeyen bir değer var mı ? " ,x not in isim) #x="e" ve e değeri Mehmet içerisinde bulunmaktadır .
print("isim adlı string değişkende a'ya karşılık gelmeyen bir değer var mı ? " ,y not in isim) # y="a" ve a değeri Mehmet içerisinde bulunmamaktadır .