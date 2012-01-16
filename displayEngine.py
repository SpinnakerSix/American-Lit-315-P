from Tkinter import *
import datetime
import thread        
import urllib2 as urllib
from PIL import Image, ImageTk
from cStringIO import StringIO

def display(message):
    print 'Displaying Coupon!'

    root = Tk()
   
    my_url = 'http://aux.iconpedia.net/uploads/1440300232.png'
    img_file = urllib.urlopen(my_url)
    im = StringIO(img_file.read())
    image1 = Image.open(im)

    #root.geometry('%dx%d' % (image1.size[0],image1.size[1]))
     
    # Convert the Image object into a TkPhoto object
    tkpi = ImageTk.PhotoImage(image1)
    label_image = Label(root, image=tkpi, width=image1.size[0], height=image1.size[1]).pack() # pack it in the display window

    #root.geometry('300x300')
    root.title("Your Reward!")
    #w = Message(root, text=message, width=400, font=("default",12), justify='center').pack()

    root.after(2000, root.destroy) # close the window after 2 seconds
    print 'Closing Coupon Window!'
    root.mainloop() #start the GUI
 
def displayCoupon(message):
  thread.start_new_thread( display, (message,) )

print 'ladfadfadsadf'
display('lalala')
print 'ladfadfadsadf'
