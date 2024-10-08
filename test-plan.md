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

This one is a simple demo that shows the various character interactions, how they affect gameplay, and seeing which one of your teammate have been found.

### UNIT TEST CASES

| \#  | OBJECTIVE | INPUT | EXPECTED RESULTS | TEST DELIVERABLES |
| --- | --------- | ----- | ---------------- | ----------------- |
| 1   |  Should Display Game and characters         |       |  Should be displayed      | Everything appears    |
| 2   |  Should Count how many are found and let me end based on if the count is thre |       |  Should only access last part is found = 3 | It accesses the last part once the found count is 3, but does not end the game yet   |

## TEST PARTICIPANTS SECTION

It works after every properly implemented change.

### TEST PARTICIPANTS STRATEGY

Let some friends and other volunteers test my demo and give me feedback

### TEST PARTICIPANTS CASES

| #   | SUBJECT NAME | BACKGROUND | PROCESS | OBSERVED |
| --- | --------- | ----- | ---------------- | -------- |
| 1   |    Evan Hill       | Dormmate      | Picked up on it pretty quickly, though I did explain that some options are recursive until a goal is met. He found the overall game neat    | Typo on the first text box, I fixed it once he was done. I also realized I hadn't implemented an option I had previously commented out in order to make room for testing, I fixed that as well by uncommenting it.         |

## INTEGRATION TEST SECTION

Combine individual software modules and test as a group.

### INTEGRATION TEST STRATEGY AND EXTENT OF INTEGRATION TESTING

Evaluate all integrations with locally developed shared libraries, with consumed services, and other touch points.

### INTEGRATION TEST CASES

| #   | OBJECTIVE | INPUT | EXPECTED RESULTS | TEST DELIVERABLES |
| --- | --------- | ----- | ---------------- | ----------------- |
| 1   |           |       |                  |                   |

## USER ACCEPTANCE TEST SECTION (To be completed by the business office)

Verify that the solution works for the user

### USER ACCEPTANCE TEST STRATEGY

{Explain how user acceptance testing will be accomplished}

### USER ACCEPTANCE TEST CASES

| #   | TEST ITEM | EXPECTED RESULTS | ACTUAL RESULTS | DATE |
| --- | --------- | ---------------- | -------------- | ---- |
| 1   |   Have it count who has been saved        | When the count is three, the "Report Back" button should finish the game                 |  It Ended the game once all had been found and I clicked "Report Back"              | 10-7-24     |


## Appendix
