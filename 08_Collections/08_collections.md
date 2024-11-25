<div align="center">
  <h1>🦀 30 Days Of Rust: Day 8 - Rust Collections 🚀</h1>
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

[<< Day 7](../07_Enums/07_enums.md) | [Day 9 >>](../09_Error%20Handling/09_error_handling.md)

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)

- [📘 Day 8 - Rust Collections](#-day-8---rust-collections)
  - [👋 Welcome](#-welcome)
  - [🔍 Overview](#-overview)
  - [🛠 Environment Setup](#-environment-setup)
  - [📖 Understanding Collections](#-understanding-collections)
    - [📦 Vectors](#-vectors)
    - [🔗 Strings](#-strings)
    - [📋 Hash Maps](#-hash-maps)
    - [📚 Other Collections](#-other-collections)
      - [🌳 BTreeMap](#-btreemap)
      - [🔄 VecDeque](#-vecdeque)
      - [🔗 LinkedList](#-linkedlist)
  - [🎯 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 8](#-exercises---day-8)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [✅ Exercise: Level 2](#-exercise-level-2)
    - [🎥 Helpful Video References](#-helpful-video-references)
  - [📝 Day 8 Summary](#-day-8-summary)

---

# 📘 Day 8 - Rust Collections

## 👋 Welcome

Welcome to **Day 8** of your Rust journey! 🎉 Today, we’ll explore **Collections** in Rust, which are essential for storing multiple values. We'll cover vectors, strings, hash maps, and other collections, and learn how to use them effectively in your programs. Let's get started! 🚀

**Congratulations!** 🎉 You've taken the first step in your journey to master the _30 Days of Rust_ programming challenge. In this challenge, you will learn the fundamentals of Rust and how to harness its power to write efficient, fast, and safe code. By the end of this journey, you'll have gained a solid understanding of Rust's core concepts and best practices, helping you become a confident Rustacean. 🦀


Feel free to join the [30 Days of Rust](https://discord.gg/dy4gAhng) community on Discord, where you can interact with others, ask questions, and share your progress!


## 🔍 Overview

In Rust, collections are data structures that hold multiple values. We'll cover:

- Using vectors for dynamic arrays.
- Working with strings for text data.
- Storing key-value pairs with hash maps.
- Exploring other collections available in Rust.

## 🛠 Environment Setup

Ensure that you have your Rust environment set up correctly from Day 1. If you haven’t installed Rust yet, please refer to the setup instructions from [Day 1](../README.md#-environment-setup).

## 📖 Understanding Collections

### 📦 Vectors

Vectors are resizable arrays that can hold multiple values of the same type. You can push or pop values dynamically.

**Example:**

```rust
fn main() {
    let mut numbers: Vec<i32> = Vec::new();

    numbers.push(1);
    numbers.push(2);
    numbers.push(3);

    println!("Numbers: {:?}", numbers);

    if let Some(last) = numbers.pop() {
        println!("Popped: {}", last);
    }

    println!("Numbers after pop: {:?}", numbers);
}
```

### 🔗 Strings

Strings in Rust are collections of characters. The `String` type is mutable, while `&str` is an immutable string slice.

**Example:**

```rust
fn main() {
    let mut greeting = String::from("Hello");

    greeting.push_str(", world!");
    println!("{}", greeting);

    let substring = &greeting[0..5]; // "Hello"
    println!("Substring: {}", substring);
}
```

### 📋 Hash Maps

Hash maps store key-value pairs and provide efficient access to data.

**Example:**

```rust
use std::collections::HashMap;

fn main() {
    let mut scores = HashMap::new();

    scores.insert(String::from("Alice"), 50);
    scores.insert(String::from("Bob"), 60);
    scores.insert(String::from("Charlie"), 70);

    println!("Scores: {:?}", scores);

    let bob_score = scores.get("Bob").unwrap();
    println!("Bob's score: {}", bob_score);
}
```

### 📚 Other Collections

Rust provides several other useful collections, each designed for specific use cases:

#### 🌳 BTreeMap

`BTreeMap` is an ordered map implementation that stores key-value pairs in a sorted manner. It is useful when you need to maintain order and perform range queries.

**Example:**

```rust
use std::collections::BTreeMap;

fn main() {
    let mut scores = BTreeMap::new();

    scores.insert("Alice", 50);
    scores.insert("Bob", 60);
    scores.insert("Charlie", 70);

    for (name, score) in &scores {
        println!("{}: {}", name, score);
    }
}
```

#### 🔄 VecDeque

`VecDeque` is a double-ended queue that allows efficient addition and removal of elements from both ends. This is beneficial when you need a queue-like structure but also require quick access to both the front and back.

**Example:**

```rust
use std::collections::VecDeque;

fn main() {
    let mut queue: VecDeque<i32> = VecDeque::new();

    queue.push_back(1);
    queue.push_back(2);
    queue.push_front(0);

    println!("Queue: {:?}", queue);

    if let Some(front) = queue.pop_front() {
        println!("Removed from front: {}", front);
    }

    println!("Queue after pop: {:?}", queue);
}
```

#### 🔗 LinkedList

`LinkedList` is a doubly linked list, which allows for efficient insertions and deletions from both ends. It is useful when you need a collection that frequently changes size and requires efficient element removal.

**Example:**

```rust
use std::collections::LinkedList;

fn main() {
    let mut list = LinkedList::new();

    list.push_back(1);
    list.push_back(2);
    list.push_front(0);

    for value in &list {
        println!("{}", value);
    }

    if let Some(front) = list.pop_front() {
        println!("Removed from front: {}", front);
    }

    println!("List after pop: {:?}", list);
}
```

Each of these collections has its specific use cases based on performance requirements, such as speed of access and mutability.

## 🎯 Hands-On Challenge

Create a Rust program that manages a simple inventory system using collections. Implement the following functionalities:

1. Store items in a vector.
2. Use a hash map to track the quantities of each item.
3. Allow adding, removing, and updating item quantities.

**Template:**

```rust
use std::collections::HashMap;

fn main() {
    let mut inventory: Vec<String> = Vec::new();
    let mut quantities: HashMap<String, i32> = HashMap::new();

    // Add items
    inventory.push(String::from("Apples"));
    quantities.insert(String::from("Apples"), 10);

    // Update quantity
    *quantities.get_mut("Apples").unwrap() += 5;

    // Remove item
    inventory.retain(|item| item != "Bananas");

    // Print inventory
    for item in &inventory {
        let quantity = quantities.get(item).unwrap();
        println!("{}: {}", item, quantity);
    }
}
```

✅ **Share your solution on GitHub and tag #30DaysOfRust on social media! Let the world see your progress! 🚀**

## 💻 Exercises - Day 8

### ✅ Exercise: Level 1

1. Create a vector of integers, push values into it, and print the vector.
2. Write a program to create a string and append characters to it, displaying the final string.
3. Implement a hash map to store names and ages of three people. Print each person's name and age.
4. Create a vector of strings, representing fruit names, and sort them in alphabetical order.

### ✅ Exercise: Level 2

1. Implement a program that tracks a list of tasks using a vector. Each task should have a description and a boolean indicating if it’s completed.
2. Create a hash map to count the occurrences of words in a given sentence. Print each word with its count.
3. Use a `VecDeque` to implement a queue for processing tasks. Demonstrate adding and removing tasks from the queue.
4. Write a program using a `BTreeMap`

 to store and print a sorted list of student names along with their scores.

### 🎥 Helpful Video References

- [Rust Collections Overview](https://www.youtube.com/watch?v=Zs-pS-egQSs)
- [Understanding Vectors in Rust](https://www.youtube.com/watch?v=LPr0KIs7ZQE)
- [Working with Hash Maps in Rust](https://www.youtube.com/watch?v=KYw3Lnf0nSY)

## 📝 Day 8 Summary

- We learned how to work with **vectors**, **strings**, and **hash maps** in Rust.
- We explored other collections available in Rust and their use cases.
- Completed exercises to reinforce our understanding of collections.

🌟 _Great job on completing Day 8! Keep practicing, and get ready for Day 9 where we will explore more advanced topics (Error Handling) in Rust!_

Thank you for joining **Day 8** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 7](../07_Enums/07_enums.md) | [Day 9 >>](../09_Error%20Handling/09_error_handling.md)

---


