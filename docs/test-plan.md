# Test Plan Document <!-- omit in toc -->

- [IDENTIFICATION INFORMATION SECTION](#identification-information-section)
  - [PRODUCT](#product)
  - [PROJECT DESCRIPTION](#project-description)
  - [TEST PERSONNEL](#test-personnel)
  - [PROGRAMMERS](#programmers)
- [UNIT TEST SECTION](#unit-test-section)
  - [UNIT TEST STRATEGY / EXTENT OF UNIT TESTING:](#unit-test-strategy--extent-of-unit-testing)
  - [UNIT TEST CASES](#unit-test-cases)
- [TEST PARTICIPANTS SECTION](#regression-test-section)
  - [TEST PARTICIPANTS STRATEGY](#regression-test-strategy)
  - [REGRESSION PARTICIPANTS CASES](#regression-test-cases)
- [INTEGRATION TEST SECTION](#integration-test-section)
  - [INTEGRATION TEST STRATEGY AND EXTENT OF INTEGRATION TESTING](#integration-test-strategy-and-extent-of-integration-testing)
  - [INTEGRATION TEST CASES](#integration-test-cases)
- [USER ACCEPTANCE TEST SECTION (To be completed by the business office)](#user-acceptance-test-section-to-be-completed-by-the-business-office)
  - [USER ACCEPTANCE TEST STRATEGY](#user-acceptance-test-strategy)
  - [DELIVERABLES](#deliverbales)
  - [USER ACCEPTANCE TEST CASES](#user-acceptance-test-cases)
- [Appendix](#appendix)

## IDENTIFICATION INFORMATION SECTION

### PRODUCT

- **Product Name:** Space Team Rescue
- **Product Line Portfolio:** Visual Novel Adventure

### PROJECT DESCRIPTION

This is a test for my upcoming senior project. The main one will be about you and your space team crash landing on a planet, and it's your job to fix the ship and make sure everyone is alive. This will be a visual novel sort of adventure, with your choices affecting the outcome. My demo focusses on character interaction and the found count.
### TEST PERSONNEL

- Joey Beasley

### PROGRAMMERS

- Joey Beasley

## UNIT TEST SECTION

### UNIT TEST STRATEGY / EXTENT OF UNIT TESTING:

The purpose of this section is to run the game beginning to end to see if everything works as planned. Me or the selected participant will play through the game, do the multiple paths, and play the minigames.

### UNIT TEST CASES

| \#  | OBJECTIVE | INPUT | EXPECTED RESULTS | TEST DELIVERABLES |
| --- | --------- | ----- | ---------------- | ----------------- |
| 1   |  Should Display Game and characters         |       |  Should be displayed      | Everything appears    |
| 2   |  Should Count how many are found and let me end based on if the count is three |       |  Should only access last part is found = 3 | It accesses the last part once the found count is 3, but does not end the game yet   |
| 3   | The count should not go up for a character if the wrong criteria is met. | Selecting what the character would not want      | The character should not have joined me, and I should be able to actiavte our convo again | It lets me try the conversation again, meaning the character has not joined me and the found counter has not gone up.   |
| 4   | If it keeps track of if someone has died and it affects the ending |  Load a file, Let someone die, Get to the ending and see if it is the corresponding one.   | The charcacters who are alive should appear at the end, with the dead characters being missing, with their absence leaving an impact | The alive are still around  |
| 5   | It should keep track of the items that have been found  | Play the game and find one of the tools (such as the wrench), Select the leave option once warped back to the hub, See if it only lets me leave if all parts are found | It knows whether or not I found the parts and only lets me leave when they have been retrieved |
| 6   | If the navigator has given us a blaster, we can use it  | After starting a new game, travel through the forest, and locate the Navigator, Get my blaster, Access both scenarios that involve the blaster, See if I am allowed to use it if I select the option, if I can, I have it! | The program knows whether or not not I have it, with the spacebar command appearing to shoot an alien | It gives me the blaster and lets me use it |
| 7   | Send the player back to the hub when a part is found or when given the option  | Play through the game and obtain the items in an area. Be sent back to the hub with the commander greeting me! | The program should send me back to the hub when a part is found | It sends me back to the main hub once I find a part |
| 8   | One mini game for repairing the ship has you select the right tool for fixing something wrong. If you pick wrong, you have to start over | Get to the part of the game where all the parts are found and the mechanic is safe,Play the mini game, | If I get all five right, we move on to flying the ship If I get one wrong, I have to start over, stopping once I get five correct, No question should show up twice in a single go, there is a boolean in the randomizer that won’t let the question repeat if answered correctly. | It works, it stops when I get five consecutive correct answers|
| 9   | One of the finales is a quick time event, four arrow keys are listed and you must enter them in the correct order in a time limit or else you will crash. | Reach the last part (I included a shortcut in the main hub to reach this) and start it The order of keys are spelled out In three seconds, type those keys in the order they were listed, |if done correctly, move on to the next promptIf failed, crash the ship and give the players a game over before provided the option to try again. | all instances are completed successfully, cue up the finale, congratulating the player, but I am having trouble making the game end afterwards|
| 10   | Another final section shows meteors in front of the ship. Depending on their positions, you must either type in the arrow key representing the opposite direction to steer around them, or press the space bar to shoot at them if they are in the center of the screen. | Get to the last part (Had a shortcut in the main hub in one build) Display a meteor on one part of the screen (up, down, left, right) Que a quick time event where you must type the arrow opposing the position of the meteor. If it is in the center, pressing the spacebar in time will blast it and allow you to move on. | If entered correctly, you will move on to the next section before winning. | all instances are completed successfully, cue up the finale, congratulating the player, but I am having trouble making the game end afterwards|
| 11   | When spending time with the mechanic, you are given the option to either ask her a question or to have her ask you a question | If you offer to be asked, she will ask for your input, which should be saved to an input variable. If you ask her a question, you pick one of three, later on an imposter appears and you use that question to decide which one is the real her.  | If entered correctly, you willeitehr ask her and imposter a question, that question being the one from earlier, or she will ask you that question | The correct question and answer are implemented|
## TEST PARTICIPANTS SECTION

It works after every properly implemented change.

### TEST PARTICIPANTS STRATEGY

For test participants, I will first ask someone, such as a friend or family member, to test the game by starting a new save. As they play through, I will see if everything not only functions properly (no glitches or typos) but will ask for their feedback as they test it, along with observing how they interact with it. Once they beat the game (or reach any of its alternate endings), I will ask for their feedback, what they liked, and what can be improved. My goal is to have at least five different people test it out and give input.

### TEST PARTICIPANTS CASES

| #   | SUBJECT NAME | BACKGROUND | PROCESS | OBSERVED |
| --- | --------- | ----- | ---------------- | -------- |
| 1   |    Evan Hill       | Dormmate      | Picked up on it pretty quickly, though I did explain that some options are recursive until a goal is met. He found the overall game neat    | Typo on the first text box, I fixed it once he was done. I also realized I hadn't implemented an option I had previously commented out in order to make room for testing, I fixed that as well by uncommenting it.         |
| 2   |    Brian      | Friend (Chemistry Major)     | I opened the game for him. I ocassionally gave him some tips on how to continue    | When it came to the part where you press the spacebar to shoot the alien, how pressed it twice, leading to the navigator getting hurt, although he was able to save him. Brian said the timing bar at the top of the screen confused him. I considered having an explanation for how the blaster works when the navigoator gives you one. He also was confused at the Quick Time Events when it came to pressing the right buttons, I will add an explanation that you need to advance the text bar before doing the arrows. He still thought the game was good and wished me luck (and thought the mechanic character looked like the one from Terraria).      |
| 2   |    James      | Friend (Biochemistry Major)     | Loaded the game for James and let him try. He did need a bit of guidance on the blaster section, even after the explanation, to hit it just once. At one point, there was a glitch that crashed the game, even after I commented it out, resulting in him having to pick the other option. On the tool section, I previously edited the images, but they were too big, so I spent a few minutes fixing their size.   | He enjoyed it but did agree there were a few bugs that needed to be fixed. He was also confused by the onscreen arrows during the quick time event, which I plan to remove. I will also make sure the propt tells you to enter the keys only once.|

## INTEGRATION TEST SECTION

Combine individual software modules and test as a group.

### INTEGRATION TEST STRATEGY AND EXTENT OF INTEGRATION TESTING

Evaluate all integrations with locally developed shared libraries, with consumed services, and other touch points.

  

## USER ACCEPTANCE TEST SECTION (To be completed by the business office) 

The purpose here is to see how a human player interacts with the game. 

Independent Variables - Gender, Age, Place of origin, Major

Dependent Variables - Experience with games, ability to beat the game, performance in the minigames and quick time events.

### USER ACCEPTANCE TEST STRATEGY

SUMMARY-I will first ask someone, such as a friend or family member, to test the game by starting a new save. As they play through, I will see if everything not only functions properly (no glitches or typos) but will ask for their feedback as they test it, along with observing how they interact with it. Once they beat the game (or reach any of its alternate endings), I will ask for their feedback, what they liked, and what can be improved. My goal is to have at least five different people test it out and give input. 

GOAL-I want to make sure the game can be easily understood, enjoyed, and accessed by different people (spanning across major, interests, age, etc). Some people I am considering using for feedback include my dormmate, some friends on campus (with differing majors), and my Grammama.

### DELIVERABLES

The ending they get
Which charcaters have survived
Scores in the shooting minigames

### USER ACCEPTANCE TEST CASES

| #   | TEST ITEM | EXPECTED RESULTS | ACTUAL RESULTS | DATE |
| --- | --------- | ---------------- | -------------- | ---- |
| 1   | Test Player should understand the basics and the goal        | My test subject easily picked up on the mechanics and what to do               |               |     |
| 2   | Test player gets the ending that corresponds to who is alive  | If a character dies off, they should not show up in the end, which impacts the story's direction  |     |     |
| 3   | The meteor dodge minigame responds to player input  | If the player crashes the ship, they have to restart the minigame  |     |     |
| 4   | The tool minigame works  | The test player can understand what tool is needed from the prompt and selects the correct one |     |     |
| 5   |  |  |     |     |



## Appendix
