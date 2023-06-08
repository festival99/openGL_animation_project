from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
import time
import numpy as np
from IPython.display import display,clear_output
from PIL import Image


height=720
weigth=1080

active=0


# Global variables
inpBld=int(input("Enter Building Number >>> "))
boom_x = 0  # X-coordinate of the boom
boom_y = 600  # Initial Y-coordinate of the boom
boom_radius = 1  # Initial radius of the boom
splash_radius = 1  # Initial radius of the splash

def Colour():
    R=((int(random.randint(0,100)))/100)
    #print(R)
    G=((int(random.randint(0,100)))/100)
    B=((int(random.randint(0,100)))/100)
    
    return R,G,B


def draw_points(x, y,ps=3):
    glPointSize(ps) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def Conv_LinePnt_Draw(ZnNum,CoodLst,ps=3):
    for Cod in range(len(CoodLst[0])):
        
        #R,G,B=Colour()
        #glColor3f(R, G, B)
        
        x0,y0=CoodLst[0][Cod],CoodLst[1][Cod]
        if ZnNum==0 :
            #return 0
            nX0,nY0=x0,y0
            draw_points(nX0,nY0,ps)
            
        elif ZnNum==3 :
            #return 3
            nX0,nY0=-x0,y0
            draw_points(nX0,nY0,ps)
            
        elif ZnNum==4 :
            #return 4
            nX0,nY0=-x0,-y0
            draw_points(nX0,nY0,ps)
            
        elif ZnNum== 7:
            #return 7
            nX0,nY0=x0,-y0
            draw_points(nX0,nY0,ps)
        
        elif ZnNum== 1 :
            #return 1
            nX0,nY0=y0,x0
            draw_points(nX0,nY0,ps)
            
        elif ZnNum==2 :
            #return 2
            nX0,nY0=-y0,x0
            draw_points(nX0,nY0,ps)
            
        elif ZnNum==5 :
            #return 5
            nX0,nY0=-y0,-x0
            draw_points(nX0,nY0,ps)
        elif ZnNum== 6:
            #return 6
            nX0,nY0=y0,-x0
            draw_points(nX0,nY0,ps)
        #print(nX0,nY0)

def Find_Zone_Line(x0,y0, x1,y1,ps=3):
    dX=x1-x0
    dY=y1-y0
    if abs(dX) > abs(dY):
        if dX>0 and dY>0 :
            #return 0
            nX0,nY0=x0,y0
            nX1,nY1=x1,y1
            Codlst=Line_Points(nX0,nY0 , nX1,nY1)
            Conv_LinePnt_Draw(0,Codlst,ps)
            
        elif dX<0 and dY>0 :
            #return 3
            nX0,nY0=-x0,y0
            nX1,nY1=-x1,y1
            Codlst=Line_Points(nX0,nY0 , nX1,nY1)
            Conv_LinePnt_Draw(3,Codlst,ps)
            
        elif dX<0 and dY<0 :
            #return 4
            nX0,nY0=-x0,-y0
            nX1,nY1=-x1,-y1
            Codlst=Line_Points(nX0,nY0 , nX1,nY1)
            Conv_LinePnt_Draw(4,Codlst,ps)
            
        else:
            #return 7
            nX0,nY0=x0,-y0
            nX1,nY1=x1,-y1
            Codlst=Line_Points(nX0,nY0 , nX1,nY1)
            Conv_LinePnt_Draw(7,Codlst,ps)
            
    else:
        if dX>0 and dY>0 :
            #return 1
            nX0,nY0=y0,x0
            nX1,nY1=y1,x1
            Codlst=Line_Points(nX0,nY0 , nX1,nY1)
            Conv_LinePnt_Draw(1,Codlst,ps)
            
        elif dX<0 and dY>0 :
            #return 2
            nX0,nY0=y0,-x0
            nX1,nY1=y1,-x1
            Codlst=Line_Points(nX0,nY0 , nX1,nY1)
            Conv_LinePnt_Draw(2,Codlst,ps)
            
        elif dX<0 and dY<0 :
            #return 5
            nX0,nY0=-y0,-x0
            nX1,nY1=-y1,-x1
            Codlst=Line_Points(nX0,nY0 , nX1,nY1)
            Conv_LinePnt_Draw(5,Codlst,ps)
        else:
            #return 6
            nX0,nY0=-y0,x0
            nX1,nY1=-y1,x1
            Codlst=Line_Points(nX0,nY0 , nX1,nY1)
            Conv_LinePnt_Draw(6,Codlst,ps)


