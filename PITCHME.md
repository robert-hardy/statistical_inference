Monday
# Key concepts in statistical inference

B can handle small data.
F has got lots of gotchas (sampling intention).

---

- PyMC3, Pyfolio and presentation by Thomas Wiecki on assessing a trading algo.
- John Kruschke: Bayesian estimation supersedes the t-test (Journal of experimental psychology 2012).
- John Kruschke, Torrin Liddell: The Bayesian New Statistics ... (Psychon Bull Rev February 2017)
- Jorge Lopez Puga, Martin Kryzwinski, Naomi Altman (Nature Methods, May 2015).

---

1. The F and B approaches
2. The Student’s t test.
3. PyMC3 demo of Kruschke’s paper.

---?image=kruschke_liddell_table.png&size=auto 70%

---
### A coin example
A coin is tossed twice and shows two heads.

How do the two camps handle this?

---
### Meet F

For a fair coin: P(HH)= 0.25

> I declare “the coin is biased!” but I expect to be wrong 25% of the time over the long term.

---

F's approach is to limit _Type-1 errors_.

---

In this example with little data, the frequentist approach struggles.

Usually people like a p-value of 5% before they say ‘statistically significant’.

---

Often F’s comment gets misunderstood as a ‘view’.

> Oh, you mean there is a 25% probability that the coin is biased?

> No, the coin is either biased or it is not.

---

What we really want is something like:

> Given the data, I’m less persuaded that the coin is fair.

---

Kruschke calls this _reallocating credibility_.

---

### Meet B

> Originally fifty-fifty fair or biased.

> Then I see HH.

> I now allocate 69% to the view that the coin is biased and 31% that the coin
is fair.

---

B updates her view based on data seen.

> Prior + Model + Data -> Posterior

B uses Bayes's theorem for the update process.

---

Bayes's theorem itself is not controversial.

What is the probability that we got the biased coin?

---?image=plots/tosses.png&size=auto 70%
---

That picture was inspired by the calculation done in the Puga, Kryzwinski and Altman paper.

---

Two coins: one is fair, one is biased (75% prob of H).

I randomly pick one.

I toss it twice and get HH.

What is the probability I chose the biased coin?

---?image=tree_of_probabilities.jpg&size=auto 70%

---
Bayes's theorem:

$$P(biased|HH) = \frac{P(HH|biased) \times P(biased)}{P(HH)}$$

---?image=coin_toss_calculations.jpg&size=auto 70%

---

That is the 69% that B mentioned earlier.

---

### Student’s t test

Is used in cases where we want to show that two populations have a different
average, based on two samples.

For example, to show that some medical treatment has a 'statistically
significant' effect.

---?image=student_t_distribution.png&size=auto 70%

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

