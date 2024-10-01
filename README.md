# Red Badger Mars Rover Test

## Business Value and Risks

In this case, I would imagine the Robots a very expensive and the client would want to minimise the number of robots being lost or damaged. There are other cost considerations to, such as optimising fuel consumption the robots, and ensuring they can explore as much of the planet as possible. 

## Approach

My approach would be to break down the problem into a smaller set of iterable deliverables/features. Designed to give early feedback and be able to adapt to business requirements. 


1. RB-002: Make the robots move.
Constraints: 
   - Only 1 robot is allowed on the grid. No previous robots have been lost and there are no scents on the grid.
   - The robot moves on a grid without any boundaries. ie It cannot be lost. 
   - The robot will start at grid position (0,0) and is orientated to face north. ie 0 0 N

Acceptance criteria:
  - The robot accepts a list of string instructions to move it forward, left and right.
  - The final position and orientation of the robot is printed out in the format x y D

2. RB-003: Robots can only move on a fixed grid size

Acceptance criteria:
  - Maximum co-ordinate size is 50.
  - First line of input determines the grid size. 

3. RB-004: Lost robots leave a scent so other robots do not get lost in the same position


Non-functional stories:
1. RB-001: Set up project - discuss language, tech stack, architecture options with the client. 
Acceptance Criteria:
   - Able to run project and tests
Out of scope:
Running tests on CI/CD server
   
## Install instructions

### Dependencies
1. Install python and venv
2. Create python virtual environment `python -m venv venv`

### Run tests
To run all tests type `python -m unittest`


## Considerations
1. All input data is valid and in the correct format. Error handling could be a future follow-up stories.
2. Off by one problem. With a grid size of say 5,3 would the robot be allowed on position 5,3 or is that considered off the grid?