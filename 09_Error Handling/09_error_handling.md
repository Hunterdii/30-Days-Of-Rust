<div align="center">
  <h1>🦀 30 Days Of Rust: Day 9 - Error Handling 🚀</h1>
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

[<< Day 8](../08_Collections/08_collections.md) | [Day 10 >>](../10_Generics/10_generics.md)

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)


- [📘 Day 9 - Error Handling](#-day-9---error-handling)
  - [👋 Welcome](#-welcome)
  - [🔍 Overview](#-overview)
  - [🛠 Environment Setup](#-environment-setup)
  - [📖 Understanding Error Handling](#-understanding-error-handling)
    - [💥 Panic](#-panic)
    - [🛑 Abort & Unwind](#-abort--unwind)
    - [⚠ Option & Unwrap](#-option--unwrap)
    - [🛠 Result Type](#-result-type)
    - [🔧 Handling Multiple Error Types](#-handling-multiple-error-types)
    - [🔄 Iterating Over Results](#-iterating-over-results)
    - [🛑 Result Type](#-result-type)
    - [🔧 Custom Error Types](#-custom-error-types)
  - [🎯 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 9](#-exercises---day-9)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [✅ Exercise: Level 2](#-exercise-level-2)
    - [🎥 Helpful Video References](#-helpful-video-references)
  - [📝 Day 9 Summary](#-day-9-summary)


# 📘 Day 9 - Error Handling

## 👋 Welcome

Welcome to **Day 9** of your Rust journey! 🎉 Today, we will explore **Error Handling**, a critical aspect of building reliable and resilient applications in Rust. Understanding how to manage errors effectively will enable you to write code that can handle unexpected situations gracefully. Let’s dive into the key concepts that Rust provides for error management! 🚀

**Congratulations!** 🎉 You've taken the first step in your journey to master the _30 Days of Rust_ programming challenge. In this challenge, you will learn the fundamentals of Rust and how to harness its power to write efficient, fast, and safe code. By the end of this journey, you'll have gained a solid understanding of Rust's core concepts and best practices, helping you become a confident Rustacean. 🦀


Feel free to join the [30 Days of Rust](https://discord.gg/dy4gAhng) community on Discord, where you can interact with others, ask questions, and share your progress!


## 🔍 Overview

In Rust, error handling is integral to writing robust code. Rust emphasizes the importance of handling errors explicitly through its type system. This day’s lesson covers:

- The `Result` type, which is used for functions that can return errors.
- The `Option` type for values that might be absent.
- Understanding panic situations and their implications.
- Creating and using custom error types for better error management.

## 🛠 Environment Setup

Ensure that you have your Rust environment set up correctly from Day 1. If you haven’t installed Rust yet, please refer to the setup instructions from [Day 1](../README.md#-environment-setup).

## 📖 Understanding Error Handling


## 💥 Panic

Panic is a mechanism Rust uses to handle unrecoverable errors. When a panic occurs, the program stops executing, and an error message is printed to the console. Panics are generally avoided in production code as they indicate critical failures.

#### Example:

```rust
fn main() {
    let v = vec![1, 2, 3];

    // This will panic because there is no element at index 99
    println!("Value at index 99: {}", v[99]);
}
```

In this case, trying to access an invalid index results in a panic, terminating the program.

## 🛑 Abort & Unwind

When a panic occurs, Rust allows two different behaviors:

1. **Unwinding:** The stack is unwound, and destructors for all in-scope variables are called. This is the default.
2. **Aborting:** The process terminates immediately without unwinding. This can be more efficient but doesn’t clean up. You can enable this behavior with `panic = "abort"` in your Cargo.toml:

```toml
[profile.release]
panic = "abort"
```

## ⚠ Option & Unwrap

The `Option` type is used for values that can be either present or absent. It has two variants:

- `Some(T)` for a value of type `T`.
- `None` to indicate the absence of a value.

Rust provides methods like `.unwrap()` to quickly extract the value from an `Option`, but it will panic if the `Option` is `None`. Use `.unwrap_or()` or `.unwrap_or_else()` for safer alternatives.

#### Example:

```rust
fn get_value(index: usize) -> Option<i32> {
    let values = vec![10, 20, 30];
    values.get(index).copied() // Return Some(value) or None
}

fn main() {
    // Safe usage with `unwrap_or`
    let value = get_value(5).unwrap_or(0); // Fallback value if index is out of bounds
    println!("Value: {}", value);
}
```

The `Option` type is used for values that can be either present or absent. It has two variants:

- `Some(T)` for a value of type `T`.
- `None` to indicate the absence of a value.

#### Example:

This function retrieves a value from a vector by its index, returning an `Option` type:

```rust
fn get_value(index: usize) -> Option<i32> {
    let values = vec![10, 20, 30];
    values.get(index).copied() // Return Some(value) or None
}

fn main() {
    match get_value(1) {
        Some(value) => println!("Value: {}", value),
        None => println!("No value found at that index."),
    }
}
```

In this example:
- We safely attempt to access an element in the vector using `get`.
- If the index is valid, we return `Some(value)`, otherwise, we return `None`.


## 🛠 Result Type

The `Result` type allows you to handle recoverable errors. It is an enum with two variants:

- `Ok(T)` for successful outcomes.
- `Err(E)` for errors.

The `?` operator simplifies error handling by propagating errors automatically.

#### Example:

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_file(filename: &str) -> Result<String, io::Error> {
    let mut file = File::open(filename)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    Ok(contents)
}

fn main() {
    match read_file("hello.txt") {
        Ok(contents) => println!("File contents:\n{}", contents),
        Err(e) => eprintln!("Error reading file: {}", e),
    }
}
```

## 🔧 Handling Multiple Error Types

When a function might return different types of errors, Rust allows you to create unified error handling using the `Box<dyn Error>` trait or a custom enum.

#### Example:

```rust
use std::fmt;
use std::fs::File;
use std::io::{self, Read};

#[derive(Debug)]
enum MyError {
    Io(io::Error),
    Parse(std::num::ParseIntError),
}

impl fmt::Display for MyError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            MyError::Io(e) => write!(f, "I/O error: {}", e),
            MyError::Parse(e) => write!(f, "Parse error: {}", e),
        }
    }
}

fn read_file(filename: &str) -> Result<String, MyError> {
    let mut file = File::open(filename).map_err(MyError::Io)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents).map_err(MyError::Io)?;
    Ok(contents)
}
```

## 🔄 Iterating Over Results

Rust allows you to work with collections of `Result`s by using methods like `.collect()`. This enables you to handle multiple possible errors efficiently.

#### Example:

```rust
fn parse_numbers(input: Vec<&str>) -> Vec<Result<i32, std::num::ParseIntError>> {
    input.iter().map(|s| s.parse::<i32>()).collect()
}

fn main() {
    let inputs = vec!["42", "93", "hello"];
    let results: Vec<_> = parse_numbers(inputs);

    for result in results {
        match result {
            Ok(num) => println!("Parsed number: {}", num),
            Err(e) => eprintln!("Error parsing input: {}", e),
        }
    }
}
```

## 🛑 Result Type

The `Result` type is a powerful feature in Rust that allows you to handle recoverable errors. It is an enum with two variants:

- `Ok(T)` for successful outcomes, where `T` is the type of the value returned.
- `Err(E)` for errors, where `E` is the type of the error.

#### Example:

Here’s a function that reads a file and returns its contents or an error if it fails:

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_file(filename: &str) -> Result<String, io::Error> {
    let mut file = File::open(filename)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    Ok(contents)
}

fn main() {
    match read_file("hello.txt") {
        Ok(contents) => println!("File contents:\n{}", contents),
        Err(e) => eprintln!("Error reading file: {}", e), // Using eprintln! for error output
    }
}
```

In this example:
- We attempt to open a file using `File::open`.
- If the file is opened successfully, we read its contents into a string.
- If any step fails, the error is returned automatically due to the `?` operator.


## 🔧 Custom Error Types

Creating custom error types allows you to handle specific scenarios descriptively.

#### Example:

```rust
use std::fmt;

#[derive(Debug)]
enum MyError {
    NotFound,
    InvalidInput,
}

impl fmt::Display for MyError {
    fn fmt(&self, f: &

mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            MyError::NotFound => write!(f, "Resource not found"),
            MyError::InvalidInput => write!(f, "Invalid input provided"),
        }
    }
}

fn perform_action() -> Result<(), MyError> {
    Err(MyError::InvalidInput)
}

fn main() {
    match perform_action() {
        Ok(_) => println!("Action performed successfully!"),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```


In this example:
- We define a custom error type `MyError` with different error variants.
- The `my_function` returns a `Result`, allowing users to handle specific error cases gracefully.

## 🎯 Hands-On Challenge

Now it’s time for you to apply what you've learned! Create a Rust program that demonstrates error handling in various scenarios. Implement the following functionalities:

1. Write a function that reads a file and returns its contents or an error if it fails.
2. Implement a function that processes user input and returns a custom error for invalid input.
3. Use `Option` to return values from a function that might not always have a result.

**Template:**

```rust
use std::fs::File;
use std::io::{self, Read};

// Function to read a file
fn read_file(filename: &str) -> Result<String, io::Error> {
    let mut file = File::open(filename)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    Ok(contents)
}

// Additional functions for processing input and handling options

fn main() {
    // Call your functions and handle errors
}
```

✅ **Share your solution on GitHub and tag #30DaysOfRust on social media! Let the world see your progress! 🚀**

## 💻 Exercises - Day 9

### ✅ Exercise: Level 1

1. Write a function that returns the result of dividing two numbers. Handle division by zero gracefully using the `Result` type.
2. Implement a function that retrieves an element from a vector by index, returning an `Option` type, and provide a fallback value if the index is out of bounds.
3. Create a simple command-line program that accepts user input and returns an error message if the input is invalid.

### ✅ Exercise: Level 2

1. Extend the division function to accept floating-point numbers, returning a custom error for invalid inputs.
2. Create a custom error type for a library that manages books. Include variants for not found and invalid format errors. Implement functions that demonstrate these errors in action.
3. Write tests for your error handling functions, ensuring they return the correct results and errors.
4. Write a function that returns the result of dividing two numbers. Handle division by zero gracefully.
5. Implement a function that retrieves an element from a vector by index, returning an `Option` type.
6. Create a program that reads an integer from user input and prints it. Handle invalid input gracefully.

### 🎥 Helpful Video References

- [Rust Error Handling Basics](https://www.youtube.com/watch?v=wM6o70NAWUI)
- [Understanding Result and Option in Rust](https://www.youtube.com/watch?v=lvhg19DmtV8)
- [Custom Error Types in Rust](https://www.youtube.com/watch?v=f9hEjMUuNjw)

## 📝 Day 9 Summary

- We learned how to handle errors in Rust using the **Result** and **Option** types.
- We discussed panic situations and how to manage them.
- Explored creating custom error types for better error management.

🌟 _Great job on completing Day 9! Keep practicing, and get ready for Day 10 where we will explore more advanced topics (Generics) in Rust!_

Thank you for joining **Day 9** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to ⭐ star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 8](../08_Collections/08_collections.md) | [Day 10 >>](../10_Generics/10_generics.md)

---
