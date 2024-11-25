<div align="center">
  <h1>🦀 30 Days Of Rust: Day 16 - File Handling in Rust 📁</h1>
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

[<< Day 15](../15_Macros/15_macros.md) | [Day 17 >>](../17_Concurrency/17_concurrency.md)

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)


- [📘 Day 16 - File Handling in Rust](#-day-16---file-handling-in-rust)
  - [👋 Welcome](#-welcome)
  - [🔍 Overview](#-overview)
  - [🛠 Environment Setup](#-environment-setup)
  - [📂 Basics of File I/O in Rust](#-basics-of-file-io-in-rust)
    - [📜 Opening a File](#-opening-a-file)
    - [📖 Reading from a File](#-reading-from-a-file)
    - [✍ Writing to a File](#-writing-to-a-file)
    - [📎 Appending to a File](#-appending-to-a-file)
    - [🗑 Removing a File](#-removing-a-file)
  - [⚠ Example for Error Handling](#-example-for-error-handling)
  - [🚀 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 16](#-exercises---day-16)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [🚀 Exercise: Level 2](#-exercise-level-2)
  - [🎥 Helpful Video References](#-helpful-video-references)
  - [📝 Day 16 Summary](#-day-16-summary)



# 📘 Day 16 - File Handling in Rust

## 👋 Welcome

Welcome to **Day 16** of the 30 Days of Rust challenge! 🎉 Today, we’ll explore **File Handling** in Rust, an essential aspect of most software applications. You’ll learn how to work with files—reading, writing, appending, and deleting. 🛠️

Join the [30 Days of Rust](https://discord.gg/dy4gAhng) community on Discord for discussions, questions, and to share your learning journey! 🚀

## 🔍 Overview

File handling allows programs to interact with files stored on disk. In Rust, file handling is achieved through the **`std::fs`** module. You'll learn how to:

1. Open files for reading or writing.
2. Read contents from files.
3. Write data to files.
4. Append data to existing files.
5. Delete files.

By the end of this lesson, you’ll have practical knowledge of handling files in Rust, complete with examples and outputs!

## 🛠 Environment Setup

If you have already set up your Rust environment on **Day 1**, you’re good to go! Otherwise, check out the [Environment Setup](../README.md#-environment-setup) section for detailed instructions. Ensure you have **Cargo** installed by running:

```bash
$ cargo --version
```

If you see a version number, you’re all set! 🎉

## 📂 Basics of File I/O in Rust

File I/O operations in Rust use the `std::fs` and `std::io` modules. The key structures and methods include:

- **`File`**: Represents a file.
- **`OpenOptions`**: Used to configure how files are opened.
- **`fs` methods**: Provide high-level file manipulation options.

Let’s explore each operation step-by-step.

## 📜 Opening a File

To open a file, use the `File::open` method. This requires the file to exist; otherwise, it returns an error.

#### Example:

```rust
use std::fs::File;

fn main() -> std::io::Result<()> {
    let file = File::open("example.txt")?;
    println!("File opened successfully: {:?}", file);
    Ok(())
}
```

#### Output:

If the file exists:

```
File opened successfully: File { fd: 3, path: "example.txt", read: true, write: false }
```

If the file does not exist:

```
Error: No such file or directory (os error 2)
```

### <div align="center">_*or*_</div>

```rust
use std::fs::File;

fn main() {
    let data_result = File::open("output.txt");
    let data_file = match data_result {
        Ok(file) => file,
        Err(error) => panic!("Problem opening the data file: {:?}", error),
    };

    println!("Data file: {:?}", data_file);
}
```
#### Output:

```
Data file: File { fd: 3, path: "output.txt", read: true, write: false }
```
If the file does not exist:

```
Error: No such file or directory (os error 2)
```

## 📖 Reading from a File

The `File::read_to_string` method reads the entire contents of a file into a string.

#### Example:

```rust
use std::fs::File;
use std::io::Read;

fn main() -> std::io::Result<()> {
    let mut file = File::open("example.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    println!("File contents:\n{}", contents);
    Ok(())
}
```

#### Output:

For a file containing `Hello, Rustaceans!`:

```
File contents:
Hello, Rustaceans!
```

### <div align="center">_*or*_</div>

```rust
use std::fs::File;
use std::io::Read;

fn main() {
    let mut data_file = File::open("output.txt").unwrap();
    let mut file_content = String::new();
    data_file.read_to_string(&mut file_content).unwrap();
    println!("File content: {:?}", file_content);
}
```
#### Output:

```
File contents:
Hello, Rustaceans!
```

## ✍ Writing to a File

To write to a file, use `File::create`, which overwrites the file if it already exists.

#### Example:

```rust
use std::fs::File;
use std::io::Write;

fn main() -> std::io::Result<()> {
    let mut file = File::create("output.txt")?;
    file.write_all(b"Writing to a file in Rust!")?;
    println!("Data written to file.");
    Ok(())
}
```

#### Output:

File `output.txt` will contain:

```
Writing to a file in Rust!
```

### <div align="center">_*or*_</div>

```rust
use std::fs::File;
use std::io::Write;

fn main() {
    let mut data_file = File::create("output.txt").expect("creation fail");
    data_file.write("Hello, World!".as_bytes()).expect("write fail");
    println!("Created a file output.txt");
}
```
#### Output:

```
Created a file output.txt
```

## 📎 Appending to a File

To append data to a file without overwriting, use the `OpenOptions` struct.

#### Example:

```rust
use std::fs::OpenOptions;
use std::io::Write;

fn main() -> std::io::Result<()> {
    let mut file = OpenOptions::new()
        .append(true)
        .open("output.txt")?;
    file.write_all(b"\nAppending more data.")?;
    println!("Data appended to file.");
    Ok(())
}
```

#### Output:

File `output.txt` will now contain:

```
Writing to a file in Rust!
Appending more data.
```

### <div align="center">_*or*_</div>

```rust
use std::fs::OpenOptions;
use std::io::Write;

fn main() {
    let mut data_file = OpenOptions::new()
        .append(true)
        .open("output.txt")
        .expect("cannot open file");
    data_file
        .write("I am learning Rust!".as_bytes())
        .expect("write fail");

    println!("Appended content to a file");
}
```
#### Output:

```
Appended content to a file
```

## 🗑 Removing a File

To delete a file, use `std::fs::remove_file`.

#### Example:

```rust
use std::fs;

fn main() -> std::io::Result<()> {
    fs::remove_file("output.txt")?;
    println!("File deleted successfully.");
    Ok(())
}
```

#### Output:

```
File deleted successfully.
```

### <div align="center">_*or*_</div>

#### Example:

```rust
use std::fs;

fn main() {
    fs::remove_file("output.txt").expect("couldn't remove file");
    println!("Removed file output.txt");
}
```
#### Output:

```
Removed file output.txt
```

## ⚠ Example for Error Handling

Rust's error-handling mechanisms allow you to write robust programs. Below are some concepts and examples to help you understand how to handle errors effectively. 💡

| 🛠 **Concept**            | 📚 **Description**                                                        | 💻 **Example Code**                                   |
|---------------------------|---------------------------------------------------------------------------|------------------------------------------------------|
| **`Result` Enum**         | Represents success (`Ok`) or failure (`Err`).                             | `let result: Result<i32, String> = Ok(10);`         |
| **`unwrap` Method**       | Extracts the `Ok` value; panics on `Err`.                                 | `let value = result.unwrap();`                      |
| **`expect` Method**       | Similar to `unwrap`, but allows a custom panic message.                   | `let value = result.expect("Failed to unwrap!");`   |
| **`match` Expression**    | Pattern matching for fine-grained error handling.                         | `match result { Ok(v) => v, Err(e) => println!("{}", e) }` |

### 🌟 Code Example 1: Using `unwrap`

```rust
fn main() {
    let result: Result<i32, &str> = Ok(10);
    let value = result.unwrap();
    println!("Value: {}", value);
}
```

### 🌟 Code Example 2: Using `expect` with Custom Message

```rust
fn main() {
    let result: Result<i32, &str> = Err("Something went wrong");
    let value = result.expect("Custom panic message");
    println!("Value: {}", value);
}
```

### 🌟 Code Example 3: Handling Errors with `match`

```rust
fn main() {
    let result: Result<i32, &str> = Err("An error occurred");
    match result {
        Ok(value) => println!("Success: {}", value),
        Err(error) => println!("Error: {}", error),
    }
}
```

### 🌟 Code Example 4: Propagating Errors with `?`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_file() -> io::Result<String> {
    let mut file = File::open("example.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    Ok(contents)
}

fn main() {
    match read_file() {
        Ok(contents) => println!("File Contents: {}", contents),
        Err(error) => println!("Failed to read file: {}", error),
    }
}
```

## 🚀 Hands-On Challenge

1. **Read from a file and print its content line by line.**  
   Implement a function that opens a file and prints each line on the console.  

2. **Create and write to a new file.**  
   Write a program to create a new file and write user-input data into it. Use error handling to manage cases where the file cannot be created.

3. **Append data to an existing file.**  
   Extend your program to take additional input and append it to the same file, ensuring the existing content remains intact.

4. **Implement a log file system.**  
   Write a function to log custom messages into a file with a timestamp. Messages should include information, warnings, and errors.

5. **Delete a file securely.**  
   Add a function to your program that deletes a specified file only after confirming with the user.

Here’s an example for the first challenge:

```rust
use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("example.txt")?;
    let reader = BufReader::new(file);

    for (index, line) in reader.lines().enumerate() {
        println!("Line {}: {}", index + 1, line?);
    }
    Ok(())
}
```
### <div align="center">_*or*_</div>

1. Create a program to write a user-provided message into a file and then read it back.
2. Extend the program to append additional user-provided data to the same file.
3. Implement a function to check if the file exists before reading or writing.


## 💻 Exercises - Day 16

### ✅ Exercise: Level 1

1. Write a program that reads the content of a file and counts:
   - The number of lines.
   - The number of words.
   - The number of characters.

2. Create a function to write an array of integers to a file, one number per line.

3. Implement a program to:
   - Create a file named `example.txt`.
   - Write "Hello, Rust!" to the file.
   - Read the content and print it to the console.
     
### <div align="center">_*or*_</div>

1. Write a program to count the number of lines in a file.
2. Create a function to read a file and return its contents as a `String`.
3. Implement a program to write an array of strings to a file, one per line.


### 🚀 Exercise: Level 2

1. **Implement a file copy utility.**  
   Write a program to copy the contents of one file into another file, using efficient file I/O techniques.

2. **Create a reverse file reader.**  
   Read a file line by line and print its contents in reverse order (last line first).

3. **Develop a file encryption tool.**  
   Write a function to encrypt a file by replacing each character with its ASCII value + 1, and save the result in a new file.  
   Additionally, create a decrypt function.

4. **Build a logging system.**  
   Implement a simple logging system that writes logs to a file, categorizing them as:
   - INFO
   - WARNING
   - ERROR  
   Include timestamps with each log entry.


### Example Code for Exercise: Reverse File Reader

```rust
use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("example.txt")?;
    let reader = BufReader::new(file);
    let lines: Vec<_> = reader.lines().collect();

    for line in lines.into_iter().rev() {
        println!("{}", line?);
    }
    Ok(())
}
```
### <div align="center">_*or*_</div>

1. Build a mini logging system that appends log messages to a file with timestamps.
2. Create a program to read a file and output its contents in reverse order (line-by-line).
3. Develop a function to copy a file from one location to another.


## 🎥 Helpful Video References

- [Rust File Handling Basics](https://www.youtube.com/watch?v=JRWgzWWMeCs)
- [Advanced File I/O in Rust](https://www.youtube.com/watch?v=mkFFtO6WA8I)

## 📝 Day 16 Summary

Today, we explored **File Handling in Rust**, covering how to open, read, write, append, and delete files. By mastering these operations, you’re well-equipped to handle file-related tasks in your Rust projects.

Stay tuned for **Day 17**, where we will explore **Concurrency** in Rust! 🚀

🌟 _Great job on completing Day 16! Keep practicing, and get ready for Day 17!_

Thank you for joining **Day 16** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 15](../15_Macros/15_macros.md) | [Day 17 >>](../17_Concurrency/17_concurrency.md)

---
