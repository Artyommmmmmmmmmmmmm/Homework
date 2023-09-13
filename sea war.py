
from random import choice
class Ship():
   def __init__(self):
      pass
   
   def small_ship(self, Z):
      try:
         pos = int(input('введите координату X(1 - 6):'))
         way = int(input('введите координату Y(1 - 6):'))
      except ValueError:
         print('Неверная позиция')
         self.small_ship(Z)

      if pos < 7 and pos > 0 and way > 0 and way < 7 and\
            Z.way_dict[way][pos].free:
         
         Z.ship_amount += 1
         Z.way_dict[way][pos].deploy()

         Z.way_dict[way-1][pos].ship_near()

         Z.way_dict[way+1][pos].ship_near()

         Z.way_dict[way][pos-1].ship_near()

         Z.way_dict[way][pos+1].ship_near()


         print('  1 2 3 4 5 6')
         print('1', *Z.way1[1:7])
         print('2', *Z.way2[1:7])
         print('3', *Z.way3[1:7])
         print('4', *Z.way4[1:7])
         print('5', *Z.way5[1:7])
         print('6', *Z.way6[1:7])

      else:
         print('Неверная позиция')
         self.small_ship(Z)

   def med_ship_hor(self, Z):
      try:
         pos = int(input('введите координату X(1 - 5):'))
         way = int(input('введите координату Y(1 - 6):'))
      except ValueError:
         print('Неверная позиция')
         self.med_ship_hor(Z)

      if pos < 6 and pos > 0 and way > 0 and way < 7 and\
            Z.way_dict[way][pos].free and\
            Z.way_dict[way][pos+1].free: 
         Z.ship_amount += 2
         Z.way_dict[way][pos].deploy()
         Z.way_dict[way][pos+1].deploy()

         Z.way_dict[way-1][pos].ship_near()
         Z.way_dict[way-1][pos+1].ship_near()   

         Z.way_dict[way+1][pos].ship_near()
         Z.way_dict[way+1][pos+1].ship_near()  

         Z.way_dict[way][pos-1].ship_near()
         Z.way_dict[way][pos+2].ship_near()


         print('  1 2 3 4 5 6')
         print('1', *Z.way1[1:7])
         print('2', *Z.way2[1:7])
         print('3', *Z.way3[1:7])
         print('4', *Z.way4[1:7])
         print('5', *Z.way5[1:7])
         print('6', *Z.way6[1:7])

      else:
         print('Неверная позиция')
         self.med_ship_hor(Z)

   def med_ship_vert(self, Z):
      try:
         pos = int(input('введите координату X(1 - 6):'))
         way = int(input('введите координату Y(1 - 5):'))
      except ValueError:
         print('Неверная позиция')
         self.med_ship_vert(Z)

      if way < 6 and way > 0 and pos > 0 and pos < 7 and\
            Z.way_dict[way][pos].free and\
            Z.way_dict[way+1][pos].free:
         Z.ship_amount += 2
         Z.way_dict[way][pos].deploy()
         Z.way_dict[way+1][pos].deploy()

         Z.way_dict[way][pos-1].ship_near()
         Z.way_dict[way+1][pos-1].ship_near()   

         Z.way_dict[way][pos+1].ship_near()
         Z.way_dict[way+1][pos+1].ship_near()  

         Z.way_dict[way-1][pos].ship_near()
         Z.way_dict[way+2][pos].ship_near()


         print('  1 2 3 4 5 6')
         print('1', *Z.way1[1:7])
         print('2', *Z.way2[1:7])
         print('3', *Z.way3[1:7])
         print('4', *Z.way4[1:7])
         print('5', *Z.way5[1:7])
         print('6', *Z.way6[1:7])

      else:
         print('Неверная позиция')
         self.med_ship_vert(Z)

   def big_ship_hor(self, Z):
      try:
         pos = int(input('введите координату X(2 - 5):'))
         way = int(input('введите координату Y(1 - 6):'))
      except ValueError:
         print('Неверная позиция')
         self.big_ship_hor(Z)

      if pos < 6 and pos > 1 and way > 0 and way < 7 and\
            Z.way_dict[way][pos-1].free and\
            Z.way_dict[way][pos].free and\
            Z.way_dict[way][pos+1].free: 
         Z.ship_amount += 3
         Z.way_dict[way][pos-1].deploy()
         Z.way_dict[way][pos].deploy()
         Z.way_dict[way][pos+1].deploy()

         Z.way_dict[way-1][pos-1].ship_near()
         Z.way_dict[way-1][pos].ship_near()
         Z.way_dict[way-1][pos+1].ship_near()   

         Z.way_dict[way+1][pos-1].ship_near()
         Z.way_dict[way+1][pos].ship_near()
         Z.way_dict[way+1][pos+1].ship_near()  

         Z.way_dict[way][pos-2].ship_near()
         Z.way_dict[way][pos+2].ship_near()

 
         print('  1 2 3 4 5 6')
         print('1', *Z.way1[1:7])
         print('2', *Z.way2[1:7])
         print('3', *Z.way3[1:7])
         print('4', *Z.way4[1:7])
         print('5', *Z.way5[1:7])
         print('6', *Z.way6[1:7])

      else:
         print('Неверная позиция')
         self.big_ship_hor(Z)


   def big_ship_vert(self, Z):
      try:
         pos = int(input('введите координату X(1 - 6):'))
         way = int(input('введите координату Y(2 - 5):'))
      except ValueError:
         print('Неверная позиция')
         self.big_ship_vert(Z)

      if way < 6 and way > 1 and pos > 0 and pos < 7 and\
            Z.way_dict[way-1][pos].free and\
            Z.way_dict[way][pos].free and\
            Z.way_dict[way+1][pos].free: 
         Z.ship_amount += 3
         Z.way_dict[way-1][pos].deploy()
         Z.way_dict[way][pos].deploy()
         Z.way_dict[way+1][pos].deploy()

         Z.way_dict[way-1][pos-1].ship_near()
         Z.way_dict[way][pos-1].ship_near()
         Z.way_dict[way+1][pos-1].ship_near()   

         Z.way_dict[way-1][pos+1].ship_near()
         Z.way_dict[way][pos+1].ship_near()
         Z.way_dict[way+1][pos+1].ship_near()  

         Z.way_dict[way-2][pos].ship_near()
         Z.way_dict[way+2][pos].ship_near()

 
         print('  1 2 3 4 5 6')
         print('1', *Z.way1[1:7])
         print('2', *Z.way2[1:7])
         print('3', *Z.way3[1:7])
         print('4', *Z.way4[1:7])
         print('5', *Z.way5[1:7])
         print('6', *Z.way6[1:7])

      else:
         print('Неверная позиция')
         self.big_ship_vert(Z)

   def bot_small_ship(self, Z):

      pos = choice([1, 2, 3, 4, 5, 6])
      way = choice([1, 2, 3, 4, 5, 6])

      if Z.way_dict[way][pos].free:
         bot.ship_amount += 1
         Z.way_dict[way][pos].deploy()

         Z.way_dict[way-1][pos].ship_near()

         Z.way_dict[way+1][pos].ship_near()

         Z.way_dict[way][pos-1].ship_near()

         Z.way_dict[way][pos+1].ship_near()


      else:
         self.bot_small_ship(Z)

   def bot_med_ship_hor(self, Z):

      pos = choice([1, 2, 3, 4, 5])
      way = choice([1, 2, 3, 4, 5, 6])


      if Z.way_dict[way][pos].free and\
            Z.way_dict[way][pos+1].free:
         bot.ship_amount += 2

         Z.way_dict[way][pos].deploy()
         Z.way_dict[way][pos+1].deploy()
 
         Z.way_dict[way-1][pos].ship_near()
         Z.way_dict[way-1][pos+1].ship_near()   

         Z.way_dict[way+1][pos].ship_near()
         Z.way_dict[way+1][pos+1].ship_near()  

         Z.way_dict[way][pos-1].ship_near()
         Z.way_dict[way][pos+2].ship_near()

      else:
         self.bot_med_ship_hor(Z)

   def bot_med_ship_vert(self, Z):

      pos = choice([1, 2, 3, 4, 5, 6])
      way = choice([1, 2, 3, 4, 5])


      if Z.way_dict[way][pos].free and\
            Z.way_dict[way+1][pos].free: 
         bot.ship_amount += 2
         Z.way_dict[way][pos].deploy()
         Z.way_dict[way+1][pos].deploy()

         Z.way_dict[way][pos-1].ship_near()
         Z.way_dict[way+1][pos-1].ship_near()   

         Z.way_dict[way][pos+1].ship_near()
         Z.way_dict[way+1][pos+1].ship_near()  

         Z.way_dict[way-1][pos].ship_near()
         Z.way_dict[way+2][pos].ship_near()




      else:
         self.bot_med_ship_vert(Z)

   def bot_big_ship_hor(self, Z):

      pos = choice([2, 3, 4, 5])
      way = choice([1, 2, 3, 4, 5, 6])


      if Z.way_dict[way][pos-1].free and\
            Z.way_dict[way][pos].free and\
            Z.way_dict[way][pos+1].free: 
         bot.ship_amount += 3
         Z.way_dict[way][pos-1].deploy()
         Z.way_dict[way][pos].deploy()
         Z.way_dict[way][pos+1].deploy()

         Z.way_dict[way-1][pos-1].ship_near()
         Z.way_dict[way-1][pos].ship_near()
         Z.way_dict[way-1][pos+1].ship_near()   

         Z.way_dict[way+1][pos-1].ship_near()
         Z.way_dict[way+1][pos].ship_near()
         Z.way_dict[way+1][pos+1].ship_near()  

         Z.way_dict[way][pos-2].ship_near()
         Z.way_dict[way][pos+2].ship_near()

 


      else:
         self.bot_big_ship_hor(Z)


   def bot_big_ship_vert(self, Z):

      pos = choice([1, 2, 3, 4, 5, 6])
      way = choice([2, 3, 4, 5])


      if Z.way_dict[way-1][pos].free and\
            Z.way_dict[way][pos].free and\
            Z.way_dict[way+1][pos].free: 
         bot.ship_amount += 3
         Z.way_dict[way-1][pos].deploy()
         Z.way_dict[way][pos].deploy()
         Z.way_dict[way+1][pos].deploy()

         Z.way_dict[way-1][pos-1].ship_near()
         Z.way_dict[way][pos-1].ship_near()
         Z.way_dict[way+1][pos-1].ship_near()   

         Z.way_dict[way-1][pos+1].ship_near()
         Z.way_dict[way][pos+1].ship_near()
         Z.way_dict[way+1][pos+1].ship_near()  

         Z.way_dict[way-2][pos].ship_near()
         Z.way_dict[way+2][pos].ship_near()


      else:
         self.bot_big_ship_vert(Z)


      
         
        

