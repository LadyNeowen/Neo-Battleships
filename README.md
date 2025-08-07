# Neo-Battleships
The neo-battleships is a fun game of battleships with a bit of a pirate flare. 
It is a terminal game which runs on the Code institute mock terminal on Heroku. 

## How to play

The game is based on the classic board game of "Sink the ship" or "Battleships".
In my version the player is thrown into some roleplay where they are asked to enter their name,
followed by a fun game against the computer where the player has to try to sink all the hidden ships (4)
and do so with 10 bombs. 
The board is 5*5 and the ships are randomly generated each time. 
Empty slots are marked with a ~
Hits are marked with an X 
And misses are marked with an O.

The player wins if they manage to find and sink all four battleships and looses if they run out of turns.
At the end of each game, the player is asked if they want to play again, if they choose yes the game starts over.
And if they choose no, the game is ended and the player is bid farewell.

## Features 

* Generate a random board
* Play against the computer in a roleplay against the computer
* Accepts users input
* Maintain a count and hit score
* Input validation and error checking
** Which means the user cannot place a ship same place twice
** They have to enter a letter/number input for where they would like to make a guess

## Future features

* Computer board is also displayed and the computer makes random guesses
* Highscore count for the player names
* Choose board size and placing ships yourself
* Have larger ships

## Testing

* I have passed the code through PEP8 linter and confirmed there are no problems
* Made sure there is an error message that prints if the user makes invalid inputs
* Tested in my local terminal as well as the Code Institute Heroku terminal

## Solved bugs

* I have built almost my entire game in the PythonCode Pad which has built in bug testing 
so it has quickly shown me when I have made something wrong. It also has a "play" function,
so I have continuously been able to play my code through to see if it worked and if it didn't the
app would point out to me what line of code was causing the trouble.
There have honestly been so many misstakes that listing them all here would be tediouos if not impossible.

## Remaining bugs

* No bugs remaining

## Validator tesing 

* PEP8 where no errors were found

## Deployment

