Group members: Aakanksha Dutta (adutta5@u) and Aabha Pandit (apandit@u)
CSC242 - Project 4

* How to run
  python mybninferencer.py 1000 aima-alarm.xml B J true M true
  Should specify a sample size for the approximate interference.

* Result
For the input (sample size of 100000), the output is formatted as below:
    With Exact Inference:  [0.2841718353643929, 0.7158281646356071]
    With Approximate Inference:  [0.29450564762264697, 0.705494352377353]
Where for each inference, the probability of each possible value of the query variable given the evidence is output.
    
* Exact Interference
For exact inference by enumeration, we implemented the enumerate_ask() and enumerate_all() with the the psuedocode defined in the book, Stuart Russell and Peter Norvig, Artificial Intelligence, A Modern Approach, 4th ed. (2020).
The enumerate_ask() is the driver method for the recursive function enumerate_all() which performs inference on a part of the larger function using evidence.

We also implemented a parse_table() and pos_prob() which parses the table and calculates the posterior probability, respectively. 
pos_prob() takes the parent and their values and the child whose posterior probability is to be calculated.

The Normalize() function calculates the sum of the distribution and assigns its reciprocal to alpha. The alpha is then multiplied with the distribution.

* Approximate Inference 
For approximate inference, we used the likelihood_wt() which only creates samples of events assuming all evidence. 
The weight variable keeps track of the probability of the evidence variable with respect to the parents. The parents could be other evidence variables or random values of non evidence variables.
At the end, the weights of those samples that are consistent with the query variable are added and normalized.

The helper method weighted_sample() helps us with creating random samples consistent with the evidence.

* No of samples needed to approximate within 1%
For our code, the number of samples needed is more than 100000 to get probability within 1% error.
The output is given above and below.

* Experimentation
For approximate inference, we experimented with the sample size. 

First with sample size = 1000, we get the following output:
    With Exact Inference:  [0.2841718353643929, 0.7158281646356071]
    With Approximate Inference:  [0.3584422967595298, 0.6415577032404703]

sample size = 10000
    With Exact Inference:  [0.2841718353643929, 0.7158281646356071]
    With Approximate Inference:  [0.2577682813174684, 0.7422317186825315]

sample size = 100000
    With Exact Inference:  [0.2841718353643929, 0.7158281646356071]
    With Approximate Inference:  [0.29450564762264697, 0.705494352377353]
    
From these results, we assume that due to the small sampler size, the weights and prosterior probability are small, so the samples are generated with less accurate probabilities and these probabilities vary each time.
As we increase sample size, the approximate inference probabilities become closer to the exact inference results.
