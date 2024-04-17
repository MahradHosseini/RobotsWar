Developers:  
Yurekce Altin  2526085   
Mahrad Hosseini 2528388
# RobotsWar
**METU NCC CNG462: Artificial Intelligence Assignment 1**   
Using Python 3.12.2 Interpreter  
JetBrains PyCharm IDE  

Install the following dependencies before running the program:  
- **Matplotlib:** for demonstration purposes
- **NetworkX:** for constructing graphs

The program will create a visualized map of your coordinates and nodes in them, then apply A* search to find the shortest paths and use them for finding a tour that visits all nodes and comes back to starting position using UCS and DFS Algorithms.

**How to use:**  
Edit the *map.txt* file as you wish to make your desirable map. For each row you should specify the range/s of white blocks in form of *y-axis: x1-start - x1-end x2-start - x2-end ...*, skip the blank rows. Also specify as many nodes as you wish under node_coordinates section. Keep in mind that your *map.txt* should include node "A" which will be used as initial position for UCS/DFS. A sample *map.txt* is available.  
The system will check for possible mistakes and raise errors.

**System Outputs:**  
After running the program you will get 3 output files:  
- **map.jpg:** this is the visual representation of the *map.txt* file that you provided previously.
- **mainGraph.jpg:** this is the initial graph made directly from your map file. Each node represents a white block in the map labeled with its coordinates (x,y). We will later use this graph to apply A* Search Algorithm and find the minimum distance between each two nodes.
- **nodeGraph.jpg:** this is the minimum distance, fully-connected graph which is constructed after running A* Search Algorithm. Each node represents a node in your map (A, B, etc.) and edge values represent the cost of going from one node to the other one. We will later use this graph to apply UCS/DFS Algorithms.

The program will inform you of the algorithm results via Command Line Interface (CLI). Initially you will see the minimum distance between each pair of nodes along with the path found. Then DFS will take place and find the first tour path, keep in mind that this path is the first found path and might not be the best one in terms of cost. At the end, UCS will give you the best tour path with the least possible cost.

Spring 2023-24
