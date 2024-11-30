<div align="center">
  <h1>🦀 30 Days of Rust: Day 21 - Building CLI Applications 🛠️</h1>
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

[<< Day 21](../21_Rust%20Lifetimes/21_rust_lifetimes.md) | [Day 23 >>](../23_Web%20Development/23_web_development.md)  

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)

- [📘 Day 22 - Building CLI Applications](#-day-22---building-cli-applications)
  - [👋 Welcome](#-welcome)  
  - [🔍 Overview](#-overview)  
  - [🛠 CLI Applications: The Basics](#-cli-applications-the-basics)  
    - [💻 A Simple CLI Application](#-a-simple-cli-application)
  - [📦 Using `clap` for Command-Line Parsing](#-using-clap-for-command-line-parsing)  
    - [🔤 Basic Parsing with `clap`](#-basic-parsing-with-clap)  
    - [➕ Adding Subcommands](#-adding-subcommands)  
    - [⚙️ Customizing CLI Help](#-customizing-cli-help)  
  - [🔄 Handling Environment Variables](#-handling-environment-variables)  
    - [📑 Reading Environment Variables](#-reading-environment-variables)  
    - [🔧 Setting Environment Variables](#-setting-environment-variables)  
  - [📂 File and Directory Operations](#-file-and-directory-operations)  
    - [📄 Reading a File](#-reading-a-file)  
    - [✏️ Writing to a File](#-writing-to-a-file)  
    - [📂 Listing Directory Contents](#-listing-directory-contents)  
  - [🌟 Building a Full CLI Application: Example](#-building-a-full-cli-application-example)
  - [🌟 Additional Topics](#-additional-topic)  
    - [🖥️ Creating a Basic CLI Application](#%EF%B8%8F-creating-a-basic-cli-application)  
    - [🔤 Parsing Command-Line Arguments](#-parsing-command-line-arguments)  
    - [🛒 Advanced Command Parsing with `clap`](#-advanced-command-parsing-with-clap)  
    - [⚠️ Handling Errors Gracefully](#-handling-errors-gracefully)  
    - [🔨 Creating Subcommands](#-creating-subcommands)  
    - [💬 Input/Output Handling](#-inputoutput-handling)  
    - [📁 Working with Files and Directories](#-working-with-files-and-directories)  
    - [🌈 Customizing Output with Colors](#-customizing-output-with-colors)  
    - [🌍 Environment Variables](#-environment-variables)  
    - [🐞 Logging and Debugging](#-logging-and-debugging)
    - [🧪 Testing CLI Applications](#-testing-cli-applications)
    - [📦 Distributing Your CLI Application](#-distributing-your-cli-application)
  - [🚀 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 22](#-exercises---day-22)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [🚀 Exercise: Level 2](#-exercise-level-2)
    - [🏆 Exercise: Level 3 (Advanced)](#-exercise-level-3-advanced)
  - [🎥 Helpful Video References](#-helpful-video-references)
  - [📚 Further Reading](#-further-reading)
  - [📝 Day 22 Summary](#-day-22-summary)




# 📘 Day 22 - Building CLI Applications

## 👋 Welcome  

Welcome to **Day 22** of the **30 Days of Rust Challenge**! 🎉  

Today’s focus is on **building CLI (Command-Line Interface) applications** with Rust. CLI applications are foundational tools in software development, enabling developers to perform tasks, automate workflows, and interact with systems efficiently.

By the end of today’s lesson, you will:  
- Understand how to create **CLI applications** in Rust.  
- Use the `clap` crate to handle **command-line arguments** and subcommands.  
- Learn to manage **environment variables** in CLI applications.  
- Work with **file and directory operations** in the context of CLI tools.  
- Build a **real-world example** of a CLI tool.  

Let’s dive into crafting powerful and efficient CLI tools with Rust! 🚀  


## 🔍 Overview  

Rust is an excellent language for building **CLI applications** because of its:  
- **Speed**: Rust’s compiled nature ensures fast execution.  
- **Safety**: Rust’s memory safety guarantees prevent crashes.  
- **Ecosystem**: Crates like `clap`, `env_logger`, and `serde` simplify CLI development.  

CLI applications often need to handle:  
- Parsing **command-line arguments** and options.  
- Working with **files and directories**.  
- Managing **environment variables**.  

Rust provides robust libraries to make these tasks efficient and intuitive.


## 🛠 CLI Applications: The Basics  

Before diving into advanced features, let’s explore the basics of creating a CLI tool.  

## 💻 A Simple CLI Application  

Here’s an example of a basic CLI app that prints arguments:  

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    println!("Arguments: {:?}", args);
}
```

In this example:  
- `env::args()` retrieves the command-line arguments as an iterator.  
- We collect them into a `Vec<String>` for processing.  

Run this program with different arguments:  

```sh
$ cargo run -- arg1 arg2 arg3
Arguments: ["target/debug/cli_app", "arg1", "arg2", "arg3"]
```



## 📦 Using `clap` for Command-Line Parsing  

The [`clap`](https://crates.io/crates/clap) crate is the most popular library for building powerful CLI tools in Rust. It provides:  
- Argument parsing.  
- Subcommand support.  
- Automatic help generation.  

Add `clap` to your `Cargo.toml`:  

```toml
[dependencies]
clap = { version = "4.3", features = ["derive"] }
```

## 🔤 Basic Parsing with `clap`  

Here’s a simple example with `clap`:  

```rust
use clap::Parser;

#[derive(Parser)]
struct Cli {
    /// The name to greet
    name: String,
    /// Number of times to greet
    #[clap(short, long, default_value_t = 1)]
    count: u32,
}

fn main() {
    let args = Cli::parse();

    for _ in 0..args.count {
        println!("Hello, {}!", args.name);
    }
}
```

Run this CLI tool:  

```sh
$ cargo run -- John --count 3
Hello, John!
Hello, John!
Hello, John!
```

## ➕ Adding Subcommands  

Subcommands allow you to organize functionality.  

```rust
use clap::{Parser, Subcommand};

#[derive(Parser)]
struct Cli {
    #[clap(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Say hello
    Hello {
        /// The name to greet
        name: String,
    },
    /// Say goodbye
    Goodbye {
        /// The name to bid farewell
        name: String,
    },
}

fn main() {
    let cli = Cli::parse();

    match &cli.command {
        Commands::Hello { name } => println!("Hello, {}!", name),
        Commands::Goodbye { name } => println!("Goodbye, {}!", name),
    }
}
```

## ⚙ Customizing CLI Help 

You can customize the help message for your CLI application:  

```rust
use clap::{Parser, Command};

#[derive(Parser)]
#[clap(author, version, about, long_about = "A detailed CLI app to greet users.")]
struct Cli {
    name: String,
}

fn main() {
    let args = Cli::parse();
    println!("Hello, {}!", args.name);
}
```



## 🔄 Handling Environment Variables  

Environment variables are key-value pairs that can influence the behavior of a CLI tool. Use Rust’s `std::env` module to work with them.  

## 📑 Reading Environment Variables

```rust
use std::env;

fn main() {
    if let Ok(value) = env::var("MY_ENV_VAR") {
        println!("Environment variable value: {}", value);
    } else {
        println!("MY_ENV_VAR is not set.");
    }
}
```

## 🔧 Setting Environment Variables   

Use the `std::env::set_var` function:  

```rust
use std::env;

fn main() {
    env::set_var("MY_ENV_VAR", "RustLang");
    println!("MY_ENV_VAR: {}", env::var("MY_ENV_VAR").unwrap());
}
```



## 📂 File and Directory Operations  

File and directory management is essential for many CLI applications. Use Rust’s `std::fs` module to handle file operations.  

## 📄 Reading a File

```rust
use std::fs;

fn main() {
    let content = fs::read_to_string("example.txt").expect("Failed to read file");
    println!("File Content:\n{}", content);
}
```

## ✏ Writing to a File 

```rust
use std::fs;

fn main() {
    let data = "Hello, CLI!";
    fs::write("output.txt", data).expect("Failed to write file");
    println!("Data written to output.txt");
}
```

## 📂 Listing Directory Contents 

```rust
use std::fs;

fn main() {
    let entries = fs::read_dir(".").expect("Failed to read directory");
    for entry in entries {
        let entry = entry.expect("Invalid entry");
        println!("{}", entry.file_name().to_string_lossy());
    }
}
```



## 🌟 Building a Full CLI Application: Example  

Let’s build a CLI tool called `filetool` that:  
1. Accepts a filename.  
2. Reads and prints its content.  
3. Allows writing to the file.  

### Complete Code  

```rust
use clap::{Parser, Subcommand};
use std::fs;

#[derive(Parser)]
#[clap(author, version, about)]
struct Cli {
    #[clap(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Read a file
    Read {
        /// File to read
        filename: String,
    },
    /// Write to a file
    Write {
        /// File to write to
        filename: String,
        /// Content to write
        content: String,
    },
}

fn main() {
    let cli = Cli::parse();

    match &cli.command {
        Commands::Read { filename } => {
            let content = fs::read_to_string(filename).expect("Failed to read file");
            println!("File Content:\n{}", content);
        }
        Commands::Write { filename, content } => {
            fs::write(filename, content).expect("Failed to write to file");
            println!("

Content written to {}", filename);
        }
    }
}
```

Run this tool:  

```sh
$ cargo run -- read example.txt
$ cargo run -- write example.txt "Hello, Rust CLI!"
```

## 🌟 Additional Topic
In this extended guide, we will cover the full spectrum of CLI app development in Rust, from basic command parsing to creating robust, interactive CLI tools. Whether you're building utilities, automation tools, or something more complex, Rust’s CLI ecosystem has everything you need.

### **What We’ll Cover Today**:

1. **🖥️ Creating a Basic CLI Application**  
2. **🔤 Parsing Command-Line Arguments**  
3. **🛒 Advanced Command Parsing with `clap`**  
4. **⚠ Handling Errors Gracefully**  
5. **🔨 Creating Subcommands**  
6. **💬 Input/Output Handling**  
7. **📁 Working with Files and Directories**  
8. **🌈 Customizing Output with Colors**  
9. **🌍 Environment Variables**  
10. **🐞 Logging and Debugging**  
11. **🧪 Testing CLI Applications**  
12. **📦 Distributing Your CLI Application**



## **🖥️ Creating a Basic CLI Application**

A basic CLI application in Rust can be created easily by defining a `main()` function. Let's start simple:

```rust
fn main() {
    println!("Hello, CLI world!");
}
```

You can compile and run this with:

```bash
cargo run
```

This prints the message `"Hello, CLI world!"`. The next steps will involve parsing arguments and adding logic to make this application interactive.



## **🔤 Parsing Command-Line Arguments** 

Rust’s standard library provides a simple way to access command-line arguments with `std::env::args()`. But for more sophisticated CLI applications, a library like `clap` is often used for better flexibility and usability.

#### Basic Argument Parsing with `std::env::args()`

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    
    if args.len() > 1 {
        println!("Hello, {}!", args[1]);
    } else {
        println!("Hello, World!");
    }
}
```

- The program accepts the name as an argument and greets the user by name.



## **🛒 Advanced Command Parsing with `clap`** 

Rust’s **`clap`** crate is essential for building feature-rich and user-friendly CLI apps. It helps you parse arguments, display help messages, and handle subcommands efficiently.

#### Adding `clap` to `Cargo.toml`

```toml
[dependencies]
clap = "3.0"
```

#### Example: Building a Basic CLI with `clap`

```rust
use clap::{Arg, Command};

fn main() {
    let matches = Command::new("greet_cli")
        .version("1.0")
        .author("Your Name")
        .about("A simple greeting CLI")
        .arg(
            Arg::new("name")
                .short('n')
                .long("name")
                .takes_value(true)
                .help("Your name to greet"),
        )
        .get_matches();

    if let Some(name) = matches.value_of("name") {
        println!("Hello, {}!", name);
    } else {
        println!("Hello, World!");
    }
}
```

This example introduces:

- **`Command`**: Main entry point for your CLI.
- **`Arg`**: Defines a command-line argument.
- **`.get_matches()`**: Processes the arguments.

#### Run the app:

```bash
cargo run -- --name Alice
```

Output: `Hello, Alice!`



## **⚠ Handling Errors Gracefully**

Handling errors properly is crucial for a reliable CLI. Rust provides `Result` and `Option` for error handling. 

#### Basic Error Handling

You can handle missing arguments or invalid inputs gracefully. Here’s how you can improve the previous example with error handling:

```rust
use clap::{Arg, Command};
use std::process;

fn main() {
    let matches = Command::new("greet_cli")
        .version("1.0")
        .author("Your Name")
        .about("A simple greeting CLI")
        .arg(
            Arg::new("name")
                .short('n')
                .long("name")
                .takes_value(true)
                .help("Your name to greet"),
        )
        .get_matches();

    match matches.value_of("name") {
        Some(name) => println!("Hello, {}!", name),
        None => {
            eprintln!("Error: Missing required argument --name");
            process::exit(1);
        }
    }
}
```

- **`eprintln!()`**: Prints errors to `stderr`.
- **`process::exit(1)`**: Exits with a non-zero exit code.

#### Handling Multiple Errors:

Rust also offers error chaining with `Result` for complex applications. For example, when working with files or external resources, use `Result` to propagate errors.



## **🔨 Creating Subcommands**

In real-world CLI tools, you often need subcommands (like `git commit`, `git push`, etc.). `clap` handles this elegantly.

#### Example: CLI with Subcommands

```rust
use clap::{Arg, Command};

fn main() {
    let matches = Command::new("cli_tool")
        .subcommand(
            Command::new("add")
                .about("Adds a new task")
                .arg(Arg::new("task").required(true).help("Task to add")),
        )
        .subcommand(Command::new("list").about("Lists all tasks"))
        .get_matches();

    match matches.subcommand() {
        Some(("add", sub_matches)) => {
            let task = sub_matches.value_of("task").unwrap();
            println!("Task added: {}", task);
        }
        Some(("list", _)) => {
            println!("Listing all tasks...");
        }
        _ => {
            eprintln!("Error: Invalid subcommand");
            std::process::exit(1);
        }
    }
}
```

- **`subcommand`**: Defines subcommands (like `add`, `list`).
- **`.subcommand()`**: Checks which subcommand was used.



## **💬 Input/Output Handling**

Handling user input and formatting output is key for good CLI experiences. You can use Rust's standard input/output mechanisms (`std::io`) or leverage crates for advanced formatting.

#### Reading User Input

```rust
use std::io::{self, Write};

fn main() {
    print!("Enter your name: ");
    io::stdout().flush().unwrap(); // flush to ensure prompt appears

    let mut name = String::new();
    io::stdin().read_line(&mut name).unwrap();

    println!("Hello, {}!", name.trim());
}
```

- **`flush()`**: Ensures the prompt appears before reading input.
- **`read_line()`**: Reads user input.



## **📁 Working with Files and Directories** 

A lot of CLI applications involve file handling, like reading and writing files, managing directories, etc. Rust’s standard library, along with crates like `std::fs`, provides robust file handling.

#### Example: Reading/Writing to Files

```rust
use std::fs::{self, OpenOptions};
use std::io::{self, Write};

fn main() -> io::Result<()> {
    let file_path = "tasks.txt";

    // Write to a file
    let mut file = OpenOptions::new().append(true).create(true).open(file_path)?;
    writeln!(file, "New task")?;

    // Read the file
    let contents = fs::read_to_string(file_path)?;
    println!("File contents: \n{}", contents);

    Ok(())
}
```

- **`fs::read_to_string()`**: Reads the contents of a file into a string.
- **`OpenOptions`**: Allows opening a file in append mode.



## **🌈 Customizing Output with Colors**

CLI applications benefit from color-coded output for readability. The `colored` crate allows you to style your terminal output with ease.

#### Example: Colorizing Output

Add `colored` to your `Cargo.toml`:

```toml
[dependencies]
colored = "2.0"
```

Then in your code:

```rust
use colored::*;

fn main() {
    println!("{}", "Hello, world!".green());
    println!("{}", "Error: Something went wrong.".red());
}
```

- **`.green()`**, **`.red()`**: Apply color to text.



## **🌍 Environment Variables** 

CLI tools often need environment variables for configuration. Rust provides `std::env::var()` to access them.

#### Example: Using Environment Variables

```rust
use std::env;

fn main() {
    match env::var("MY_CONFIG") {
        Ok(val) => println!("The config value is: {}", val),
        Err(_) => eprintln!("Error: MY_CONFIG is not set"),
    }
}
```

- **`env::var()`**: Retrieves environment variable values.



## **🐞 Logging and Debugging** 

Logging is critical for debugging and monitoring. The `log` and `env_logger` crates allow you to output logs based on various levels (e.g., `info`, `debug`, `error`).

#### Example: Using `log` and `env_logger`

Add dependencies to `Cargo.toml`:

```toml
[dependencies]
log = "0.4"
env_logger = "0.10"
```



Then in the code:

```rust
use log::{info, error};
use env_logger;

fn main() {
    env_logger::init();
    info!("This is an info log");
    error!("This is an error log");
}
```



## **🧪 Testing CLI Applications** 

Testing CLI apps can be tricky, but Rust’s built-in test framework makes it possible. You can run tests that simulate running commands and parsing their outputs.

#### Example: Testing CLI

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_greeting() {
        let output = std::process::Command::new("./target/debug/cli_tool")
            .arg("--name")
            .arg("Alice")
            .output()
            .expect("Failed to execute command");

        assert_eq!(String::from_utf8_lossy(&output.stdout), "Hello, Alice!\n");
    }
}
```



## **📦 Distributing Your CLI Application** 

To distribute your Rust CLI app, you can compile it for various platforms and publish it to **crates.io** or package it as a binary.

#### Build for a Specific Target

```bash
cargo build --release --target=x86_64-unknown-linux-gnu
```

- **`--release`**: Builds the project in release mode for better performance.



### **Conclusion**

In this comprehensive guide, we’ve covered everything from basic CLI applications in Rust to advanced features such as error handling, subcommands, file manipulation, and testing. Rust’s powerful ecosystem, combined with libraries like `clap`, `serde`, and `colored`, make it an excellent choice for building CLI tools that are both fast and reliable.



## 🚀 Hands-On Challenge  

1. Build a CLI tool that:  
   - Accepts a directory path as input.  
   - Lists all files and directories within it.  
   - Optionally filters results by file type.  
2. Extend the `filetool` example to support file deletion with a `delete` subcommand.  

## 💻 Exercises - Day 22

## ✅ Exercise: Level 1

1. **Create a Basic CLI Application**:  
   - Build a simple CLI application that accepts a user’s name as input and prints a greeting message.  
   - Use `clap` to parse a single argument for the user’s name.

2. **Handle Flags and Options**:  
   - Enhance the CLI app by adding a flag `--uppercase` that, if provided, prints the greeting in uppercase.

3. **Use Environment Variables**:  
   - Modify the CLI app to accept an environment variable `USER_NAME`. If this variable is set, use it to greet the user instead of the command-line input.

## 🚀 Exercise: Level 2

1. **Add Multiple Subcommands**:  
   - Create a CLI application that accepts multiple subcommands, such as `greet` and `farewell`.
   - Each subcommand should take an argument (e.g., name) and print a greeting or farewell message accordingly.

2. **File Operations**:  
   - Implement a subcommand `save` that writes the greeting message to a text file.  
   - The file name should be passed as an argument.

3. **Implement a Help Option**:  
   - Add a global `--help` option that prints detailed usage instructions for each subcommand.

## 🏆 Exercise: Level 3 (Advanced)

1. **Building a To-Do CLI Application**:  
   - Create a more complex CLI application that allows the user to manage a to-do list.  
   - Use `clap` to add subcommands like `add`, `list`, and `remove` to manage the to-do items.  
   - Store the to-do list in a file, ensuring it persists between program runs.

2. **Use `serde` for JSON Handling**:  
   - Modify the to-do app to serialize and deserialize to-do items using the `serde` crate.  
   - Allow users to save the list to a JSON file and load it back.

3. **Integrate Logging**:  
   - Add logging functionality using the `log` crate and print logs during the execution of the app. Ensure the logs are visible when running the app with a `--verbose` flag.

## 🎥 Helpful Video References

- [Building CLI Applications in Rust](https://youtu.be/4km2UijVC3M?si=bOC54E0aeW4Iwx_m)
- [Rust `clap` crate tutorial](https://www.youtube.com/watch?v=Ot3qCA3Iv_8)
- [Advanced CLI Application Features](https://www.youtube.com/watch?v=XYkiwsplDTg)

## 📚 Further Reading

#### 📘 Official `clap` Documentation

For in-depth details and usage examples, check out the official `clap` crate documentation:
- [Clap Documentation](https://docs.rs/clap/latest/clap/)

#### 🔍 Command-Line Application Design Best Practices

Learn how to design intuitive and efficient CLI applications:
- [Best Practices for CLI Apps](https://betterprogramming.pub/building-cli-apps-in-rust-what-you-should-consider-99cdcc67710c)

#### 🌍 Environment Variables: A Deeper Dive

Explore advanced usage of environment variables in Rust applications:
- [Environment Variables in Rust](https://doc.rust-lang.org/book/ch12-05-working-with-environment-variables.html)


## 📝 Day 22 Summary  

Today, you learned how to:  
- Build CLI applications with Rust.  
- Use `clap` for parsing command-line arguments and creating subcommands.  
- Handle environment variables for customization.  
- Work with files and directories in Rust.  

CLI tools are a cornerstone of efficient workflows, and Rust’s ecosystem makes building them a joy. Continue experimenting with more advanced CLI features to deepen your knowledge.  


Stay tuned for **Day 23**, where we will explore **Web Development in Rust** in Rust! 🚀

🌟 _Great job on completing Day 22! Keep practicing, and get ready for Day 23!_

Thank you for joining **Day 22** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 21](../21_Rust%20Lifetimes/21_rust_lifetimes.md) | [Day 23 >>](../23_Web%20Development/23_web_development.md)  

---
