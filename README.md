For use:
run the script by command: 

python main.py **parameters

where parameters should be in format: 
Square TopRight 1 1 Side 1
or 
Rectangle TopRight 2 2 BottomLeft 1 1
or
Circle Center 1 1 Radius 2

New shapes could be easily added just by adding new python-file into folder "shapes".
No manipulation in core file "main.py" necessary for it.


---------------------------------------
TASK
The test task is to write a program that reads from standard input and writes to standard output.
It receives data about different geometrical 2D shapes. For each of them it should calculate perimeter and area.

Sample input:
Square TopRight 1 1 Side 1
Rectangle TopRight 2 2 BottomLeft 1 1
Circle Center 1 1 Radius 2

Sample output:
Square Perimeter 4 Area 1
Rectangle Perimeter 4 Area 1
Circle Perimeter 1 Area 2

Bonus points for:
- tests
- code that is easy to extend to add more shapes
for example “Triangle Point1 5 5 Point2 8 8 Point3 10 2”
---------------------------------------