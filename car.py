import time

class Car:
    def Start(self):
        print('Машина заведена!')

    def Stop(self):
        print('Машина занлушена!')

    def Pochin(self):
        time.sleep(3)
        print('Ваша машина теперь в идеальном состоянии!')

    def Kond_on(self,on_or):
        m = 1
        a = int(input('сколько градусов вы хотите поставить?'))
        if a < 16:
            print('Минимальный градус в машиине 16 градусов!')
            a = 16
        elif a > 30:
            print('Максимальный градус в машине')
        time.sleep(2)
        print(f'В машине теперь включен кондиционер на {a} градусов')

    @property
    def Kond_off(self):

        print('Кондиционер выключен.')


class Mercedez(Car):
    name = 'AMG GT'
    mark = 'Mercedez'
    year = '2018'
    motor = '4.0'
    polomki = ['Сломана магнитола, левое боковое зеркало']

class BMW(Car):
    name = 'M8 Coupe'
    mark = 'BMW'
    year = '2019'
    motor = '4.4'
    polomki = ['Сломан двигатель, на бампере есть вмятина']

car = Car()

merc = Mercedez()
bmw = BMW()
print('Выберите машину:\n'
      '1.Mercedez\n'
      '2.BMW')
car_quest = int(input('1/2: '))
while True:
    if car_quest == 1:
        print('Что вы хотите сделать?\n'
              '1.Завести машину\n'
              '2.Заглушить машину\n'
              '3.Включить кондиционер\n'
              '4.Выключить кондиционер\n'
              '5.Починить машину\n'
              '6.Узнать название серии машины\n'
              '7.Узнать марку машины\n'
              '8.Узнать год машины\n'
              '9.Узнать обьем двигателя\n'
              '10.Узнать состояние машины\n'
              '11.Выход')
        que = int(input('>>>: '))
        if que == 1:
            car.Start()
            time.sleep(3)
        elif que == 2:
            car.Stop()
            time.sleep(3)
        elif que == 3:
            car.Kond_on()
            time.sleep(3)
        elif que == 4:
            car.Kond_off()
            time.sleep(3)
        elif que == 5:
            merc.polomki.pop()
            merc.polomki.append('Ваша машина в отличном состоянии!')
            print(merc.polomki)
            time.sleep(3)
        elif que == 6:
            print(merc.name)
            time.sleep(3)
        elif que == 7:
            print(merc.mark)
            time.sleep(3)
        elif que == 8:
            print(merc.year)
            time.sleep(3)
        elif que == 9:
            print(merc.motor)
            time.sleep(3)
        elif que == 10:
            print(merc.polomki)
            time.sleep(3)
        elif que == 11:
            break
        else:
            print('Такого варианта ответа нету!')





while True:
    if car_quest == 2:
        print('Что вы хотите сделать?\n'
              '1.Завести машину\n'
              '2.Заглушить машину\n'
              '3.Включить кондиционер\n'
              '4.Выключить кондиционер\n'
              '5.Починить машину\n'
              '6.Узнать название серии машины\n'
              '7.Узнать марку машины\n'
              '8.Узнать год машины\n'
              '9.Узнать обьем двигателя\n'
              '10.Узнать состояние машины\n'
              '11.Выход')

        que = int(input('>>>: '))
        if que == 1:
            car.Start()
            time.sleep(3)
        elif que == 2:
            car.Stop()
            time.sleep(3)
        elif que == 3:
            car.Kond_on()
            time.sleep(3)
        elif que == 4:
            car.Kond_off()
            time.sleep(3)
        elif que == 5:
            bmw.polomki.pop()
            bmw.polomki.append('Ваша машина в отличном состоянии!')
            time.sleep(3)
        elif que == 6:
            print(bmw.name)
            time.sleep(3)
        elif que == 7:
            print(bmw.mark)
            time.sleep(3)
        elif que == 8:
            print(bmw.year)
            time.sleep(3)
        elif que == 9:
            print(bmw.motor)
            time.sleep(3)
        elif que == 10:
            print(bmw.polomki)
            time.sleep(3)
        elif que == 11:
            exit()
        else:
            print('Такого варианта ответа нету!')


