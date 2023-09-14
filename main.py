from Factories import beg_factory
from Factories import exp_factory
import hero
import map
import random
import check_input

def main():
  hero_name = str(input("What is your name, traveler? "))
  user = hero.Hero(hero_name)
  user_factory = check_input.get_int_range("Difficuly:\n1.Beginner\n2.Expert\n", 1, 2)
  if user_factory == 1:
    fact = beg_factory.BeginnerFactory()
  elif user_factory == 2:
    fact = exp_factory.ExpertFactory()
  map1 = map.Map()
  lvlCounter = 1
  game_switch = True
  while game_switch != False:
    print(user)
    map1.reveal(user.loc)
    print(map1.show_map(user.loc))
    user_choice = check_input.get_int_range("1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit\nEnter choice: ", 1, 5)

    if user_choice == 1:
      outcome = user.go_north()
      map1.reveal(user.loc)
      if outcome == "x":
        print("You can't go that way...")
      elif outcome == "m":
        enemy1 = fact.create_random_enemy()
        print("You encounter a " + str(enemy1))
        while True:
          choice = check_input.get_int_range("1. Attack " + enemy1.name + "\n2. Run Away\nEnter choice: ", 1 ,2)
          if choice == 1:
            userAttack = user.attack(enemy1)
            print(userAttack)
            if enemy1.hp == 0:
              print("You have slain a " + str(enemy1.name) + "\n")
              map1.remove_at_loc(user.loc)
              break
            enemyAttack = enemy1.attack(user)
            print(enemyAttack)
            if user.hp == 0:
              print("You have died")
              game_switch = False
              break
          if choice == 2:
            print("You ran away!")
            while True:
              random_direction = random.randint(1,4)
              if random_direction == 1:
                direction = user.go_north()
                if direction == "x":
                  continue
                else:
                  break
              elif random_direction == 2:
                direction = user.go_south()
                if direction == "x":
                  continue
                else:
                  break
              elif random_direction == 3:
                direction = user.go_east()
                if direction == "x":
                  continue
                else:
                  break
              elif random_direction == 4:
                direction = user.go_west()
                if direction == "x":
                  continue
                else:
                  break
            break
            
              
      elif outcome == "i":
        user.heal()
        map1.remove_at_loc(user.loc)
        print("You found a Health Potion! You drink it to restore your health.")        
      elif outcome == "n":
        print("There is nothing here...")
      elif outcome == "s":
        print("You wounded up back at the start.")
      elif outcome == "f":
        print("Congratulations! You found the stairs to the next floor of the dungeon.")
        lvlCounter += 1
        if lvlCounter == 4:
          lvlCounter = 1
        map1.load_map(lvlCounter)
        
        
      
    
    if user_choice == 2:
      outcome = user.go_south()
      map1.reveal(user.loc)
      if outcome == "x":
        print("You can't go that way...")
      elif outcome == "m":
        enemy1 = fact.create_random_enemy()
        print("You encounter a " + str(enemy1))
        while True:
          choice = check_input.get_int_range("1. Attack " + enemy1.name + "\n2. Run Away\nEnter choice: ", 1 ,2)
          if choice == 1:
            userAttack = user.attack(enemy1)
            print(userAttack)
            if enemy1.hp == 0:
              print("You have slain a " + str(enemy1.name) + "\n")
              map1.remove_at_loc(user.loc)
              break
            enemyAttack = enemy1.attack(user)
            print(enemyAttack)
            if user.hp == 0:
              print("You have died")
              game_switch = False
              break
          if choice == 2:
            print("You ran away!")
            while True:
              random_direction = random.randint(1,4)
              if random_direction == 1:
                direction = user.go_north()
                if direction == "x":
                  continue
                else:
                  break
              elif random_direction == 2:
                direction = user.go_south()
                if direction == "x":
                  continue
                else:
                  break
              elif random_direction == 3:
                direction = user.go_east()
                if direction == "x":
                  continue
                else:
                  break
              elif random_direction == 4:
                direction = user.go_west()
                if direction == "x":
                  continue
                else:
                  break
            break
      elif outcome == "i":
        user.heal()
        map1.remove_at_loc(user.loc)
        print("You found a Health Potion! You drink it to restore your health.")        
      elif outcome == "n":
        print("There is nothing here...")
      elif outcome == "s":
        print("You wounded up back at the start.")
      elif outcome == "f":
        print("Congratulations! You found the stairs to the next floor of the dungeon.")
        lvlCounter += 1
        if lvlCounter == 4:
          lvlCounter = 1
        map1.load_map(lvlCounter)

    if user_choice == 3:
      outcome = user.go_east()
      map1.reveal(user.loc)
      if outcome == "x":
        print("You can't go that way...")
      elif outcome == "m":
        enemy1 = fact.create_random_enemy()
        print("You encounter a " + str(enemy1))
        while True:
          choice = check_input.get_int_range("1. Attack " + enemy1.name + "\n2. Run Away\nEnter choice: ", 1 ,2)
          if choice == 1:
            userAttack = user.attack(enemy1)
            print(userAttack)
            if enemy1.hp == 0:
              print("You have slain a " + str(enemy1.name) + "\n")
              map1.remove_at_loc(user.loc)
              break
            enemyAttack = enemy1.attack(user)
            print(enemyAttack)
            if user.hp == 0:
              print("You have died")
              game_switch = False
              break
          if choice == 2:
            print("You ran away!")
            while True:
              random_direction = random.randint(1,4)
              if random_direction == 1:
                direction = user.go_north()
                if direction == "x":
                  continue
                else:
                  break
              elif random_direction == 2:
                direction = user.go_south()
                if direction == "x":
                  continue
                else:
                  break
              elif random_direction == 3:
                direction = user.go_east()
                if direction == "x":
                  continue
                else:
                  break
              elif random_direction == 4:
                direction = user.go_west()
                if direction == "x":
                  continue
                else:
                  break
            break
              
              
      elif outcome == "i":
        user.heal()
        map1.remove_at_loc(user.loc)
        print("You found a Health Potion! You drink it to restore your health.")        
      elif outcome == "n":
        print("There is nothing here...")
      elif outcome == "s":
        print("You wounded up back at the start.")
      elif outcome == "f":
        print("Congratulations! You found the stairs to the next floor of the dungeon.")
        lvlCounter += 1
        if lvlCounter == 4:
          lvlCounter = 1
        map1.load_map(lvlCounter)

    if user_choice == 4:
      outcome = user.go_west()
      map1.reveal(user.loc)
      if outcome == "x":
        print("You can't go that way...")
      elif outcome == "m":
        enemy1 = fact.create_random_enemy()
        print("You encounter a " + str(enemy1))
        while True:
          choice = check_input.get_int_range("1. Attack " + enemy1.name + "\n2. Run Away\nEnter choice: ", 1 ,2)
          if choice == 1:
            userAttack = user.attack(enemy1)
            print(userAttack)
            if enemy1.hp == 0:
              print("You have slain a " + str(enemy1.name) + "\n")
              map1.remove_at_loc(user.loc)
              break
            enemyAttack = enemy1.attack(user)
            print(enemyAttack)
            if user.hp == 0:
              print("You have died")
              game_switch = False
              break
          if choice == 2:
            print("You ran away!")
            while True:
              random_direction = random.randint(1,4)
              if random_direction == 1:
                direction = user.go_north()
                if direction == "x":
                  continue
                else:
                  break
              elif random_direction == 2:
                direction = user.go_south()
                if direction == "x":
                  continue
                else:
                  break
              elif random_direction == 3:
                direction = user.go_east()
                if direction == "x":
                  continue
                else:
                  break
              elif random_direction == 4:
                direction = user.go_west()
                if direction == "x":
                  continue
                else:
                  break
            break
            
      elif outcome == "i":
        user.heal()
        map1.remove_at_loc(user.loc)
        print("You found a Health Potion! You drink it to restore your health.")        
      elif outcome == "n":
        print("There is nothing here...")
      elif outcome == "s":
        print("You wounded up back at the start.")
      elif outcome == "f":
        print("Congratulations! You found the stairs to the next floor of the dungeon.")
        lvlCounter += 1
        if lvlCounter == 4:
          lvlCounter = 1
        map1.load_map(lvlCounter)
    
    if user_choice == 5:
      print("Game over.")
      break
  
main()
