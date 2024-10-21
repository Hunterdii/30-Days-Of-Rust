<div align="center">
  <h1>🦀 30 Days Of Rust: Day 10 - Generics 🚀</h1>
  <a href="https://www.linkedin.com/in/het-patel-8b110525a/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank">
    <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social" alt="LinkedIn" />
  </a>
  <a href="https://github.com/Hunterdii" target="_blank">
    <img src="https://img.shields.io/badge/Follow%20me%20on-GitHub-blue?style=flat-square&logo=github" alt="Follow me on GitHub" />
  </a>

<sub><h4><i>Author:
  <a href="https://www.linkedin.com/in/het-patel-8b110525a/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank">Het Patel</a></h4></i>
<small> October, 2024</small>
</sub>

</div>

[<< Day 9](../09_Error%20Handling/09_error_handling.md) | [Day 11 >>](../README.md)

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)

- [📘 Day 10 - Generics](#-day-10---generics)
  - [👋 Welcome](#-welcome)
  - [🔍 Overview](#-overview)
  - [🛠 Environment Setup](#-environment-setup)
  - [📖 Understanding Generics in Rust](#-understanding-generics-in-rust)
    - [📦 Why Use Generics?](#-why-use-generics)
    - [💡 Creating Generic Functions](#-creating-generic-functions)
    - [🔧 Structs with Generics](#-structs-with-generics)
    - [🔄 Enums with Generics](#-enums-with-generics)
    - [⚙ Generics with Traits](#-generics-with-traits)
    - [📜 Type Constraints and Bounds](#-type-constraints-and-bounds)
    - [🌍 Lifetimes with Generics](#-lifetimes-with-generics)
  - [🎯 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 10](#-exercises---day-10)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [✅ Exercise: Level 2](#-exercise-level-2)
    - [🎥 Helpful Video References](#-helpful-video-references)
  - [📝 Day 10 Summary](#-day-10-summary)

# 📘 Day 10 - Generics

## 👋 Welcome

Welcome to **Day 10** of your Rust journey! 🎉 Today, we’ll explore the power of **Generics**. Generics allow you to write flexible, reusable code that can work with different data types. They make your code more concise and reduce repetition. Let’s dive in! 🚀

**Congratulations!** 🎉 You've taken the first step in your journey to master the _30 Days of Rust_ programming challenge. In this challenge, you will learn the fundamentals of Rust and how to harness its power to write efficient, fast, and safe code. By the end of this journey, you'll have gained a solid understanding of Rust's core concepts and best practices, helping you become a confident Rustacean. 🦀


Feel free to join the [30 Days of Rust](https://discord.gg/dy4gAhng) community on Discord, where you can interact with others, ask questions, and share your progress!

## 🔍 Overview

Generics in Rust enable the creation of functions, structs, enums, and traits that can operate on different data types. In today’s lesson, we will cover:

- What Generics are and their significance.
- How to create generic functions.
- How to use generics with structs and enums.
- Understanding generics with traits.
- Applying type constraints and bounds.
- Exploring lifetimes in conjunction with generics.
- Using generics with traits to write more flexible code

  
## 🛠 Environment Setup

Ensure that you have your Rust environment set up correctly from Day 1. If you haven’t installed Rust yet, please refer to the setup instructions from [Day 1](../README.md#-environment-setup).

## 📖 Understanding Generics in Rust

### 📦 Why Use Generics?

Without generics, you'd have to duplicate code for each type you want to support. Generics remove this redundancy by allowing you to write a single function, struct, or enum that can operate on multiple types. Rust's powerful type inference and zero-cost abstractions make using generics highly efficient without adding runtime overhead.

Generics allow us to write code that can handle multiple types. For example, instead of writing separate functions for `i32` and `f64`, we can write a single generic function that works with any type.

**Example:**

```rust
fn print_item<T>(item: T) {
    println!("{:?}", item);
}

fn main() {
    print_item(10); // Works with integers
    print_item(3.14); // Works with floats
    print_item("Hello, Rust!"); // Works with strings
}
```

### 💡 Creating Generic Functions

Generics make functions more flexible by enabling them to work with different types. Let’s look at an example of a generic function:

Generic functions allow you to create more flexible and reusable code by defining functions that can work with any data type. You specify a placeholder for the type, and the compiler figures out the specific types at compile time.

```rust
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in list.iter() {
        if item > largest {
            largest = item;
        }
    }
    largest
}

fn main() {
    let numbers = vec![34, 50, 25, 100, 65];
    println!("The largest number is {}", largest(&numbers));

    let chars = vec!['y', 'm', 'a', 'q'];
    println!("The largest char is {}", largest(&chars));
}
```

### 🔧 Structs with Generics

Structs can also benefit from generics, allowing you to create data structures that work with different types. Here’s an example of a generic struct:

```rust
struct Point<T> {
    x: T,
    y: T,
}

fn main() {
    let integer_point = Point { x: 5, y: 10 };
    let float_point = Point { x: 1.0, y: 4.0 };

    println!("Integer Point: ({}, {})", integer_point.x, integer_point.y);
    println!("Float Point: ({}, {})", float_point.x, float_point.y);
}
```

### 🔄 Enums with Generics

Enums can also be made generic to handle different types. This is particularly useful when representing optional values or result types:

```rust
enum Option<T> {
    Some(T),
    None,
}

fn main() {
    let number = Option::Some(5);
    let text = Option::Some("Generics in Rust!");
    let no_value: Option<i32> = Option::None;
}
```


### ⚙ Generics with Traits

Generics can be constrained by traits to ensure they implement specific behavior. For instance, you can use `Display` to ensure a type can be printed:

```rust
fn print_item<T: std::fmt::Display>(item: T) {
    println!("{}", item);
}

fn main() {
    print_item(42);       // Prints an integer
    print_item("Hello");  // Prints a string
}
```

Generics can be combined with traits to specify behavior constraints. Here's an example:

```rust
fn print_number<T: std::fmt::Display>(value: T) {
    println!("The number is: {}", value);
}

fn main() {
    print_number(10);
    print_number(4.5);
}
```

### 📜 Type Constraints and Bounds

When defining generics, you can specify constraints using trait bounds to ensure that the generic type meets certain criteria. For example, a generic function can require that the type implements the `Clone` trait:

```rust
fn clone_item<T: Clone>(item: T) -> T {
    item.clone()
}
```

### 🌍 Lifetimes with Generics

Lifetimes can be specified with generics to ensure that references are valid for as long as needed. For example:

```rust
fn longest<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    if s1.len() > s2.len() {
        s1
    } else {
        s2
    }
}
```


### 🎯 Hands-On Challenge

Create a Rust program that uses generics to perform the following:

1. **Write a generic function** that can accept two values and return the larger of the two.
2. **Create a struct with two generic types** and implement a method to display both.
3. **Define an enum** that uses generics to store either a number or text.

Here's a basic template to get you started:

```rust
struct Pair<T, U> {
    first: T,
    second: U,
}

impl<T, U> Pair<T, U> {
    fn show(&self) {
        println!("Pair contains: ({:?}, {:?})", self.first, self.second);
    }
}

fn main() {
    let pair = Pair { first: "Rust", second: 101 };
    pair.show();
}
```

✅ **Share your solution on GitHub and tag #30DaysOfRust on social media! Let the world see your progress! 🚀**

## 💻 Exercises - Day 10

### ✅ Exercise: Level 1

1. Write a generic function `min_value<T>` that returns the smaller of two values.
2. Create a generic struct `Rectangle<T>` and add a method `area` to calculate its area.
3. Implement a generic function that takes a `Vector` of any type and prints each element.

### ✅ Exercise: Level 2

1. Write a generic function that swaps two variables of any type.
2. Create an enum `Result<T, E>` similar to Rust's standard `Result` to handle success and error scenarios generically.
3. Implement a trait `Summary` for a struct that provides a summary of the data it holds using generics.

### 🎥 Helpful Video References

- [Generics in Rust Explained](https://www.youtube.com/watch?v=6rcTSxPJ6Bw)
- [Rust Generics: A Deep Dive](https://www.youtube.com/watch?v=nvur2Ast8hE)

## 📝 Day 10 Summary

- Today, we explored how **Generics** make your Rust code more reusable and flexible.
- From generic functions to structs, enums, and traits, you now have a solid understanding of how to use generics to write cleaner and more efficient code.
- Keep practicing, and don't forget to share your journey with the community! 🎉

🌟 _Great job on completing Day 10! Keep practicing, and get ready for Day 11 where we will explore Traits in Rust!_

Thank you for joining **Day 10** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to ⭐ star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 9](../09_Error%20Handling/09_error_handling.md) | [Day 11 >>](../README.md)

---
