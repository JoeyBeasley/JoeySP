Criteria 1: Characters and Text should appear
  
  Motivation: Players should be able to see and read what is going on in-game
  
  Examples: When a character is talking to the player and soemthing is happening, we should be able to see the       character, the background, and text displaying what they are saying.
  
  Fit Criterion: Everytime a character speaks, a text appears in a readable font of at least 12 pts.

________________________________________________________________
Criteria 2: Text Options should appear and be clickable
  
  Motivation: Selecting text-based options is what moves the game forward. Visual Novel style games rely on this     so that the plot and gameplay can progress.
  
  Examples: After a character talks to you, you should be given an option to go either left with them, or go to      the right and continue on your own.
  
  Fit Criterion: If these text options display in a readable font and leads to the next textbox and scenario.

________________________________________________________________
Criteria 3: The game should keep track of who is alive
 
  Motivation: The more Non Playable Characters that die, the worse ending you get.
 
  Examples: If one of the side characters, like the technician die, rebuilding the ship will be harder. If most     of the crew is dead and your tough as nails engineer is still around, he will abandon you.
 
  Fit Criterion: The game should give you diffferent endings based on who is alive, with some endings being darker depending on who is alive.

________________________________________________________________
Criteria 4: The voice clips playing
 
  Motivation: When characters talk or react to something, a voice clip provided by me should play.
  
  Examples: When the technician is talking to you, a voice clip should start that reads out what he is saying.       When he reacts in shock to a dangerous encounter, a sound of shock must exclaim.
  
  Fit Criterion: Hearing the audio.

________________________________________________________________
Criteria 5: Counting who is alive
 
  Motivation: There should be an internal counter capping at the number of members still alive.
  
  Examples: The game starts off at the max number of crew members, and if that number is the same by the end, the best ending is rewarded.
  
  Fit Criterion: Running tests on the code to see if the counter keeps up with who is alive.

________________________________________________________________
Criteria 6: Counting who is gone
 
  Motivation: There should be an internal counter capping at the number of members who died
  
  Examples: The counter starts at 0, with the number going up everytime a crew member is lost along the way. The higher the count, the worse the ending.
  
  Fit Criterion: Testing to see if the counter increased when a teammate is eliminated.

  ________________________________________________________________
Criteria 7: Play the right audio file
 
  Motivation: The correct audio should play for the respective character and their dialogue.
  
  Examples: The tehcnician has a younger, higher piteched voice, while the engineer has a deeper, gruffer voice. It is important that these two do not get mixed up.
  
  Fit Criterion: Hearing the audio play for the right line and character.

________________________________________________________________
Criteria 8: Make the player's name enterable
 
  Motivation: When starting the game, players should enter the name they want to be referred by.
  
  Examples: The name entered at the beggining will be stored in the game.
  
  Fit Criterion: Checking the name variable

________________________________________________________________
Criteria 9: Have the characters refer to the player by their entered name.
 
  Motivation: Once the name is added, it will be included in a name string
  
  Examples: When the technician acknowldges you, he will say, "Hello Captain (name)! Shall we head out?"
  
  Fit Criterion: Testing the name variable in an in-game string.

________________________________________________________________
Criteria 10: Let players save progress
 
  Motivation: A session's data and progress should be saved.
  
  Examples: If a player needs to do something else and come back later, the can click the save button to hold their data.
  
  Fit Criterion: Testing the save feature to see if everything from the session is still intact.

________________________________________________________________
Criteria 11: Let players see previous text
 
  Motivation: There should be an option to view previously displayed text and dialogue
  
  Examples: When clicking the log button, players should be able to read something that was said a few boxes ago
  
  Fit Criterion: Clicking the button and viewing previously displayed text. I can do this by saving the text to an array after being cleared.

________________________________________________________________
Criteria 12: Make the different paths lead to different stories and scenarios
 
  Motivation: This is a visual novel style adventure where your actions count, so some actions must lead to a unique situation
  
  Examples: Going right will lead you to a cave where somebody might get lost, but going left will make you meet up with the technician and give you an option as to whether or not you should investigate a strange noise in the distance.
  
  Fit Criterion: Testing the different scenarios and seeing if they lead to their own arc in the story

________________________________________________________________
Criteria 13: Plan out where each choice will lead
 
  Motivation: This is a visual novel style adventure where your actions count. Every choice should have its own unique outcome and reaction, no two playthroughs will be the same.
  
  Examples: Going right will lead you to a cave where somebody might get lost, but going left will make you meet up with the technician and give you an option as to whether or not you should investigate a strange noise in the distance. If you do, your technician will be eaten offscreen by an unknown speciman
  
  Fit Criterion: Map out where I want everything to go and where it should lead to next, along with its potential impacts on the crew.

________________________________________________________________
Criteria 14: Have all the characters maintain a unique dynamic with the main character
 
  Motivation: This is will make the interactions all the more meaningful and help players gain a connection to the non-playable characters. This will also have a different effect on the overall story if anything bad happens to said characters.
  
  Examples: The technician is like a little brother the the captain, very eager and trusting. Meanwhile, the engineer is more gruff and distrusting, so if he is the only one surviving, he might as well ditch you.
  
  Fit Criterion: Coming up wiht the characters and seeing how to make their personalities crucial to the game's momentum.

________________________________________________________________
Criteria 15: Keep track of the items needed to fix the ship
 
  Motivation: Following your crew or venturing out alone to collect parts is the key to getting off the planet and back home to base.
  
  Examples: There are at least five parts needed, the game will tell you what those parts are. Advancing in the story will lead to you finding them.
  
  Fit Criterion: Testing the counter.

________________________________________________________________
Criteria 16: Tell us when we have a part and how many we still need
 
  Motivation: The game should be able to keep track of which parts are collected and give us a count
  
  Examples: If the gears are found, the remaining parts count is displayed when the blueprint is opened
  
  Fit Criterion: There should be an in-game counter for the parts

________________________________________________________________
Criteria 17: Display the part when found
 
  Motivation: When a part is found, the blueprint menu should fill in the silhouette of that part
  
  Examples: Opening up the blueprint menu after finding an item should display a diagram blueprint with the missing parts filled in once collected.
  
  Fit Criterion: Testing a booleon for collected that when set to true, displays that part

________________________________________________________________
Criteria 18: Create in game map
 
  Motivation: A map option from the options should show where the player is
  
  Examples: Opening up the map menu will show the parts of the planet that have been discorvered with a colored dot representing the player and their current location.
  
  Fit Criterion: Create a map background and a booleon for which dot should be lit.

________________________________________________________________
Criteria 19: Have the in game map reveal the covered up places once they are interacted with
 
  Motivation: Since this is a desolate planet, the characters have never been here before. Their space gps-equivalents cannot pick up any familiarity, leaving them blank until they make progress
  
  Examples: Once a new area, such as the cave, is found, that area will no longer be obscured on the navigator.
  
  Fit Criterion: Create a map background and a booleon for when an area should be visible.

________________________________________________________________
Criteria 20: Give the player the option to back up in certain scenarios
 
  Motivation: There has to be a way for a player to go back a plave when the situation calls for it.
  
  Examples: When there is nothing to do or there is a dead end, clicking a back arrow should make you go back a spot.
  
  Fit Criterion: Implement a function for going backwards and having the map react.

________________________________________________________________
Criteria 21: Send you back to start to meet up with everyone when given the option
 
  Motivation: After a certain point has been reached, a button should emerge so you will be warped back to where the crew is suppossed to meet up
  
  Examples: When you find a part or lose a crewmember, you must report it back to base
  
  Fit Criterion: Implement a function for sending you back to the others.
