<div align="center">
  <h1>🦀 30 Days Of Rust: Day 6 - Structs 🚀</h1>
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

[<< Day 5](../05_Ownership%20and%20Borrowing/05_ownership_and_borrowing.md) | [Day 7 >>](../07_Enums/07_enums.md)

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)

- [📘 Day 6 - Structs](#-day-6---structs)
  - [👋 Welcome](#-welcome)
  - [🔍 Overview](#-overview)
  - [🛠 Environment Setup](#-environment-setup)
  - [📖 Understanding Structs](#-understanding-structs)
    - [🧩 What is a Struct?](#-what-is-a-struct)
    - [📌 Defining Structs](#-defining-structs)
    - [🔄 Creating Instances of Structs](#-creating-instances-of-structs)
    - [🛠 Using Structs in Functions](#-using-structs-in-functions)
    - [🔄 Updating Structs](#-updating-structs)
    - [🔄 Tuple Structs](#-tuple-structs)
    - [🛠 Unit-Like Structs](#-unit-like-structs)
    - [🛠 Structs with Methods](#-structs-with-methods)
  - [🎯 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 6](#-exercises---day-6)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [✅ Exercise: Level 2](#-exercise-level-2)
    - [🎥 Helpful Video References](#-helpful-video-references)
  - [📝 Day 6 Summary](#-day-6-summary)

<br/>

# 📘 Day 6 - Structs

## 👋 Welcome

Welcome to **Day 6** of the 30 Days of Rust! 🎉 Today, we will explore **Structs** in Rust. Structs allow you to create custom data types that can group related values together. Let’s understand how they work and how you can use them effectively! 🚀

**Congratulations!** 🎉 You've taken the first step in your journey to master the _30 Days of Rust_ programming challenge. In this challenge, you will learn the fundamentals of Rust and how to harness its power to write efficient, fast, and safe code. By the end of this journey, you'll have gained a solid understanding of Rust's core concepts and best practices, helping you become a confident Rustacean. 🦀


Feel free to join the [30 Days of Rust](https://discord.gg/dy4gAhng) community on Discord, where you can interact with others, ask questions, and share your progress!


## 🔍 Overview

In this lesson, you will learn:

- How to define and create instances of structs.
- Different types of structs: classic, tuple, and unit-like.
- How to update structs and create methods associated with them.
- Practical applications of structs through examples and exercises.

## 🛠 Environment Setup

Ensure that you have your Rust environment set up correctly from Day 1. If you haven’t installed Rust yet, please refer to the setup instructions from [Day 1](../README.md#-environment-setup).


## 📖 Understanding Structs

### 🧩 What is a Struct?

A **struct** in Rust is a custom data type that allows you to name and package multiple related values together.

### 📌 Defining Structs

You can define a struct with named fields:

**Example:**

```rust
struct User {
    username: String,
    email: String,
    active: bool,
    sign_in_count: u64,
}
```

### 🔄 Creating Instances of Structs

To create an instance of a struct, specify the values for its fields:

**Example:**

```rust
fn main() {
    let user1 = User {
        username: String::from("Rustacean"),
        email: String::from("rust@example.com"),
        active: true,
        sign_in_count: 1,
    };
    
    println!("Username: {}", user1.username);
}
```

**Output:**

```
Username: Rustacean
```

### 🛠 Using Structs in Functions

You can pass structs to functions or return them from functions.

**Example:**

```rust
fn main() {
    let user1 = create_user(String::from("rustacean@rust.com"), String::from("Rustacean"));
    println!("Email: {}", user1.email);
}

fn create_user(email: String, username: String) -> User {
    User {
        email,
        username,
        active: true,
        sign_in_count: 1,
    }
}
```

### 🔄 Updating Structs

Use struct update syntax to create a new instance from an existing one.

**Example:**

```rust
fn main() {
    let user1 = User {
        username: String::from("Rustacean"),
        email: String::from("rust@example.com"),
        active: true,
        sign_in_count: 1,
    };
    
    let user2 = User {
        email: String::from("new@example.com"),
        ..user1
    };
    
    println!("Username: {}", user2.username);
}
```

**Output:**

```
Username: Rustacean
```

### 🔄 Tuple Structs

Tuple structs are similar to tuples, but they have a custom name and allow creating different types:

**Example:**

```rust
struct Color(i32, i32, i32);
fn main() {
    let black = Color(0, 0, 0);
    println!("Color: {}, {}, {}", black.0, black.1, black.2);
}
```

### 🛠 Unit-Like Structs

A struct without any fields is called a unit-like struct:

**Example:**

```rust
struct AlwaysEqual;
fn main() {
    let _subject = AlwaysEqual;
}
```

### 🛠 Structs with Methods

You can implement methods on structs using `impl`:

**Example:**

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

fn main() {
    let rect = Rectangle { width: 30, height: 50 };
    println!("Area: {}", rect.area());
}
```

**Output:**

```
Area: 1500
```

## 🎯 Hands-On Challenge

1. Create a program that defines and uses a struct for a book with fields like `title`, `author`, `pages`, and `publisher`.
2. Write functions to calculate and display book details using the struct.

## 💻 Exercises - Day 6

### ✅ Exercise: Level 1

1. Define a struct for a rectangle and implement methods to calculate area and perimeter.
2. Create a program to demonstrate the use of struct update syntax.

### ✅ Exercise: Level 2

1. Write a program that uses a tuple struct to store RGB color values.
2. Implement a method on a struct that compares two struct instances for equality.
3. Write a function that returns an instance of a unit-like struct.

## 🎥 Helpful Video References

- [Rust Structs and Enums(Language : Hindi)](https://www.youtube.com/watch?v=P1rfrhdrOeA)
- [Rust Structs and Enums(Language : English)](https://www.youtube.com/watch?v=90jSoJkBasA&t=10s)
- [Methods in Rust](https://www.youtube.com/watch?v=7EYSXQFRyKY)
- [Structs in Rust Explained](https://www.youtube.com/watch?v=n3bPhdiJm9I)

## 📝 Day 6 Summary

- Learned about defining and using structs.
- Explored different types of structs, including tuple and unit-like.
- Understood how to implement methods and use structs in practical scenarios.

🌟 _Great job on completing Day 6! Keep practicing, and get ready for Day 7 where we will explore Enums in Rust!_

Thank you for joining **Day 6** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 5](../05_Ownership%20and%20Borrowing/05_ownership_and_borrowing.md) | [Day 7 >>](../07_Enums/07_enums.md)

---
