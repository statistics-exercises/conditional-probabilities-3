# Continuous conditional variables

We can do what we have just done with discrete random variables with continuous random variables also.  Consider for instance the following:

![](https://render.githubusercontent.com/render/math?math=P(X=x|Y=y)=\frac{1}{y}e^{-\frac{x}{y}}\qquad\textrm{where}\qquad)

The conditional probability density for the random variable X here is an exponential distribution.  The parameter in this distribution, meanwhile, is a sample from a standard normal distribution.  Once again we have a complicated distribution that we have not seen in this course.  This complex distribution is constructed, however, from simpler pieces (normal distributions and exponential distribution) that we have seen.

__Your task in this exercise is to complete the function `gen_x` and to thus generate samples of the distribution X.__  As with the previous exercise, I have written code to generate a graph showing the values of the random variable.
