import util
import displayEngine

# detects 3 things
# achievement (passed a level)
# high score (score achieved)
# close calls (enemy close, almost dying)
# CUSTOM #
# GHOST HUNTER #

from datetime import datetime

class reader():
  def __init__(self):
     self.highScoresLimit = 1
     self.achievementsLimit = 1
     self.closeCallsLimit = 3
     
     # delay 20sec between displaying coupons
     self.bufferTime = 5
     self.lastCallTime = datetime.now()
  
  # calculate the amount of time passed
  # uses to delay call time between coupons
  def timePassed(self):
     t =  datetime.now() - self.lastCallTime
     return t.seconds

  def highScore(self, currentScore, targetScore):
     if (self.highScoresLimit > 0 and currentScore >= targetScore):
       self.highScoresLimit -= 1
       print 'Display NEW HIGH SCORE coupon!'
       displayEngine.displayCoupon('New High Score!')
 
  def victory(self, yesNo):
     if (self.achievementsLimit > 0 and yesNo):
       self.achievementsLimit -= 1
       print 'Display ACHIEVEMENT coupon!'
       displayEngine.displayCoupon('Victory!')
    
  def closeCall(self, pacmanState, ghostState):
    distance = util.manhattanDistance(pacmanState, ghostState)
    
    if (self.timePassed() > self.bufferTime and self.closeCallsLimit > 0 and distance < 2):
      self.closeCallsLimit -= 1
      print 'Display CLOSE CALL coupon!'
      self.lastCallTime = datetime.now()
      displayEngine.displayCoupon('Close Call!')


