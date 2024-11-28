<div align="center">
  <h1>🦀 30 Days of Rust: Day 20 - Unsafe Rust 🚨 </h1>
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


[<< Day 19](../19_Networking/19_networking.md) | [Day 21 >>](../21_Rust%20Lifetimes/21_rust_lifetimes.md)

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)

- [📘 Day 20 - Unsafe Rust](#-day-20---unsafe-rust)
  - [👋 Welcome](#-welcome)
  - [🔍 Overview](#-overview)
  - [🛠 Environment Setup](#-environment-setup)
  - [🔍 What is Unsafe Rust?](#-what-is-unsafe-rust)
  - [⚠️ Why Use Unsafe Rust?](#️-why-use-unsafe-rust)
  - [⚡ Unsafe Superpowers](#-unsafe-superpowers)
    - [1. Dereferencing Raw Pointers](#1-dereferencing-raw-pointers)
    - [2. Calling Unsafe Functions](#2-calling-unsafe-functions)
    - [3. Accessing or Modifying Mutable Static Variables](#3-accessing-or-modifying-mutable-static-variables)
    - [4. Implementing Unsafe Traits](#4-implementing-unsafe-traits)
    - [5. Accessing Union Fields](#5-accessing-union-fields)
  - [🔐 Unsafe Blocks](#-unsafe-blocks)  
  - [🔎 Common Scenarios for Unsafe Rust](#-common-scenarios-for-unsafe-rust)  
  - [🧑‍💻 FFI (Foreign Function Interface) in Rust](#-ffi-foreign-function-interface-in-rust)
    - [Calling C Functions from Rust](#calling-c-functions-from-rust)
  - [⚡ Unsafe and Performance](#-unsafe-and-performance)
  - [⚙️ Unsafe and Performance](#-unsafe-and-performance)  
  - [📖 Real-World Example: Interfacing with C Libraries](#-real-world-example-interfacing-with-c-libraries)
  - [🔐 Unsafe Blocks & Best Practices](#-unsafe-blocks--best-practices)
  - [🔎 Real-World Scenarios for Unsafe Rust](#-real-world-scenarios-for-unsafe-rust)
  - [⚡ Practical Examples and Code Walkthroughs](#-practical-examples-and-code-walkthroughs)
  - [🚀 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 20](#-exercises---day-20)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [🚀 Exercise: Level 2](#-exercise-level-2)
  - [🎥 Helpful Video References](#-helpful-video-references)
  - [📝 Day 20 Summary](#-day-20-summary)

---

# 📘 Day 20 - Unsafe Rust

## 👋 Welcome  

Welcome to **Day 20** of our **30 Days of Rust Challenge**! 🎉

If Rust’s memory safety is its superhero cape, then **Unsafe Rust** is its secret weapon. Today, we dive into the most powerful, yet perilous, aspect of Rust programming. You’ll learn how to harness **Unsafe Rust** effectively and responsibly, enabling you to tackle low-level programming challenges without compromising control or performance.

Today’s lesson is all about mastering **Unsafe Rust**, a powerful feature that allows you to step outside the safety net of Rust's compiler. Rust guarantees memory safety in most cases, but when you need low-level control or to interface with hardware and other languages (like C), you need to leverage Unsafe Rust.  

But **with great power comes great responsibility!** ⚡ Unsafe Rust gives you more control over your program's memory, but you must use it with care. If misused, it can lead to bugs and undefined behavior.
Get ready to unlock the **raw power** of Rust—but beware, with great power comes great responsibility! 🕶️✨

Join the [30 Days of Rust](https://discord.gg/dy4gAhng) community on Discord for discussions, questions, and to share your learning journey! 🚀

## 🔍 Overview  

Rust’s primary goal is to ensure memory safety, concurrency safety, and thread safety without needing a garbage collector. However, **unsafe code** in Rust allows you to write code that can bypass some of these safety guarantees, enabling you to work directly with memory and interfaces outside of the Rust ecosystem. While this can lead to more performant code, it requires careful attention to avoid introducing undefined behavior.

In Rust, **unsafe** means that you, the programmer, are promising the compiler that certain actions will not break the safety guarantees Rust normally provides. Rust’s ownership system, borrowing rules, and lifetime management are all checked at compile-time, but **unsafe code** can bypass these checks.

Unsafe Rust should only be used when necessary, as it can potentially introduce bugs and crashes if not handled correctly.

### Unsafe Code in Rust can be broken into three categories:

1. **Raw pointers**: Working with raw pointers (`*const T` and `*mut T`).
2. **Unsafe blocks**: Blocks of code where you manually promise the compiler that certain code will uphold safety guarantees.
3. **Foreign Function Interface (FFI)**: Calling functions from other programming languages like C.

## 🛠 Environment Setup  

If you have already set up your Rust environment on **Day 1**, you’re good to go! Otherwise, check out the [Environment Setup](../README.md#-environment-setup) section for detailed instructions. Ensure you have **Cargo** installed by running:

```bash
$ cargo --version
```

If you see a version number, you’re all set! 🎉


## **🔎 What Will You Learn?**

By the end of today’s session, you’ll be able to:
- Understand **what Unsafe Rust is** and why it exists.
- Master the **five unsafe superpowers**.
- Identify **when and where Unsafe Rust is necessary**.
- Learn how to **write safe abstractions around unsafe code**.
- Build confidence to handle real-world scenarios with Unsafe Rust.


## **🔍 What is Unsafe Rust?**  

Unsafe Rust is a special feature of the Rust language that allows you to bypass Rust’s strict compile-time checks for memory safety. By opting into "unsafe" code, you get access to operations that are normally not allowed under Rust’s safety guarantees.  

While Rust's default mode ensures that your code is memory-safe—no dangling pointers, no data races, no buffer overflows—there are scenarios where these checks are **too restrictive**. That’s where Unsafe Rust comes in.

**Unsafe Rust** is a subset of the Rust language that allows you to write code that the compiler cannot statically verify for safety. This is often needed when interfacing with low-level system components, dealing with raw memory, or using libraries written in other languages.

Rust uses a concept called **safety guarantees**, which ensures that references are always valid, data races do not occur, and memory is properly allocated and deallocated. By default, Rust ensures all of this through its ownership and borrowing rules.

However, some operations—such as directly working with memory or calling external code (e.g., C libraries)—require a more flexible approach. **Unsafe Rust** allows you to write these types of operations, but it’s your responsibility to ensure they don’t break the safety guarantees.

You mark sections of your code as `unsafe` using the `unsafe` keyword.

```rust
unsafe {
    // Unsafe code goes here
}
```


## **⚠️ Why Use Unsafe Rust?**  

Unsafe Rust unlocks the full potential of low-level programming and system development. Here’s why it’s important:  

1. **Performance Optimization**: By eliminating runtime checks, Unsafe Rust can dramatically improve performance in critical sections of code.  
2. **Foreign Function Interface (FFI)**: It allows Rust to communicate with other programming languages (e.g., C, C++) that don’t have the same memory safety guarantees.  
3. **Low-Level Systems Programming**: Unsafe Rust is ideal for writing operating systems, device drivers, or any code that interacts directly with hardware.  
4. **Advanced Data Structures**: Some complex data structures, like linked lists or arenas, require unsafe operations to optimize memory layout and access.

Unsafe Rust doesn't make your program unsafe; it just shifts the responsibility for safety onto you, the programmer. **If you misuse it, the compiler won't stop you**—but your code could break in unpredictable ways.

## ⚡ Unsafe Superpowers  

Unsafe Rust grants **five superpowers**—capabilities prohibited in safe Rust to ensure safety. Let’s explore each of them:  


### **1. Dereferencing Raw Pointers**  

Raw pointers (`*const T` and `*mut T`) allow you to directly manipulate memory locations, bypassing Rust’s ownership and borrowing rules. This is powerful, but it’s also risky because raw pointers can easily become null or dangling.

```rust
fn main() {
    let x = 42;
    let raw_ptr = &x as *const i32;

    unsafe {
        println!("Raw pointer points to: {}", *raw_ptr);  // Dereferencing
    }
}
```

**Key Risks**:  
- Dereferencing null or dangling pointers causes undefined behavior.  
- Rust can't guarantee pointer validity, which means that bugs can be hard to track down.

### <div align="center">_*or*_</div>

Raw pointers (`*const T` and `*mut T`) are akin to C/C++ pointers but lack Rust’s guarantees:  
- They can be null or dangling.  
- They bypass ownership and borrowing rules.  

#### Example:  
```rust  
let x = 42;
let r1 = &x as *const i32;
let r2 = &x as *mut i32;

unsafe {
    println!("r1 points to: {}", *r1);
} 
```  

#### Use Cases:  
- Interfacing with hardware or foreign libraries.  
- Low-level memory management.  



### **2. Calling Unsafe Functions**  

Certain functions perform inherently unsafe operations, like interfacing with hardware or manipulating raw memory. These functions must be explicitly marked as `unsafe` to prevent accidental misuse.

```rust
unsafe fn dangerous() {
    println!("This is an unsafe function!");
}

fn main() {
    unsafe {  // Unsafe block required to call the function
        dangerous();
    }
}
```

### <div align="center">_*or*_</div>

Some functions are marked as `unsafe` due to the invariants they require. You must call them inside an `unsafe` block.  

#### Example:  
```rust  
unsafe fn dangerous() {  
    println!("This is an unsafe function!");  
}  

fn main() {  
    unsafe {  
        dangerous();  
    }  
}  
```  

#### Use Cases:  
- Interfacing with system APIs.  
- Foreign Function Interface (FFI).  


### **3. Accessing or Modifying Mutable Static Variables**  

Mutable static variables are globally accessible and can lead to **data races** if modified concurrently. However, in a single-threaded context or with proper synchronization, they can be useful.

```rust
static mut COUNTER: u32 = 0;

fn increment_counter() {
    unsafe {
        COUNTER += 1;
        println!("Counter: {}", COUNTER);
    }
}

fn main() {
    increment_counter();
}
```

**Best Practice**:  
To avoid issues, use synchronization primitives like `Mutex` or `RwLock` in multithreaded contexts.

### <div align="center">_*or*_</div>

Static variables have a single memory location throughout the program’s lifetime. Modifying mutable static variables is unsafe due to potential data races.  

#### Example:  
```rust  
static mut COUNTER: u32 = 0;  

fn increment() {  
    unsafe {  
        COUNTER += 1;  
        println!("Counter: {}", COUNTER);  
    }  
}  

fn main() {  
    increment();  
    increment();  
}  
```  

#### Use Cases:  
- Maintaining global state.  
- Interfacing with low-level hardware.  


### **4. Implementing Unsafe Traits**  

Rust allows you to define traits that are inherently unsafe. The idea is that using these traits could lead to undefined behavior if not implemented correctly. Only certain types can implement unsafe traits.

```rust
unsafe trait DangerousTrait {
    fn risky_method();
}

unsafe impl DangerousTrait for i32 {
    fn risky_method() {
        println!("Risky method executed for i32!");
    }
}
```

### <div align="center">_*or*_</div>

A trait can be marked `unsafe` if implementing it requires upholding invariants the compiler cannot verify.  

#### Example:  
```rust  
unsafe trait UnsafeTrait {  
    fn do_something(&self);  
}  

unsafe impl UnsafeTrait for i32 {  
    fn do_something(&self) {  
        println!("Unsafe trait implemented for i32!");  
    }  
}  

fn main() {  
    let x: i32 = 42;  
    unsafe {  
        x.do_something();  
    }  
}  
```  

#### Use Cases:  
- Traits involving low-level guarantees.  
- Abstractions over foreign types.  


### **5. Accessing Union Fields**  

Unions allow multiple types to occupy the same memory space. Accessing fields in unions can be risky because the compiler doesn’t check the type of data stored, so you must handle this with care.

```rust
union MyUnion {
    int_val: u32,
    float_val: f32,
}

fn main() {
    let u = MyUnion { int_val: 42 };

    unsafe {
        println!("Union value (as int): {}", u.int_val);
    }
}
```

### <div align="center">_*or*_</div>

Unions store multiple data types in the same memory space. Accessing a union field is unsafe because Rust cannot guarantee which field is active.  

#### Example:  
```rust  
union MyUnion {  
    int_val: i32,  
    float_val: f32,  
}  

fn main() {  
    let u = MyUnion { int_val: 42 };  

    unsafe {  
        println!("Union value: {}", u.int_val);  
    }  
}  
```  

#### Use Cases:  
- Interfacing with C unions.  
- Memory optimization.  


## **🔐 Unsafe Blocks & Best Practices**  

An **unsafe block** allows you to isolate operations that the Rust compiler cannot guarantee are safe. You need to wrap potentially dangerous operations in these blocks.

```rust
let ptr = 42 as *const i32;

unsafe {
    println!("Dereferenced pointer: {}", *ptr);
}
```

**Best Practices**:  
1. **Minimize Unsafe Code**: Keep unsafe blocks small and as isolated as possible.  
2. **Encapsulate Unsafe Code**: Write safe abstractions to hide unsafe details.  
3. **Document Assumptions**: Clearly explain the invariants required for unsafe code to work correctly.  
4. **Test Thoroughly**: Always test unsafe code thoroughly to avoid undefined behavior.



## **🔎 Real-World Scenarios for Unsafe Rust**  

### **1. Calling C Functions (FFI)**  

Rust provides the ability to interact with C libraries through FFI (Foreign Function Interface). To call C functions safely, Rust’s `unsafe` blocks are used.

```rust
extern "C" {
    fn abs(input: i32) -> i32;
}

fn main() {
    unsafe {
        println!("Absolute value of -5: {}", abs(-5));
    }
}
```



### **2. Manual Memory Management**  

You can use unsafe code for manual memory management, allocating and de

allocating memory without the Rust ownership system.

```rust
use std::ptr;

fn main() {
    let x = Box::new(42);
    let raw = Box::into_raw(x);

    unsafe {
        println!("Raw pointer points to: {}", *raw);
    }
}
```

## 🛠 Working with Pointers  

One of the main features of Unsafe Rust is working directly with **pointers**. Rust has two types of raw pointers:

- `*const T` — Immutable raw pointer.
- `*mut T` — Mutable raw pointer.

### Dereferencing Raw Pointers

Dereferencing raw pointers allows you to access the value at the pointer location, just like in languages like C or C++. In Rust, dereferencing a raw pointer is considered unsafe because the compiler cannot guarantee that the pointer is valid.

```rust
let x: i32 = 42;
let r: *const i32 = &x;

unsafe {
    println!("r points to: {}", *r);
}
```

Here, `r` is a raw pointer to `x`, and we use an unsafe block to dereference it.

### Creating Unsafe Blocks

The `unsafe` block is used to wrap code that is inherently unsafe, like dereferencing raw pointers or calling unsafe functions.

```rust
let x: i32 = 10;
let r: *const i32 = &x;

unsafe {
    println!("Value of x is: {}", *r); // Dereferencing a raw pointer
}
```

In this example, dereferencing the raw pointer `r` is marked as `unsafe` because Rust cannot guarantee its safety.

### Working with Mutable References

Unsafe Rust also allows you to mutate data through mutable raw pointers. This is dangerous if not handled correctly, as it can lead to data races or memory corruption.

```rust
let mut x: i32 = 10;
let r: *mut i32 = &mut x;

unsafe {
    *r = 20;
    println!("x is now: {}", *r);
}
```

## 🔐 Unsafe Blocks  

An **unsafe block** encapsulates unsafe operations, ensuring that you clearly mark where manual checks are required.  

### Example  

```rust
let raw_pointer = 42 as *const i32;

unsafe {
    println!("Value: {}", *raw_pointer);
}
```



## 🔎 Common Scenarios for Unsafe Rust  

1. **Interfacing with C Libraries**  
   Use Rust’s `std::ffi` module to work with C-style strings or data structures.  

   ```rust
   extern "C" {
       fn abs(input: i32) -> i32;
   }

   unsafe {
       println!("Absolute value: {}", abs(-42));
   }
   ```

2. **Memory Management**  
   Use `Box::from_raw` or `Vec::from_raw_parts` to manage heap memory directly.  

   ```rust
   let x = Box::new(42);
   let raw = Box::into_raw(x);

   unsafe {
       let boxed = Box::from_raw(raw);
       println!("Value: {}", *boxed);
   }
   ```

3. **Custom Allocators**  
   Create custom memory allocators for performance-critical tasks.  



## ⚡ Practical Examples  

### Example 1: Manual Memory Allocation  

```rust
use std::alloc::{alloc, dealloc, Layout};

fn main() {
    let layout = Layout::new::<u32>();

    unsafe {
        let ptr = alloc(layout) as *mut u32;
        if ptr.is_null() {
            panic!("Failed to allocate memory");
        }

        *ptr = 42;
        println!("Value: {}", *ptr);

        dealloc(ptr as *mut u8, layout);
    }
}
```



### Example 2: Using Unsafe Traits  

```rust
unsafe trait Dangerous {
    fn perform_action(&self);
}

struct Action;

unsafe impl Dangerous for Action {
    fn perform_action(&self) {
        println!("Performing dangerous action!");
    }
}

fn main() {
    let action = Action;

    unsafe {
        action.perform_action();
    }
}
```



## 🧑‍💻 FFI (Foreign Function Interface) in Rust  

One of the most common uses for Unsafe Rust is working with **FFI (Foreign Function Interface)**, which allows Rust to interact with functions and libraries written in other languages, like C or C++. Rust’s FFI support makes it easy to call functions from these languages in a safe way, but you still need to be careful when interacting with low-level constructs.

### Calling C Functions from Rust

To call a C function, we use the `extern` keyword to declare the function’s signature and mark it as external.

Here’s an example of calling a C function in Rust:

```rust
extern "C" {
    fn printf(format: *const u8);
}

fn main() {
    unsafe {
        printf("Hello, FFI!\0".as_ptr());
    }
}
```

In this example:
- We declare a C function `printf` using `extern "C"`.
- We call it in an unsafe block, because we are interfacing with an external language.



## ⚡ Unsafe and Performance  

Unsafe Rust is often used for performance optimizations, particularly in situations where the overhead of Rust’s safety checks is too high. By using raw pointers, unchecked mutable references, and bypassing ownership and borrowing rules, you can optimize critical sections of your code.

While it’s possible to write code that’s both safe and fast, there are cases where unsafe operations are necessary to achieve the best performance.

### Example: Avoiding Redundant Memory Allocations

In Rust, memory allocations are tracked and managed by the ownership system. However, there are cases where unsafe code allows you to manually manage memory, avoiding some allocations and making performance improvements.

Unsafe Rust enables optimizations by bypassing runtime checks, allowing you to:  
- Avoid redundant memory allocations.  
- Directly manipulate memory.  

#### Example: Manual Memory Management  
```rust
use std::ptr;

unsafe {
    let mut vec: Vec<i32> = Vec::new();
    let ptr = vec.as_mut_ptr();

    // Manual memory management using raw pointers
    ptr::write(ptr, 42); // Write to raw pointer directly
}
```

### Risks:  
- Undefined behavior.  
- Hard-to-debug memory issues.  

Always encapsulate unsafe code in safe abstractions.  

While this can lead to performance gains, it is important to

 note that manual memory management introduces the possibility of bugs like double frees or memory leaks.

## 📖 Real-World Example: Interfacing with C Libraries

Let’s create an example where we call a C function from a Rust program. We’ll use the `libc` crate, which provides bindings to C standard libraries.

Add the `libc` crate to your `Cargo.toml`:

```toml
[dependencies]
libc = "0.2"
```

Here’s an example that uses `libc` to call the C function `printf`:

```rust
extern crate libc;

use libc::printf;

fn main() {
    unsafe {
        printf(b"Hello from C!\0".as_ptr() as *const i8);
    }
}
```

This shows how you can use **unsafe Rust** to interact with C libraries and functions.


## **⚡ Practical Examples and Code Walkthroughs**  

- **Memory-mapped I/O** for embedded systems.  
- **Low-level optimizations** like fine-tuned performance enhancements in video game engines.  
- **Direct interfacing with hardware** in OS development.  


## **⚡ Tips for Using Unsafe Rust**

1. **Minimize Unsafe Code**: Keep unsafe blocks small and isolated.
2. **Encapsulate Unsafe Code**: Use safe abstractions to hide unsafe details from the user.
3. **Document Assumptions**: Clearly state any invariants or conditions required for your unsafe code to work correctly.
4. **Test Thoroughly**: Unsafe code requires rigorous testing to prevent undefined behavior.

## **Benefits and Risks**

### **Benefits:**
- Access to low-level system operations.
- Better control over performance-critical sections of code.

### **Risks:**
- Potential for undefined behavior.
- Data races and memory safety issues.
- Hard-to-debug errors.

## 🚀 Hands-On Challenge  

### 1. **Exploring Unsafe Rust**  

1. **Create a Raw Pointer**: Write a program that demonstrates the creation and dereferencing of raw pointers.  
2. **Modify Immutable Data**: Use `unsafe` to modify data declared as immutable.  
3. **Call Unsafe Functions**: Define and call an unsafe function within a safe block.  

**Example Code:**  
```rust
fn main() {
    let x = 42;
    let r = &x as *const i32; // Raw pointer to immutable data
    let mut y = 42;
    let rw = &mut y as *mut i32; // Raw pointer to mutable data

    unsafe {
        println!("Raw pointer value: {}", *r);
        *rw += 1;
        println!("Modified value: {}", *rw);
    }
}
```



### 2. **Working with Unsafe Blocks**  

- Create a struct containing private fields and implement a function to access and modify the fields using unsafe code.  



### 3. **Unsafe Traits and Abstractions**  

1. **Unsafe Traits**:  
   - Implement a custom unsafe trait and a type that implements the trait.  
2. **FFI (Foreign Function Interface)**:  
   - Call a C function from Rust using `extern "C"`.  

**Example Code:**  
```rust
extern "C" {
    fn abs(input: i32) -> i32;
}

fn main() {
    let num = -10;
    unsafe {
        println!("Absolute value of {}: {}", num, abs(num));
    }
}
```



### 4. **Using `unsafe` for Optimizations**  

- Write a program that uses `unsafe` code to bypass bounds checking in arrays and measure the performance improvement.  



### 5. **Static Variables and Unsafe Code**  

- Demonstrate the use of `static mut` for global mutable variables with proper synchronization using unsafe blocks.  



## 💻 Exercises - Day 20  

### ✅ Exercise: Level 1  

1. Use a raw pointer to read and modify data.  
2. Implement a function using unsafe code to access elements in an array without bounds checking.  
3. Create a program that demonstrates the use of an unsafe block for typecasting between incompatible types.  

### 🚀 Exercise: Level 2  

1. **Custom Memory Allocator**:  
   - Write a simple custom memory allocator using `std::alloc` and `unsafe`.  

2. **Interfacing with C**:  
   - Create a Rust program that calls a simple C function to add two numbers.  

3. **Simulating a Data Race**:  
   - Write a program that simulates a data race using `static mut` variables and fix it using proper synchronization.  



## 🎥 Helpful Video References  

- [Understanding Unsafe Rust](https://www.youtube.com/watch?v=z_RekEdKcfk)  
- [FFI in Rust](https://www.youtube.com/watch?v=5xkc6dVJ0YU)  
- [Rust Memory Safety and Unsafe](https://www.youtube.com/watch?v=9E2v8pCUc48)  

## **📝 Day 20 Summary**  

Today, we learned about **Unsafe Rust**, which gives us the flexibility to perform low-level operations that are usually disallowed by Rust’s safety system. We covered the core operations of Unsafe Rust, learned how to use raw pointers, unsafe functions, mutable statics, unsafe traits, and unions. The challenge is to balance control with safety—**use with care**!

Using `unsafe` Rust gives you access to powerful low-level operations that are otherwise restricted. While these superpowers are essential for certain scenarios, they should be used sparingly and responsibly. Always prefer safe Rust wherever possible, and encapsulate unsafe blocks in safe abstractions to minimize risks.


### **🔥 Key Takeaways**:  
- Unsafe Rust gives you power and flexibility but requires responsibility.  
- Use **unsafe blocks** to encapsulate risky operations.  
- Always strive to write safe abstractions around unsafe code.


Stay tuned for **Day 20**, where we will explore **Rust Lifetimes** in Rust! 🚀

🌟 _Great job on completing Day 20! Keep practicing, and get ready for Day 21!_

Thank you for joining **Day 20** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 19](../19_Networking/19_networking.md) | [Day 21 >>](../21_Rust%20Lifetimes/21_rust_lifetimes.md)

---
