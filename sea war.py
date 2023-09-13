
class Ship():
   def __init__(self):
      pass
   
   def small_ship(self, Z, bot=True):
      try:
         pos = int(input('введите координату X(1 - 6):'))
         way = int(input('введите координату Y(1 - 6):'))
      except ValueError:
         print('Неверная позиция')
         self.small_ship(Z)

      if pos < 7 and pos > 0 and way > 0 and way < 7 and\
            Z.way_dict[way][pos].free:

         Z.way_dict[way][pos].deploy()

         Z.way_dict[way-1][pos].ship_near()

         Z.way_dict[way+1][pos].ship_near()

         Z.way_dict[way][pos-1].ship_near()

         Z.way_dict[way][pos+1].ship_near()

         if bot:
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

   def med_ship_hor(self, Z, bot=True):
      try:
         pos = int(input('введите координату X(1 - 5):'))
         way = int(input('введите координату Y(1 - 6):'))
      except ValueError:
         print('Неверная позиция')
         self.med_ship_hor(Z)

      if pos < 6 and pos > 0 and way > 0 and way < 7 and\
            Z.way_dict[way][pos].free and\
            Z.way_dict[way][pos+1].free: 
         Z.way_dict[way][pos].deploy()
         Z.way_dict[way][pos+1].deploy()

         Z.way_dict[way-1][pos].ship_near()
         Z.way_dict[way-1][pos+1].ship_near()   

         Z.way_dict[way+1][pos].ship_near()
         Z.way_dict[way+1][pos+1].ship_near()  

         Z.way_dict[way][pos-1].ship_near()
         Z.way_dict[way][pos+2].ship_near()

         if bot:
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

   def med_ship_vert(self, Z, bot=True):
      try:
         pos = int(input('введите координату X(1 - 6):'))
         way = int(input('введите координату Y(1 - 5):'))
      except ValueError:
         print('Неверная позиция')
         self.med_ship_vert(Z)

      if way < 6 and way > 0 and pos > 0 and pos < 7 and\
            Z.way_dict[way][pos].free and\
            Z.way_dict[way+1][pos].free: 
         Z.way_dict[way][pos].deploy()
         Z.way_dict[way+1][pos].deploy()

         Z.way_dict[way][pos-1].ship_near()
         Z.way_dict[way+1][pos-1].ship_near()   

         Z.way_dict[way][pos+1].ship_near()
         Z.way_dict[way+1][pos+1].ship_near()  

         Z.way_dict[way-1][pos].ship_near()
         Z.way_dict[way+2][pos].ship_near()

         if bot:
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

   def big_ship_hor(self, Z, bot=True):
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

         if bot:
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


   def big_ship_vert(self, Z, bot=True):
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

         if bot:
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
        self.ship = 'X'

    def miss(self):
        self.ship = 'T'

    def hit(self):
       self.ship = '#'


class Sea():
   def __init__(self):
      self.shoots_x = []
      self.shoots_y = []
      self.way0 = [Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord()]
      self.way1 = [Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord()]
      self.way2 = [Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord()]
      self.way3 = [Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord()]
      self.way4 = [Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord()]
      self.way5 = [Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord()]
      self.way6 = [Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord()]
      self.way7 = [Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord(), Cord()]
      self.way_dict = {0:self.way0, 1:self.way1, 2:self.way2, 3:self.way3, 4:self.way4, 5:self.way5, 6:self.way6, 7:self.way7}


   def field_1_2_4(self, field):
      q1 = input('Введите Y если хотите разместить большой кораболь по горизонтали и N если по вертикали:')

      if q1 == 'Y':
         factory.big_ship_hor(field)
      else:
         factory.big_ship_vert(field)

      q2 = input('Введите Y если хотите разместить первый средний кораболь по горизонтали и N если по вертикали:')

      if q2 == 'Y':
         factory.med_ship_hor(field)
      else:
         factory.med_ship_vert(field)

      q3 = input('Введите Y если хотите разместить второй средний кораболь по горизонтали и N если по вертикали:')

      if q3 == 'Y':
         factory.med_ship_hor(field)
      else:
         factory.med_ship_vert(field)
      print('Далее разместите 4 малых корабля')
      factory.small_ship(field)
      print('второй')
      factory.small_ship(field)
      print('третий')
      factory.small_ship(field)
      print('четвёртый')
      factory.small_ship(field)

   def shoot(self):
      X = int(input('Введите X позицию выстрела'))
      Y = int(input('Введите Y позицию выстрела'))
      if X in self.shoots_x and Y in self.shoots_y:
         print('Вы уже стреляли по этой позиции')
         self.shoot(bot)
      else:
         self.shoots_x.append(X)
         self.shoots_y.append(Y)
         if bot.way_dict[Y][X].ship_on:
            print('Попадание')
            Z.way_dict[Y][X].hit()
         else:
            print('Промах')
            Z.way_dict[Y][X].miss()

            print('  1 2 3 4 5 6')
            print('1', *Z.way1[1:7])
            print('2', *Z.way2[1:7])
            print('3', *Z.way3[1:7])
            print('4', *Z.way4[1:7])
            print('5', *Z.way5[1:7])
            print('6', *Z.way6[1:7])


      

   



    

factory = Ship()
Z = Sea()
bot = Sea()

Z.shoot()



# Z.field_1_2_4(Z)
# print('  1 2 3 4 5 6')
# print('1', *Z.way1[1:7])
# print('2', *Z.way2[1:7])
# print('3', *Z.way3[1:7])
# print('4', *Z.way4[1:7])
# print('5', *Z.way5[1:7])
# print('6', *Z.way6[1:7])
        
    

