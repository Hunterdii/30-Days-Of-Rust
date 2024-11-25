<div align="center">
  <h1>🦀 30 Days of Rust: Day 17 - Concurrency in Rust 🚀 </h1>
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
 

[<< Day 16](../16_File%20Handling/16_file_handling.md) | [Day 18 >>](../18_Asynchronous%20Programming/18_asynchronous_programming.md)  

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)



- [📘 Day 17 - Concurrency in Rust](#-day-17---concurrency-in-rust)
  - [👋 Welcome](#-welcome)  
  - [🔍 Overview](#-overview)  
  - [🛠 Environment Setup](#-environment-setup)  
  - [⚙ What is Concurrency?](#-what-is-concurrency)  
  - [💡 Rust's Concurrency Model](#-rusts-concurrency-model)  
    - [📜 Background: Send and Sync](#-background-send-and-sync)  
  - [💻 Concurrency in Practice](#-concurrency-in-practice)  
    - [🔄 Using Threads](#-using-threads)  
    - [💬 Communication Between Threads](#-communication-between-threads)  
    - [🛠 Mutex for Shared State](#-mutex-for-shared-state)  
    - [🔒 Avoiding Deadlocks](#-avoiding-deadlocks)  
  - [🔧 Advanced Concurrency Topics](#-advanced-concurrency-topics)  
    - [🌟 Atomic Reference Counting (Arc)](#-atomic-reference-counting-arc)  
    - [📊 Parallel Iterators with Rayon](#-parallel-iterators-with-rayon)  
    - [🔑 Choosing Your Guarantees: Cell, RefCell, Mutex](#-choosing-your-guarantees-cell-refcell-mutex)  
  - [🚀 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 17](#-exercises---day-17)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [🚀 Exercise: Level 2](#-exercise-level-2)
  - [🎥 Helpful Video References](#-helpful-video-references)  
  - [📝 Day 17 Summary](#-day-17-summary)  

# 📘 Day 17 - Concurrency in Rust

## 👋 Welcome  

Welcome to **Day 17** of the **30 Days of Rust Challenge**! 🎉 Today, we embark on an exciting journey into **Concurrency in Rust**. Rust’s fearless concurrency model enables developers to write robust and safe multithreaded applications. 🚀  

Join the [30 Days of Rust](https://discord.gg/dy4gAhng) community on Discord for discussions, questions, and to share your learning journey! 🚀

## 🔍 Overview  

Concurrency is the ability to execute multiple tasks simultaneously or interleave their execution to improve responsiveness and performance.  

In this lesson, we will learn about:  

- Rust's traits for concurrency: `Send` and `Sync`.  
- Using threads and message passing.  
- Synchronizing shared state with `Mutex`.  
- Preventing and debugging deadlocks.  
- Advanced concurrency concepts like `Arc`, `Rayon`, and when to use `Cell`, `RefCell`, or `Mutex`.  



## 🛠 Environment Setup  

If you have already set up your Rust environment on **Day 1**, you’re good to go! Otherwise, check out the [Environment Setup](../README.md#-environment-setup) section for detailed instructions. Ensure you have **Cargo** installed by running:

```bash
$ cargo --version
```

If you see a version number, you’re all set! 🎉


## ⚙ What is Concurrency?  

Concurrency is about enabling multiple tasks to progress concurrently. Rust provides:  

1. **Fearless concurrency**: Ensures safety through its ownership and type system.  
2. **Memory safety**: Prevents data races at compile time.  
3. **Customizability**: Offers primitives like threads, channels, `Mutex`, and community crates like `Rayon`.  

**Concurrency ≠ Parallelism**:  
- **Concurrency**: Multiple tasks interleaved.  
- **Parallelism**: Tasks executed simultaneously on multiple processors/cores.  



## 💡 Rust's Concurrency Model  

### 📜 Background: Send and Sync  

Rust ensures concurrency safety through two marker traits:  

1. **`Send`**: Allows transferring ownership between threads.  
   - Types like `u8`, `String`, and `Vec` are `Send`.  
   - Non-thread-safe types like `Rc` are not `Send`.  

2. **`Sync`**: Allows shared access across threads via immutable references.  
   - Types without interior mutability (e.g., `i32`) are `Sync`.  
   - `Arc` is `Sync` if its contents are `Sync`.  



## 💻 Concurrency in Practice  

## 🔄 Using Threads

Rust’s `std::thread` module provides an easy way to create and manage threads.  

Example: Creating a thread:  

```rust  
use std::thread;  

fn main() {  
    let handle = thread::spawn(|| {  
        for i in 1..5 {  
            println!("Hi from thread: {}", i);  
        }  
    });  

    for i in 1..5 {  
        println!("Hi from main: {}", i);  
    }  

    handle.join().unwrap();  
}  
```  

**Output**:  
```
Hi from main: 1  
Hi from thread: 1  
Hi from main: 2  
Hi from thread: 2  
...  
```  

- `thread::spawn`: Spawns a new thread to execute a closure.  
- `handle.join()`: Waits for the thread to finish.  

### <div align="center">_*or*_</div>


Rust's `std::thread` module allows spawning threads easily.  

```rust  
use std::thread;  

fn main() {  
    let handle = thread::spawn(|| {  
        println!("Hello from a thread!");  
    });  
    handle.join().unwrap(); // Wait for the thread to finish  
}  
```  

To move data into threads:  

```rust  
let data = vec![1, 2, 3];  
let handle = thread::spawn(move || {  
    println!("{:?}", data);  
});  
handle.join().unwrap();  
```  



## 💬 Communication Between Threads

Rust uses **message passing** to enable threads to communicate safely. This is implemented using **channels** from the `std::sync::mpsc` module (multiple producer, single consumer).  

Rust's `mpsc` (multiple producer, single consumer) channels allow safe message passing.  

Example: Sending messages between threads:  

```rust  
use std::sync::mpsc;  
use std::thread;  

fn main() {  
    let (tx, rx) = mpsc::channel();  

    thread::spawn(move || {  
        tx.send("Hello from the thread!").unwrap();  
    });  

    let received = rx.recv().unwrap();  
    println!("{}", received);  
}  
```  

**Output**:  
```
Hello from the thread!  
```  


## 🛠 Mutex for Shared State  
To share data between threads, Rust provides **Mutex** (mutual exclusion). A `Mutex` ensures that only one thread accesses data at a time.  

`Mutex<T>` provides mutual exclusion for shared mutable data. Combine it with `Arc` for multithreading: 

Example: Using `Mutex`:  

```rust  
use std::sync::{Arc, Mutex};  
use std::thread;  

fn main() {  
    let counter = Arc::new(Mutex::new(0));  
    let mut handles = vec![];  

    for _ in 0..10 {  
        let counter = Arc::clone(&counter);  
        let handle = thread::spawn(move || {  
            let mut num = counter.lock().unwrap();  
            *num += 1;  
        });  
        handles.push(handle);  
    }  

    for handle in handles {  
        handle.join().unwrap();  
    }  

    println!("Result: {}", *counter.lock().unwrap());  
}  
```  
**Output**:  
```
Result: 10  
```  


## 🔒 Avoiding Deadlocks  

A **deadlock** occurs when two or more threads wait indefinitely for each other to release a resource.  
Deadlocks occur when threads block each other indefinitely.  

**Avoid deadlocks by:**  
- Locking resources in a consistent order.  
- Using non-blocking algorithms.  
- Leveraging message passing over shared state. 
- Use timeouts for locking.  
- Prefer message-passing or atomics for simpler cases.  
  

Example of deadlock (avoid this pattern!):  

```rust  
use std::sync::{Arc, Mutex};  
use std::thread;  

fn main() {  
    let lock1 = Arc::new(Mutex::new(()));  
    let lock2 = Arc::new(Mutex::new(()));  

    let lock1_clone = Arc::clone(&lock1);  
    let lock2_clone = Arc::clone(&lock2);  

    let thread1 = thread::spawn(move || {  
        let _ = lock1_clone.lock().unwrap();  
        let _ = lock2_clone.lock().unwrap();  
    });  

    let thread2 = thread::spawn(move || {  
        let _ = lock2.lock().unwrap();  
        let _ = lock1.lock().unwrap();  
    });  

    thread1.join().unwrap();  
    thread2.join().unwrap();  
}  
```  



## 🔧 Advanced Concurrency Topics  

## 🌟 Atomic Reference Counting (Arc)  

`Arc<T>` allows shared ownership of immutable data across threads. Combine it with `Mutex<T>` for mutability.  



## 📊 Parallel Iterators with Rayon  

`Rayon` provides easy parallelism with iterators:  

```rust  
use rayon::prelude::*;  

fn main() {  
    let data = vec![1, 2, 3, 4, 5];  
    let result: Vec<_> = data.par_iter().map(|x| x * 2).collect();  
    println!("{:?}", result);  
}  
```  



## 🔑 Choosing Your Guarantees: Cell, RefCell, Mutex  

| Type      | Use Case                              | Thread-Safe | Notes                          |  
|-----------|---------------------------------------|-------------|--------------------------------|  
| `Cell`    | Single-threaded, interior mutability | ❌          | For simple cases              |  
| `RefCell` | Single-threaded runtime checks       | ❌          | Panics on multiple borrows    |  
| `Mutex`   | Multithreaded, shared state          | ✅          | Thread-safe with locking      |  



## 🚀 Hands-On Challenge  


### 1. **Threads and Shared State**  

1. Create a program that spawns multiple threads to increment a shared counter. Use `Arc` and `Mutex` to protect the shared counter.  
2. Extend the program to print the value of the counter after each increment.  

**Example Code:**  

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));

    let handles: Vec<_> = (0..5)
        .map(|_| {
            let counter = Arc::clone(&counter);
            thread::spawn(move || {
                let mut num = counter.lock().unwrap();
                *num += 1;
                println!("Counter: {}", *num);
            })
        })
        .collect();

    for handle in handles {
        handle.join().unwrap();
    }
}
```

### <div align="center">_*or*_</div>

1. **Threads**: Create a program that spawns 10 threads, each printing its ID.  
2. **Shared State**: Implement a thread-safe counter with `Arc` and `Mutex`.  
3. **Message Passing**: Write a producer-consumer model with `mpsc`.  
4. **Parallelism**: Use `Rayon` to parallelize a computationally heavy task. 

### 2. **Message Passing**  

Write a program to simulate a producer-consumer system using Rust's `mpsc` channel. The producer generates random numbers, and the consumer calculates their sum.  



### 3. **Advanced Concurrency**  

Use the `Rayon` library to parallelize a computation-heavy task, such as calculating the sum of squares for a large range of numbers.  



### 4. **Deadlock Prevention**  

Write a program that intentionally creates a deadlock by locking multiple `Mutex` objects in different orders. Extend the program to resolve the deadlock by reordering the locks.  



### 5. **Build a Logger**  

Create a simple logging system that writes log entries to a file with timestamps. Categorize logs as `INFO`, `WARNING`, and `ERROR`.  



## 💻 Exercises - Day 17 

### ✅ Exercise: Level 1  

1. Implement a program to:  
   - Create a file named `example.txt`.  
   - Write "Concurrency is fun in Rust!" into the file.  
   - Read the file content and print it to the console.  

2. Use threads to print numbers from 1 to 5 in parallel.  

3. Create a thread-safe counter that increments in multiple threads and prints its final value.  



### 🚀 Exercise: Level 2  

1. **Reverse Message Passing**: Modify the producer-consumer program to send data in reverse order (consumer sends back processed results to the producer).  

2. **File-based Thread Communication**: Write two programs:  
   - A writer program that writes data to a file.  
   - A reader program that reads and processes the data from the same file.  

3. **Build a File Copier with Threads**: Implement a program that reads from one file and writes to another file in parallel threads.  

4. **Deadlock Debugger**: Write a program that detects and logs deadlocks between threads to a file.  
 



## 🎥 Helpful Video References  

- [Rust Concurrency Explained](https://www.youtube.com/watch?v=06WcsNPUNC8)  
- [Fearless Concurrency in Rust](https://www.youtube.com/watch?v=CCDSW4DjCsc)  
- [Rayon: Data Parallelism in Rust](https://www.youtube.com/watch?v=gof_OEv71Aw)  



## 📝 Day 17 Summary  

Today, we explored Rust's approach to concurrency:  

- Created and managed threads with `std::thread`.  
- Used channels for safe message passing.  
- Implemented shared state with `Mutex`.  
- Learned to identify and avoid deadlocks.  

Rust's ownership model ensures safe and efficient concurrency. Practice these concepts and experiment with concurrent programs to solidify your understanding.  

Stay tuned for **Day 18**, where we will explore **Asynchronous Programming in Rust** in Rust! 🚀

🌟 _Great job on completing Day 17! Keep practicing, and get ready for Day 18!_

Thank you for joining **Day 17** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 16](../16_File%20Handling/16_file_handling.md) | [Day 18 >>](../18_Asynchronous%20Programming/18_asynchronous_programming.md)  

---
