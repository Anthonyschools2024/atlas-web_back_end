
Introduction

This guide covers JavaScript ES6 classes, how to define and extend them, and advanced features like static methods and metaprogramming.

Class Basics

ES6 introduced the class syntax, making it easier to work with objects and prototypes.

Defining a Class

class Animal {
  constructor(name, type) {
    this.name = name;
    this.type = type;
  }

  describe() {
    return `${this.name} is a ${this.type}.`;
  }
}

const myPet = new Animal('Buddy', 'Dog');
console.log(myPet.describe()); // Output: Buddy is a Dog.

Extending Classes

Inheritance allows a new class to derive properties and methods from an existing one using extends and super().

class Dog extends Animal {
  constructor(name, breed) {
    super(name, 'dog'); // Calls the parent constructor
    this.breed = breed;
  }

  bark() {
    return `${this.name} barks!`;
  }
}

const myDog = new Dog('Buddy', 'Golden Retriever');
console.log(myDog.describe()); // Output: Buddy is a dog.
console.log(myDog.bark()); // Output: Buddy barks!

Adding Methods

Methods are functions inside a class and can be called on class instances.

class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    return `Hello, my name is ${this.name}.`;
  }

  haveBirthday() {
    this.age += 1;
    return `I just turned ${this.age}!`;
  }
}

const john = new Person('John', 30);
console.log(john.greet()); // Output: Hello, my name is John.
console.log(john.haveBirthday()); // Output: I just turned 31!

Static Methods

Static methods belong to the class itself and are not tied to instances.

class MathUtils {
  static add(a, b) {
    return a + b;
  }
}

console.log(MathUtils.add(5, 3)); // Output: 8

Another example using static methods:

class Car {
  constructor(brand, model) {
    this.brand = brand;
    this.model = model;
  }

  static generateVIN() {
    return 'VIN-' + Math.random().toString(36).substring(2, 15);
  }
}

const vin = Car.generateVIN();
console.log(vin); // Random VIN number

Metaprogramming in JavaScript

Metaprogramming allows code to modify or generate other code dynamically.

Example Using Reflect

class User {
  constructor(name) {
    this.name = name;
  }
}

const user = new User('Alice');
console.log(Reflect.has(user, 'name')); // Output: true