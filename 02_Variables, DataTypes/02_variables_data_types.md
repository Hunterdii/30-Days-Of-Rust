<div align="center">
  <h1>🦀 30 Days Of Rust: Day 2 - Variables and Data Types 🚀</h1>
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

[<< Day 1](../README.md) | [Day 3 >>](../03_Control%20Flow/03_control_flow.md)

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)

- [📘 Day 2 - Variables and Data Types](#-day-2---variables-and-data-types)
  - [👋 Welcome](#-welcome)
  - [🔍 Overview](#-overview)
  - [🛠 Environment Setup](#-environment-setup)
  - [📖 Variables in Rust](#-variables-in-rust)
    - [📦 Declare a Variable](#-declare-a-variable)
  - [🔄 Variables and Mutability](#-variables-and-mutability)
    - [📦 Variable Binding](#-variable-binding)
    - [🔒 Mutable vs Immutable Variables](#-mutable-vs-immutable-variables)
  - [📚 Data Types](#-data-types)
    - [🔢 Numeric Type](#-numeric-types)
    - [💡 Boolean Type](#-boolean-type)
    - [🔤 Character Type](#-character-type)
    - [📝 String Type](#-string-type)
    - [🎯 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 2](#-exercises---day-2)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [✅ Exercise: Level 2](#-exercise-level-2)
    - [🎥 Helpful Video References](#-helpful-video-references)
  - [📝 Day 2 Summary](#-day-2-summary)

---

# 📘 Day 2 - Variables and Data Types

## 👋 Welcome

Welcome to **Day 2** of your Rust journey! 🎉 Today, we’ll dive into **variables** and **data types** in Rust, which are fundamental concepts that will help you write efficient and safe code.

In Rust, understanding how to declare and use variables, along with knowing the different data types, is essential for building robust applications. Let's get started! 🚀

Feel free to join the [30 Days of Rust](https://discord.gg/dy4gAhng) community on Discord, where you can interact with others, ask questions, and share your progress!

## 🔍 Overview

In Rust, variables are used to store data, and understanding data types is crucial for effective programming. We will cover:

- How to declare and use variables
- The difference between mutable and immutable variables
- Various data types available in Rust, including scalar and compound types

## 🛠 Environment Setup

Ensure that you have your Rust environment set up correctly from Day 1. If you haven’t installed Rust yet, please refer to the setup instructions from [Day 1](../README.md#-environment-setup).

## 📖 Variables in Rust

### 📦 Declare a Variable

To create a variable in Rust, you utilize the `let` keyword. This allows you to assign a value to the variable, making it accessible for use in your program.

Here’s how it works:

```rust
fn main() {
    let repository_nickname = "30-Days-Of-Rust";    // string type
    let rating_float = 4.7;                         // float type
    let is_growing_boolean = true;                  // boolean type
    let icon_char = '♥';                            // Unicode character type

    println!("Repository name is: {}", repository_nickname);
    println!("Repository rating on 5 is: {}", rating_float);
    println!("Repository is growing: {}", is_growing_boolean);
    println!("Repository icon is: {}", icon_char);
}
```

In this example, Rust infers the data type of each variable based on the assigned value. For instance, `repository_nickname` is recognized as a string, `rating_float` as a float, etc.

The `println!` macro used here takes two arguments:

1. A unique syntax `{}` which acts as a placeholder.
2. The name of the variable or constant to replace the placeholder with its value.

When this code runs, the output will be:

```
Repository name is: 30-Days-Of-Rust
Repository rating on 5 is: 4.7
Repository is growing: true
Repository icon is: ♥
```

## 🔄 Variables and Mutability

In Rust, a variable is a binding to a value. By default, variables are **immutable**, meaning you cannot change their value once they are set. However, you can make them **mutable** if needed.

## 📦 Variable Binding

In Rust, you create a variable using the `let` keyword. Here's an example:

```rust
let x = 5; // Immutable variable
```

### 🔒 Mutable vs Immutable Variables

By default, variables are immutable in Rust. If you want to create a mutable variable, use the `mut` keyword:

```rust
let mut y = 10; // Mutable variable
y = 15; // Now this is valid
```

**Example:1**

```rust
fn main() {
    let mut mutable_variable = 10;
    println!("Before: {}", mutable_variable);
    mutable_variable += 5;
    println!("After: {}", mutable_variable);
}
```

Output:

```
Before: 10
After: 15
```

This shows that we can modify the value of `mutable_variable` after its initial declaration.

**Example:2**

```rust
fn main() {
    let x = 5; // Immutable
    println!("Value of x: {}", x);

    let mut y = 10; // Mutable
    y = 20;
    println!("Updated value of y: {}", y);
}
```

**Example:3**

You declare a variable using the `let` keyword:

```rust
let x = 5; // Immutable variable
```

To make a variable mutable, use the `mut` keyword:

```rust
let mut y = 10; // Mutable variable
y += 5; // Now y is 15
```

## 📚 Data Types

Rust has several built-in data types, including:

- **Scalar types**: represent a single value (e.g., integers, floating-point numbers, booleans, characters).
- **Compound types**: can group multiple values (e.g., tuples, arrays).

Rust is a statically typed language, which means data types are known at compile time. Here are some of the most common data types:

1. **Integer**: `i8`, `u8`, `i16`, `u16`, `i32`, `u32`, `i64`, `u64`, `isize`, `usize`
2. **Float**: `f32`, `f64`
3. **Boolean**: `true` or `false`
4. **Character**: `char` (supports Unicode)
5. **String**: `String`, `&str`

**Example:1**

```rust
let integer: i32 = 42;               // integer
let float: f64 = 3.14;               // floating-point
let boolean: bool = true;            // boolean
let character: char = 'R';           // character
let tuple: (i32, f64) = (10, 20.5);  // tuple
let array: [i32; 3] = [1, 2, 3];     // array
```

**Example:2**

```rust
fn main() {
    let integer: i32 = 42;
    let float: f64 = 3.14;
    let is_active: bool = true;
    let letter: char = 'R';
    let name: &str = "Rust";

    println!("{} {} {} {} {}", integer, float, is_active, letter, name);
}
```

Rust has a strong static type system. This means that the data type of every variable must be known at compile time. Here are the most common data types in Rust:

## 🔢 Numeric Types

Rust provides several numeric types, including:

- **Integer Types**: `i32`, `u32`, `i64`, etc.
- **Floating-Point Types**: `f32` and `f64`.

Example of using integer and floating-point types:

### 🌈 Integer Type

Integers are whole numbers, and Rust supports various integer types:

```rust
let a: i32 = 42; // 32-bit signed integer
let b: u32 = 10; // 32-bit unsigned integer
```

### 🔢 Floating Point Type

Floating point numbers represent decimal values:

```rust
let c: f32 = 3.14; // 32-bit floating point
let d: f64 = 2.718; // 64-bit floating point
```

### 💡 Boolean Type

The boolean type is represented as `bool`, which can hold either `true` or `false`.

```rust
let is_rust_fun: bool = true;
```

### 🔤 Character Type

The character type is represented as `char`, which holds a single character. It is defined with single quotes.

```rust
let letter: char = 'R';
```

### 📝 String Type

Rust has two types of strings:

1. **String**: A mutable string type.
2. **&str**: A string slice, which is immutable.

Example:

```rust
let mut my_string: String = String::from("Hello, Rust!");
let slice: &str = "Hello, Rust!";
```

### 🔗 Compound Types

Compound types can group multiple values together.

#### 📜 Tuples

Tuples are used to group a fixed number of values of different types:

```rust
let tuple: (i32, f64, char) = (42, 3.14, 'R');
```

#### 📦 Arrays

Arrays hold multiple values of the same type:

```rust
let array: [i32; 3] = [1, 2, 3]; // An array of three integers
```

### 🎯 Hands-On Challenge

Create a Rust program that uses variables and demonstrates different data types. Your program should:

1. **Declare and print** a variable holding your name.
2. **Create a mutable integer variable** representing your current age and update it by adding one.
3. **Use a floating-point variable** to store your favorite number and print it.
4. **Include a boolean variable** that indicates whether you are learning Rust (set it to `true`).
5. **Use a character variable** to store the first letter of your name.

Here's a basic template to get you started:

```rust
fn main() {
    let name = "Your Name"; // String type
    let mut age = 25; // Mutable integer
    age += 1; // Updating age
    let favorite_number = 3.14; // Float type
    let is_learning_rust = true; // Boolean type
    let initial = 'Y'; // Character type

    println!("Name: {}", name);
    println!("Updated Age: {}", age);
    println!("Favorite Number: {}", favorite_number);
    println!("Learning Rust: {}", is_learning_rust);
    println!("Initial: {}", initial);
}
```

✅ **Share your solution on GitHub and tag #30DaysOfRust on social media! Let the world see your progress! 🚀**

## 💻 Exercises - Day 2

### ✅ Exercise: Level 1

1. Declare a variable named `my_age` and set it to your age.
2. Print the value of `my_age` to the console.
3. Create a mutable variable named `my_height` and assign it your height in centimeters. Update it to a new height.
4. Declare a variable `my_name` and assign it your name as a string. Print it to the console.
5. Create a variable `is_student` and set it to `true` if you are a student, or `false` otherwise. Print the value.
6. Create a variable `birth_year` and calculate your birth year by subtracting your age from the current year (you can use a hardcoded current year, e.g., `2024`). Print the value.

### ✅ Exercise: Level 2

1. Create variables for each numeric type (integer and float) and print their values:
   - An integer variable `my_integer` set to any integer value.
   - A floating-point variable `my_float` set to any float value.
2. Declare a boolean variable `is_learning_rust` and set it to `true`. Print the value.
3. Create a character variable `favorite_letter` and assign it your favorite letter. Print it.
4. Create an array of integers called `my_scores` that holds your last five test scores. Print the entire array.
5. Create a string variable `hobby` and assign it one of your hobbies. Print it, and then concatenate it with another string to create a sentence (e.g., "I enjoy [hobby]!"). Print the complete sentence.

## 🎥 Helpful Video References

- [Rust Variables and Data Types](https://www.youtube.com/watch?v=MJrBLTHJPCo)
- [Understanding Rust: Scalars vs. Compound Types](https://www.youtube.com/watch?v=qtBJm328VC4)

## 📝 Day 2 Summary

- We explored **variables** in Rust, understanding the difference between immutable and mutable variables.
- We covered the various **data types** available in Rust, including numeric types, boolean, character, and string.
- We completed exercises to solidify our understanding of variables and data types.

🌟 _Great job on completing Day 2! Keep practicing, and get ready for Day 3 where we will explore Control Flow in Rust!_

Thank you for joining **Day 2** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 1](../README.md) | [Day 3 >>](../03_Control%20Flow/03_control_flow.md)

---

