# Grab-food Modeling
A GrabFood driver receives n food delivery requests, labeled 1, 2, ..., n, to transport food packages from restaurants to customers.  
For each request i, the driver must pick up one package at point i and deliver it to point i+n. 
The driver can carry up to Q packages at a time (it means that at any time, there are at most Q packages on board) and must start and end the tour at point 0 (the depot). <br />
Given a distance matrix c, where c(i,j) represents the travel distance from point i to point j (i, j = 0, 1, ..., 2n), determine the shortest route for the driver to complete all deliveries and return to the depot. <br />
Input <br />
Line 1 contains n and Q (1≤n≤15,1≤Q≤10) <br />
Line i+1 (i=1,2,…,2n+1) contains the (i−1)th line of the matrix c (rows and columns are indexed from 0,1,2,..,2n). <br />
Output <br />
Line 1: write the value n <br />
Line 2: Write the sequence of points that visited by the driver (tour of the driver without depot). The points in the tour are separated by SPACE characters) <br />
Example <br />
Input <br />
5 3  <br />
0 5 8 11 12 8 3 3 7 5 5 <br />
5 0 3 5 7 5 3 4 2 2 2 <br />
8 3 0 7 8 8 5 7 1 6 5 <br />
11 5 7 0 1 5 9 8 6 5 6 <br />
12 7 8 1 0 6 10 10 7 7 7 <br />
8 5 8 5 6 0 8 5 7 3 4 <br />
3 3 5 9 10 8 0 3 4 5 4 <br />
3 4 7 8 10 5 3 0 6 2 2 <br />
7 2 1 6 7 7 4 6 0 5 4 <br />
5 2 6 5 7 3 5 2 5 0 1 <br />
5 2 5 6 7 4 4 2 4 1 0 <br />
Output <br />
5 <br />
1 2 6 7 5 10 3 4 8 9 

