<div align="center">
  <h1>🦀 30 Days of Rust: Day 18 - Asynchronous Programming in Rust 🚀 </h1>
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


[<< Day 17](../17_Concurrency/17_concurrency.md) | [Day 19 >>](../19_Networking/19_networking.md)

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)



- [📘 Day 18 - Asynchronous Programming in Rust](#-day-18---asynchronous-programming-in-rust)
  - [👋 Welcome](#-welcome)
  - [🔍 Overview](#-overview)
    - [When Should You Use Async Programming?](#when-should-you-use-async-programming)  
  - [🛠 Environment Setup](#-environment-setup)
  - [⚙ Understanding Asynchronous Programming](#-understanding-asynchronous-programming)
  - [⚙ Fundamentals of Asynchronous Programming](#-fundamentals-of-asynchronous-programming)  
  - [⚙ Asynchronous Programming Basics](#-asynchronous-programming-basics)
    - [🕸 Async in Rust](#-async-in-rust)  
    - [🔧 Understanding `async` and `await`](#-understanding-async-and-await)
    - [📚 Futures and Their Role](#-futures-and-their-role)
    - [🔄 Executors and Their Importance](#-executors-and-their-importance)
    - [💬 Tasks and Executors](#-tasks-and-executors)  
    - [🔧 Using Tokio and async-std](#-using-tokio-and-async-std)  
    - [🔀 Combining and Managing Async Tasks](#-combining-and-managing-async-tasks)
  - [📖 Real-World Example: HTTP Fetcher](#-real-world-example-http-fetcher)
  - [🚀 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 18](#-exercises---day-18)
    - [✅ Exercise: Level 1](#-exercise-level-1)  
    - [🚀 Exercise: Level 2](#-exercise-level-2)  
  - [🎥 Additional Resources](#-additional-resources)
  - [📚 More Insights](#-more-insights)
  - [📝 Day 18 Summary](#-day-18-summary)


---

# 📘 Day 18 - Asynchronous Programming in Rust

## 👋 Welcome

Welcome to **Day 18** of the **30 Days of Rust Challenge**! 🎉  

Today’s focus is **Asynchronous Programming in Rust**—a critical paradigm for building modern, efficient, and scalable systems. Async programming is all about handling tasks like I/O, event-driven code, and network communication without blocking execution. Rust offers a unique async model powered by its **zero-cost abstractions** and **compile-time guarantees** for safety.


## 🔍 Overview

### Why Async Programming?

Asynchronous programming allows tasks to run concurrently without blocking the main thread. This approach is especially useful for:  

Async programming allows you to:

1. **Avoid Blocking**: Handle I/O or timers without halting the program.
2. **Enable Concurrency**: Execute multiple tasks simultaneously on fewer threads.
3. **Achieve Scalability**: Ideal for applications like web servers, which handle thousands of requests.

- I/O-bound tasks (e.g., HTTP requests, file reading).  
- Event-driven systems.  
- Applications requiring high scalability.  

### When Should You Use Async Programming?  

- **Best Use Cases**:  
  - Network-intensive applications (HTTP clients/servers).  
  - Programs with idle time (e.g., waiting for I/O responses).  

- **Avoid for CPU-bound Tasks**:  
  - Async is not suitable for heavy computations. Use **multi-threading** instead for true parallelism.  

**Key Difference from Multi-threading:**

| Feature                  | Multi-threading                       | Asynchronous Programming            |
|--------------------------|---------------------------------------|-------------------------------------|
| **Performance**          | High overhead for threads            | Lower overhead                      |
| **Best for**             | CPU-intensive tasks                  | I/O-bound or idle tasks             |
| **Complexity**           | Potential for race conditions        | Safe at compile time                |

By the end of this lesson, you’ll:  

- Understand the `async` and `await` syntax.  
- Learn about `Futures` and their role in async programming.  
- Use executors like `Tokio` to run async code.  
- Combine and manage multiple async tasks with utilities like `join!` and `select!`.  

## 🛠 Environment Setup

Ensure you have **Cargo** installed and are working with Rust **1.39 or later** (the version that introduced async/await). If not, update Rust using:
```bash
rustup update
```

For today’s lessons, we’ll also need the **Tokio** crate. Add it to your project with:
```bash
cargo add tokio --features full
```

To work with async programming in Rust, you’ll need an **async runtime**. We'll use **Tokio**, the most popular runtime.

### Step 1: Add Dependencies

Add this to your `Cargo.toml`:

```toml
[dependencies]
tokio = { version = "1", features = ["full"] }
reqwest = { version = "0.11", features = ["json"] }  # Optional for HTTP
```

### Step 2: Verify the Setup

Run the following command to ensure your dependencies are installed:

```bash
cargo build
```

## ⚙ Understanding Asynchronous Programming  

### Why Asynchronous Programming?  

- **Efficiency**: It uses fewer threads while handling many tasks.  
- **Scalability**: Ideal for applications like web servers that need to handle thousands of connections.  

### Sync vs Async  

| **Synchronous**         | **Asynchronous**       |  
|--------------------------|-------------------------|  
| Blocks the thread.       | Does not block threads. |  
| Simpler to write.        | More scalable.          |  

## ⚙ Fundamentals of Asynchronous Programming  

### Why Async Programming?  

- **Traditional Approach**: In synchronous programming, tasks are executed one after another. If a task waits for an operation (e.g., reading a file), the entire thread is blocked.  
- **Async Approach**: Tasks yield control during waits, allowing other tasks to execute.  

Example comparison:  

**Synchronous**:  

```rust  
use std::thread::sleep;  
use std::time::Duration;  

fn main() {  
    println!("Task 1 started!");  
    sleep(Duration::from_secs(2));  
    println!("Task 1 completed!");  

    println!("Task 2 started!");  
    sleep(Duration::from_secs(1));  
    println!("Task 2 completed!");  
}  
```  

**Asynchronous**:  

```rust  
use tokio::time::{sleep, Duration};  

#[tokio::main]  
async fn main() {  
    let task1 = async {  
        println!("Task 1 started!");  
        sleep(Duration::from_secs(2)).await;  
        println!("Task 1 completed!");  
    };  

    let task2 = async {  
        println!("Task 2 started!");  
        sleep(Duration::from_secs(1)).await;  
        println!("Task 2 completed!");  
    };  

    tokio::join!(task1, task2);  
}  
```  

**Output**: Both tasks run concurrently, reducing total execution time.  



## ⚙ Asynchronous Programming Basics

## 🕸 Async in Rust  

Rust async programming revolves around three core concepts:  

1. `async` functions.  
2. `await` expressions.  
3. `Future` trait.  


### 🔧 Understanding `async` and `await`  

- **`async`**: Marks a function as asynchronous.  
- **`await`**: Waits for a `Future` to complete.  

#### Example  

```rust  
async fn add(a: u8, b: u8) -> u8 {  
    a + b  
}  

#[tokio::main]  
async fn main() {  
    let result = add(10, 20).await;  
    println!("Result: {}", result);  
}  
```  


### <div align="center">_*or*_</div>

### 🔧 `async` and `await`  

- **`async fn`**: Marks a function as asynchronous, returning a `Future`.  
- **`.await`**: Waits for the completion of a `Future`.  

Example:  

```rust  
async fn hello_world() {  
    println!("Hello, world!");  
}  

#[tokio::main]  
async fn main() {  
    hello_world().await;  
}  
```  




## 📚 Futures and Their Role

- **What is a Future?**  
  A Future is a placeholder for a value that may not yet exist.
   
  A **Future** in Rust represents a value that may not yet be available.

- **Lazy Execution**: A Future does nothing until `.await` is called.  
- **Lazy Execution**: Futures do nothing until explicitly awaited.

- **Polling States**:  
  - **`Poll::Pending`**: Task in progress.  
  - **`Poll::Ready`**: Task completed.  

- **Polled by Executors**: Executors like Tokio drive futures to completion.

#### Example: Returning a Future

```rust
async fn compute() -> u32 {
    42
}

#[tokio::main]
async fn main() {
    let result = compute().await;
    println!("Result: {}", result);
}
```

## 💡 Rust's Async Model  

Rust’s async model is built around:
- **Futures**: A computation that will produce a value at some point in the future.
- **async/await**: Keywords for writing async code in a synchronous style.
- **Executors**: Runtime systems like Tokio that poll futures to completion.


### 📜 Background: `Future` and `async`/`await`  

In Rust:
- **`Future`**: A trait representing an asynchronous computation.
- **`async`**: Turns a function into one that returns a `Future`.
- **`await`**: Suspends execution until a `Future` is ready.

Example:
```rust
use tokio::time;

#[tokio::main]
async fn main() {
    println!("Task started...");
    time::sleep(time::Duration::from_secs(2)).await;
    println!("Task completed!");
}
```


## 🔄 Executors and Their Importance

Executors are responsible for running async code. They manage task scheduling and drive Futures to completion.

Async code requires an executor to drive futures to completion. Common executors:  

- **Tokio**: High-performance async runtime.  
- **async-std**: Async-friendly standard library.  

Tokio example:  

```rust  
use tokio::time::{sleep, Duration};  

async fn task() {  
    sleep(Duration::from_secs(1)).await;  
    println!("Task completed!");  
}  

#[tokio::main]  
async fn main() {  
    task().await;  
}  
```
 
## 💬 Tasks and Executors  

To run async functions, we need an executor. Executors like **Tokio** or **async-std** poll futures until they’re complete. 



### 🔧 Using Tokio and async-std  

#### Using Tokio
Tokio is the most popular async runtime in Rust:
```rust
use tokio::time;

#[tokio::main]
async fn main() {
    println!("Fetching data...");
    time::sleep(time::Duration::from_secs(2)).await;
    println!("Data fetched!");
}
```

#### Using async-std
Async-std is another runtime for async programming:
```rust
use async_std::task;

#[async_std::main]
async fn main() {
    println!("Processing...");
    task::sleep(std::time::Duration::from_secs(1)).await;
    println!("Done!");
}
```



## 🔀 Combining and Managing Async Tasks

### 🔀 Combining Futures with `join!` and `select!`  

- **`join!`**: Runs multiple futures concurrently, waiting for all to complete.  
- **`select!`**: Waits for the first future to complete.  

Example:  

```rust  
use tokio::time::{sleep, Duration};  

async fn task1() {  
    sleep(Duration::from_secs(2)).await;  
    println!("Task 1 done!");  
}  

async fn task2() {  
    sleep(Duration::from_secs(1)).await;  
    println!("Task 2 done!");  
}  

#[tokio::main]  
async fn main() {  
    tokio::join!(task1(), task2());  
}  
```  

**Output**:  
```
Task 2 done!  
Task 1 done!  
```  

#### `join!`: Run Multiple Futures Concurrently  

```rust  
use tokio::time::{sleep, Duration};  

async fn task1() {  
    sleep(Duration::from_secs(2)).await;  
    println!("Task 1 done!");  
}  

async fn task2() {  
    sleep(Duration::from_secs(1)).await;  
    println!("Task 2 done!");  
}  

#[tokio::main]  
async fn main() {  
    tokio::join!(task1(), task2());  
}  
```  

#### `select!`: Wait for the First Completed Future  

```rust  
use tokio::time::{sleep, Duration};  

#[tokio::main]  
async fn main() {  
    tokio::select! {  
        _ = sleep(Duration::from_secs(2)) => println!("2 seconds passed"),  
        _ = sleep(Duration::from_secs(1)) => println!("1 second passed"),  
    };  
}  
```  


## 📖 Real-World Example: HTTP Fetcher

Let’s build a simple HTTP fetcher using the `reqwest` library.

### Add `reqwest` Dependency

Include the following in `Cargo.toml`:

```toml
[dependencies]
reqwest = { version = "0.11", features = ["json"] }
```

### Example Code

```rust
use reqwest::Error;

async fn fetch_url(url: &str) -> Result<(), Error> {
    let response = reqwest::get(url).await?;
    let body = response.text().await?;
    println!("Response: {}", body);
    Ok(())
}

#[tokio::main]
async fn main() {
    let url = "https://jsonplaceholder.typicode.com/posts/1";
    if let Err(e) = fetch_url(url).await {
        eprintln!("Error: {}", e);
    }
}
```

### <div align="center">_*or*_</div>

### Example  

```rust  
use reqwest::Error;  

async fn fetch_url(url: &str) -> Result<(), Error> {  
    let response = reqwest::get(url).await?;  
    println!("Response: {}", response.text().await?);  
    Ok(())  
}  

#[tokio::main]  
async fn main() {  
    fetch_url("https://jsonplaceholder.typicode.com/posts/1").await.unwrap();  
}  
```  


## 🚀 Hands-On Challenge

1. Write an async program that:
   - Fetches data from three APIs concurrently.
   - Logs the fastest response using `select!`.
2. Implement error handling for async functions.
4. Write a program with multiple async tasks using `join!`.  
5. Use `select!` to handle the first completed task.  
6. Implement an async function that makes multiple HTTP requests concurrently (use `reqwest` library).  

## 💻 Exercises - Day 18  

### ✅ Exercise: Level 1  

1. Write an async program that:
   - Prints "Starting task...".
   - Waits for 3 seconds using `async-std` or `Tokio`.
   - Prints "Task completed!".

2. Implement a function `async_fetch` that simulates fetching data from a server and returns the string `"Data received!"`.

### 🚀 Exercise: Level 2  

1. **Async Web Server**:
   - Use `tokio` to build a simple web server that responds to HTTP requests with `"Hello, Rust Async!"`.

2. **Concurrent Tasks**:
   - Create a program that spawns three async tasks, each waiting for a random amount of time before printing its completion.

3. **Async File I/O**:
   - Write an async function to read a file’s content and print it to the console.


## 🎥 Additional Resources

- [Understanding Async/Await in Rust](https://www.youtube.com/watch?v=K8LNPYNvT-U)
- [Tokio Async Runtime Overview](https://www.youtube.com/watch?v=psrzkcyOBJM)
- [Async Programming in Rust](https://www.youtube.com/watch?v=ThjvMReOXYM)  
- [Tokio Crash Course](https://www.youtube.com/watch?v=PabDPIrt9fk)  
- [Async I/O with async-std](https://www.youtube.com/watch?v=yfcJGEISsLc)  





## 📚 More Insights

### async/.await in Rust

Async functions return Futures. Use `.await` to pause execution until a Future is ready.

#### Example:

```rust
async fn add(a: u8, b: u8) -> u8 {
    a + b
}

#[tokio::main]
async fn main() {
    let result = add(2, 3).await;
    println!("Sum: {}", result);
}
```

### Alternatives for Running Async Code

1. **Tokio**: Adds async capabilities with `#[tokio::main]`.
2. **Futures Library**: Provides `block_on` to block until a Future is ready.


## 📝 Day 18 Summary

Today, you’ve mastered:  

- **Async basics**: `async`, `await`, and Futures.  
- **Task management**: Combining tasks with `join!` and `select!`.  
- **Executors**: Running async code efficiently.  
- **Real-world use cases**: HTTP requests and concurrency patterns.  

Stay tuned for **Day 19**, where we will explore **Networking in Rust** in Rust! 🚀

🌟 _Great job on completing Day 18! Keep practicing, and get ready for Day 19!_

Thank you for joining **Day 18** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 17](../17_Concurrency/17_concurrency.md) | [Day 19 >>](../19_Networking/19_networking.md)

---
