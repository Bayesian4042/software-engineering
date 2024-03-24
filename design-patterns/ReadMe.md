# What are design patterns?
- Design patterns are well-tested, reusable solutions. They are solution templates for how to solve common software engineering problems.

# Why to use them
- Design patterns are associated with good, well organized software design. As a developer we are prone to mistakes and sometimes inexperienced decisions. Think of design patterns as a bag of reusable experience form many generations of coders and Software Engineers, that we get to learn from.

# Most crucial design patterns:
- Creational Design Pattern (Deals with ways of creating objects): 
    - Singleton
    - Factory Method
    - Builder pattern
- Structural (Deals with ways of managing complex objects hirerachies): 
    - Adaptor pattern
- Behaviour (Deals with ways of identifying and improving object messaging): 
    - Stratgey pattern
    - Observer pattern
    - State pattern

once you master these patterns, you will see the world of coding differently. 

# Why do we need software architecture?
  ## Complex software system are plagued with many issues:
    - Timelines are streteched because of changing requirements.
    - Multiple developers have hard time coordinating their efforts.
    - Often there is code redundancy and poor documentation.
  This creates issues with maintenance and overall flexibility of adding new features. 
  One answer to overall cited problems is having a proper design and architecture.

# Why use UML?
- UML is good tool to document something as well defined as Design Patterns. UML communicates design pattern structure very well. 
    - class Diagram
    - sequence Diagram

# Difference between organized and unorganized code?
- 

# What makes a good architecture ?
1. Loose coupling
   - weak knowledge association between components
   - changes to one component least affect existence or performance of another component.
2. Separation of concerns
    - breaking your architecture into tiers:
     presentation layer, bussiness layer, 
3. Law of demeter (LoD): principle of least knowledge.

# SOLID principles
1. single responsibility principle: 
- There should never be more than one reason for a class to change. Each class should have only one central responsibility. For example it should only deal with persistence or persistance, or only logging, or only notification or only error handling.

2. open/close principle: 
- Should be open for extension, closed for modification.
- For example, you have calculator class which has add, sub, div, mul methods. Now, when you have to add scientifc calculator, you should not modify but rather extend this class to support scientific operations. There can be new class which extends the calculator class.

3. The liskov substitution principle: 
- Function that use pointers or references to base class, must be able to use objects of derived classes without knowing it. 

4. The interface segregation principle: 
- Clients should not be forced to depend upon interfaces that they don't use.
- Declaring methods in an interface that the caller doesn't need pollutes the interface and leads to bulky or fat interface.
- 

5. The dependency inversion principle: depends on abstraction, not on concretion.

