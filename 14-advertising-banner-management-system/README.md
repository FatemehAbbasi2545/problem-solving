# advertising-banner-management-system
Advertising banner management system:
We have a set of advertising banners, each banner has a name, dimensions, and probability of being displayed. Also, each campaign contains a set of banners and display rules.
Write a program that tells us which banner to display in each round of the experiment. And at the end, a report is provided showing how many rounds each banner has been displayed in.
The goal is to implement a module in Python that:
Uses NamedTuple to perform structural definitions.
Builds an object-oriented model for banners and campaigns using the concept of classes and inheritance.
Generates a banner in sequence based on display rules using iterators and generators (i.e., the banner that will be placed in the next round as a "playlist" using campaign rules).
Uses a simple mechanism to improve performance with memoization and caching to reduce costly rework.
Provides an option to generate a simple report of the banner delivery path.