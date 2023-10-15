#implement a class called player that represents a cricket player.
#The player class should have a method called play() which prints "The player is playing cricket".
#derive two classes called Batsman and Bowler from the player class.
#Override the play() method in each derived class to print" The batsman is batting" and "bowler is bowling", respectively.
#write a program yo create objects to both are Batsman and Bowler classes and call the play() method for each object.
#define the player class
class player:

  def play(self):
    print("The player is playing cricket.")


#define the Batsman class, derived from player
class Batsman(player):

  def play(self):
    print("The batsman is batting.")


#define the Bowler class, derived from player
class Bowler(player):

  def play(self):
    print("The bowler is bowling.")


#create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()
#call the play() method for each object
batsman.play()
bowler.play()
