This lab demonstrates is the first part of demonstrating how using multiple cores can speed up our computation speed. Though not exactly displayed in this lab, it is evident that when we increase the size of the matrix that we are multiplying, the longer it takes to complete the computations. For a matrices size 200, it took approximately 15 seconds to complete. I belive that when we do this some lab using parallel programming the time to complete computation will be cut in half. 

There were a couple of difficulties I had with this lab, none of which being severe. FIrst and foremost, getting back into the rythm of programming in python took me a bit as it had been a while since i developed my own python file from scratch. One I became familiarized with python syntex, the next big problem was figuring out the algorithm to multiply the matrices in the order that they needed to be multiplied and added. I used nested loops to accomplish this and manipulted the indices to get the correct output. Thankfully the different functions provided in matrixUtils.py saved me from the headache of things such as printing only a certain amount of the array.

It is also imporant to note that i used the genMatrix function from matrixUtils. py to generate the 2 matrices to be multiplied and one to hold the values (product) of the matrices.

Overall, this assignment helped me see how slow computations can be when we do this lab in the traditional, non parallel way.

-------------
