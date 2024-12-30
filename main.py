import pgzrun
import random
WIDTH = 500
HEIGHT = 500

TITLE='Good Shot Game'
message=''

#any image that we need to make as a character - we use actor function
image=Actor('alien') #this is the path of the image 

def draw():
    screen.clear() #this clears the screen
    screen.fill(color=(255,119,51))
    
    image.draw()
    screen.draw.text(message,center=(250,20),fontsize=30,color='blue')

def place_alien():   
    image.x=random.randint(100,WIDTH-100)
    image.y=random.randint(100,HEIGHT-50)

def on_mouse_down(pos):
    global message
    if image.collidepoint(pos):
        message='well done'
        place_alien()
    else:
        message='you missed the shot try again'

    

place_alien()




   
pgzrun.go()