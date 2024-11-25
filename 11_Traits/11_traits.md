<div align="center">
  <h1>🦀 30 Days Of Rust: Day 11 - Traits in Rust 🚀</h1>
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

[<< Day 10](../10_Generics/10_generics.md) | [Day 12 >>](../12_Modules%20and%20Crates/12_modules_and_crates.md)

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)

- [📘 Day 11 - Traits in Rust](#-day-11---traits-in-rust)
  - [👋 Welcome](#-welcome)
  - [🔍 Overview](#-overview)
  - [🛠 Environment Setup](#-environment-setup)
  - [📖 Understanding Traits](#-understanding-traits)
    - [📝 Defining Traits](#-defining-traits)
    - [🔧 Implementing Traits](#-implementing-traits)
    - [📚 Common Traits in Rust](#-common-traits-in-rust)
    - [🔗 Traits for Structs](#-traits-for-structs)
    - [⚙ Traits with Generics](#-traits-with-generics)
    - [🕹 Trait Bounds](#-trait-bounds)
  - [🎯 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 11](#-exercises---day-11)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [✅ Exercise: Level 2](#-exercise-level-2)
    - [🎥 Helpful Video References](#-helpful-video-references)
  - [📝 Day 11 Summary](#-day-11-summary)

---

# 📘 Day 11 - Traits in Rust

## 👋 Welcome

Welcome to **Day 11** of your Rust journey! 🎉 Today, we will explore **Traits** in Rust, which allow you to define shared behavior across multiple types. They play a crucial role in Rust programming by enabling polymorphism and code reuse.

Get ready to learn how to define, implement, and use traits effectively. 🚀

Feel free to join the [30 Days of Rust](https://discord.gg/dy4gAhng) community on Discord to interact with others, ask questions, and share your progress!

## 🔍 Overview

Traits in Rust are a way to define shared behavior, allowing you to specify a set of methods that various types can implement. We will cover:

- How to define and implement traits
- Using traits with structs
- Traits and generics
- Trait bounds and how they enhance flexibility

## 🛠 Environment Setup

Ensure that you have your Rust environment set up correctly from Day 1. If you haven’t installed Rust yet, please refer to the setup instructions from [Day 1](../README.md#-environment-setup).

## 📖 Understanding Traits

## 📝 Defining Traits

Traits are defined using the `trait` keyword. They act as interfaces for structs, specifying a set of methods that must be implemented.

```rust
trait Greet {
    fn greet(&self) -> String;
}
```

This `Greet` trait declares a method `greet` that any type implementing this trait must define.

## 🔧 Implementing Traits

To use a trait, you need to implement it for a specific type:

```rust
struct Person {
    name: String,
}

impl Greet for Person {
    fn greet(&self) -> String {
        format!("Hello, my name is {}", self.name)
    }
}
```

To implement a trait for a type, use the `impl` keyword followed by the trait name. Here’s a more detailed example:

### Example: Implementing a Trait for a Struct

```rust
trait Describe {
    fn description(&self) -> String;
}

struct Person {
    name: String,
    age: u32,
}

impl Describe for Person {
    fn description(&self) -> String {
        format!("{} is {} years old.", self.name, self.age)
    }
}

fn main() {
    let person = Person {
        name: String::from("Alice"),
        age: 30,
    };

    println!("{}", person.description()); // Outputs: Alice is 30 years old.
}
```

In this example, the `Describe` trait has a method `description`, and we implement it for the `Person` struct. The `description` method formats the information about the person.

## 📚 Common Traits in Rust

Rust provides several common traits that can be implemented, including:

- **`Clone`**: Allows for creating a copy of a value.
- **`Debug`**: Enables formatting a value for debugging.
- **`PartialEq`**: Allows for comparing two values for equality.
- **`Iterator`**: Provides functionality for iterating over collections.

### Example: Using Common Traits

```rust
#[derive(Debug, Clone)]
struct Item {
    name: String,
    value: i32,
}

fn main() {
    let item1 = Item {
        name: String::from("Rust Book"),
        value: 50,
    };

    let item2 = item1.clone(); // Cloning item1

    println!("{:?}", item1); // Outputs: Item { name: "Rust Book", value: 50 }
    println!("{:?}", item2); // Outputs: Item { name: "Rust Book", value: 50 }
}
```

In this example, we use the `Debug` and `Clone` traits by deriving them for the `Item` struct.

## 🔗 Traits for Structs

Traits can be implemented for structs, allowing them to share behavior:

```rust
fn main() {
    let person = Person {
        name: String::from("Alice"),
    };
    println!("{}", person.greet());
}
```

Output:

```
Hello, my name is Alice
```

## ⚙ Traits with Generics

Traits are often used with generics to make code more flexible:

```rust
struct Container<T> {
    value: T,
}

impl<T> Container<T> {
    fn new(value: T) -> Self {
        Container { value }
    }
}
```

## 🕹 Trait Bounds

Trait bounds restrict the types that can be used with generics, ensuring that the generic type implements specific traits:

```rust
fn print_greet<T: Greet>(item: T) {
    println!("{}", item.greet());
}
```

The function `print_greet` ensures that `T` implements the `Greet` trait.

## 🎯 Hands-On Challenge

Create a Rust program that:

1. **Defines a trait** named `Describe` with a method `describe` that returns a string.
2. **Implements the trait** for two different structs: `Car` and `Bike`.
3. **Uses a generic function** to print the description of any item that implements `Describe`.

Here’s a basic template to get you started:

```rust
trait Describe {
    fn describe(&self) -> String;
}

struct Car {
    brand: String,
}

impl Describe for Car {
    fn describe(&self) -> String {
        format!("This is a car from {}", self.brand)
    }
}

struct Bike {
    brand: String,
}

impl Describe for Bike {
    fn describe(&self) -> String {
        format!("This is a bike from {}", self.brand)
    }
}

fn main() {
    let car = Car { brand: String::from("Toyota") };
    let bike = Bike { brand: String::from("Yamaha") };

    println!("{}", car.describe());
    println!("{}", bike.describe());
}
```

✅ **Share your solution on GitHub and tag #30DaysOfRust on social media! Show the world your progress! 🚀**

## 💻 Exercises - Day 11

### ✅ Exercise: Level 1

1. Define a trait `Summarize` with a method `summarize` that returns a string.
2. Implement the `Summarize` trait for a `Book` struct. The summary should include the book’s title and author.
3. Implement the `Summarize` trait for an `Article` struct. The summary should include the article's title and publication date.
4. Create an instance of both `Book` and `Article`, and call the `summarize` method.

### ✅ Exercise: Level 2

1. Implement a trait `Area` that calculates the area for different shapes (e.g., `Rectangle` and `Circle`).
2. Create a function that accepts a generic type constrained by the `Area` trait and prints the area of the shape.
3. Define a struct `Dog` and a struct `Cat`. Implement a common `Speak` trait for both.
4. Create an array of `Speak` trait objects and loop over it to call the `speak` method on each object.
5. Create a trait `Move` with a method `move` and implement it for different types. Create a vector of trait objects and iterate over them to demonstrate dynamic dispatch.

### 🎥 Helpful Video References

- [Rust Traits Explained](https://www.youtube.com/watch?v=Lrayq0UW7nA)
- [Understanding Rust Trait Bounds](https://www.youtube.com/watch?v=w8lmMaKY3Hs)
- [Dynamic Dispatch and Traits](https://www.youtube.com/watch?v=3biW5NkNnrk)

## 📝 Day 11 Summary

- Today, we learned about **Traits** in Rust, which allow different types to share behavior.
- By defining and implementing traits, you can create clean and modular code.
- We explored how traits work with generics and how they enable dynamic behavior through trait objects.

See you tomorrow for **Day 12** where we'll dive into **more advanced features**! 🚀

🌟 _Great job on completing Day 11! Keep practicing, and get ready for Day 12 where we will explore Modules and Crates in Rust!_

Thank you for joining **Day 11** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 10](../10_Generics/10_generics.md) | [Day 12 >>](../12_Modules%20and%20Crates/12_modules_and_crates.md)

---
