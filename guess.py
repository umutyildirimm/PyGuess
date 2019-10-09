import random

random = random.randint(1,20)
print('7 deneme hakkın var :)')

for i in range(7):
    number = int(input('1 ile 20 arasında bir sayı tahmin et: '))

    if(random>number):
        print('Daha büyük bir rakam :)')

    elif(random<number):
        print('Daha küçük bir rakam :)')

    else:
        print('Doğru!')
        break

        if(random!=number):
            print('Bilemedin! Sayı:', random)
