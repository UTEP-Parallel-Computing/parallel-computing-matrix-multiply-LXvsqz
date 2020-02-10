This lab demonstrates is the first part of demonstrating how using multiple cores can speed up our computation speed. Though not exactly displayed in this lab, it is evident that when we increase the size of the matrix that we are multiplying, the longer it takes to complete the computations. For a matrices size 200, it took approximately 18 seconds to complete. The test when implented went as followed for size 200 matrices:

Serial: 18.78 Seconds


Parallel:
1 Thread: 60.9174s
2 Threads: 22.6370s
4 Threads: 19.3492s
8 Threads: 15.2354s

Though there was not a huge difference, I believe that with larger matrices we would see a huge difference. Perhaps the way that the computation was time was also an issue however this is the method that I have followed in previous classes and for part one of the assignment. Since there are more threads, each one can handle a given amount of data rather than just one doing the majority of the work.

There were a couple of difficulties I had with this lab, none of which being severe. FIrst and foremost, getting back into the rythm of programming in python took me a bit as it had been a while since i developed my own python file from scratch. One I became familiarized with python syntex, the next big problem was figuring out the algorithm to multiply the matrices in the order that they needed to be multiplied and added. I used nested loops to accomplish this and manipulted the indices to get the correct output. 

Thankfully the different functions provided in matrixUtils.py saved me from the headache of things such as printing only a certain amount of the array. For the parallel part of the lab, figuring out the correct format to create a shared array was a problem. Though this is very very simple, I kept getting simple errors pertaining to the dytpe. I overcame this by following the word doc provided. Another problem I had was making sure that i was using pyMP the correct way. It felt a little simple so i thought I was messing up somewhere. After meeting with Professor Pruitt, I had a clear understanding of what exactly was happening with the threads being spawned. I am unsure if i am timing the computation the correct way, I did not get the chance to ask. Lastly this assignment took me a total of 3-4 hours to complete. 

Overall, this assignment helped me "get my feet wet" in the parallel world. It was very interesting to see how we could use multiple threads to handle the computations for a shared memory array. I would love to make sure I timed the computations the correct way with Professor Pruit. Other than that, I felt like learned and understood a great deal from both parts of the assignemnt.


-------------
