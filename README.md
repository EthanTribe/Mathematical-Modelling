# Lindenmayer Systems
A Lindenmayer system (or L-System for short) is a set of recursive rules to form a branching sequence iteratively.
They are typically used to model plant growth or generate other fractals.

To program this I have implimentend the recursion in Python and used a turtle to draw out the configured system.

In a system's rules the letters represent segments, + and - represent turning left or right respectively, and square brackets mean the enclosed section is a subset.

## Barnsley Fern
This fractal has two variables variables X and F.

The rules are:
* X -> F+[[X]-X]-F[-FX]+X
* F -> FF

The system's initial sequence is "-X".

![](Barnsley%20Fern.png)