class Cord():
    def __init__(self):
        self.ship = '~'
        self.free = True
        self.ship_on = False

    def __str__(self):
        return self.ship
    
    def ship_near(self):
        self.free = False

    def deploy(self):
        self.ship = '■'
        self.ship_on = True
        self.free = False

    def lost(self):
        self.ship = '#'

    def miss(self):
        self.ship = 'T'

    def hit(self):
       self.ship = 'X'


class Sea():

   def __init__(self):
      self.shoot_list = []
      self.way0 = [Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord()]
      self.way1 = [Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord()]
      self.way2 = [Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord()]
      self.way3 = [Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord()]
      self.way4 = [Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord()]
      self.way5 = [Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord()]
      self.way6 = [Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord()]
      self.way7 = [Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord()]
      self.way_dict = {0:self.way0, 1:self.way1, 2:self.way2, 3:self.way3, 4:self.way4, 5:self.way5, 6:self.way6, 7:self.way7}
      self.point_list = []
      for i in range(1, 7):
         for n in range(1, 7):
            self.point_list.append((i, n))
      self.ship_amount = 0
   
   def get_field(self):
         print('  1 2 3 4 5 6', ' ', ' ', '  1 2 3 4 5 6',)
         print('1', *Z.way1[1:7], ' ', ' ', '1', *empty.way1[1:7])
         print('2', *Z.way2[1:7], ' ', ' ', '2', *empty.way2[1:7])
         print('3', *Z.way3[1:7], ' ', ' ', '3', *empty.way3[1:7])
         print('4', *Z.way4[1:7], ' ', ' ', '4', *empty.way4[1:7])
         print('5', *Z.way5[1:7], ' ', ' ', '5', *empty.way5[1:7])
         print('6', *Z.way6[1:7], ' ', ' ', '6', *empty.way6[1:7])

   def field_1_2_4(self):
      q1 = input('Введите Y если хотите разместить большой кораболь по горизонтали и N если по вертикали:')

      if q1 == 'Y':
         factory.big_ship_hor(self)
      else:
         factory.big_ship_vert(self)

      q2 = input('Введите Y если хотите разместить первый средний кораболь по горизонтали и N если по вертикали:')

      if q2 == 'Y':
         factory.med_ship_hor(self)
      else:
         factory.med_ship_vert(self)

      q3 = input('Введите Y если хотите разместить второй средний кораболь по горизонтали и N если по вертикали:')

      if q3 == 'Y':
         factory.med_ship_hor(self)
      else:
         factory.med_ship_vert(self)
      print('Далее разместите 4 малых корабля')
      factory.small_ship(self)
      print('второй')
      factory.small_ship(self)
      print('третий')
      factory.small_ship(self)
      print('четвёртый')
      factory.small_ship(self)

   def bot_field_1_2_4(self):
      q1 = choice(['Y', 'N'])
      if q1 == 'Y':
         factory.bot_big_ship_hor(self)
      else:
         factory.bot_big_ship_vert(self)

      q2 = choice(['Y', 'N'])

      if q2 == 'Y':
         factory.bot_med_ship_hor(self)
      else:
         factory.bot_med_ship_vert(self)

      q3 = choice(['Y', 'N'])

      if q3 == 'Y':
         factory.bot_med_ship_hor(self)
      else:
         factory.bot_med_ship_vert(self)

      factory.bot_small_ship(self)

      factory.bot_small_ship(self)

      factory.bot_small_ship(self)

      factory.bot_small_ship(self)


   def shoot(self):
      X = int(input('Введите X позицию выстрела(1 - 6):'))
      Y = int(input('Введите Y позицию выстрела(1 - 6):'))

      if X > 6 or X < 1 or Y > 6 or Y < 1:
         print('Неверная позиция')
         self.shoot()
      if (X, Y) in self.shoot_list:
         print('Вы уже стреляли по этой позиции')
         self.shoot()
      else:
         self.shoot_list.append((X, Y))
         if bot.way_dict[Y][X].ship_on:
            print('Попадание')
            empty.way_dict[Y][X].hit()
            bot.ship_amount -= 1
         else:
            print('Промах')
            empty.way_dict[Y][X].miss()

   def bot_shoot(self):
      X, Y = choice(self.point_list)
      self.point_list.remove((X, Y))


      if Z.way_dict[Y][X].ship_on:
         print('Противник попал')
         Z.way_dict[Y][X].lost()
         Z.ship_amount -= 1
      else:
         print('Противник промахнулся')
         Z.way_dict[Y][X].miss()




      

   



    

factory = Ship()
Z = Sea()
bot = Sea()
empty = Sea()



bot.bot_field_1_2_4()
Z.field_1_2_4()



game = True
while game:
   Z.get_field()

   Z.shoot()
   bot.bot_shoot()

   if bot.ship_amount == 0:
      print('Флотилия врага разбита!')
      Z.get_field()
      game = False
   if Z.ship_amount == 0:
      print('Наш флот разгромлен!')
      Z.get_field()
      game = False
