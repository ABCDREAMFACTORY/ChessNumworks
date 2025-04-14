from math import *
from kandinsky import *
from ion import *
from time import sleep
from pieceschess import *
from kandinsky import draw_string as d
fill_rect(0,0,320,230,color(146,24,36))

def p(i,j):
  if (i+j)%2 == 1:
      fill_rect(10+(j*25),10+(i*25),25,25,color(105,146,62))
  else:
      fill_rect(10+(j*25),10+(i*25),25,25,color(190,199,212))
for i in range(8):
  for j in range(8):
    p(i,j)
cor = [0,0]
global tower,pawns,knight,fool,queen,king
def printPieces(list,i,j,color):
  if j > 9:
    mult = 3
    add = 0
    if list == tower:
      mult = 2
      add = 4
  elif pieces[i][j][0] == "t":
    mult = 2
    add = 4
  else:
    mult = 3
    add = 0
  for k in range(len(list)):
    for l in range(len(list[0])):
      if list[k][l]:
        fill_rect(10+j*25+l*mult,10+i*25+k*mult+add,mult,mult,color)
def show(pieces):
  for i in range(8):
    for j in range(8):
      if pieces[i][j] != "":
        pPut(pieces,i,j)
def pPut(pieces,i,j):        
  if pieces[i][j][1] == "b":
    color = (255,255,255)
  if pieces[i][j][1] == "n":
    color = (0,0,0)
  if pieces[i][j][0] == "t":
    printPieces(tower,i,j,color)
  elif pieces[i][j][0] == "p":
    printPieces(pawns,i,j,color)
  elif pieces[i][j][0] == "c":
    printPieces(cavalier,i,j,color)
  elif pieces[i][j][0] == "f":
    printPieces(fool,i,j,color)
  elif pieces[i][j][0] == "q":
    printPieces(queen,i,j,color)
  elif pieces[i][j][0] == "k":
    printPieces(king,i,j,color)
        

