
import random as rd

from inflection import pluralize
from rules import order, rotate
from player import uno
import player
#import LinkedList

players = ['bruce','ke']
players_obj = []



if __name__ == '__main__': 
    order_dict = order(players)
    print('order of this game is')
    print(order_dict)
    players_obj = [uno(i) for i in players]
    
    for i in players_obj:
        uno.initdraw(i)
  
    while (0 not in [len(i.onhand) for i in players_obj]):

        for i in range(len(players_obj)):
            print(players_obj[i])
            uno.play(players_obj[i])
            if players_obj[i].decision == 'Play':
                if players_obj[i].plc == '+4':
                        if i == len(players_obj)-1:
                        
                            players_obj = rotate(players_obj,i)
                            
                            players_obj[1].onhand += [*rd.choices(player.cards,k=4)]
                        else:    
                            players_obj[i+1].onhand += [*rd.choices(player.cards,k=4)]

                elif players_obj[i].plc in ['+2g','+2r','+2y']:
                        if i == len(players_obj)-1:
                            
                            players_obj = rotate(players_obj,i)
                            
                            players_obj[1].onhand += [*rd.choices(player.cards,k=2)]
                        else:
                            players_obj[i+1].onhand += [*rd.choices(player.cards,k=2)]
        
        
    print('Congradulations, u the winner', players_obj[[len(i.onhand) for i in players_obj].index(0)].ID)


    
