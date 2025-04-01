# Documentation <!-- omit in toc -->

- [Statement of Purpose (with the Problem Statement)](#statement)
- [Research and Background](#research-and-background)
- [Project Language(s), Software, and Hardware](#languages-software-hardware)

- [Project Requirements](#project-requirements)

- [Project Implementation Description & Explanation](#implementation)

- [Test Plan](#test-plan)
  - [USER ACCEPTANCE TEST STRATEGY](#user-acceptance-test-strategy)
  - [DELIVERABLES](#deliverbales)
  - [USER ACCEPTANCE TEST CASES](#user-acceptance-test-cases)
- [Appendix](#appendix)

## Statement of Purpose (with the Problem Statement)

In most visual novel type games, players do not receive any consequence for failure, being allowed to correct themselves or go back to a previous point to fix their mistakes. Adding consequences to somebody's failures in a game not only adds to the challenge, but also makes any error all the more impactful. My idea is to make a game where everyone's survival is dependent on you. This will result in a game that is more impactful on players by giving them perosnal connections to characters that may not survive if things go wrong.



## Research and Background

In the summer of 2024, I downloaded Renpy and practiced coding some simple tests and demos in Visual Studio Code to run on there. I also drew the characters in Clip Studio Paint and imported them into the code. When it came time to incorporate minigames into the gameplay, I researched a few basic minigames online and used them as a basis for the code during those sections.

## Project Language(s), Software, and Hardware

The language used for the game is Python. The code was typed up in Visual Studio Code and ran in Renpy. The character designs were drawn in Clip Studio Paint with a Wacom Cintiq drawing tablet. All of this was created on my MacBook Pro.


## Project Requirements

To run this, you need to download the files from github and then use Renpy to open and play.

## Project Implementation Description & Explanation



![screenshot](images/TitleSenior.png)  
Fig 1. The launch screen

![screenshot](images/promptmechanic.jpeg)  
Fig 2. Offering if you want the mechanic to ask a question, or for you to ask her a question. This comes in handy later when a shapeshifting alien poses as her.

![screenshot](images/shotprompt.jpeg)  
Fig 3. Players must press the spacebar to shoot an alien before it attacks their team.

![screenshot](images/toolquiz.jpeg)  
Fig 4. The correct tool must be selected from a prompt describing what needs to be fixed on the ship.

https://github.com/JoeyBeasley/JoeySP

## Test Plan

| #   | SUBJECT NAME | BACKGROUND | PROCESS | OBSERVED |
| --- | --------- | ----- | ---------------- | -------- |
| 1   |    Evan Hill       | Dormmate      | Picked up on it pretty quickly, though I did explain that some options are recursive until a goal is met. He found the overall game neat    | Typo on the first text box, I fixed it once he was done. I also realized I hadn't implemented an option I had previously commented out in order to make room for testing, I fixed that as well by uncommenting it.         |

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