def verif(pieces,s,cor,hasJump):
  
  if hasJump[0] != -1:
    if pieces[hasJump[1]][hasJump[0]][1] == "n":
      if turn%2 == 1:
        hasJump[0] = -1
    elif pieces[hasJump[1]][hasJump[0]][1] == "b":
      if turn%2 == 0:
        hasJump[0] = -1
        
  list = []
  
  if pieces[s[1]][s[0]][0] == "k":
    if selec[1] > 0: 
      list.append([s[1]-1,s[0]])
    if selec[0] < 7: 
      list.append([s[1],s[0]+1])
    if s[1] < 7 and s[0] < 7: 
      list.append([s[1]+1,s[0]+1])
    if s[1] > 0 and s[0] > 0:
      list.append([s[1]-1,s[0]-1])
    if s[1] < 7 and s[0] > 0:
      list.append([s[1]+1,s[0]-1])
    if s[1] > 0 and s[0] < 7:
      list.append([s[1]-1,s[0]+1])
    if selec[1] < 7:
      list.append([s[1]+1,s[0]])
    if selec[0] > 0:
      list.append([s[1],s[0]-1])
    if pieces[s[1]][s[0]][2] == "f":
      if s[0] == 4 and s[1] == 7:
        if pieces[s[1]][s[0]+3] != "":
          if pieces[s[1]][s[0]+3][0] == "t":
            if pieces[s[1]][s[0]+3][2] == "f":
              if pieces[s[1]][s[0]+1] == "" and pieces[s[1]][s[0]+2] == "":
                list.append([s[1],s[0]+2])
        if pieces[s[1]][s[0]-4] != "":
          if pieces[s[1]][s[0]-4][0] == "t":
            if pieces[s[1]][s[0]-4][2] == "f":
              if pieces[s[1]][s[0]-1] == "" and pieces[s[1]][s[0]-2] == "" and pieces[s[1]][s[0]-3] == "":
                list.append([s[1],s[0]-2])
              
      if s[0] == 4 and s[1] == 0:
        if pieces[s[1]][s[0]+3] != "":
          if pieces[s[1]][s[0]+3][0] == "t":
            if pieces[s[1]][s[0]+3][2] == "f":
              if pieces[s[1]][s[0]+1] == "" and pieces[s[1]][s[0]+2] == "":
                list.append([s[1],s[0]+2])
        if pieces[s[1]][s[0]-4][0] != "":
          if pieces[s[1]][s[0]-4][0] == "t":
            if pieces[s[1]][s[0]-4][2] == "f":
              if pieces[s[1]][s[0]-1] == "" and pieces[s[1]][s[0]-2] == "" and pieces[s[1]][s[0]-3] == "":
                list.append([s[1],s[0]-2])
    
  if pieces[s[1]][s[0]][0] == "t" or pieces[s[1]][s[0]][0] == "q":
    for k in range(s[1]):
      list.append([s[1]-(k+1),s[0]])
      if pieces[s[1]-(k+1)][s[0]] != "":
        print(str(list))
        break
    for k in range(7-s[1]):
      list.append([s[1]+(k+1),s[0]])
      if pieces[s[1]+(k+1)][s[0]] != "":
        print(str(list))
        break
    for k in range(7-s[0]):
      list.append([s[1],s[0]+(k+1)])
      if pieces[s[1]][s[0]+(k+1)] != "":
        print(str(list))
        break
    for k in range(s[0]):
      list.append([s[1],s[0]-(k+1)])
      if pieces[s[1]][s[0]-(k+1)] != "":
        print(str(list))
        break
  elif pieces[s[1]][s[0]][0] == "p":
    if pieces[s[1]][s[0]][1] == "b":
      if pieces[s[1]-1][s[0]] == "":
        list.append([s[1]-1,s[0]])
        if s[1] == 6 and pieces[s[1]-2][s[0]] == "":
          list.append([s[1]-2,s[0]])
      if s[0]<7:
        if pieces[s[1]-1][s[0]+1] != "":
          list.append([s[1]-1,s[0]+1])
        if pieces[s[1]][s[0]+1] != "" and pieces[s[1]][s[0]+1][0] == "p" and pieces[s[1]][s[0]+1][1] == "n" and s[1] == hasJump[1] and s[0]+1 == hasJump[0]:
          list.append([s[1]-1,s[0]+1])
      if selec[0]>0:
        if pieces[s[1]-1][s[0]-1] != "":
          list.append([s[1]-1,s[0]-1])
        if pieces[s[1]][s[0]-1] != "" and pieces[s[1]][s[0]-1][0] == "p" and pieces[s[1]][s[0]-1][1] == "n" and s[1] == hasJump[1] and s[0]-1 == hasJump[0]:
          list.append([s[1]-1,s[0]-1])
          
    if pieces[s[1]][s[0]][1] == "n":
      if pieces[s[1]+1][s[0]] == "":
        list.append([s[1]+1,s[0]])
        if s[1] == 1 and pieces[s[1]+2][s[0]] == "":
          list.append([s[1]+2,s[0]])
          
      if selec[0]<7:
        if pieces[s[1]+1][s[0]+1] != "":
          list.append([s[1]+1,s[0]+1])
        if pieces[s[1]][s[0]+1] != "" and pieces[s[1]][s[0]+1][0] == "p" and pieces[s[1]][s[0]+1][1] == "b" and s[1] == hasJump[1] and s[0]+1 == hasJump[0]:
          list.append([s[1]+1,s[0]+1])
      if selec[0]>0:
        if pieces[s[1]+1][s[0]-1] != "":
          list.append([s[1]+1,s[0]-1])
        if pieces[s[1]][s[0]-1] != "" and pieces[s[1]][s[0]-1][0] == "p" and pieces[s[1]][s[0]-1][1] == "b" and s[1] == hasJump[1] and s[0]-1 == hasJump[0]:
          list.append([s[1]+1,s[0]-1])
      
  elif pieces[s[1]][s[0]][0] == "c":
    for k in range(-2,2):
      if k > -1:
        k += 1
      for l in range(-2,2):
        if l > -1:
          l += 1
        if k != l and k != -l and -k != l:
          if k + s[1] >= 0 and k + s[1] <=7 and l + s[0] <=7 and l + s[0]>=0:
            list.append([k+s[1],l+s[0]])
            print(str(list))

  if pieces[s[1]][s[0]][0] == "f" or pieces[s[1]][s[0]][0] == "q":
    k = 0
    while s[1]-(k+1) >=0 and s[0]-(k+1) >= 0:
      list.append([s[1]-(k+1),s[0]-(k+1)])
      if pieces[s[1]-(k+1)][s[0]-(k+1)] != "":
        print(str(list))
        break
      k += 1
      print(str(list))
    k = 0
    while s[1]+(k+1) <=7 and s[0]+(k+1) <= 7:
      list.append([s[1]+(k+1),s[0]+(k+1)])
      if pieces[s[1]+(k+1)][s[0]+(k+1)] != "":
        print(str(list))
        break
      k += 1
    k = 0
    while s[1]-(k+1) >=0 and s[0]+(k+1) <= 7:
      list.append([s[1]-(k+1),s[0]+(k+1)])
      if pieces[s[1]-(k+1)][s[0]+(k+1)] != "":
        print(str(list))
        break
      k += 1
    k = 0
    while s[1]+(k+1) <=7 and s[0]-(k+1) >= 0:
      list.append([s[1]+(k+1),s[0]-(k+1)])
      if pieces[s[1]+(k+1)][s[0]-(k+1)] != "":
        print(str(list))
        break
      k += 1
  for k in range(len(list)):
    if pieces[list[k][0]][list[k][1]] == "" or pieces[s[1]][s[0]][1] == "b" and pieces[list[k][0]][list[k][1]][1] == "n" or pieces[s[1]][s[0]][1] == "n" and pieces[list[k][0]][list[k][1]][1] == "b":
      v = cursor([list[k][1],list[k][0]],(255,255,255))
      v.draw()
  return list

