<div align="center">
  <h1>🦀 30 Days Of Rust: Day 4 - Functions 🚀</h1>
  <a href="https://www.linkedin.com/in/het-patel-8b110525a/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank">
    <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social" alt="LinkedIn" />
  </a><a href="https://github.com/Hunterdii" target="_blank">
    <img src="https://img.shields.io/badge/Follow%20me%20on-GitHub-blue?style=flat-square&logo=github" alt="Follow me on GitHub" />
</a>

<sub><h4><i>Author:
  <a href="https://www.linkedin.com/in/het-patel-8b110525a/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank">Het Patel</a></h4></i>
<small> October, 2024</small>
</sub>

</div>

[<< Day 3](../03_Control%20Flow/03_control_flow.md) | [Day 5 >>](../05_Ownership%20and%20Borrowing/05_ownership_and_borrowing.md)

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)

- [📘 Day 4 - Functions](#-day-4---functions)
  - [👋 Welcome](#-welcome)
  - [🔍 Overview](#-overview)
  - [🛠 Environment Setup](#-environment-setup)
  - [📖 Functions in Rust](#-functions-in-rust)
    - [🧩 Defining a Simple Function](#-defining-a-simple-function)
    - [🔄 Function Parameters](#-function-parameters)
    - [📋 Return Values from Functions](#-return-values-from-functions)
    - [🔄 Nested Functions](#-nested-functions)
    - [🔄 Functions with Multiple Return Values](#-functions-with-multiple-return-values)
    - [🛑 Function Recursion](#-function-recursion)
  - [🎯 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 4](#-exercises---day-4)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [✅ Exercise: Level 2](#-exercise-level-2)
    - [🎥 Helpful Video References](#-helpful-video-references)
  - [📝 Day 4 Summary](#-day-4-summary)

<br/>

# 📘 Day 4 - Functions

## 👋 Welcome

Welcome to **Day 4** of the 30 Days of Rust! 🎉 Today, we are going to learn about **Functions**. Functions are fundamental building blocks in Rust and enable you to organize your code into reusable pieces. Let’s get started! 🚀

**Congratulations!** 🎉 You've taken the first step in your journey to master the _30 Days of Rust_ programming challenge. In this challenge, you will learn the fundamentals of Rust and how to harness its power to write efficient, fast, and safe code. By the end of this journey, you'll have gained a solid understanding of Rust's core concepts and best practices, helping you become a confident Rustacean. 🦀


Feel free to join the [30 Days of Rust](https://discord.gg/dy4gAhng) community on Discord, where you can interact with others, ask questions, and share your progress!


## 🔍 Overview

In Rust, functions:

- Allow you to encapsulate code into reusable components.
- Make it easier to understand and manage the flow of logic in your program.
- Can accept parameters, return values, and even call themselves recursively.

We will cover:

- How to define and call functions
- Passing parameters and returning values
- Nested functions, recursion, and more

## 🛠 Environment Setup

Ensure that you have your Rust environment set up correctly from Day 1. If you haven’t installed Rust yet, please refer to the setup instructions from [Day 1](../README.md#-environment-setup).


## 📖 Functions in Rust

## 🧩 Defining a Simple Function

Functions in Rust are defined using the `fn` keyword followed by the function name and parentheses.

**Example:**

```rust
fn greet() {
    println!("Hello, Hunterdii!");
}

fn main() {
    greet();
}
```

**Output:**

```
Hello, Hunterdii!
```

## 🔄 Function Parameters

You can pass values to functions as parameters, allowing you to create flexible and reusable functions.

**Example:**

```rust
fn greet_user(name: &str) {
    println!("Hello, {}!", name);
}

fn main() {
    greet_user("Het");
}
```

**Output:**

```
Hello, Het!
```

## 📋 Return Values from Functions

Functions can return values using the `->` symbol followed by the return type.

**Example:**

```rust
fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn main() {
    let sum = add(5, 3);
    println!("The sum is: {}", sum);
}
```

**Output:**

```
The sum is: 8
```

## 🔄 Nested Functions

You can define functions inside other functions, known as nested functions. This is useful when you need helper functions that are only relevant within the parent function.

**Example:**

```rust
fn outer_function() {
    fn inner_function() {
        println!("This is an inner function.");
    }

    inner_function();
}

fn main() {
    outer_function();
}
```

**Output:**

```
This is an inner function.
```

## 🔄 Functions with Multiple Return Values

Rust can return multiple values using tuples.

**Example:**

```rust
fn calculate(a: i32, b: i32) -> (i32, i32) {
    (a + b, a * b)
}

fn main() {
    let (sum, product) = calculate(4, 5);
    println!("Sum: {}, Product: {}", sum, product);
}
```

**Output:**

```
Sum: 9, Product: 20
```

## 🛑 Function Recursion

A function that calls itself is called a recursive function. Make sure to include a base condition to avoid infinite loops.

**Example:**

```rust
fn factorial(n: u32) -> u32 {
    if n == 0 {
        1
    } else {
        n * factorial(n - 1)
    }
}

fn main() {
    let result = factorial(5);
    println!("Factorial of 5 is: {}", result);
}
```

**Output:**

```
Factorial of 5 is: 120
```

## 🎯 Hands-On Challenge

Write a program that:

1. Defines a function to check if a number is even or odd.
2. Includes a function to calculate the area of a circle given its radius.
3. Uses a recursive function to find the greatest common divisor (GCD) of two numbers.

## 💻 Exercises - Day 4

### ✅ Exercise: Level 1

1. Write a function that takes a string and returns its length.
2. Create a function that returns the maximum of two numbers.
3. Define a function to convert Celsius temperatures to Fahrenheit.
4. Write a function to print the multiplication table of a given number.
5. Implement a function that takes two integers and returns their greatest common divisor (GCD).

### ✅ Exercise: Level 2

1. Write a recursive function to find the nth Fibonacci number.
2. Create a function that takes a list of numbers and returns the average.
3. Implement a function that accepts a string and returns the number of vowels in it.
4. Write a program that simulates a calculator with functions for addition, subtraction, multiplication, and division.
5. Implement a function to sort an array of integers using the bubble sort algorithm.
6. Write a function that uses nested functions to calculate the area and circumference of a circle.

## 🎥 Helpful Video References

- [Rust Functions & Recursion (Hindi)](https://www.youtube.com/watch?v=GY74ezA3O_Q)
- [Functions in Rust - Rust Programming Tutorial](https://www.youtube.com/watch?v=hJLc2Zu405A)
- [Understanding Functions & Parameters in Rust](https://www.youtube.com/watch?v=W3h7TmkswWI)

## 📝 Day 4 Summary

- Learned how to define and call functions in Rust.
- Explored passing parameters and returning values from functions.
- Understood how to work with nested functions, recursion, and multiple return values.

🌟 _Great job on completing Day 4! Keep practicing, and get ready for Day 5 where we will explore Ownership and Borrowing in Rust!_

Thank you for joining **Day 4** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!


**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 3](../03_Control%20Flow/03_control_flow.md) | [Day 5 >>](../05_Ownership%20and%20Borrowing/05_ownership_and_borrowing.md)

---
