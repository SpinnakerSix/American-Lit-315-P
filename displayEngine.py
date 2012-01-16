from Tkinter import *
import datetime
import thread        

def display(message):
    print 'Displaying Coupon!'

    root = Tk()
    root.geometry('300x300')
    root.title("Your Reward!")
    w = Message(root, text=message, width=400, font=("default",12), justify='center')
    w.pack()
    root.after(2000, root.destroy)
    print 'Closing Coupon Window!'

    # mainloop() has to be called AFTER to make sure the coupons show up
    root.mainloop()
 
def displayCoupon(message):
  thread.start_new_thread( display, (message,) )