def upgrade(col):
  fill_rect(10+(10*25),10+(5*25),25,25,color(105,146,62))
  fill_rect(10+(11*25),10+(6*25),25,25,color(105,146,62))
  fill_rect(10+(11*25),10+(5*25),25,25,color(190,199,212))
  fill_rect(10+(10*25),10+(6*25),25,25,color(190,199,212))
  printPieces(tower,5,10,col)
  printPieces(queen,6,11,col)
  printPieces(cavalier,5,11,col)
  printPieces(fool,6,10,col)
  keyPressed = False
  p(c.cor[1],c.cor[0])
  pPut(pieces,c.cor[1],c.cor[0])
  p(selec[1],selec[0])
  if col == (0,0,0):
    co = "n"
  else:
    co = "b"
  while keyPressed == False:
    if keydown(KEY_ONE):
      pieces[c.cor[1]][c.cor[0]] = "t" + co + "f"
      keyPressed = True
    elif keydown(KEY_TWO):
      pieces[c.cor[1]][c.cor[0]] = "c" + co
      keyPressed = True
    elif keydown(KEY_THREE):
      pieces[c.cor[1]][c.cor[0]] = "f" + co
      keyPressed = True
    elif keydown(KEY_FOUR):
      pieces[c.cor[1]][c.cor[0]] = "q" + co
      keyPressed = True
class cursor:
  def __init__(self,cor,col):
    self.cor = cor
    self.col = col
  def draw(self):
    for i in range(24):
      fill_rect(10+self.cor[0]*25+i,10+self.cor[1]*25,2,2,self.col)  
      fill_rect(10+self.cor[0]*25+i,10+self.cor[1]*25+23,2,2,self.col)
      fill_rect(10+self.cor[0]*25,10+self.cor[1]*25+i,2,2,self.col)
      fill_rect(10+self.cor[0]*25+23,10+self.cor[1]*25+i,2,2,self.col)
                  
  def remove(self):
      if (self.cor[0]+self.cor[1])%2 == 1:
        fill_rect(10+(self.cor[0]*25),10+(self.cor[1]*25),25,25,color(105,146,62))
      else:
        fill_rect(10+(self.cor[0]*25),10+(self.cor[1]*25),25,25,color(190,199,212))
      if pieces[self.cor[1]][self.cor[0]] != "":
        pPut(pieces,self.cor[1],self.cor[0])
  def move(self):
    if keydown(KEY_DOWN) == True and self.cor[1] < 7:
      while keydown(KEY_DOWN) == True:
        sleep(0.01)
      c.mv()
      self.cor = [self.cor[0],self.cor[1]+1]
      c.draw()
    if keydown(KEY_UP) == True and self.cor[1] > 0:
      while keydown(KEY_UP) == True:
        sleep(0.01)
      c.mv()
      self.cor = [self.cor[0],self.cor[1]-1]
      c.draw()
    if keydown(KEY_RIGHT) == True and self.cor[0] < 7:
      while keydown(KEY_RIGHT) == True:
        sleep(0.01)
      c.mv()
      self.cor = [self.cor[0]+1,self.cor[1]]
      c.draw()
    if keydown(KEY_LEFT) == True and self.cor[0] > 0:
      while keydown(KEY_LEFT) == True:
        sleep(0.01)
      c.mv()
      self.cor = [self.cor[0]-1,self.cor[1]]
      c.draw()
  def mv(self):
    c.remove()
    if listv != []:
      for k in range(len(listv)):
        if [listv[k][1],listv[k][0]] == c.cor:
          if pieces[listv[k][0]][listv[k][1]] == "" or pieces[selec[1]][selec[0]][1] == "b" and pieces[listv[k][0]][listv[k][1]][1] == "n" or pieces[selec[1]][selec[0]][1] == "n" and pieces[listv[k][0]][listv[k][1]][1] == "b":
            v = cursor([listv[k][1],listv[k][0]],(255,255,255))
            v.draw()         

