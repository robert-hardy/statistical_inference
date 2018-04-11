Monday evening

# Key concepts in statistical inference

---

- PyMC3, Pyfolio and presentation by Thomas Wiecki on assessing a trading algo.
- How does the Student-t test work?
- John Kruschke: Bayesian estimation supersedes the t-test (Journal of experimental psychology 2012).
- John Kruschke, Torrin Liddell: The Bayesian New Statistics ... (Psychon Bull Rev February 2017)
- Jorge Lopez Puga, Martin Kryzwinski, Naomi Altman (Nature Methods, May 2015).

---
1. Different approaches
2. The F approach.
3. The Student’s t test.
4. The B approach.
5. PyMC3 demo of Kruschke’s paper.

---?image=kruschke_liddell_table.png&size=auto 70%

---
### A coin example
A coin is tossed twice and shows two heads.

---

I was hoping for something like:

> Given the data, I’m less persuaded that the coin is fair.

---

Kruschke calls this _reallocating credibility_.

---

What does the frequentist have to say?

---
### Meet F

For a fair coin: P(HH)= 1/4.

> I declare “the coin is biased!” but I expect to be wrong 25% of the time over the long term.

That is not what I was expecting.

---

F is actually carrying out a different exercise:

> F tries to limit _Type-1 errors_.

Clue to everything:

> ... over the long term.

---

In this example with little data, the frequentist approach struggles.

Usually people like a p-value of 5% before they say ‘statistically significant’.

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

Different variations:
- **One sample**: to ‘prove’ that the population mean is not zero.
- **Two sample**: to ‘prove’ that two populations have a different mean.

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

### Meet B

> Originally I was fifty-fifty.

> Then I saw HH.

> I now allocate 69% to the view that the coin is biased and 31% that the coin
is fair.

---

B updates her view based on data seen.

> Prior + Model + Data -> Posterior

B uses Bayes's theorem for the update process.

---

Bayes's theorem itself is not controversial.

It’s just how the Bayesian use it as an inference tool that annoys the Frequentists.

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
