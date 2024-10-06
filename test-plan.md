# Test Plan Document <!-- omit in toc -->

- [IDENTIFICATION INFORMATION SECTION](#identification-information-section)
  - [PRODUCT](#product)
  - [PROJECT DESCRIPTION](#project-description)
  - [TEST PERSONNEL](#test-personnel)
  - [PROGRAMMERS](#programmers)
- [UNIT TEST SECTION](#unit-test-section)
  - [UNIT TEST STRATEGY / EXTENT OF UNIT TESTING:](#unit-test-strategy--extent-of-unit-testing)
  - [UNIT TEST CASES](#unit-test-cases)
- [REGRESSION TEST SECTION](#regression-test-section)
  - [REGRESSION TEST STRATEGY](#regression-test-strategy)
  - [REGRESSION TEST CASES](#regression-test-cases)
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
- **Product Line Portfolio:** Insurance

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

## REGRESSION TEST SECTION

It works after every properly implemented change.

### REGRESSION TEST STRATEGY

Evaluate all reports introduced in previous releases

### REGRESSION TEST CASES

| #   | OBJECTIVE | INPUT | EXPECTED RESULTS | OBSERVED |
| --- | --------- | ----- | ---------------- | -------- |
| 1   |           |       |                  |          |

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
| 1   |           |                  |                |      |

## Appendix
