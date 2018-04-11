# Key concepts in statistical inference

---

- PyMC3, Pyfolio and presentation by Thomas Wiecki on assessing a trading algo.
- John Kruschke: Bayesian estimation supersedes the t-test (Journal of experimental psychology 2012).
- How does the Student-t test work?
- John Kruschke, Torrin Liddell: The Bayesian New Statistics ... (Psychon Bull Rev February 2017)
- Jorge Lopez Puga, Martin Kryzwinski, Naomi Altman (Nature Methods, May 2015).

---?image=kruschke_liddell_table.png&size=auto 70%

---

A coin is tossed twice and shows two heads.

> Given the data, I’m less persuaded that the coin is fair.

Kruschke calls this _reallocating credibility_.

---
### Meet F

For a fair coin: P(HH)= 1/4.

> I declare “the coin is biased!” but I expect to be wrong 25% of the time over the long term.

---

F is actually carrying out a different exercise:

> F tries to limit _Type-1 errors_.

---

In this example with little data, the frequentist approach struggles.

---

Usually people like a p-value of 5% before they say ‘statistically significant’.

---
### Meet B

> Originally I was fifty-fifty.

> Then I saw HH.

> I now allocate 69% to the view that the coin is biased.

---

B has an update process:

> Prior + Model + Data -> Posterior

B uses Bayes's theorem for the update process.

---

Coming next, a picture inspired by the Puga, Kryzwinski and Altman paper

---?image=plots/tosses.png&size=auto 70%
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

Often F’s comment gets misunderstood as a ‘view’.

> Oh, you mean there is a 25% probability that the coin is biased?

> No, the coin is either biased or it is not.

---

For F:

> Probability == long term frequency.

For B:

> Probability == Algebra of Credibility

---
### Student’s t test

- **One sample**: to determine whether $\mu == 0$.
- **Two sample**: to determine whether $\mu_1 == \mu_2$.

NB ‘sample’ here is a collection: ‘we sampled once and collected 10 data points’.
---

See [this page here](https://www.statisticssolutions.com/manova-analysis-one-sample-t-test/), and discuss the assumptions.

---?image=student_t_distribution.png&size=auto 85%

---?image=t_test_in_a_spreadsheet.png&size=auto 50%

---
### The Bayesian approach

What would they say about the coin toss?

---

For B:

> Probability == Algebra of Credibility

---


Bayes's theorem itself is not controversial.

It’s just how the Bayesian use it as an inference tool that annoys the Frequentists.

---
Questions

- Is The B approach more stable? ‘Dance of the CIs’.
- B approaches the building of a model, prob with PyMC3.
- F gotchas, like sampling intentions.
- F: I don’t distort my results with a prior.

---

Snippets
====

Bayesian is more _accessible_

In frequentist analysis a primary goal is to keep the false alarm rate (type 1 errors) limited to 5% say.  Kruschke

Model calibration. In rates we build our models so that they are calibrated on expectations. But perhaps we should calibrate like credibility reallocation?

B can handle small data.
F has got lots of gotchas (sampling intention).
