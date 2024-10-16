<div align="center">
  <h1>🦀 30 Days Of Rust: Day 5 - Ownership & Borrowing 🚀</h1>
  <a href="https://www.linkedin.com/in/het-patel-8b110525a/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank">
    <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social" alt="LinkedIn" />
  </a><a href="https://github.com/Hunterdii" target="_blank">
    <img src="https://img.shields.io/badge/Follow%20me%20on-GitHub-blue?style=flat-square&logo=github" alt="Follow me on GitHub" />
</a>

<sub>Author:
<a href="https://www.linkedin.com/in/het-patel-8b110525a/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank">Het Patel</a><br>
</sub>

</div>

[<< Day 4](../Functions/04_functions.md) | [Day 6 >>](../Structs/06_structs.md)

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)

- [📘 Day 5 - Ownership & Borrowing](#-day-5---ownership--borrowing)
  - [👋 Welcome](#-welcome)
  - [🔍 Overview](#-overview)
  - [🛠 Environment Setup](#-environment-setup)
  - [📖 Understanding Ownership](#-understanding-ownership)
    - [🧩 What is Ownership?](#-what-is-ownership)
    - [🔄 Moving Ownership](#-moving-ownership)
    - [🔄 Borrowing and References](#-borrowing-and-references)
    - [🔄 Mutable References](#-mutable-references)
    - [🛑 The Rules of Ownership](#-the-rules-of-ownership)
    - [🛠 Working with Ownership in Functions](#-working-with-ownership-in-functions)
  - [🎯 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 5](#-exercises---day-5)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [✅ Exercise: Level 2](#-exercise-level-2)
    - [🎥 Helpful Video References](#-helpful-video-references)
  - [📝 Day 5 Summary](#-day-5-summary)

<br/>

# 📘 Day 5 - Ownership & Borrowing

## 👋 Welcome

Welcome to **Day 5** of the 30 Days of Rust! 🎉 Today, we dive into **Ownership and Borrowing**. Understanding these concepts is crucial because they form the core of Rust's memory safety model. Let’s explore them together! 🚀

**Congratulations!** 🎉 You've taken the first step in your journey to master the _30 Days of Rust_ programming challenge. In this challenge, you will learn the fundamentals of Rust and how to harness its power to write efficient, fast, and safe code. By the end of this journey, you'll have gained a solid understanding of Rust's core concepts and best practices, helping you become a confident Rustacean. 🦀


Feel free to join the [30 Days of Rust](https://discord.gg/dy4gAhng) community on Discord, where you can interact with others, ask questions, and share your progress!

## 🔍 Overview

In Rust, **Ownership** and **Borrowing**:

- Help manage memory automatically and safely.
- Ensure there are no data races or dangling references.
- Define how values are passed around and used in Rust programs.

We will cover:

- The concept of ownership and borrowing.
- How to pass data by value and by reference.
- Managing mutable and immutable references.
- Applying these concepts with examples and exercises.

## 🛠 Environment Setup

Ensure that you have your Rust environment set up correctly from Day 1. If you haven’t installed Rust yet, please refer to the setup instructions from [Day 1](../README.md#-environment-setup).


## 📖 Understanding Ownership

### 🧩 What is Ownership?

In Rust, every value has a single owner. When the owner goes out of scope, the value is automatically dropped (freed from memory).

**Example:**

```rust
fn main() {
    let s = String::from("Hello, Rust!");
    println!("{}", s); // s is valid here
}
// s goes out of scope and is dropped
```

### 🔄 Moving Ownership

When a variable is assigned to another, the ownership is moved, not copied.

**Example:**

```rust
fn main() {
    let s1 = String::from("Rust");
    let s2 = s1; // s1 is now invalid, ownership is moved to s2
    println!("{}", s2);
    // println!("{}", s1); // This will cause an error
}
```

**Output:**

```
Rust
```

### 🔄 Borrowing and References

Borrowing allows you to pass references to values without taking ownership.

**Example:**

```rust
fn main() {
    let s = String::from("Hello");
    print_string(&s); // Passing a reference
    println!("{}", s); // s is still valid here
}

fn print_string(s: &String) {
    println!("{}", s);
}
```

**Output:**

```
Hello
Hello
```

### 🔄 Mutable References

You can borrow a mutable reference to allow modifying the data without taking ownership.

**Example:**

```rust
fn main() {
    let mut s = String::from("Hello");
    modify_string(&mut s);
    println!("{}", s); // Modified string
}

fn modify_string(s: &mut String) {
    s.push_str(", world!");
}
```

**Output:**

```
Hello, world!
```

### 🛑 The Rules of Ownership

1. Each value has a single owner.
2. When the owner goes out of scope, the value is dropped.
3. You can have multiple immutable references, but only one mutable reference at a time.

### 🛠 Working with Ownership in Functions

Passing values to functions can also transfer ownership or borrow values, depending on how they are passed.

**Example:**

```rust
fn main() {
    let s = String::from("Rust");
    takes_ownership(s); // s is moved, and no longer valid here
    let x = 5;
    makes_copy(x); // x is still valid because integers are Copy
}

fn takes_ownership(s: String) {
    println!("{}", s);
}

fn makes_copy(x: i32) {
    println!("{}", x);
}
```

**Output:**

```
Rust
5
```

## 🎯 Hands-On Challenge

Write a program that:

1. Demonstrates moving and copying with variables.
2. Creates functions that take ownership of their parameters and return a result.
3. Uses references to avoid unnecessary data copying.

## 💻 Exercises - Day 5

### ✅ Exercise: Level 1

1. Write a function that takes a string, borrows it, and returns its length.
2. Create a program that demonstrates moving ownership between variables.
3. Implement a function that accepts a mutable reference and modifies the data.

### ✅ Exercise: Level 2

1. Write a program that uses mutable references to swap two variables.
2. Implement a function to clone a vector without transferring ownership.
3. Create a recursive function to find the factorial of a number using borrowed values.
4. Write a function that counts the occurrences of a character in a string without taking ownership.

## 🎥 Helpful Video References

- [Rust Ownership Explained](https://www.youtube.com/watch?v=VFIOSWy93H0)
- [Borrowing and References in Rust](https://www.youtube.com/watch?v=qIhoi-74IXc)
- [Rust: Understanding Ownership and Borrowing](https://www.youtube.com/watch?v=oI94lrLc2R8)

## 📝 Day 5 Summary

- Learned about the core concepts of ownership and borrowing.
- Explored passing data by value and reference.
- Understood the rules and nuances of working with mutable and immutable references.

🌟 _Great job on completing Day 5! Keep practicing, and get ready for Day 6 where we will explore Structs in Rust!_

Thank you for joining **Day 5** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to ⭐ star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 4](../Functions/04_functions.md) | [Day 6 >>](../Structs/06_structs.md)

---
