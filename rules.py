def order(lst): 
   return {i+1:lst[i] for i in range(len(lst))}

def order_legal(last,next):
        if last == None:
            return True
        elif (next not in ['+4','ban','+2r','+2g','+2y','reverse'] and last not in ['+4','ban','+2r','+2g','+2y','reverse']):
            temp_list = [char for char in next if char in [char for char in last]]
            if temp_list != []:
                return True
            else:
                return False
        elif (next == '+4'):
            return True 
        elif (last == 'ban') and (next == 'ban'):
            return True
        elif (('g' in last) or ('+2' in last)) and (next == '+2g'):
            return True
        elif (('r' in last) or ('+2' in last)) and (next == '+2r'):
            return True
        elif (('y' in last) or ('+2' in last)) and (next == '+2y'):
            return True
        else:
            return False

def judge(name):
    global card_on_stage
    if card_on_stage == None:
        card_on_stage = name.plc
        name.onhand.remove(name.plc)
    elif (card_on_stage != None) and (order_legal(name.plc,card_on_stage)):
        card_on_stage = name.plc
        name.onhand.remove(name.plc)
    else:
        print('not legal, please select again')
        
'''
poc -> point of change (index not value)
lis -> list
'''

def reverse(poc,lis):
    return [lis[i] for i in range(lis[lis == poc]-1,-lis[lis == poc],-1)]
    

def rotate(l,i):
    if i == 0:
        return l
    else:
        temp1 = l[0:i]
        temp2 = l[i:len(l)]
        return temp2 + temp1
    