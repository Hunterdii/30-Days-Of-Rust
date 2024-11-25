<div align="center">
  <h1>🦀 30 Days Of Rust: Day 7 - Rust Enums 🚀</h1>
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

[<< Day 6](../06_Structs/06_structs.md) | [Day 8 >>](../08_Collections/08_collections.md)

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)

- [📘 Day 7 - Rust Enums](#-day-7---rust-enums)
  - [👋 Welcome](#-welcome)
  - [🔍 Overview](#-overview)
  - [🛠 Environment Setup](#-environment-setup)
  - [📖 Understanding Enums](#-understanding-enums)
    - [📦 Declaring Enums](#-declaring-enums)
    - [🔄 Using Enums with `match`](#-using-enums-with-match)
    - [📚 Methods on Enums](#-methods-on-enums)
    - [🔗 Enums with Data](#-enums-with-data)
  - [🎯 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 7](#-exercises---day-7)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [✅ Exercise: Level 2](#-exercise-level-2)
    - [🎥 Helpful Video References](#-helpful-video-references)
  - [📝 Day 7 Summary](#-day-7-summary)

---

# 📘 Day 7 - Rust Enums

## 👋 Welcome

Welcome to **Day 7** of your Rust journey! 🎉 Today, we’ll explore **Enums** in Rust, a powerful way to define types that can hold different but related kinds of data. Enums help in creating more readable and maintainable code. Let's get started! 🚀

**Congratulations!** 🎉 You've taken the first step in your journey to master the _30 Days of Rust_ programming challenge. In this challenge, you will learn the fundamentals of Rust and how to harness its power to write efficient, fast, and safe code. By the end of this journey, you'll have gained a solid understanding of Rust's core concepts and best practices, helping you become a confident Rustacean. 🦀


Feel free to join the [30 Days of Rust](https://discord.gg/dy4gAhng) community on Discord, where you can interact with others, ask questions, and share your progress!


## 🔍 Overview

In Rust, enums allow you to define a type that can be one of several variants. We'll cover:

- How to declare and use enums.
- Using enums with `match` and `if let`.
- Defining methods on enums.
- Creating enums that carry data.

## 🛠 Environment Setup

Ensure that you have your Rust environment set up correctly from Day 1. If you haven’t installed Rust yet, please refer to the setup instructions from [Day 1](../README.md#-environment-setup).

## 📖 Understanding Enums

## 📦 Declaring Enums

Enums in Rust are declared using the `enum` keyword, and they allow us to define a type that can be one of a few different variants.

**Example:**

```rust
enum Direction {
    North,
    South,
    East,
    West,
}

fn main() {
    let move_direction = Direction::North;
    match move_direction {
        Direction::North => println!("Heading North!"),
        Direction::South => println!("Heading South!"),
        Direction::East => println!("Heading East!"),
        Direction::West => println!("Heading West!"),
    }
}
```

## 🔄 Using Enums with `match`

The `match` statement is a powerful control flow construct that helps to match different enum variants.

**Example:**

```rust
enum TrafficLight {
    Red,
    Yellow,
    Green,
}

fn action(light: TrafficLight) {
    match light {
        TrafficLight::Red => println!("Stop!"),
        TrafficLight::Yellow => println!("Get Ready!"),
        TrafficLight::Green => println!("Go!"),
    }
}

fn main() {
    let current_light = TrafficLight::Red;
    action(current_light);
}
```

## 📚 Methods on Enums

Enums can also have methods defined on them, similar to structs.

**Example:**

```rust
enum Vehicle {
    Car(String),
    Bike(String),
}

impl Vehicle {
    fn drive(&self) {
        match self {
            Vehicle::Car(name) => println!("Driving a car: {}", name),
            Vehicle::Bike(name) => println!("Riding a bike: {}", name),
        }
    }
}

fn main() {
    let my_car = Vehicle::Car(String::from("Sedan"));
    let my_bike = Vehicle::Bike(String::from("Mountain Bike"));

    my_car.drive();
    my_bike.drive();
}
```

## 🔗 Enums with Data

Enums can also hold data, which makes them very versatile.

**Example:**

```rust
enum IpAddr {
    V4(String),
    V6(String),
}

fn main() {
    let home = IpAddr::V4(String::from("127.0.0.1"));
    let loopback = IpAddr::V6(String::from("::1"));

    println!("Home address: {:?}", home);
    println!("Loopback address: {:?}", loopback);
}
```

## 🎯 Hands-On Challenge

Create a Rust program that defines an enum representing a payment method: `CreditCard`, `DebitCard`, `Cash`, and `PayPal`. Write a function to print the payment method used.

**Template:**

```rust
enum PaymentMethod {
    CreditCard(String),
    DebitCard(String),
    Cash,
    PayPal,
}

fn print_payment_method(method: PaymentMethod) {
    match method {
        PaymentMethod::CreditCard(card_number) => println!("Paid with Credit Card: {}", card_number),
        PaymentMethod::DebitCard(card_number) => println!("Paid with Debit Card: {}", card_number),
        PaymentMethod::Cash => println!("Paid with Cash"),
        PaymentMethod::PayPal => println!("Paid with PayPal"),
    }
}

fn main() {
    let payment = PaymentMethod::CreditCard(String::from("1234-5678-9012-3456"));
    print_payment_method(payment);
}
```

✅ **Share your solution on GitHub and tag #30DaysOfRust on social media! Let the world see your progress! 🚀**

## 💻 Exercises - Day 7

### ✅ Exercise: Level 1

1. Create an enum called `Weather` with variants: `Sunny`, `Rainy`, `Cloudy`, and `Windy`.
2. Use a `match` statement to print out a message for each weather condition.
3. Define an enum `Device` that can hold values `Laptop`, `Tablet`, and `Phone`, each containing a string (e.g., model name). Write a method to display the device information.
4. Create an enum called `TrafficLight` with variants `Red`, `Yellow`, and `Green`.
5. Implement a function `get_light_duration` that returns the duration for each light:
   - Red: 30 seconds
   - Yellow: 5 seconds
   - Green: 20 seconds
6. Use a match statement to print the duration of each traffic light.

### ✅ Exercise: Level 2

1. Write an enum `FileFormat` with variants `PDF`, `Word`, and `Excel`, each variant containing a file size (integer). Define a method on the enum to print the file format and size.
2. Create an enum `Status` with variants: `Active`, `Inactive`, and `Suspended`. Use the `if let` control flow to handle the enum.
3. Define a program that mimics an online order with enum `OrderStatus` containing `Pending`, `Shipped`, and `Delivered`. Write a function that takes `OrderStatus` as input and prints out the current order status.
4. Create an enum called `Shape` with variants `Circle(f64)` for the radius, `Rectangle(f64, f64)` for width and height, and `Triangle(f64, f64, f64)` for the lengths of the three sides.
5. Implement a function `calculate_area` that takes a `Shape` and returns the area of the shape:
   - For a circle, use the formula πr².
   - For a rectangle, use width * height.
   - For a triangle, use Heron's formula.
6. Test your function with different shapes and print the areas.


## 🎥 Helpful Video References

- [Understanding Enums in Rust](https://www.youtube.com/watch?v=DSZqIJhkNCM)
- [Mastering `match` in Rust](https://www.youtube.com/watch?v=pf8eQwWkTaY)

## 📝 Day 7 Summary

- We learned how to declare and use **enums** in Rust, including defining enums that hold data.
- We explored how to leverage the `match` statement with enums for effective control flow.
- We defined methods on enums, making them more versatile and functional.
- Completed exercises to reinforce our understanding of enums.

🌟 _Great job on completing Day 7! Keep practicing, and get ready for Day 8 where we will explore Collections in Rust!_

Thank you for joining **Day 7** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 6](../06_Structs/06_structs.md) | [Day 8 >>](../08_Collections/08_collections.md)

---
