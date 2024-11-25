<div align="center">
  <h1>🦀 30 Days Of Rust: Day 13 - Testing in Rust 🚀</h1>
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

[<< Day 12](../12_Modules%20and%20Crates/12_modules_and_crates.md) | [Day 14 >>](../14_Cargo%20and%20Package%20Management/14_cargo_and_package_management.md)

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)

- [📘 Day 13 - Testing in Rust](#-day-13---testing-in-rust)
  - [👋 Welcome](#-welcome)
  - [🔍 Overview](#-overview)
  - [🛠 Environment Setup](#-environment-setup)
  - [📖 Writing Tests](#-writing-tests)
    - [🛠️ Getting Started](#️-getting-started)
    - [🧪 Unit Tests](#-unit-tests)
    - [⚠️ Handling Failures](#️-handling-failures)
    - [⚡ The `should_panic` Attribute](#-the-should_panic-attribute)
    - [📊 Integration Tests](#-integration-tests)
    - [📝 Documentation Tests](#-documentation-tests)
    - [⚙️ Concurrency in Testing](#️-concurrency-in-testing)
  - [🎯 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 13](#-exercises---day-13)
    - [✅ Exercise: Level 1](#-exercise-level-1)
  - [🎥 Helpful Video References](#-helpful-video-references)
  - [📝 Day 13 Summary](#-day-13-summary)

---

# 📘 Day 13 - Testing in Rust

## 👋 Welcome

Welcome to **Day 13** of your Rust journey! 🎉 Today, we’ll explore the essential topic of **testing** in Rust, a critical practice that helps ensure your code works as expected.

Testing is a fundamental part of software development, enabling you to catch bugs early, improve code quality, and maintain reliability. Let’s dive in and learn how to implement tests in Rust! 🚀

Feel free to join the [30 Days of Rust](https://discord.gg/dy4gAhng) community on Discord, where you can interact with others, ask questions, and share your progress!

## 🔍 Overview

In Rust, testing is built into the language, allowing you to write unit tests, integration tests, and documentation tests seamlessly. We will cover:

- How to write and run tests
- The difference between unit tests and integration tests
- How to test your documentation examples

## 🛠 Environment Setup

Ensure that you have your Rust environment set up correctly from Day 1. If you haven’t installed Rust yet, please refer to the setup instructions from [Day 1](../README.md#-environment-setup).

## 📖 Writing Tests


## 🛠️ Getting Started

To start writing tests in Rust, create a new project using Cargo:

```bash
$ cargo new adder
$ cd adder
```

Cargo will automatically generate a simple test when you make a new project.

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
    }
}
```
---

## 🧪 Unit Tests

Unit tests are designed to test small units of code, such as functions or methods, in isolation. In Rust, you typically write unit tests within the same file as the code they test. Here’s how to write a simple unit test:

```rust
fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
        assert_eq!(add(-1, 1), 0);
        assert_eq!(add(0, 0), 0);
    }
}
```

In this example:

- The `#[cfg(test)]` attribute indicates that the following module should only be compiled when running tests.
- The `#[test]` attribute marks a function as a test case.
- The `assert_eq!` macro checks if the expected value matches the actual value.

In Rust, tests are annotated with `#[test]`. Here's a basic unit test:

```rust
#[test]
fn it_works() {
    assert_eq!(4, add_two(2));
}
```

The `assert_eq!` macro ensures the function's output is as expected.

---

## ⚠️ Handling Failures

By default, any test that panics fails. Let's force a failure to see how Rust handles it:

```rust
#[test]
fn it_fails() {
    assert!(false); // This will panic!
}
```

Running the test will show a failure result:

```bash
$ cargo test
```

---

## ⚡ The `should_panic` Attribute

You can write tests that expect a panic using the `#[should_panic]` attribute:

```rust
#[test]
#[should_panic]
fn it_panics() {
    assert_eq!("Hello", "world");
}
```

You can make this even safer by specifying the expected panic message:

```rust
#[test]
#[should_panic(expected = "assertion failed")]
fn it_panics_with_message() {
    assert_eq!("Hello", "world");
}
```

---

## 📊 Integration Tests

Integration tests verify that different parts of your application work together. They are typically placed in the `tests` directory. Here’s how to create an integration test:

1. Create a `tests` directory in your project root if it doesn’t exist.
2. Inside the `tests` directory, create a new Rust file (e.g., `integration_test.rs`).

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn test_integration() {
        let result = super::add(2, 3); // Import the function to test
        assert_eq!(result, 5);
    }
}
```

Rust's integration tests are written in the `tests/` directory. Each file in this directory is treated as a separate crate.

Example:

```rust
extern crate adder;

#[test]
fn it_works() {
    assert_eq!(4, adder::add_two(2));
}
```

Run your integration tests with `cargo test`.

---



## 📝 Documentation Tests

Documentation tests check that the examples in your code comments work as expected. To write documentation tests, include example code in your comments using the following format:

```rust
/// Adds two numbers.
///
/// # Examples
///
/// ```
/// let result = add(2, 3);
/// assert_eq!(result, 5);
/// ```
fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

Rust can automatically run examples in your documentation as tests! Here's an example with a simple function:

```rust
/// This function adds two to its argument.
///
/// # Examples
///
/// ```
/// assert_eq!(4, adder::add_two(2));
/// ```
pub fn add_two(a: i32) -> i32 {
    a + 2
}
```

When you run `cargo test`, these examples will be executed as tests.

---

## ⚙️ Concurrency in Testing

Tests in Rust are run concurrently by default. This means you should ensure your tests do not depend on each other or on shared state, including the environment.

To disable concurrency:

```bash
$ RUST_TEST_THREADS=1 cargo test
```
---

When you run your tests, Rust will verify that the code in the documentation examples compiles and behaves as expected.

## 🎯 Hands-On Challenge

Create a Rust program that implements functions with unit tests and integration tests. Your program should:

1. **Implement a function** that subtracts two numbers.
2. **Write unit tests** for the subtraction function.
3. **Create an integration test** in a separate file to test the subtraction function.
4. **Include a documentation test** in the function’s comments.

Here’s a basic template to get you started:

```rust
/// Subtracts two numbers.
///
/// # Examples
///
/// ```
/// let result = subtract(5, 2);
/// assert_eq!(result, 3);
/// ```
fn subtract(a: i32, b: i32) -> i32 {
    a - b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_subtract() {
        assert_eq!(subtract(5, 2), 3);
        assert_eq!(subtract(10, 5), 5);
    }
}
```

✅ **Share your solution on GitHub and tag #30DaysOfRust on social media! Let the world see your progress! 🚀**

## 💻 Exercises - Day 13

### ✅ Exercise: Level 1

1. Implement a function named `multiply` that multiplies two integers.
2. Write unit tests for the `multiply` function to cover various cases.
3. Create an integration test in the `tests` directory to test the `multiply` function.
4. Include a documentation test with examples in the function’s comments.

## 🎥 Helpful Video References

- [Rust Testing Tutorial](https://www.youtube.com/watch?v=UyJ1mEqKMvE)
- [Writing Tests in Rust](https://www.youtube.com/watch?v=0G_5uUe_NXk)

## 📝 Day 13 Summary

Today, we learned how to write tests in Rust, covering unit tests, integration tests, and documentation tests. Testing is crucial for ensuring that our code behaves as expected, and Rust provides excellent support for it. Keep practicing by writing tests for your functions to enhance your programming skills!

See you tomorrow for **Day 14** where we'll dive into **more advanced features**! 🚀

🌟 _Great job on completing Day 13! Keep practicing, and get ready for Day 14 where we will explore Cargo and Package Management in Rust!_

Thank you for joining **Day 13** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 12](../12_Modules%20and%20Crates/12_modules_and_crates.md) | [Day 14 >>](../14_Cargo%20and%20Package%20Management/14_cargo_and_package_management.md)

---
