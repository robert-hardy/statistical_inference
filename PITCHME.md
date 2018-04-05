Key concepts in statistical inference

Starting point(s)
====

- PyMC3 & presentation by Thomas Wiecki on assessing a trading algo.
- Pyfolio.
- John Kruschke: Bayesian estimation supersedes the t-test (Journal of experimental psychology 2012).

---

Overview
====
1. What is statistical inference?
2. Meet F and B
3. How come B is the disrupter?
4. Inference in real life.
5. The Student’s t test.
6. PyMC3 demo of Kruschke’s paper.

Disclaimer: the Bayesian approach appeals to me (my reasons why are in the following).

---

A coin example
====
A coin is tossed twice and shows two heads.
What can your infer?

Logical inference gives conclusions that are guaranteed to be true it which give no real value here:
- Could the could be biased? Yes.
- Could the coin be fair? Yes.
- Could the coin have only tails? No.

---

Meet F
====
F: <thinks> … for a fair coin: P(HH)= 0.25, so if I declare “the coin is biased!” I will commit a Type-1 error 25% of the time …

F: <says> I declare that the coin is biased (and reserve the right to be wrong 25% of the time).

‘Yes, but do you _reckon_ the coin is biased?’

F: <no answer> (F is avoiding the question).

---

Meet B
====

B: ‘I originally reckoned that the coin was fair, but given the HH data I see, I have updated my estimate and now calculate that there is a 75% chance that the coin is biased.’

---



---

‘Classical’ statistical inference makes precise, conclusions that often seem too technical:
- I reject the null hypothesis with a p value of 0.25 (0.05 is a favourite).

In this example with little data, the frequentist is clearly struggling.

---

Bayesian inference gives conclusions that seem much more intuitive:
- Given the data, I’m more persuaded the coin is biased (and I can be very precise about what I mean).

---

Aside
====
How come F is considered to be the ‘official’ approach, with B the newcomer?

Many coins
====
I toss the coin 50 times and see this:

What do you think now?

F replies
====
For a fair coin P(33 heads in 50 tosses)=, so if I declare “the coin


Poker
====
You have a pair of tens. The fourth street shows a Jack. What is the probability that your opponent has made a pair of Jacks?

Amateur? Higher probability, because they are more likely to punt if holding a single queen.

---
My point
====
Inference is not an isolated practice. The question you ask depends on the problem you are facing.


Intuition
====
We toss a coin 10 times and get 8 heads. But still it could be a fair coin.

We toss a coin 100 times and get 80 heads.

---

More samples, tighter distribution
====

Bimomial(10, 0.5): 90%=Prob(2<X<8)

Binomial(100, 0.5): 90%=Prob(40<X<60)

There is rarely any _conclusive_ evidence.

Student’s t test
====

Coin tossing
====
Model: Binomial(10, 0.5)
Statistic: nb heads



Bayesian approach
====
What is our best guess at the long-term average?
Rather than imagining the existence of some ideal ‘probability p’.

What is a probability?
====
We only ever carry out experiments. We never see a real probability.
From the point of view of experiments, only something like a long-term average or an updated big process shows any kind of regularity in time.

Our probability models are an algebra of probabilities and do give us the right answers, but reality is more grungy — we only ever get a sequence that looks like it gets closer to a limit but within a distribution of ‘error’.

---

What is the question?
====
A coin is tossed twice and shows two heads.
What now?

Could the could be biased? Yes.
Could the coin be fair? Yes.
Could the coin have only tails? No.

---
Poker
====
You have a pair of tens. The fourth street shows a Jack. What is the probability that your opponent has made a pair of Jacks?

Amateur? Higher probability, because they are more likely to punt if holding a single queen.

---
My point
====
Inference is not an isolated practice. The question you ask depends on the problem you are facing.

---
P values
====
A cutoff of 5% is common. It means that you hope to make a type-1 error on fewer than 5% of the repetitions.

It suggests ‘extreme’, or that you would be unlucky if you got the wrong answer.


A problem we all can agree on
====
Two coins (p=0.5 and p=0.75). One is randomly chosen then tossed twice.
We see HH.
What is the probability that the biased coin was picked?

---

Application of Bayes’s theorem
====
$$P(biased|HH) = frac{P(HH|biased) P(biased)}{P(HH)}$$

This gives $$P(biased|HH)=0.69$$.

---

A continuity argument
====
Statistical inference should tend to the same result as logical inference.

---

NHST
====
A fair could tossed 10 times will show 10 heads in a row, 0.05% of the time.

We will commit a Type 1 error 5 times every 10,000 repetitions, declaring that ‘the coin is biased’ when in fact it is not.

---

Student’s t test
====
We have some sample data. The ‘t statistic’ would have that value or higher on p% of the repetitions. So if we reject the null hypothesis we will commit a type 1 error on p% of the repetitions.

---
Bayesian approach
====
What is a credible setting for p given that we have seen 10 heads in a row.

MLE says p=1.

Bayesian just updates your previous guess.

---
What is better about updating, rather than MLE?
====


Snippets
====

Bayesian is more _accessible_

In frequentist analysis a primary goal is to keep the false alarm rate (type 1 errors) limited to 5% say.  Kruschke

Example of a hustler — does everything possible to make the data look like it was produced by a ‘fair coin’. I suspect that NHST would absolutely fail here.

Model calibration. In rates we build our models so that they are calibrated on expectations. But perhaps we should calibrate like credibility reallocation?