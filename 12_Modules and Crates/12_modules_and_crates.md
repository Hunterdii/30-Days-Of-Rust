<div align="center">
  <h1>🦀 30 Days Of Rust: Day 12 - Modules and Crates 🚀</h1>
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

[<< Day 11](../11_Traits/11_traits.md) | [Day 13 >>](../13_Testing/13_testing.md)

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)

- [📘 Day 12 - Modules and Crates](#-day-12---modules-and-crates)
  - [👋 Welcome](#-welcome)
  - [🔍 Overview](#-overview)
  - [🛠 Environment Setup](#-environment-setup)
  - [📖 Understanding Modules](#-understanding-modules)
    - [📦 Creating a Module](#-creating-a-module)
    - [🔄 Using a Module](#-using-a-module)
  - [📦 What Are Crates?](#-what-are-crates)
    - [🔍 Creating a Crate](#-creating-a-crate)
    - [🔗 External Crates](#-external-crates)
  - [🎯 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 12](#-exercises---day-12)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [✅ Exercise: Level 2](#-exercise-level-2)
    - [🎥 Helpful Video References](#-helpful-video-references)
  - [📝 Day 12 Summary](#-day-12-summary)

# 📘 Day 12 - Modules and Crates

## 👋 Welcome

Welcome to **Day 12** of your Rust journey! 🎉 Today, we’ll explore the powerful concepts of **modules** and **crates**, which help organize and encapsulate your code effectively.

**Congratulations!** 🎉 You've taken the first step in your journey to master the _30 Days of Rust_ programming challenge. In this challenge, you will learn the fundamentals of Rust and how to harness its power to write efficient, fast, and safe code. By the end of this journey, you'll have gained a solid understanding of Rust's core concepts and best practices, helping you become a confident Rustacean. 🦀


Feel free to join the [30 Days of Rust](https://discord.gg/dy4gAhng) community on Discord, where you can interact with others, ask questions, and share your progress!

## 🔍 Overview

In Rust, **modules** provide a way to organize code into separate namespaces, while **crates** are packages of Rust code that can be shared. In this lesson, we will cover:

- The role of modules in organizing code
- How to create and use modules
- Understanding crates and their structure
- How to create and manage your own crates

## 🛠 Environment Setup

Ensure that you have your Rust environment set up correctly from Day 1. If you haven’t installed Rust yet, please refer to the setup instructions from [Day 1](../README.md#-environment-setup).

## 📖 Understanding Modules

## 📦 Creating a Module

Modules are defined using the `mod` keyword. They help encapsulate code and prevent naming conflicts. Here’s how to create a simple module:

```rust
mod greetings {
    pub fn hello() {
        println!("Hello, Rustaceans!");
    }
}
```

In this example, we define a module called `greetings` with a public function `hello` that prints a message.

## 🔄 Using a Module

To use a module, you simply call its function by referencing the module name:

```rust
fn main() {
    greetings::hello();
}
```

When you run this code, the output will be:

```
Hello, Rustaceans!
```

Modules can also contain sub-modules, structs, enums, and more, providing a flexible structure for organizing your code.

## Creating Modules

Modules are created using the `mod` keyword. Here's a simple example:

```rust
mod my_module {
    pub fn hello() {
        println!("Hello from my_module!");
    }
}
```

## Accessing Module Contents

To access functions or structs from a module, use the `::` operator:

```rust
fn main() {
    my_module::hello();
}
```

## Nested Modules

You can create nested modules for better organization:

```rust
mod outer {
    pub mod inner {
        pub fn greet() {
            println!("Hello from the inner module!");
        }
    }
}

fn main() {
    outer::inner::greet();
}
```

## 📦 What Are Crates?

A **crate** is a package of Rust code. It can be a binary crate (an executable program) or a library crate (a reusable library). Crates are the fundamental unit of code organization in Rust.

## 🔍 Creating a Crate

To create a new crate, you can use the `cargo` command:

```bash
cargo new my_crate --lib
```

This command creates a new library crate named `my_crate`. You can navigate to the `my_crate` directory to find the `src/lib.rs` file, where you can start adding your code.

## 🔗 External Crates

## Using External Crates

To use an external crate, add it to your `Cargo.toml` file:

```toml
[dependencies]
serde = "1.0"
```

Then, you can use it in your code:

```rust
use serde::Serialize;

#[derive(Serialize)]
struct MyStruct {
    name: String,
    age: u32,
}
```

## Examples 💡

Here's a more comprehensive example demonstrating both modules and crates:

```rust
mod my_utils {
    pub fn add(a: i32, b: i32) -> i32 {
        a + b
    }
}

fn main() {
    let result = my_utils::add(5, 7);
    println!("The result is: {}", result);
}
```

## 🎯 Hands-On Challenge

Create a Rust program that demonstrates the use of modules and crates. Your program should:

1. Create a module named `math_operations` that contains two public functions: `add` and `subtract`.
2. In the `main` function, call these functions and print their results.
3. Create a new library crate named `geometry` with a function that calculates the area of a rectangle.
4. Use your `geometry` crate in another binary crate to calculate and print the area.

Here’s a basic template to get you started:

```rust
// src/lib.rs of the geometry crate
pub fn rectangle_area(length: f64, width: f64) -> f64 {
    length * width
}

// src/main.rs of your binary crate
mod math_operations {
    pub fn add(a: i32, b: i32) -> i32 {
        a + b
    }

    pub fn subtract(a: i32, b: i32) -> i32 {
        a - b
    }
}

fn main() {
    let sum = math_operations::add(5, 3);
    let difference = math_operations::subtract(5, 3);

    println!("Sum: {}", sum);
    println!("Difference: {}", difference);

    let area = geometry::rectangle_area(10.0, 5.0);
    println!("Area of rectangle: {}", area);
}
```

✅ **Share your solution on GitHub and tag #30DaysOfRust on social media! Let the world see your progress! 🚀**

## 💻 Exercises - Day 12

### ✅ Exercise: Level 1

1. Create a module named `shapes` that contains a function `circle_area` to calculate the area of a circle given its radius.
2. In the `main` function, call `circle_area` and print the result.
3. Create a library crate named `unit_converter` with functions to convert units (e.g., meters to kilometers).

### ✅ Exercise: Level 2

1. Create a binary crate named `temperature_converter` that uses the `unit_converter` library crate to convert temperatures (Celsius to Fahrenheit).
2. Create a module named `statistics` within your binary crate, containing functions to calculate mean and median of a list of numbers.
3. Create a module named `math_operations` with functions for addition, subtraction, multiplication, and division.
4. Implement a nested module `trigonometry` inside `math_operations` that includes functions for sine and cosine.
5. Create a new crate that uses the `rand` crate to generate random numbers.

### 🎥 Helpful Video References

- [Rust Modules and Crates Tutorial](https://www.youtube.com/watch?v=5LdnfzFdWhE)
- [Understanding Cargo and Crates](https://www.youtube.com/watch?v=NeNx0ZgKrVg)

## 📝 Day 12 Summary

- In this lesson, you learned about modules and crates in Rust. You explored how to create and use modules for code organization, as well as how to create and manage crates for packaging your Rust code.
- Understanding these concepts will help you write cleaner, more modular code in your Rust projects.
- Keep up the great work, and see you on Day 13! 🎉

See you tomorrow for **Day 13** where we'll dive into **more advanced features**! 🚀

🌟 _Great job on completing Day 12! Keep practicing, and get ready for Day 13 where we will explore Modules and Crates in Rust!_

Thank you for joining **Day 12** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 11](../11_Traits/11_traits.md) | [Day 13 >>](../13_Testing/13_testing.md)

---
