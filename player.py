import random as rd
import rules
cards = ['1g','2g','3g','1r','2r','3r','1y','2y','3y','reverse','ban','+4','+2g','+2r',"+2y"]
cards_on_stage = None
class uno:
    
    def __init__(self,ID):
        self.ID = ID
    def initdraw(self):
        onhand = [*rd.choices(cards,k=7)]
        self.onhand = onhand
        self.last = None

    def play(self):
        print("Player  {}  This is your card on hand, {}".format(self.ID,self.onhand))
        global cards_on_stage
        print('card on stage now is    ---------->    ',cards_on_stage)

        decision = input("Play or draw                       ")
        self.decision = decision
        if decision == 'Play':
            print('which card u want to use, please specify the order of one you want from left to right ')
            plc = input() 
            if plc == '':
                print('plz make your choice')
            plc = self.onhand[int(plc)]
            print('You select   ' ,plc)
            
            if rules.order_legal(cards_on_stage,plc):
                self.plc = plc
                self.onhand.pop(self.onhand.index(self.plc))
                cards_on_stage = plc
            else:
                print('you ruin this game, go read the rules and reselect')
                print('I give you another chance.')
                uno.play(self) 
                

        elif decision == 'draw':
            draw = [*rd.choices(cards,k=1)]
            self.plc = None
            self.onhand = self.onhand + draw
            print(self.onhand)
