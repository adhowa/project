from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')

#draw order is equel to the creation order ( player should always be last )
log1 = drawpad.create_rectangle(20,420,100,390, fill="brown")
log2 = drawpad.create_rectangle(20,540,100,570, fill="brown")
log3 = drawpad.create_rectangle(20,450,100,420, fill="brown")
log4 = drawpad.create_rectangle(20,480,100,450, fill="brown")
log5 = drawpad.create_rectangle(20,510,100,480, fill="brown")
log6 = drawpad.create_rectangle(20,540,100,510, fill="brown")
player = drawpad.create_oval(390,580,410,600, fill="green")

direction1 = 15
direction2 = -10
direction3 = 7
direction4 = 13
direction5 = -5
direction6 = 10

bPlayerFollowLog1 = False
bPlayerFollowLog2 = False
bPlayerFollowLog3 = False 
bPlayerFollowLog4 = False
bPlayerFollowLog5 = False 
bPlayerFollowLog6 = False 

class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        self.rocketFired = False
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    
    def animate(self):
        global drawpad
        global log1
        global log2
        global direction1
        global direction2
        global direction3
        global direction4
        global direction5
        global direction6
        px1,py1,px2,py2 = drawpad.coords(player)
        x1,y1,x2,y2 = drawpad.coords(log1)
        lx1,ly1,lx2,ly2 = drawpad.coords(log2)
        ox1,oy1,ox2,oy2 = drawpad.coords(log3)
        gx1,gy1,gx2,gy2 = drawpad.coords(log4)
        Lx1,Ly1,Lx2,Ly2 = drawpad.coords(log5)
        Ox1,Oy1,Ox2,Oy2 = drawpad.coords(log6)
        
        if x2 > 800:
            direction1 = - 5
        elif x1 < 0:
            direction1 = 5 
        
        if lx2 > 800:
            direction2 = -5
        elif lx1 < 0:
            direction2 = 5 
                
        if ox2 > 800:
            direction3 = -5
        elif ox1 < 0:
            direction3 = 5
            
        if gx2 > 800:
            direction4 = -5
        elif gx1 < 0:
            direction4 = 5
        
        if Lx2 > 800:
            direction5 = -5
        elif Lx1 < 0:
            direction5 = 5
        
        if Ox2 > 800:
            direction6 = -5
        elif Ox1 < 0:
            direction6 = 5
            
        drawpad.move(log1, direction1, 0)
        drawpad.move(log2, direction2, 0) 
        drawpad.move(log3, direction3, 0)      
        drawpad.move(log4, direction4, 0)  
        drawpad.move(log5, direction5, 0)         
        drawpad.move(log6, direction6, 0)
        
        if bPlayerFollowLog1:
            drawpad.move(player, direction1, 0)
        else: 
            if px2 > 800:
                drawpad.move(player,-4,0)
            
            if px1 < 0:
                drawpad.move(player,4,0) 
               
            if py2 > 600:
                drawpad.move(player,0,-4)
                
        if bPlayerFollowLog2:
            drawpad.move(player, direction2, 0)
        else:
            if px2 > 800:
                drawpad.move(player,-4,0)
            
            if px1 < 0:
                drawpad.move(player,4,0) 
               
            if py2 > 600:
                drawpad.move(player,0,-4)
                
        if bPlayerFollowLog3:
            drawpad.move(player, direction3, 0)
        else:
            if px2 > 800:
                drawpad.move(player,-4,0)
            
            if px1 < 0:
                drawpad.move(player,4,0)
            
            if py2 > 600:
                drawpad.move(player,0,-4)
                        
        if bPlayerFollowLog4:
            drawpad.move(player, direction4, 0)
        else:
            if px2 > 800:
                drawpad.move(player,-4,0)
            
            if px1 < 0:
                drawpad.move(player,4,0)
            
            if py2 > 600:
                drawpad.move(player,0,-4) 
                       
        if bPlayerFollowLog5:
            drawpad.move(player, direction5, 0)
        else:
            if px2 > 800:
                drawpad.move(player,-4,0)
            
            if px1 < 0:
                drawpad.move(player,4,0)
            
            if py2 > 600:
                drawpad.move(player,0,-4)
                
        if bPlayerFollowLog6:
            drawpad.move(player, direction6, 0)
        else:
            if px2 > 800:
                drawpad.move(player,-4,0)
            
            if px1 < 0:
                drawpad.move(player,4,0)
            
            if py2 > 600:
                drawpad.move(player,0,-4)
        
        drawpad.after(5,self.animate)
        
    def key(self,event):
        global player
        global log2
        global bPlayerFollowLog1
        global bPlayerFollowLog2
        global bPlayerFollowLog3
        global bPlayerFollowLog4
        global bPlayerFollowLog5
        global bPlayerFollowLog6
        px1,py1,px2,py2 = drawpad.coords(player)
        x1,y1,x2,y2 = drawpad.coords(log1)
        lx1,ly1,lx2,ly2 = drawpad.coords(log2)
        ox1,oy1,ox2,oy2 = drawpad.coords(log3)
        gx1,gy1,gx2,gy2 = drawpad.coords(log4)
        Lx1,Ly1,Lx2,Ly2 = drawpad.coords(log5)
        Ox1,Oy1,Ox2,Oy2 = drawpad.coords(log6)
        
        if event.char == "w":
            drawpad.move(player,0,-32)
            px1,py1,px2,py2 = drawpad.coords(player)
            if px1+25 >= lx1 and px2-25 <= lx2 and py1+25 >= ly1 and py2-25 <= ly2:
                bPlayerFollowLog2 = True
            else:
                bPlayerFollowLog2 = False
            if px1+25 >= x1 and px2-25 <= x2 and py1+25 >= y1 and py2-25 <= y2:
                bPlayerFollowLog1 = True
            else:
                bPlayerFollowLog1 = False 
            if px1+25 >= ox1 and px2-25 <= ox2 and py1+25 >= oy1 and py2-25 <= oy2:
                bPlayerFollowLog3 = True
                bPlayerFollowLog6 = False
                bPlayerFollowLog5 = False
                bPlayerFollowLog4 = False
                bPlayerFollowLog2 = False
                bPlayerFollowLog1 = False 
            else:
                bPlayerFollowLog3 = False
            if px1+25 >= gx1 and px2-25 <= gx2 and py1+25 >= gy1 and py2-25 <= gy2:
                bPlayerFollowLog4 = True
            else:
                bPlayerFollowLog4 = False
            if px1+25 >= Lx1 and px2-25 <= Lx2 and py1+25 >= Ly1 and py2-25 <= Ly2:
                bPlayerFollowLog5 = True
            else:
                bPlayerFollowLog5 = False
            if px1+25 >= Ox1 and px2-25 <= Ox2 and py1+25 >= Oy1 and py2-25 <= Oy2:
                bPlayerFollowLog6 = True
                bPlayerFollowLog5 = False
                bPlayerFollowLog4 = False
                bPlayerFollowLog3 = False
                bPlayerFollowLog2 = False
                bPlayerFollowLog1 = False 
            else:
                bPlayerFollowLog6 = False
                    
        if event.char == "s":
            drawpad.move(player,0,32)
            px1,py1,px2,py2 = drawpad.coords(player)
            if px1+25 >= lx1 and px2-25 <= lx2 and py1+25 >= ly1 and py2-25 <= ly2:
                bPlayerFollowLog2 = True
            else:
                bPlayerFollowLog2 = False
            if px1+25 >= x1 and px2-25 <= x2 and py1+25 >= y1 and py2-25 <= y2:
                bPlayerFollowLog1 = True
            else:
                bPlayerFollowLog1 = False
            if px1+25 >= ox1 and px2-25 <= ox2 and py1+25 >= oy1 and py2-25 <= oy2:
                bPlayerFollowLog3 = True
                bPlayerFollowLog6 = False
                bPlayerFollowLog5 = False
                bPlayerFollowLog4 = False
                bPlayerFollowLog2 = False
                bPlayerFollowLog1 = False
            else:
                bPlayerFollowLog3 = False
            if px1+25 >= gx1 and px2-25 <= gx2 and py1+25 >= gy1 and py2-25 <= gy2:
                bPlayerFollowLog4 = True
            else:
                bPlayerFollowLog4 = False
            if px1+25 >= Lx1 and px2-25 <= Lx2 and py1+25 >= Ly1 and py2-25 <= Ly2:
                bPlayerFollowLog5 = True
            else:
                bPlayerFollowLog5 = False
            if px1+25 >= Ox1 and px2-25 <= Ox2 and py1+25 >= Oy1 and py2-25 <= Oy2:
                bPlayerFollowLog6 = True
                bPlayerFollowLog5 = False
                bPlayerFollowLog4 = False
                bPlayerFollowLog3 = False
                bPlayerFollowLog2 = False
                bPlayerFollowLog1 = False 
            else:
                bPlayerFollowLog6 = False
                        
        if event.char == "d":
            drawpad.move(player,32,0)
            px1,py1,px2,py2 = drawpad.coords(player)
            if px1+25 >= lx1 and px2-25 <= lx2 and py1+25 >= ly1 and py2-25 <= ly2:
                bPlayerFollowLog2 = True
            else:
                bPlayerFollowLog2 = False
            if px1+25 >= x1 and px2-25 <= x2 and py1+25 >= y1 and py2-25 <= y2:
                bPlayerFollowLog1 = True
            else:
                bPlayerFollowLog1 = False 
            if px1+25 >= ox1 and px2-25 <= ox2 and py1+25 >= oy1 and py2-25 <= oy2:
                bPlayerFollowLog3 = True
                bPlayerFollowLog6 = False
                bPlayerFollowLog5 = False
                bPlayerFollowLog4 = False
                bPlayerFollowLog2 = False
                bPlayerFollowLog1 = False
            else:
                bPlayerFollowLog3 = False 
            if px1+25 >= gx1 and px2-25 <= gx2 and py1+25 >= gy1 and py2-25 <= gy2:
                bPlayerFollowLog4 = True
            else:
                bPlayerFollowLog4 = False
            if px1+25 >= Lx1 and px2-25 <= Lx2 and py1+25 >= Ly1 and py2-25 <= Ly2:
                bPlayerFollowLog5 = True
            else:
                bPlayerFollowLog5 = False
            if px1+25 >= Ox1 and px2-25 <= Ox2 and py1+25 >= Oy1 and py2-25 <= Oy2:
                bPlayerFollowLog6 = True
                bPlayerFollowLog5 = False
                bPlayerFollowLog4 = False
                bPlayerFollowLog3 = False
                bPlayerFollowLog2 = False
                bPlayerFollowLog1 = False 
            else:
                bPlayerFollowLog6 = False
                        
        if event.char == "a":
            drawpad.move(player,-32,0)
            px1,py1,px2,py2 = drawpad.coords(player)
            if px1+25 >= lx1 and px2-25 <= lx2 and py1+25 >= ly1 and py2-25 <= ly2:
                bPlayerFollowLog2 = True
            else:
                bPlayerFollowLog2 = False
            if px1+25 >= x1 and px2-25 <= x2 and py1+25 >= y1 and py2-25 <= y2:
                bPlayerFollowLog1 = True
            else:
                bPlayerFollowLog1 = False
            if px1+25 >= ox1 and px2-25 <= ox2 and py1+25 >= oy1 and py2-25 <= oy2:
                bPlayerFollowLog3 = True
                bPlayerFollowLog6 = False
                bPlayerFollowLog5 = False
                bPlayerFollowLog4 = False
                bPlayerFollowLog2 = False
                bPlayerFollowLog1 = False 
            else:
                bPlayerFollowLog3 = False 
            if px1+25 >= gx1 and px2-25 <= gx2 and py1+25 >= gy1 and py2-25 <= gy2:
                bPlayerFollowLog4 = True
            else:
                bPlayerFollowLog4 = False
            if px1+25 >= Lx1 and px2-25 <= Lx2 and py1+25 >= Ly1 and py2-25 <= Ly2:
                bPlayerFollowLog5 = True
            else:
                bPlayerFollowLog5 = False
            if px1+25 >= Ox1 and px2-25 <= Ox2 and py1+25 >= Oy1 and py2-25 <= Oy2:
                bPlayerFollowLog6 = True
                bPlayerFollowLog5 = False
                bPlayerFollowLog4 = False
                bPlayerFollowLog3 = False
                bPlayerFollowLog2 = False
                bPlayerFollowLog1 = False 
            else:
                bPlayerFollowLog6 = False
                         
    def collisionDetect(self, player):
        global log1
        px1,py1,px2,py2 = drawpad.coords(player)
        x1,y1,x2,y2 = drawpad.coords(log1)
        
        
        
app = myApp(root)
root.mainloop()