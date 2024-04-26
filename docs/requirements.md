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

________________________________________________________________
Criteria 22: Keep track of which ending to give the player
 
  Motivation: The goodness of the ending should vary depending on who is still alive
  
  Examples: If you go through without anyone dying, you get the best enidng. If all of the crewmates die, you get the worst ending.
  
  Fit Criterion: PLay through the game and see how the endings have changed

________________________________________________________________
Criteria 23: Give the perfect ending
 
  Motivation: If all the members make it to the end of the game, the perfect ending should be rewarded
  
  Examples: Once all the crew have made it to rebuilding the ship, they will all be shown escaping
  
  Fit Criterion: Play through the game without anyone dying and see if the perfect ending has been rewarded

________________________________________________________________
Criteria 24: Give the worst ending
 
  Motivation: If none the members make it to the end of the game, the  worst ending will be shown.
  
  Examples: If you make it to the end and all your teammates have died, you are shown all alone
  
  Fit Criterion: Play through the game with everyone dying and see if the worst ending has been rewarded

________________________________________________________________
Criteria 24: Tell players which ending they achieved
 
  Motivation: After the ending is shown, we should tell players which type of ending they earned, along with a score
  
  Examples: Once the game is done, a text box will display the type of ending you got along with a score that goes up to three stars (like Angry Birds)
  
  Fit Criterion: Play through the game and get all the endings

________________________________________________________________
Criteria 24: Have some ambient music or sound effects included
 
  Motivation: Including sound will add to the atmosphere and overall experience.
  
  Examples: When starting your adventure on the planet, appropriate background music will start
  
  Fit Criterion: Insert audio files and see if they work and play in the right locations

________________________________________________________________
Criteria 25: Have a shock chord play when a team member dies
 
  Motivation: Adding this sound will make each death recognizable and impactful.
  
  Examples: If we go back and find the technician dead, the sound will start.
  
  Fit Criterion: See if this plays with the death of a crew member.

________________________________________________________________
Criteria 26: Include a list in the main menu containing the different endings earned
 
  Motivation: The players can see what endings they got
  
  Examples: For each ending you earn, the summary and score is unlocked in the main menu.
  
  Fit Criterion: Everytime I finish the game, I will check the menu

________________________________________________________________
Criteria 27: Include a mission log
 
  Motivation: Include a summary from the main character explaining what has happened so far
  
  Examples: When something happens, such as a part being found, it will be included in the summary
  
  Fit Criterion: After an event, I will check the log menu

________________________________________________________________
Criteria 28: Have a load menu option if a previous unfinished game is saved
 
  Motivation: When returning to a session, players should be able to pick up from where they left off.
  
  Examples: If I saved after three parts have been found and the technician died, when I load again, the game should have all these.
  
  Fit Criterion: Save the game, leave, click load, and see if the progress has been remembered

________________________________________________________________
Criteria 29: Have the options to turn sound, music, or voices off
 
  Motivation: Not all players want to hear talking or music, so we should include the option to turn it off.
  
  Examples: If I click for the music to turn off, the music should be muted.
  
  Fit Criterion: Turn the mute for one of the options on and see if it is silent

________________________________________________________________
Criteria 30: If there is a saved game, it should be over written when a new game is saved
 
  Motivation: Saving a new game over an old one should replace it
  
  Examples: If the saved game has to found parts and I start a new game and save it, that should overwrite the original game
  
  Fit Criterion: Save on an old game, start a new one, and save over it. The new game should take its place.

________________________________________________________________
Criteria 31: The game should be able to run on any desktop
 
  Motivation: Mac users, microsfot users, etc should have the game playable on their machine.
  
  Examples: If I can play this on a Mac, I should also be able to play it on a Windows computer
  
  Fit Criterion: Test the game on different computer brands and see if they work.

________________________________________________________________
Criteria 32: The game should be able to run on any browser
 
  Motivation: Safari, Chrome, Firefox, etc should be able to play the game
  
  Examples: If I can play this on Safari, I should also be able to play it on Chrome.
  
  Fit Criterion: Test the game on different browsers and see if they work.

________________________________________________________________
Criteria 33: The game should be able to run on any virtual machine
 
  Motivation: Mac, Ubuntu, etc should be able to play the game
  
  Examples: If I can play this on Mac, I should also be able to play it on Ubuntu.
  
  Fit Criterion: Test the game on different virtual machines and see if they work.

________________________________________________________________
Criteria 34: The game should be accessable even to people who don't play these sorts of games
 
  Motivation: I want this game to be enjoyable for anyone curious to play and for them to not feel alienated by the mechanics and set up
  
  Examples: My dormmate, my mom, and my professor are all able to understand how the game works and are able to get invested.
  
  Fit Criterion: Show the game to other people of differing demographics and get feedback from them.

________________________________________________________________
Criteria 35: The game should be able to simply explain itself to players
 
  Motivation: To ensure the game can be enjoyed and picked up by anyone, the game should give a brief summary of how it works.
  
  Examples: Before players are able to make their first action, a text box should explain how this works, what the goals are, and what to avoid.
  
  Fit Criterion: While letting others play test, see if they can understand what to do once the game begins.

________________________________________________________________
Criteria 36: Players should feel a connection to the NPC's (Non-Playable Characters)
 
  Motivation: Any good story must have characters that appeal to the audience, this game should be no exception since it is the player's duty to keep them safe.
  
  Examples: The characters should have appealing designs and personalities so that the players agree they need to look out for the others.
  
  Fit Criterion: Get player feedback on how they react to the characters.

________________________________________________________________
Criteria 37: Upon completion, the endings must impact the viewers
 
  Motivation: Since the game has overarcing stories based on the player's decisions, they must feel good on the good endings and feel bad if they lose a crew member.
  
  Examples: When getting the worst ending, the player is suppossed to feel like they failed not only the game, but their crew.
  
  Fit Criterion: Get player feedback on how they react to the ending.

________________________________________________________________
Criteria 38: The player should feel a sense of progress when obtaining items
 
  Motivation: The goal is to find all the parts and get everyone to safety. Whenever a part is found, the player feels like they are making progress and can do this.
  
  Examples: The game should inform you when a part has been obtained and including the part count will give a sense of progression.
  
  Fit Criterion: See how players feel when they find a part or save a crewmate.

________________________________________________________________
Criteria 39: The world should feel strange but not overwhelming
 
  Motivation: This is a slow paced game but with high consequence, and another key to creating this on top of a good story is giving people a world they have never seen before, especially since the game is in space.
  
  Examples: When exploring, the planet must feel intimidating, but still give players the urge to keep exploring.
  
  Fit Criterion: Gauge how players react to the environments.

________________________________________________________________
Criteria 40: Keep the game engaging
 
  Motivation: This is a slow paced game that involves a lot of reading, which for many can get boring very quickly. Every game has o be fun, they are made to entertain after all.
  
  Examples: Keep the text short, sweet, and too the point, and maybe add a bit to the character interaction.
  
  Fit Criterion: Ask how the players are enjoying the game as they test it out and see what can be improved.




