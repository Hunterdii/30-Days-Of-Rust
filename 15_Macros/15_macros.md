<div align="center">
  <h1>🦀 30 Days Of Rust: Day 15 - Macros in Rust 🛠️</h1>
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

[<< Day 14](../14_Cargo%20and%20Package%20Management/14_cargo_and_package_management.md) | [Day 16 >>](../16_File%20Handling/16_file_handling.md)

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)

- [📘 Day 15 - Macros in Rust](#-day-15---macros-in-rust)
  - [👋 Welcome](#-welcome)
  - [🔍 Overview](#-overview)
  - [🛠 Environment Setup](#-environment-setup)
  - [🛠 Understanding Macros](#-understanding-macros)
    - [🧩 Macro Basics](#-macro-basics)
    - [⚙ Declarative Macros (`macro_rules!`)](#-declarative-macros-macro_rules)
    - [🛠 Creating a Simple Declarative Macro](#-creating-a-simple-declarative-macro)
    - [💻 Procedural Macros](#-procedural-macros)
    - [📋 Attribute Macros](#-attribute-macros)
    - [📐 Derive Macros](#-derive-macros)
    - [🔍 Function-like Macros](#-function-like-macros)
  - [🚀 Macro Use Cases](#-macro-use-cases)
  - [📝 When to Use Macros](#-when-to-use-macros)
  - [🔧 Best Practices for Macros](#-best-practices-for-macros)
  - [🎯 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 15](#-exercises---day-15)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [🚀 Exercise: Level 2](#-exercise-level-2)
  - [🎥 Helpful Video References](#-helpful-video-references)
  - [📝 Day 15 Summary](#-day-15-summary)

# 📘 Day 15 - Macros in Rust

## 👋 Welcome

Welcome to **Day 15** of the 30 Days of Rust challenge! 🎉 Today, we will explore the fascinating world of **macros** in Rust. Macros are a powerful feature that allows you to write code that generates other code. They are especially useful for reducing repetitive code and creating domain-specific languages (DSLs). 🛠️

Join the [30 Days of Rust](https://discord.gg/dy4gAhng) community on Discord for discussions, questions, and to share your learning journey! 🚀

## 🔍 Overview

Macros in Rust allow for metaprogramming, where you write code that can write other code. There are different types of macros, each serving different purposes:

- Declarative macros: The most common type, written using the `macro_rules!` syntax.
- Procedural macros: Allow more complex code generation and transformation.
- Function-like, attribute, and derive macros: Specialized procedural macros for specific use cases.

Today, we will cover:

- The basics of macros and how they differ from functions
- Writing and using declarative and procedural macros
- Different types of procedural macros: derive, attribute, and function-like
- When to use macros and best practices for writing them

By the end of today, you will have a clear understanding of macros in Rust and how to leverage them effectively!

## 🛠 Environment Setup

If you have already set up your Rust environment on **Day 1**, you’re good to go! Otherwise, check out the [Environment Setup](../README.md#-environment-setup) section for detailed instructions. Ensure you have **Cargo** installed by running:

```bash
$ cargo --version
```

If you see a version number, you’re all set! 🎉

## 🛠 Understanding Macros

Macros are a way to write code that writes other code (often called "metaprogramming"). They allow you to reduce boilerplate, create custom syntaxes, and generate repetitive code on-the-fly. Unlike functions, macros are expanded at compile-time, meaning they run before your code is compiled.

In Rust, macros can be a bit more complex than in other languages, but they provide exceptional power and flexibility. Macros expand at compile time, which means they can manipulate the code itself before it is compiled.

## 🧩 Macro Basics

Macros in Rust aren't functions. While functions are evaluated at runtime, macros work at compile-time. This gives them unique powers, such as the ability to generate code and avoid duplication.

Key differences between **functions** and **macros**:

- Functions take values as input; macros take code as input.
- Macros can work on syntax; functions cannot.
- Macros are expanded during the compilation phase, while functions are evaluated at runtime.

Let's look at how they work!

### <div align="center">_*or*_</div>

Rust macros are not the same as functions. While functions operate on values and execute at runtime, macros operate on code and expand at compile-time. This allows macros to generate code dynamically, based on patterns and rules.

**Why use macros?**

- **Reduce repetition**: Write once, use multiple times.
- **Implement domain-specific languages**: Create custom syntaxes for your needs.
- **Powerful code generation**: Automate tedious and repetitive coding tasks.

## ⚙ Declarative Macros (`macro_rules!`)

The most common type of macro is the declarative macro. These are written using `macro_rules!` and are used to define patterns that the Rust compiler matches and expands.

Here's an example of a simple macro:

```rust
macro_rules! say_hello {
    () => {
        println!("Hello, Rustaceans!");
    };
}

fn main() {
    say_hello!();
}
```

This macro replaces the `say_hello!()` with `println!("Hello, Rustaceans!");` at compile time. Simple but powerful! Let's explore more about the patterns:

- **Pattern matching**: Declarative macros rely on pattern matching, similar to how `match` works in Rust.
- **Repetitions**: Macros can handle repetitions (`*`, `+`, `?`) to create loops over repeated input.

Example with repetition:

```rust
macro_rules! repeat {
    ($x:expr; $count:expr) => {
        for _ in 0..$count {
            println!("{}", $x);
        }
    };
}

fn main() {
    repeat!("Rust is awesome!"; 3);
}
```

This macro prints `"Rust is awesome!"` three times by expanding the `repeat!` call into a loop.

### <div align="center">_*or*_</div>

Declarative macros, also known as **macros by example**, are defined using `macro_rules!`. They are the most common type of macro in Rust and are perfect for creating simple patterns.

## 🛠 Creating a Simple Declarative Macro

Here’s how you can define and use a simple macro:

```rust
macro_rules! say_hello {
    () => {
        println!("Hello, Rustaceans!");
    };
}

fn main() {
    say_hello!(); // Outputs: Hello, Rustaceans!
}
```

In this example, `say_hello!()` expands to `println!("Hello, Rustaceans!");`. Notice the exclamation mark (`!`) at the end of the macro name—this differentiates macros from regular functions.

## 💻 Procedural Macros

Procedural macros are more powerful and complex than declarative macros. They allow you to manipulate Rust's Abstract Syntax Tree (AST), giving you the ability to transform code at a deeper level.

There are three types of procedural macros:

1. **Derive macros**: Used to automatically implement traits for structs or enums.
2. **Attribute macros**: Apply attributes to functions, structs, or enums.
3. **Function-like macros**: Create custom code generation patterns similar to function calls.

## 📋 Attribute Macros

Attribute macros allow you to define custom attributes that can be applied to code items (e.g., structs, functions).

```rust
#[proc_macro_attribute]
pub fn my_attribute_macro(_attr: TokenStream, item: TokenStream) -> TokenStream {
    // Your code transformation logic here
}
```

## 📐 Derive Macros

Derive macros are used when you want to automatically generate code to implement traits for structs or enums. For example, to serialize or deserialize data, you might use the `#[derive(Serialize, Deserialize)]` attribute.

```rust
#[derive(Debug)]
struct Book {
    title: String,
    author: String,
}

fn main() {
    let book = Book { title: String::from("Rust Book"), author: String::from("John Doe") };
    println!("{:?}", book);
}
```
### <div align="center">_*or*_</div>

Custom derive macros allow you to automatically implement traits for your structs or enums. For example, you can derive serialization traits like this:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct MyStruct {
    name: String,
    age: u8,
}
```

Here, the `Serialize` and `Deserialize` traits are derived using procedural macros provided by the `serde` crate.


## 🔍 Function-like Macros

Function-like macros look like regular function calls but are more flexible. They can accept any valid Rust code as input and output new code.

```rust
macro_rules! create_function {
    ($func_name:ident) => {
        fn $func_name() {
            println!("Function {:?} called", stringify!($func_name));
        }
    };
}

create_function!(hello_rust);

fn main() {
    hello_rust();
}
```

### <div align="center">_*or*_</div>

Function-like procedural macros take arguments like regular functions, but they operate at the syntax level. You invoke them like functions but without parentheses.

Example:

```rust
my_macro!(some, input);
```

Function-like macros operate just like functions, but they accept tokens as input. They can be quite flexible and are typically used when custom syntax is needed for special cases.

```rust
macro_rules! calculate {
    ($a:expr, $b:expr) => {
        println!("The result is: {}", $a + $b);
    };
}

fn main() {
    calculate!(5, 10);
}
```

In this example, the macro `calculate!` takes two expressions and prints their sum. This is another instance of code generation at compile time!


## 🚀 Macro Use Cases

Macros are invaluable when you need to:

- **Eliminate boilerplate**: Write code that writes code!
- **Simplify repetitive tasks**: Macros are excellent for tasks that involve repetitive patterns, such as repetitive structures, function signatures, or trait implementations.
- **Custom derive**: Automatically implement traits for your types.

Common use cases:

- Implementing logging.
- Simplifying serialization and deserialization.
- Defining domain-specific languages (DSLs).
- Reducing the repetition in test setups.

## 📝 When to Use Macros

Macros are incredibly powerful but should be used judiciously. Consider using macros when:

- You have repetitive code patterns that need to be generated.
- You want to create domain-specific languages or custom syntaxes.
- You need to write generic code that operates over multiple types.

## 🔧 Best Practices for Macros

- **Keep it simple**: Write macros that are easy to read and understand.
- **Use functions if possible**: If a function can achieve the same result, prefer it over a macro.
- **Limit complexity**: Avoid overly complex macros that are difficult to debug.
- **Document your macros**: Explain how the macro works and provide examples.

## 🎯 Hands-On Challenge

1. **Create a simple `macro_rules!` macro** that takes input and generates repeated code.
2. **Experiment with function-like macros** and create one to simplify repeated calculations in a program.
3. **Use a procedural macro** from a crate like `serde` to automatically derive traits for a struct.

Here’s a simple macro for you to try:

```rust
macro_rules! my_macro {
    ($a:expr) => {
        println!("My macro says: {}", $a);
    };
}

fn main() {
    my_macro!("Rust is fun!");
}
```

### <div align="center">_*or*_</div>

1. Write a macro that simplifies a common task like printing a message with a timestamp.
2. Create a procedural macro that automatically implements a custom trait for your struct.

### <div align="center">_*or*_</div>

1. **Create a simple macro** that takes two numbers and prints their sum.
2. **Write a derive macro** to automatically implement a custom trait.
3. **Implement an attribute macro** that can transform a function's behavior.
4. **Experiment with procedural macros** to gain a deeper understanding.

Here’s an example to get you started:

```rust
macro_rules! add {
    ($a:expr, $b:expr) => {
        println!("{} + {} = {}", $a, $b, $a + $b);
    };
}

fn main() {
    add!(5, 7); // Outputs: 5 + 7 = 12
}
```

## 💻 Exercises - Day 15

### ✅ Exercise: Level 1

1. Create a basic macro to convert strings to uppercase.
2. Write a procedural macro to implement custom debugging information for a struct.
3. Write a simple `macro_rules!` macro that accepts a string and prints it in uppercase.
4. Implement a function-like macro to calculate the square of a number.

### 🚀 Exercise: Level 2

1. Implement a derive macro that can automatically generate a display implementation.
2. Experiment with attribute macros to create a simple logging mechanism for functions.
3. Create a procedural macro that derives a custom trait for printing data in JSON format.
4. Write a function-like macro that accepts two integers and prints their product.

## 🎥 Helpful Video References

- [Rust Macros Tutorial](https://youtube.com/watch?v=KsJHlqULpO4)
- [Advanced Rust - Procedural Macros](https://www.youtube.com/watch?v=9IbYBl48eTQ)


## 📝 Day 15 Summary

Today, we dove into **macros in Rust**. We learned about declarative and procedural macros, and explored how they can reduce code repetition and introduce powerful code generation capabilities. You also got hands-on practice with writing your own macros. 🎉 Continue experimenting and see where you can incorporate macros in your Rust projects!

Stay tuned for **Day 16**, where we will explore **File Handling** in Rust! 🚀

🌟 _Great job on completing Day 15! Keep practicing, and get ready for Day 16 where we will explore **File Handling** in Rust!_

Thank you for joining **Day 15** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 14](../14_Cargo%20and%20Package%20Management/14_cargo_and_package_management.md) | [Day 16 >>](../16_File%20Handling/16_file_handling.md)

---

