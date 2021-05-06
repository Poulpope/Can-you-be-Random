## PCBS Project - Nathan Vidal
# Can you be Random ?
In a paper released in 2010, Jeffrey P. Ebert and Daniel M. Wegner elaborated on an individual’s randomness, meaning the ability to be as random as possible. Randomness implies both the equal probability of alternative events and the inability of an observer to make a prediction of the next event from knowledge of any previous event. However, it has been shown that human cannot behave randomly. More precisely, no set of parameters reliably engenders random responses, despite instructions to behave as randomly as possible. I want to assess randomness through a key-pressing task to demonstrate this finding.

References : Ebert, Jeffrey & Wegner, Daniel. (2011). Mistaking randomness for free will. Consciousness and cognition. 20. 965-71. 10.1016/j.concog.2010.12.012. 

# How to run the experiment ?
You can download the main experiment PCBS_keypressing_task.py and run it on Python. Pygame is required. This will create a csv file listing all of the keys you pressed (with the label "left" or "right").

# Analyzing the results
I took inspiration from Aaronson's oracle (https://www.expunctis.com/2019/03/07/Not-so-random.html).
I gathered the data of several participants to show you what I mean when I say people cannot act randomly. I transfered the data on R where my script can analyze the results (PCBS_5gram_analysis.R) : it makes predictions about the keys you will press based on the keys you already pressed using a 5-gram paradigm. I collected the predictions and assessed the percentage of good predictions made over the last 50 keys you pressed across the 1000 trials. Here are the results for 7 participants :

![image](https://user-images.githubusercontent.com/81677999/117113370-a75e4f80-ad8a-11eb-9ad5-3a531b88148c.png)

For one participant :

![image](https://user-images.githubusercontent.com/81677999/117114058-a1b53980-ad8b-11eb-888d-f16328fa3491.png)

There is an average of 67,45% good predictions for my 7 participants over the 1000 trials : the program is better than randomness (50%) to predict your next choice.

# Explanations
Your fingers tend to repeat unconsciously certain patterns. My program on R keeps a database of every possible combination of 5 presses (this is a 5-gram) and count the number of iterations where this 5gram was followed by left or by right. So every time you press a key, the database is updated. To make a prediction, the program checks the 5gram corresponding to the last 5 presses, checks whether it is usually followed by left or right and decide which key press is most likely to follow. 
The probability of the program guessing your inputs is usually around 67% suggesting that you really are not good at making random choices.

# Previous coding experience and PCBS
I learnt the basics of Python in my classe préparatoire but I only used it this year since then : I mostly used R in biology and Matlab during my internships. I liked the lectures of PCBS because they are very useful but I think that writing a whole script+posting it on github plus the lectures/exercises are a lot. 
