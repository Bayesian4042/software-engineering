# Singleton Pattern
Singleton Pattern is creational design pattern that ensures that,
a class has only one instance and provides a global point of access to it.
All the client will get the same instance of the class.

## What is good for?
- When you want controller the access to shared resource like loggers, caching, Thread pools, Database connection, configuration access. 

- This pattern is used with other patterns like Abstract factory, builder etc
- make sure it follows SRP.
- make sure controll is properly controlled and locked in multi-thread env. 



