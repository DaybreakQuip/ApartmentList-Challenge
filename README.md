# ApartmentList Challenge

## Important Notes:
---

Final Code for Challenge: Social.py

As I was doing this project, I realized that the original Python interpreter was extremely slow in searching for friends. Therefore, I switched to the more efficient PyPy interpreter. No code was changed in the process. This sped up my program by x10 times (from 10 minutes to 1 minute on the entire dictionary), which was significant, because it meant that the programming language mattered in this case. So in other languages, like Java, my code might have been speedier. Below is my runtime for the testcases I developed, which is also in the repository.

![results](https://user-images.githubusercontent.com/27522432/37992224-134da65e-31d9-11e8-9cc5-d15b453e4982.JPG)

Below is the link for PyPy.

https://pypy.org/

---
## General Notes:
---

My solution for this code is built off of Steve Hanov's code for Levenshtein Distance, and his code is based off of Wikipedia definition of Levenshtein distance. Below are the links to both. 

http://stevehanov.ca/blog/index.php?id=114

https://en.wikipedia.org/wiki/Levenshtein_distance

The original implementation file was what I originally coded, but was less efficient than the final code. The reason being is that the original implementation used extra storage space and kept appending and popping neighbors that were already accounted for, which took extra time (not much, but it would add up). However, that code proved to be useful in developing test cases for the final implementation, as I know that the original implementation is correct.

The final implementation uses a boolean to check for double counting, and is overall more efficient. 

Extra: JustForFun.py contains code for Damerau–Levenshtein distance search. It's related to Levenshtein Distance and is used to test my understanding of the overall code for this challenge. This code does not impact challenge.

---