def Line_Points(x0,y0, x1,y1):
    dX=x1-x0
    dY=y1-y0
    
    d1=2*dY-dX
    dE=2*dY
    dNE=2*(dY-dX)
    
    #draw_points(x0,y0)
    xn,yn=x0,y0
    
    RlX=[xn]
    RlY=[yn]
    
    while(xn<x1):
        if d1<=0:
            xn+=1
            d1+=dE
        else:
            xn+=1
            yn+=1
            d1+=dNE
        #draw_points(xn,yn)
        #print(xn,yn)
        RlX+=[xn]
        RlY+=[yn]
    return (RlX,RlY)

def Draw_Rect(PLst,ps=3):
    X0,Y0, X1,Y1=PLst[0],PLst[1], PLst[2],PLst[3]
    
    #X-Axis
    Find_Zone_Line(X0,Y0, X1,Y0,ps)
    #Find_Zone_Line(X0,0, X1,0)
    Find_Zone_Line(X0,Y1, X1,Y1,ps)
    
    #Y-Axis
    Find_Zone_Line(X0,Y0, X0,Y1,ps)
    #Find_Zone_Line(X0,0, X1,0)
    Find_Zone_Line(X1,Y0, X1,Y1,ps)

def Num_8(PLst,ps=3):
    X0,Y0, X1,Y1=PLst[0],PLst[1], PLst[2],PLst[3]
    
    #X-Axis
    Find_Zone_Line(X0,Y0, X1,Y0,ps)
    Find_Zone_Line(X0,(Y1+Y0)//2, X1,(Y1+Y0)//2,ps)
    Find_Zone_Line(X0,Y1, X1,Y1,ps)
    
    #Y-Axis
    Find_Zone_Line(X0,Y0, X0,Y1,ps)
    #Find_Zone_Line(X0,0, X1,0)
    Find_Zone_Line(X1,Y0, X1,Y1,ps)

def Num_1(PLst,ps=3):
    X0,Y0, X1,Y1=PLst[0],PLst[1], PLst[2],PLst[3]
    
    #X-Axis
    #Find_Zone_Line(X0,Y0, X1,Y0,ps)
    Find_Zone_Line(X0,(Y1+Y0)//2, X1,Y0,ps)
    #Find_Zone_Line(X0,Y1, X1,Y1,ps)
    
    #Y-Axis
    #Find_Zone_Line(X0,Y0, X0,Y1,ps)
    #Find_Zone_Line(X0,0, X1,0)
    Find_Zone_Line(X1,Y0, X1,Y1,ps)

def Num_2(PLst,ps=3):
    X0,Y0, X1,Y1=PLst[0],PLst[1], PLst[2],PLst[3]
    
    #X-Axis
    Find_Zone_Line(X0,Y0, X1,Y0,ps)
    Find_Zone_Line(X0,(Y1+Y0)//2, X1,(Y1+Y0)//2,ps)
    Find_Zone_Line(X0,Y1, X1,Y1,ps)
    
    #Y-Axis
    Find_Zone_Line(X0,(Y1+Y0)//2, X0,Y1,ps)
    #Find_Zone_Line(X0,0, X1,0)
    Find_Zone_Line(X1,Y0, X1,(Y1+Y0)//2,ps)

def Num_3(PLst,ps=3):
    X0,Y0, X1,Y1=PLst[0],PLst[1], PLst[2],PLst[3]
    
    #X-Axis
    Find_Zone_Line(X0,Y0, X1,Y0,ps)
    Find_Zone_Line(X0,(Y1+Y0)//2, X1,(Y1+Y0)//2,ps)
    Find_Zone_Line(X0,Y1, X1,Y1,ps)
    
    #Y-Axis
    #Find_Zone_Line(X0,Y0, X0,Y1,ps)
    #Find_Zone_Line(X0,0, X1,0)
    Find_Zone_Line(X1,Y0, X1,Y1,ps)

def Num_4(PLst,ps=3):
    X0,Y0, X1,Y1=PLst[0],PLst[1], PLst[2],PLst[3]
    
    #X-Axis
    #Find_Zone_Line(X0,Y0, X1,Y0,ps)
    Find_Zone_Line(X0,(Y1+Y0)//2, X1,(Y1+Y0)//2,ps)
    #Find_Zone_Line(X0,Y1, X1,Y1,ps)
    
    #Y-Axis
    Find_Zone_Line(X0,Y0, X0,(Y1+Y0)//2,ps)
    #Find_Zone_Line(X0,0, X1,0)
    Find_Zone_Line(X1,Y0, X1,Y1,ps)

def Num_5(PLst,ps=3):
    X0,Y0, X1,Y1=PLst[0],PLst[1], PLst[2],PLst[3]
    
    #X-Axis
    Find_Zone_Line(X0,Y0, X1,Y0,ps)
    Find_Zone_Line(X0,(Y1+Y0)//2, X1,(Y1+Y0)//2,ps)
    Find_Zone_Line(X0,Y1, X1,Y1,ps)
    
    #Y-Axis
    Find_Zone_Line(X0,Y0, X0,(Y1+Y0)//2,ps)
    #Find_Zone_Line(X0,0, X1,0)
    Find_Zone_Line(X1,(Y1+Y0)//2, X1,Y1,ps)

def Num_6(PLst,ps=3):
    X0,Y0, X1,Y1=PLst[0],PLst[1], PLst[2],PLst[3]
    
    #X-Axis
    Find_Zone_Line(X0,Y0, X1,Y0,ps)
    Find_Zone_Line(X0,(Y1+Y0)//2, X1,(Y1+Y0)//2,ps)
    Find_Zone_Line(X0,Y1, X1,Y1,ps)
    
    #Y-Axis
    Find_Zone_Line(X0,Y0, X0,Y1,ps)
    #Find_Zone_Line(X0,0, X1,0)
    Find_Zone_Line(X1,(Y1+Y0)//2, X1,Y1,ps)

def Num_7(PLst,ps=3):
    X0,Y0, X1,Y1=PLst[0],PLst[1], PLst[2],PLst[3]
    
    #X-Axis
    Find_Zone_Line(X0,Y0, X1,Y0,ps)
    #Find_Zone_Line(X0,(Y1+Y0)//2, X1,(Y1+Y0)//2,ps)
    #Find_Zone_Line(X0,Y1, X1,Y1,ps)
    
    #Y-Axis
    #Find_Zone_Line(X0,Y0, X0,Y1,ps)
    #Find_Zone_Line(X0,0, X1,0)
    Find_Zone_Line(X0,Y1, X1,Y0,ps)

def areazone(PLst,ps=3):
    X0,Y0, X1,Y1=PLst[0],PLst[1], PLst[2],PLst[3]
    #Y-Axis
    Find_Zone_Line(X0,720, X0,-720,ps)
    #Find_Zone_Line(X0,0, X1,0)
    Find_Zone_Line(X1,720, X1,-720,ps)

    midx,midy= (X1+X0)//2 , (Y0+Y0)//2
    #Find_Zone_Line(midx, midy, X1, 600)
    return [midx,midy]

    
def Draw_JetPlane(x0 , y0,PlnSz=200):

    R,G,B=Colour()
    glColor3f(R, G, B)

    #PlnSz=200
    #roof
    Rf_X0 , Rf_Y0 = x0 , y0       
    Rf_X1 , Rf_Y1 = Rf_X0+PlnSz , Rf_Y0
    Find_Zone_Line(Rf_X0 , Rf_Y0 , Rf_X1 , Rf_Y1,1)  #roof

    #bottom
    ext=PlnSz//3
    tp_bm_dis=PlnSz//10
    Btm_X0 , Btm_Y0 = Rf_X0-ext , Rf_Y0 - tp_bm_dis        
    Btm_X1 , Btm_Y1 = Btm_X0+PlnSz+ext , Btm_Y0
    Find_Zone_Line(Btm_X0,Btm_Y0 , Btm_X1,Btm_Y1 , 1)  #bottom

    #front
    Fnt_X0 , Fnt_Y0 = Rf_X0 , Rf_Y0        
    Fnt_X1 , Fnt_Y1 = Btm_X0 , Btm_Y1
    Find_Zone_Line(Fnt_X0 , Fnt_Y0, Fnt_X1 , Fnt_Y1  ,1)

    #Back
    #BkTP
    BckTp_X0 , BckTp_Y0 = Rf_X1 , Rf_Y1         
    BckTp_X1 , BckTp_Y1 = BckTp_X0 + PlnSz//40 , BckTp_Y0 - ((tp_bm_dis//2)-PlnSz//40 )
    Find_Zone_Line(BckTp_X0 , BckTp_Y0, BckTp_X1 , BckTp_Y1  ,1)

    #BkBtm
    BckBtm_X0 , BckBtm_Y0 = Btm_X1 , Btm_Y1         
    BckBtm_X1 , BckBtm_Y1 = BckBtm_X0 + PlnSz//40 , BckBtm_Y0 + ((tp_bm_dis//2)-PlnSz//40 )
    Find_Zone_Line(BckBtm_X0 , BckBtm_Y0, BckBtm_X1 , BckBtm_Y1  ,1)

    #BkMdl
    BckMdl_X0 , BckMdl_Y0 = BckTp_X1 , BckTp_Y1      
    BckMdl_X1 , BckMdl_Y1 = BckBtm_X1 , BckBtm_Y1
    Find_Zone_Line(BckMdl_X0 , BckMdl_Y0, BckMdl_X1 , BckMdl_Y1  ,1)

    #backFin
    FinBksiz=PlnSz//5
    Finang=PlnSz//10
    #BckLine
    BkLnFin_X0 , BkLnFin_Y0 =  Rf_X1 , Rf_Y1       
    BkLnFin_X1 , BkLnFin_Y1 =  Rf_X1 + Finang , Rf_Y1 + FinBksiz
    Find_Zone_Line(BkLnFin_X0 , BkLnFin_Y0 , BkLnFin_X1 , BkLnFin_Y1  ,1)

    #TopLine
    FinTpSize=PlnSz//10
    TpLnFin_X0 , TpLnFin_Y0 =  BkLnFin_X1 - FinTpSize , BkLnFin_Y1      
    TpLnFin_X1 , TpLnFin_Y1 =  BkLnFin_X1 , BkLnFin_Y1
    Find_Zone_Line(TpLnFin_X0 , TpLnFin_Y0 , TpLnFin_X1 , TpLnFin_Y1  ,1)
    #FntLine
    FntFinDis=PlnSz//5
    FntLnFin_X0 , FntLnFin_Y0 =  Rf_X1 - FntFinDis , Rf_Y1    
    FntLnFin_X1 , FntLnFin_Y1 =  TpLnFin_X0 , TpLnFin_Y0
    Find_Zone_Line(FntLnFin_X0 , FntLnFin_Y0 , FntLnFin_X1 , FntLnFin_Y1  ,1)

    #window
    #Wndwroof
    Wndwrf_X1,Wndwrf_Y1 = Rf_X0 , Rf_Y0 
    Wndwrf_X2,Wndwrf_Y2 = Rf_X0 +PlnSz//7 , Rf_Y0 - PlnSz//30
    Draw_Rect([Wndwrf_X1,Wndwrf_Y1 , Wndwrf_X2,Wndwrf_Y2],1)

    ##Wings
    ##WngFnt
    #WngFnt_X0 , WngFnt_Y0 = ((-Btm_X0+Btm_X1)//2) - PlnSz//3 , Btm_Y1 +  tp_bm_dis//2    
    #WngFnt_X1 , WngFnt_Y1 = WngFnt_X0 + PlnSz//5 , Btm_Y1 - PlnSz//9
    #Find_Zone_Line(WngFnt_X0 , WngFnt_Y0, WngFnt_X1 , WngFnt_Y1  ,1)
#
    ##WngBk
    #WngBk_X0 , WngBk_Y0 = ((-Btm_X0+Btm_X1)//2) - PlnSz//8 , Btm_Y1 +  tp_bm_dis//2    
    #WngBk_X1 , WngBk_Y1 = WngBk_X0 + PlnSz//8 , Btm_Y1 - PlnSz//9
    #Find_Zone_Line(WngBk_X0 , WngBk_Y0, WngBk_X1 , WngBk_Y1  ,1)
#
    ##WngMdl
    #WngMdl_X0 , WngMdl_Y0 = WngFnt_X1 , WngFnt_Y1 
    #WngMdl_X1 , WngMdl_Y1 = WngBk_X1 , WngBk_Y1
    #Find_Zone_Line(WngMdl_X0 , WngMdl_Y0, WngMdl_X1 , WngMdl_Y1  ,1)




def Draw_Building():
    codlist=[]

    #building 00
    Rshft=600*0
    hgt=50
    glColor3f(0.9, 0.9, 0.9)
    X1,Y1= -1080,-190-hgt
    X2,Y2= -820,-730
    Draw_Rect([X1,Y1 , X2,Y2])
    Num_1([X1+100,Y1-140 , X2-100,Y2+140])

    glColor3f(0.3, 0.3, 0.3)
    MidP=areazone([X1,Y1 , X2,Y2],1)
    codlist.append([[X1,Y1 , X2,Y2],[MidP]])

    #building 01
    Rshft=600*1
    hgt=240
    glColor3f(0.9, 0.9, 0.9)
    X1,Y1= -1080+Rshft,-190-hgt
    X2,Y2= -820+Rshft,-730
    Draw_Rect([X1,Y1 , X2,Y2])
    Num_2([X1+100,Y1-100 , X2-100,Y2+100])

    glColor3f(0.3, 0.3, 0.3)
    MidP=areazone([X1,Y1 , X2,Y2],1)
    codlist.append([[X1,Y1 , X2,Y2],[MidP]])

    #building 02
    Rshft=600*2
    hgt=-140
    glColor3f(0.9, 0.9, 0.9)
    X1,Y1= -1080+Rshft,-190-hgt
    X2,Y2= -820+Rshft,-730
    Draw_Rect([X1,Y1 , X2,Y2])
    Num_3([X1+100,Y1-100 , X2-100,Y2+100])

    glColor3f(0.3, 0.3, 0.3)
    MidP=areazone([X1,Y1 , X2,Y2],1)
    codlist.append([[X1,Y1 , X2,Y2],[MidP]])

    #building 03
    Rshft=600*3
    hgt=140
    glColor3f(0.9, 0.9, 0.9)
    X1,Y1= -1080+Rshft,-190-hgt
    X2,Y2= -820+Rshft,-730
    Draw_Rect([X1,Y1 , X2,Y2])
    Num_4([X1+100,Y1-100 , X2-100,Y2+100])

    glColor3f(0.3, 0.3, 0.3)
    MidP=areazone([X1,Y1 , X2,Y2],1)
    codlist.append([[X1,Y1 , X2,Y2],[MidP]])

    #building 31
    Rshft=300*1
    hgt=-220
    glColor3f(0.9, 0.9, 0.9)
    X1,Y1= -1080+Rshft,-190-hgt
    X2,Y2= -820+Rshft,-730
    Draw_Rect([X1,Y1 , X2,Y2])
    Num_5([X1+100,Y1-100 , X2-100,Y2+100])

    glColor3f(0.3, 0.3, 0.3)
    MidP=areazone([X1,Y1 , X2,Y2],1)
    codlist.append([[X1,Y1 , X2,Y2],[MidP]])

    #building 33
    Rshft=300*3
    hgt=100
    glColor3f(0.9, 0.9, 0.9)
    X1,Y1= -1080+Rshft,-190-hgt
    X2,Y2= -820+Rshft,-730
    Draw_Rect([X1,Y1 , X2,Y2])
    Num_6([X1+100,Y1-100 , X2-100,Y2+100])

    glColor3f(0.3, 0.3, 0.3)
    MidP=areazone([X1,Y1 , X2,Y2],1)
    codlist.append([[X1,Y1 , X2,Y2],[MidP]])


    #building 35
    Rshft=300*5
    hgt=300
    glColor3f(0.9, 0.9, 0.9)
    X1,Y1= -1080+Rshft,-190-hgt
    X2,Y2= -820+Rshft,-730
    Draw_Rect([X1,Y1 , X2,Y2])
    Num_7([X1+100,Y1-80 , X2-100,Y2+80])

    glColor3f(0.3, 0.3, 0.3)
    MidP=areazone([X1,Y1 , X2,Y2],1)
    codlist.append([[X1,Y1 , X2,Y2],[MidP]])


    return codlist
        
        
def DropBoom(endpoint):
    global boom_x, boom_y, boom_radius, splash_radius

    glColor3f(1.0, 1.0, 1.0)  # Set color to white

    if boom_y > endpoint:  # Check if the boom has reached the end position
        boom_y -= 80  # Decrement Y-coordinate to make the boom drop
        boom_radius += 0.8  # Increment radius of the boom

    if boom_y <= endpoint and splash_radius < 130:  # Check if the boom has hit the bottom and the splash is not complete
        splash_radius += 5  # Increment radius of the splash
    

    glPushMatrix()
    glTranslatef(boom_x, boom_y, 0)  # Apply translation to boom's position
    for i in range(360):  # Draw points in a circular pattern for the boom
        angle = math.radians(i)
        x = boom_radius * math.cos(angle)
        y = boom_radius * math.sin(angle)
        draw_points(x, y,1)  # Draw a point at (x, y)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(boom_x, endpoint, 0)  # Apply translation to splash's position
    for i in range(360):  # Draw points in a circular pattern for the splash
        angle = math.radians(i)
        x = splash_radius * math.cos(angle)
        y = splash_radius * math.sin(angle)
        draw_points(x, y,2)  # Draw a point at (x, y)
    glPopMatrix()

    time.sleep(0.01)
            

def iterate():
    glViewport(0, 0, weigth, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-weigth, weigth, -height, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def Xplus(x1):
    x1-=50 # Decrement x1 by 1 to move from right to left
    #if x1<-1080:
    #    return 1000
    #else:
    return x1

def showScreen():
    global X1x, boom_x, boom_y, boom_radius, splash_radius,active, endP, inpBld

    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    iterate()
                   
    midcodlist=Draw_Building()

    X1x = Xplus(X1x) # Call Xplus function to get the updated x-coordinate
    Y1y = 600 # Fixed y-coordinate
    #inpBld=int(input("Enter Building Number >>> "))
    #boom zone
    b01=midcodlist[inpBld-1]
    print(b01,b01[1][0][0])
    if b01[0][0]<X1x and X1x<b01[0][2] : #1
        boom_x, boom_y,= b01[1][0][0],Y1y
        endP = b01[1][0][1]
        active=True

    if active== True:
        DropBoom(endP)


    R=((int(random.randint(0,100)))/100)
    G=((int(random.randint(0,100)))/100)
    B=((int(random.randint(0,100)))/100)

    glColor3f(R, G, B)
    
    
    #Draw_JetPlane(0,600, 200) #X,y, size of plane
    

    Draw_JetPlane(X1x,Y1y, 100) #X,y, size of plane
 
    time.sleep(0.01)

    glutSwapBuffers()
    glutPostRedisplay()

X1x = 1000 # Initial x-coordinate


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(1080, 720) #window size
glutInitWindowPosition(110, 100)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()