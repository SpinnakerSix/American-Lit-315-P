from Tkinter import *
import datetime
import thread        
#import Image, ImageTk
import urllib2 as urllib
from PIL import Image, ImageTk
from cStringIO import StringIO
import Tkinter

def display(message):
    print 'Displaying Coupon!'

    root = Tk()
   
    my_url = 'http://aux.iconpedia.net/uploads/1440300232.png'
    img_file = urllib.urlopen(my_url)
    print img_file
    im = StringIO(img_file.read())
    image1 = Image.open(im)

#root = Tkinter.Tk()  # A root window for displaying objects

 # Convert the Image object into a TkPhoto object
#tkimage = ImageTk.PhotoImage(im)

#Tkinter.Label(root, image=tkimage).pack() # Put it in the display window

#root.mainloop() # Start the GUI

    #image1 = Image.open(f)
    #root.geometry('%dx%d' % (image1.size[0],image1.size[1]))
    tkpi = ImageTk.PhotoImage(image1)
    print tkpi
    print dir(tkpi)
    print tkpi.width()
    label_image = Label(root, image=tkpi).pack()
    #label_image.place(x=0,y=0,width=image1.size[0],height=image1.size[1])

    #root.geometry('300x300')
    root.title("Your Reward!")
    #w = Message(root, text=message, width=400, font=("default",12), justify='center')


    #w.pack()
    root.after(2000, root.destroy)
    print 'Closing Coupon Window!'
    # mainloop() has to be called AFTER to make sure the coupons show up
    root.mainloop()
 
def displayCoupon(message):
  thread.start_new_thread( display, (message,) )

print 'ladfadfadsadf'
display('lalala')
print 'ladfadfadsadf'