c = cursor(cor,(252,3,28))
show(pieces)
c.draw()
cpt = 0
hasJump = [-1,-1]
global turn
turn = 0
d("White",230,0,(255,255,255),(146,24,36))
d("Turn " + str(turn),225,15,(255,255,255),(146,24,36)) 
d("Select:OK",212,80,(255,255,255),(146,24,36))
d("Unselect:0",212,100,(255,255,255),(146,24,36))
listv = []
rock = "f"
while True:
  cor = c.move()
  if keydown(KEY_ZERO) == True:
    while keydown(KEY_ZERO) == True:
      sleep(0.01)
    for k in range(len(listv)):
      if (listv[k][0]+listv[k][1])%2 == 1:
        col = (105,146,62)
      else:
        col = (190,199,212) 
            
      v = cursor([listv[k][1],listv[k][0]],col)
      v.remove()
    listv = []
    cpt = 0
    
    
  if keydown(KEY_OK):
    while keydown(KEY_OK):
      sleep(0.01)
    if cpt == 0 and pieces[c.cor[1]][c.cor[0]] != "" and turn%2 == 0 and pieces[c.cor[1]][c.cor[0]][1] == "b" or cpt == 0 and pieces[c.cor[1]][c.cor[0]] != "" and turn%2 == 1 and pieces[c.cor[1]][c.cor[0]][1] == "n":
      fill_rect(210,200,110,17,(146,24,36))
      selec = c.cor
      print(selec)
      cpt = 1
      listv = verif(pieces,selec,c.cor,hasJump)
    elif cpt == 1:
      if pieces[c.cor[1]][c.cor[0]] == "" or pieces[selec[1]][selec[0]][1] != pieces[c.cor[1]][c.cor[0]][1]:
        for k in range(len(listv)):
          if [c.cor[1],c.cor[0]] == listv[k]:
            if pieces[selec[1]][selec[0]][0] == "k":
              if selec[1] == 7 or selec[1] == 0:
                if selec[0] == 4 and listv[k][1] == c.cor[0]:
                  if c.cor[0] == 6 and c.cor[1] == selec[1] or c.cor[0] == 2 and c.cor[1] == selec[1]: 
                    if 6 == listv[k][1]:
                      pieces[selec[1]][7],pieces[c.cor[1]][5] = "",pieces[selec[1]][7]
                      p(selec[1],7)          
                    if 2 == listv[k][1]:
                      pieces[selec[1]][0],pieces[c.cor[1]][3] = "",pieces[selec[1]][0]
                      p(selec[1],0)  
            if pieces[selec[1]][selec[0]][0] == "k" or pieces[selec[1]][selec[0]][0] == "t":
               pieces[selec[1]][selec[0]] = pieces[selec[1]][selec[0]][0] + pieces[selec[1]][selec[0]][1] + "t"
                 
            pieces[selec[1]][selec[0]],pieces[c.cor[1]][c.cor[0]] = "",pieces[selec[1]][selec[0]]
            if pieces[c.cor[1]][c.cor[0]][0] == "p":
              if pieces[c.cor[1]][c.cor[0]][1] == "n": 
                if c.cor[1] == 3 and selec[1] == 1:
                  hasJump = [c.cor[0],c.cor[1]]
                elif c.cor[1] == 7:
                  upgrade((0,0,0))
                elif [c.cor[0],c.cor[1]-1] == hasJump:
                   pieces[c.cor[1]-1][c.cor[0]] = ""
                   p(c.cor[1]-1,c.cor[0])
                  
              if pieces[c.cor[1]][c.cor[0]][1] == "b":
                if c.cor[1] == 4 and selec[1] == 6:
                  hasJump = [c.cor[0],c.cor[1]]
                elif c.cor[1] == 0:
                  upgrade((255,255,255))
                elif [c.cor[0],c.cor[1]+1] == hasJump:
                   pieces[c.cor[1]+1][c.cor[0]] = ""
                   p(c.cor[1]+1,c.cor[0])
            
            p(selec[1],selec[0])
            p(c.cor[1],c.cor[0])
               
            if pieces[c.cor[1]][c.cor[0]] != "":
              pPut(pieces,c.cor[1],c.cor[0])
              c.draw()
            turn += 1
            cpt = 0
            
            if turn%2 == 1:
              d("Black",230,0,(0,0,0),(146,24,36))
              d("Turn " + str(turn),225,15,(0,0,0),(146,24,36))      
            if turn%2 == 0:
              d("White",230,0,(255,255,255),(146,24,36))
              d("Turn " + str(turn),225,15,(255,255,255),(146,24,36))             
            for k in range(len(listv)):
              if(listv[k][0]+listv[k][1])%2 == 1:
                col = (105,146,62)
              else:
                col = (190,199,212)
              v = cursor([listv[k][1],listv[k][0]],col)
              v.remove()
            
            listv = []
            c.draw()  
            rock = "f"        
            break
    else:
      d("wrong color",210,200,(0,0,0),(146,24,36))
