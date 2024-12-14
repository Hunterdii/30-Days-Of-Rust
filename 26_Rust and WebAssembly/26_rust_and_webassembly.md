<div align="center">
  <h1>🦀 30 Days of Rust: Day 26 - Rust and WebAssembly 🌐</h1>
  <a href="https://www.linkedin.com/in/het-patel-8b110525a/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank">
    <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social" alt="LinkedIn" />
  </a>
  <a href="https://github.com/Hunterdii" target="_blank">
    <img src="https://img.shields.io/badge/Follow%20me%20on-GitHub-blue?style=flat-square&logo=github" alt="Follow me on GitHub" />
  </a>

<sub><h4><i>Author:
<a href="https://www.linkedin.com/in/het-patel-8b110525a/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank">Het Patel</a></h4></i>
<small> October, 2024</small>
</sub>

</div>

[<< Day 25](../25_Rust%20on%20Embedded%20Systems/25_rust_on_embedded_systems.md) | [Day 27 >>](../27_Graphics%20Programming%20with%20Rust/27_graphics_programming_with_rust.md)  

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)

- [📘 Day 26 - Rust and WebAssembly 🌐](#-day-26---rust-and-webassembly-)
  - [👋 Welcome](#-welcome)  
  - [🔍 What is WebAssembly?](#-what-is-webassembly)  
  - [🤔 Why Use Rust for WebAssembly?](#-why-use-rust-for-webassembly)  
  - [🛠 Setting Up Your Environment](#-setting-up-your-environment)  
    - [💻 Installing Rust](#-installing-rust)  
    - [⚙️ Installing wasm32-unknown-unknown Target](#%EF%B8%8F-installing-wasm32-unknown-unknown-target)  
    - [🔗 Installing wasm-pack](#-installing-wasm-pack)  
  - [⚡ Writing Your First WebAssembly Program](#-writing-your-first-webassembly-program)  
    - [1. Hello, WebAssembly!](#1-hello-webassembly)  
    - [2. Key Concepts](#2-key-concepts)  
  - [🧰 Tools and Frameworks for WebAssembly with Rust](#-tools-and-frameworks-for-webassembly-with-rust)  
  - [📊 Understanding Memory Management in WebAssembly](#-understanding-memory-management-in-webassembly)  
  - [🔗 Key Concepts in WebAssembly with Rust](#-key-concepts-in-webassembly-with-rust)  
    - [🚀 Wasm Bindgen](#-wasm-bindgen)  
    - [📟 WebAssembly Imports and Exports](#-webassembly-imports-and-exports)  
  - [📦 Starting a WebAssembly Project](#-starting-a-webassembly-project)  
    - [🛠️ Create a New Project](#️-create-a-new-project)  
    - [🛡️ Configure Your Target](#️-configure-your-target)  
    - [📤 Build and Bundle](#-build-and-bundle)  
  - [🔄 Essential Tools and Crates](#-essential-tools-and-crates)  
  - [💻 Example Project: WebAssembly in Action](#-example-project-webassembly-in-action)  
    - [🖊️ Writing the Code](#️-writing-the-code)  
    - [🚀 Running Your WebAssembly Code](#-running-your-webassembly-code)  
  - [🛡️ Debugging Tips](#-debugging-tips)
  - [🌐 Integrating WebAssembly with JavaScript](#-integrating-webassembly-with-javascript)  
    - [1. Exporting Functions](#1-exporting-functions)  
    - [2. Importing Functions](#2-importing-functions)  
  - [📊 Performance Optimization with WebAssembly](#-performance-optimization-with-webassembly)
  - [🎯 Hands-On Challenge](#-hands-on-challenge)   
  - [💻 Exercises - Day 26](#-exercises---day-26)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [🚀 Exercise: Level 2](#-exercise-level-2)
    - [🏆 Exercise: Level 3 (Advanced)](#-exercise-level-3-advanced)
  - [🎥 Helpful Video References](#-helpful-video-references)
  - [📚 Further Reading](#-further-reading)
  - [📝 Day 26 Summary](#-day-26-summary)

---

# 📘 Day 26 - Rust and WebAssembly 🌐  

Welcome to **Day 26** of the **30 Days of Rust Challenge**! 🎉  

Today, we explore **Rust and WebAssembly (Wasm)**—an exciting way to run Rust code in the browser or on the web. With WebAssembly, we can run Rust at near-native speed while ensuring the safety and concurrency features of Rust, making it ideal for building fast, secure, and cross-platform web applications.  

Let’s dive into WebAssembly with Rust! 🚀  

## 👋 Welcome  

Welcome to **Day 26** of the **30 Days of Rust Challenge**! 🎉  

Today, we’ll explore **WebAssembly (Wasm)**, which allows us to execute Rust code in web browsers, in serverless environments, or anywhere that WebAssembly is supported. We’ll focus on:  
- Setting up Rust for WebAssembly.
- Writing a simple WebAssembly program.
- Using key WebAssembly concepts in Rust.
- Using tools like `wasm-pack` and `wasm-bindgen`.

By the end of this lesson, you will:  
- Set up a Rust environment for WebAssembly development.
- Write and run a simple WebAssembly program using Rust.
- Understand WebAssembly’s memory management model and its key concepts.

  

## 🔍 What is WebAssembly?  

**WebAssembly (Wasm)** is a binary instruction format that allows code to be executed in web browsers or outside of them with near-native performance. It's designed to be fast, efficient, and portable.  

**Why use WebAssembly?**  
- **Performance**: WebAssembly runs at near-native speed because it is compiled to binary format.
- **Portability**: It can be executed in browsers, servers, and various platforms.
- **Language Agnostic**: WebAssembly supports multiple languages, but Rust shines due to its speed and memory safety.

**Common Use Cases of WebAssembly**  
- Running **high-performance applications** in the browser, like games, image editors, and video processing tools.
- **Serverless computing**: Run computations in isolated environments.
- **Cross-platform development**: Deploy applications across different platforms with minimal changes.

In short, WebAssembly makes it possible to run languages like C, C++, Rust, and others directly in the browser, enabling faster and more powerful web applications.

### Key Features:  
- **Fast execution**: Close to native performance.  
- **Language-agnostic**: Compile from multiple languages.  
- **Sandboxed**: Secure runtime environment.  

## 🤔 Why Use Rust for WebAssembly?

Rust is a systems programming language that is particularly well-suited for WebAssembly for several reasons:

1. **Performance**  
   Rust compiles to highly optimized machine code, which means that the code compiled into WebAssembly from Rust runs efficiently and quickly. WebAssembly takes advantage of this performance boost, so when you use Rust, you get the best performance possible in the browser.

2. **Memory Safety**  
   One of Rust’s biggest advantages is its focus on memory safety. In traditional low-level programming languages like C, memory management is done manually, which can lead to bugs and security vulnerabilities. Rust prevents these issues with its **ownership system**, which automatically ensures that memory is managed safely without relying on garbage collection. This is crucial in WebAssembly, where you manually manage memory in a more direct way.

3. **Concurrency**  
   Rust supports concurrency (running multiple things at once) without risking data races, which is important for creating fast, multi-threaded applications. This can be especially helpful in WebAssembly for applications that require high performance and smooth user experiences.

4. **Tooling**  
   Rust has an excellent toolchain for compiling to WebAssembly. Using tools like `wasm-pack`, it's easy to package and deploy Rust code as WebAssembly modules, enabling seamless integration with web technologies like JavaScript.

In summary, Rust is a great choice for WebAssembly because it provides high performance, memory safety, and excellent support for concurrent programming.



## 🛠 Setting Up Your Environment

Before you start building WebAssembly applications with Rust, you need to set up your development environment. Follow the steps below to get everything ready.

## 💻 Installing Rust

To use Rust, you first need to install it on your computer. Rust is installed through **rustup**, which is an installer and version management tool for Rust.

1. Open your terminal or command prompt.
2. Run the following command to download and install rustup:
   ```bash
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   ```
   This command will automatically download and install the Rust toolchain, including the **Rust compiler (`rustc`)** and the **Cargo package manager**.

3. Follow the on-screen instructions to complete the installation process. Once the installation is complete, you can verify it by running:
   ```bash
   rustc --version
   ```
   This command will display the version of Rust you’ve installed.

## ⚙️ Installing wasm32-unknown-unknown Target

Once Rust is installed, you need to add the WebAssembly target. This allows you to compile Rust code to WebAssembly. Follow these steps:

1. In your terminal, run the following command to add the WebAssembly target:
   ```bash
   rustup target add wasm32-unknown-unknown
   ```
   This command tells Rust to prepare the toolchain for compiling Rust to WebAssembly.

2. After this, you’ll be able to compile your Rust code for WebAssembly by specifying the target when you build your project.

## 🔗 Installing wasm-pack

`wasm-pack` is a tool that simplifies the process of building, packaging, and publishing WebAssembly modules generated from Rust. It handles the creation of WebAssembly packages that can be used directly in web applications.

To install `wasm-pack`, follow these steps:

1. Run the following command to install it using Cargo (Rust’s package manager):
   ```bash
   cargo install wasm-pack
   ```
   This command installs `wasm-pack` globally, so you can use it in any project.

2. After installation, you can verify it by checking its version:
   ```bash
   wasm-pack --version
   ```
   This will confirm that `wasm-pack` is installed and ready to use.

With `wasm-pack` installed, you can now build your Rust project into a WebAssembly module and generate the necessary bindings for JavaScript.




## 🤔 Why Use Rust for WebAssembly?  

Rust is an excellent choice for WebAssembly due to:  

| **Feature**                     | **Rust**                                      | **Other Languages**                      |  
|--|--|--|  
| **Performance**                  | Compiles to efficient WebAssembly code.       | Varies with other languages.             |  
| **Memory Safety**                | Safe by default with no garbage collection.   | May require manual memory management.    |  
| **Concurrency**                  | Fearless concurrency using ownership.        | Other languages may face challenges.     |  
| **Tooling**                       | Excellent tools for WebAssembly (e.g., `wasm-pack`, `wasm-bindgen`). | Not as seamless as Rust’s tooling.       |  

Rust’s **memory safety**, **performance**, and **tooling** make it an excellent match for WebAssembly, especially for resource-heavy applications like games and simulations.  


## 🛠 Setting Up Your Environment  

### 💻 Installing Rust  

Start by installing Rust with the **nightly toolchain** for WebAssembly support.  
```bash
rustup install nightly
rustup default nightly
rustup target add wasm32-unknown-unknown
```  

### ⚙️ Installing wasm32-unknown-unknown Target  

To build WebAssembly binaries, you need to install the `wasm32-unknown-unknown` target:  
```bash
rustup target add wasm32-unknown-unknown
```  

### 🔗 Installing wasm-pack  

`wasm-pack` is a tool for building and packaging WebAssembly projects.  
Install it via Cargo:  
```bash
cargo install wasm-pack
```  


## ⚡ Writing Your First WebAssembly Program  


#### 1. Hello, WebAssembly!

Writing your first WebAssembly program using Rust is easy! You just need a simple "Hello, World!" example to understand how everything comes together.

Here’s how to write a basic WebAssembly program with Rust:

1. **Create a new Rust project**  
   Start by creating a new Rust project with the following command:
   ```bash
   cargo new --lib hello-wasm
   cd hello-wasm
   ```
   This creates a new library project.

2. **Edit your `Cargo.toml` file**  
   To use `wasm-bindgen` (which helps Rust interact with JavaScript), add it as a dependency in your `Cargo.toml` file:
   ```toml
   [dependencies]
   wasm-bindgen = "0.2"
   ```

3. **Write the Rust code**  
   In the `src/lib.rs` file, write the following code:
   ```rust
   use wasm_bindgen::prelude::*;

   #[wasm_bindgen]
   pub fn greet() -> String {
       "Hello, WebAssembly!".to_string()
   }
   ```
   This code defines a simple function `greet` that returns a string. The `#[wasm_bindgen]` attribute is used to make Rust functions available for JavaScript.

4. **Build your WebAssembly module**  
   To compile your Rust code to WebAssembly, run:
   ```bash
   wasm-pack build --target web
   ```
   This will create a `pkg` directory with everything you need to use your Rust code in the web.

5. **Use your WebAssembly in a web app**  
   Once compiled, you can use the WebAssembly module in a JavaScript environment (e.g., in a browser). Import and call the function as shown in the example:
   ```javascript
   import { greet } from './pkg/hello_wasm.js';

   console.log(greet());  // Should print "Hello, WebAssembly!"
   ```

#### 2. Key Concepts

1. **`wasm-bindgen`**: This crate provides bindings to call Rust code from JavaScript, and vice versa.
2. **WebAssembly Imports/Exports**: Functions and data can be imported from or exported to the WebAssembly environment.  
   - Import: Java

Script → WebAssembly.
   - Export: WebAssembly → JavaScript.

To fully understand how WebAssembly works, you need to grasp some important concepts:

1. **WebAssembly Modules**  
   A WebAssembly module is the output of your Rust code after it’s compiled to WebAssembly. This module can be imported into JavaScript or used in any other environment that supports WebAssembly.

2. **wasm-bindgen**  
   This is a Rust crate (package) that allows you to communicate between Rust and JavaScript. It helps to expose Rust functions to JavaScript and vice versa.

3. **Imports and Exports**  
   WebAssembly has a concept of imports and exports. These allow you to share functions and data between WebAssembly and JavaScript. For example, your WebAssembly module can export functions that JavaScript can call, and it can also import JavaScript functions it needs.



## 🧰 Tools and Frameworks for WebAssembly with Rust

To make working with WebAssembly in Rust easier, there are several tools and frameworks available:

1. **wasm-pack**  
   This is the primary tool for building and packaging WebAssembly projects in Rust. It bundles everything you need to interact with JavaScript and handles all the configurations, including WebAssembly bindings.

2. **wasm-bindgen**  
   `wasm-bindgen` is essential when you need to bridge Rust with JavaScript. It allows you to write Rust functions and easily export them for use in web applications. It also allows JavaScript code to call Rust functions efficiently.

3. **yew**  
   Yew is a modern Rust framework for building multi-threaded front-end web apps using WebAssembly. It allows you to write fast, reliable, and highly concurrent web apps.

4. **stdweb**  
   Another library for creating WebAssembly projects in Rust is `stdweb`. It’s a more mature library and offers an easy-to-use interface to work with the web, but it’s slowly being replaced by `wasm-bindgen`.

5. **WebAssembly System Interface (WASI)**  
   WASI is an API that allows WebAssembly programs to run outside of the browser. It provides a way for WebAssembly to interact with files, networks, and more, which is great for non-browser applications.



## 📊 Understanding Memory Management in WebAssembly

Memory management is a critical concept in WebAssembly because WebAssembly code runs in a sandboxed environment, which doesn’t have direct access to the system’s memory like a normal program would.

1. **Linear Memory**  
   WebAssembly uses a system called **linear memory**, which means memory is allocated in a contiguous block, and it’s up to the program to manage this memory efficiently. WebAssembly has an array-like structure to store memory that grows as needed.

2. **Memory Management in Rust**  
   Rust’s memory management system, with its strict ownership and borrowing rules, aligns well with WebAssembly’s memory model. When you compile Rust to WebAssembly, you need to manually manage memory using `wasm-bindgen` for JavaScript interoperation. 

3. **Using the WebAssembly Memory API**  
   The WebAssembly `Memory` API allows you to interact with WebAssembly’s memory. For example, you can create a new memory block with a specified size, grow the memory dynamically, and access the memory from JavaScript.



## 🔗 Key Concepts in WebAssembly with Rust

## 🚀 Wasm Bindgen

**`wasm-bindgen`** is a tool and Rust crate that provides bindings for JavaScript and WebAssembly. It allows Rust functions to be easily accessed from JavaScript and vice versa. Here’s what it helps you do:

1. **Export Functions from Rust to JavaScript**  
   You can export Rust functions so they can be called directly from JavaScript.

2. **Pass Data Between Rust and JavaScript**  
   With `wasm-bindgen`, you can send data back and forth between Rust and JavaScript (e.g., strings, arrays, objects).

3. **Handle Complex Types**  
   You can pass complex types such as `Vec<T>`, `HashMap`, and other Rust data structures between Rust and JavaScript, with `wasm-bindgen` converting them to suitable JavaScript types.



## 📟 WebAssembly Imports and Exports

1. **Exports**  
   Exports in WebAssembly are functions, variables, or other items that a WebAssembly module makes available to be used outside its scope. For example, a Rust function might be exported so it can be called from JavaScript.

2. **Imports**  
   Imports are functions or resources that a WebAssembly module needs to access from the outside world, such as functions from JavaScript. These are used when you need to call JavaScript functions from your WebAssembly module, or access things like the DOM or network resources.

3. **Calling Imports and Exports**  
   In Rust, you typically use `wasm-bindgen` to handle imports and exports. For example, you might import a JavaScript function that updates the DOM, and in Rust, you would call that function by referencing it as an import.


## 📦 Starting a WebAssembly Project

Before diving into WebAssembly (Wasm) programming, let's go over how to set up and start a new project that can use WebAssembly. We'll start from creating a new Rust project, configuring it, and building it.

## 🛠️ Create a New Project

Creating a new Rust project for WebAssembly is very similar to creating a normal Rust project, with just a few extra steps to set it up for WebAssembly.

1. **Initialize a New Project**  
   First, create a new Rust project using the following command:
   ```bash
   cargo new --lib wasm_project
   cd wasm_project
   ```
   This creates a library project (i.e., a project that compiles into a `.rlib` or `.wasm` file) named `wasm_project`.

2. **Add WebAssembly Dependencies**  
   Next, you need to add WebAssembly-related dependencies in your `Cargo.toml`. The essential one is `wasm-bindgen`, which will help you work with JavaScript. Open `Cargo.toml` and add:
   ```toml
   [dependencies]
   wasm-bindgen = "0.2"
   ```

3. **Configure the Target**  
   Rust can compile to many different targets, but for WebAssembly, you need to specify a WebAssembly target.


## 🛡️ Configure Your Target

For your Rust code to be compiled into WebAssembly, you need to configure the WebAssembly target.

1. **Install WebAssembly Target**  
   The first step is to install the WebAssembly target for Rust. Run the following command in your terminal:
   ```bash
   rustup target add wasm32-unknown-unknown
   ```

2. **Ensure Your Project Uses the Target**  
   When you build the project, you'll need to specify the WebAssembly target. For example:
   ```bash
   cargo build --target wasm32-unknown-unknown
   ```

This command will compile the project into a `.wasm` file, which you can later use in a web environment.


## 📤 Build and Bundle

Once your project is set up and configured, it's time to build and bundle the project for WebAssembly.

1. **Build the WebAssembly Module**  
   To compile your project into WebAssembly, use:
   ```bash
   cargo build --target wasm32-unknown-unknown --release
   ```

2. **Bundle Using wasm-pack**  
   To make it easier to work with WebAssembly in the web, you can use `wasm-pack`. `wasm-pack` helps you package your Rust code into a format that is easier to use in JavaScript projects.
   Install `wasm-pack` if you don’t have it:
   ```bash
   cargo install wasm-pack
   ```

   Then, you can build and bundle your project:
   ```bash
   wasm-pack build --target web
   ```

This will create a `pkg/` directory with everything you need to use the WebAssembly module in a JavaScript or web app.


## 🔄 Essential Tools and Crates

Several tools and crates are essential when working with WebAssembly in Rust:

1. **wasm-pack**  
   `wasm-pack` is a command-line tool that builds, tests, and bundles your Rust code into WebAssembly. It simplifies the process of using Rust for web development.

2. **wasm-bindgen**  
   `wasm-bindgen` is crucial for making Rust functions available to JavaScript. It acts as a bridge, allowing you to call Rust functions from JavaScript and vice versa.

3. **wasm-bindgen-cli**  
   This is a command-line version of `wasm-bindgen` that makes it easier to generate the necessary JavaScript bindings when working with WebAssembly.

4. **stdweb**  
   `stdweb` is another crate for working with WebAssembly in Rust, providing web APIs to interact with the browser. However, it’s less commonly used now, with `wasm-bindgen` becoming the go-to solution.


## 💻 Example Project: WebAssembly in Action

Now, let's walk through a simple example project that demonstrates how to use Rust and WebAssembly in action. 

## 🖊️ Writing the Code

In this step, you'll write some Rust code that will be compiled to WebAssembly. For example, you can write a simple function that adds two numbers together:

```rust
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

This function is a simple addition function that takes two integers and returns their sum. The `#[wasm_bindgen]` attribute is used to make the function accessible to JavaScript.

## 🚀 Running Your WebAssembly Code

To run the WebAssembly code, you’ll need to set up an HTML and JavaScript file that interacts with the Rust code compiled to WebAssembly.

1. **Create an HTML file**  
   In your project, create an `index.html` file:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>WebAssembly with Rust</title>
   </head>
   <body>
       <h1>WebAssembly with Rust</h1>
       <button id="addButton">Add 5 and 7</button>
       <script type="module">
           import init, { add } from './pkg/wasm_project.js';

           async function run() {
               await init();
               document.getElementById("addButton").onclick = () => {
                   alert(add(5, 7));  // It should alert 12
               };
           }
           run();
       </script>
   </body>
   </html>
   ```

2. **Launch the Project**  
   To see it in action, run a simple local server or open it directly in a browser with WebAssembly support. The button on the page will trigger the addition operation, and you’ll see the result in an alert.


## 🛡 Debugging Tips

Debugging WebAssembly can sometimes be tricky. Here are a few tips:

1. **Use Console Logs in JavaScript**  
   You can use `console.log` in JavaScript to log the output of your WebAssembly functions and check if they behave as expected.

2. **Check the Browser Console for Errors**  
   Browsers with WebAssembly support (like Chrome or Firefox) will show detailed error messages in the JavaScript console if something goes wrong during execution.

3. **Use wasm-opt for Optimization**  
   If your WebAssembly module is too large or slow, consider using `wasm-opt` to optimize it. This tool reduces the size and improves the performance of WebAssembly modules.

## 🌐 Integrating WebAssembly with JavaScript  

### 1. Exporting Functions  

Use the compiled module in your web application:  

#### JavaScript Code (`index.js`):  
```javascript
import init, { greet } from './pkg/wasm_example.js';

async function run() {
    await init(); // Initialize the Wasm module
    console.log(greet("World"));
}

run();
```

### 2. Importing Functions  

Rust can also call JavaScript functions using `wasm-bindgen`.  

#### Add to `src/lib.rs`:  
```rust
use wasm_bindgen::prelude::*;

// Import a JavaScript alert function
#[wasm_bindgen]
extern "C" {
    fn alert(s: &str);
}

#[wasm_bindgen]
pub fn say_hello(name: &str) {
    alert(&format!("Hello, {}!", name));
}
```


## 📊 Performance Optimization with WebAssembly  

1. **Use the `wee_alloc` Crate**:  
   - Replace the default allocator with `wee_alloc` for smaller Wasm binaries.  

   Add to `Cargo.toml`:  
   ```toml
   [dependencies]
   wee_alloc = "0.4"
   ```

   Modify `lib.rs`:  
   ```rust
   #[global_allocator]
   static ALLOC: wee_alloc::WeeAlloc = wee_alloc::WeeAlloc::INIT;
   ```

2. **Avoid Unnecessary Dependencies**:  
   - Minimize binary size by only including required crates.  

3. **Inlining and Dead Code Elimination**:  
   - Use compiler flags like `--release` to enable optimizations:  
     ```bash
     wasm-pack build --release
     ```

## 🎯 Hands-On Challenge

#### **Objective**:  
Create a complete WebAssembly-based project using Rust. This project will involve writing Rust code, compiling it to WebAssembly, and integrating it with a simple web page. You'll apply everything you've learned, from setting up the environment to understanding memory management, key concepts, and debugging.



### Step 1: **Create a New Rust Project for WebAssembly**

- Initialize a new Rust library project for WebAssembly:
  ```bash
  cargo new --lib wasm_challenge
  cd wasm_challenge
  ```

- Add dependencies for `wasm-bindgen` in the `Cargo.toml`:
  ```toml
  [dependencies]
  wasm-bindgen = "0.2"
  ```



### Step 2: **Write Rust Code to Implement Multiple Functions**

- **Function 1**: Implement a simple function that adds two integers together:
  ```rust
  use wasm_bindgen::prelude::*;

  #[wasm_bindgen]
  pub fn add(a: i32, b: i32) -> i32 {
      a + b
  }
  ```

- **Function 2**: Implement a function that takes an array of integers and returns the sum:
  ```rust
  #[wasm_bindgen]
  pub fn sum_array(arr: Vec<i32>) -> i32 {
      arr.iter().sum()
  }
  ```

- **Function 3**: Implement a function that takes a string, converts it to uppercase, and returns the result:
  ```rust
  #[wasm_bindgen]
  pub fn to_uppercase(input: String) -> String {
      input.to_uppercase()
  }
  ```



### Step 3: **Set Up the Project for WebAssembly**

- Install the `wasm32-unknown-unknown` target:
  ```bash
  rustup target add wasm32-unknown-unknown
  ```

- Install `wasm-pack` if you haven't already:
  ```bash
  cargo install wasm-pack
  ```

- Build the project for the WebAssembly target:
  ```bash
  wasm-pack build --target web
  ```



### Step 4: **Create a Web Page to Integrate the WebAssembly Module**

- Create a `index.html` file to interact with the WebAssembly functions:
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>WebAssembly Challenge</title>
  </head>
  <body>
      <h1>WebAssembly with Rust Challenge</h1>
      
      <button id="addBtn">Add 5 + 7</button>
      <button id="sumBtn">Sum Array [1, 2, 3, 4]</button>
      <button id="upperBtn">To Uppercase ("hello")</button>

      <p id="result"></p>
      
      <script type="module">
          import init, { add, sum_array, to_uppercase } from './pkg/wasm_challenge.js';

          async function run() {
              await init();
              
              document.getElementById("addBtn").onclick = () => {
                  const result = add(5, 7);
                  document.getElementById("result").innerText = `Add Result: ${result}`;
              };

              document.getElementById("sumBtn").onclick = () => {
                  const result = sum_array([1, 2, 3, 4]);
                  document.getElementById("result").innerText = `Sum Array Result: ${result}`;
              };

              document.getElementById("upperBtn").onclick = () => {
                  const result = to_uppercase("hello");
                  document.getElementById("result").innerText = `Uppercase Result: ${result}`;
              };
          }

          run();
      </script>
  </body>
  </html>
  ```



### Step 5: **Build and Run the WebAssembly Code**

- Use `wasm-pack` to build your project:
  ```bash
  wasm-pack build --target web
  ```

- Start a local server (you can use `python -m http.server` or any other web server) to run the `index.html` file.



### Step 6: **Test the Project in Your Browser**

1. Click on the **Add** button to see the result of `5 + 7`.
2. Click on the **Sum Array** button to see the result of summing an array `[1, 2, 3, 4]`.
3. Click on the **To Uppercase** button to see `"hello"` converted to `"HELLO"`.



### Step 7: **Bonus Debugging Tasks**

- If you encounter any issues, check the browser’s **Developer Console** for errors related to WebAssembly.
- Use `console.log` in JavaScript to output data and debug your code step by step.



### Step 8: **Submission**

- Once your project is working, submit the following:
  - Your Rust code (`src/lib.rs`).
  - The `index.html` file.
  - Any additional files you used for setting up the project.
  


### Challenge Recap

This challenge covers all the key aspects:
- Writing Rust code to be compiled into WebAssembly.
- Integrating WebAssembly into a simple web page.
- Using JavaScript to interact with Rust functions in WebAssembly.
- Debugging and ensuring that everything runs smoothly in the browser.




## 💻 Exercises - Day 26

Here are some exercises to help you practice what you've learned today. 

## ✅ Exercise: Level 1

**Task:**  
- Create a new WebAssembly project in Rust that has a function to multiply two numbers.
- Use `wasm-pack` to build the project and export the function to JavaScript.
- Write a function in Rust that takes a string and returns the reversed string, using WebAssembly.

## 🚀 Exercise: Level 2

**Task:**  
- Modify your WebAssembly project to take an array of integers, sum them up, and return the result.
- Write JavaScript code to call the Rust function and display the sum on the webpage.
- Create a simple interactive webpage with WebAssembly where users can input their name and see a personalized greeting.

## 🏆 Exercise: Level 3 (Advanced)

**Task:**  
- Create a WebAssembly project that takes a string, converts it to uppercase, and returns it.
- Use `wasm-bindgen` to export the function and demonstrate it in a simple HTML page with a text input field.
- Build a small interactive game using WebAssembly and Rust, where the game runs in the browser with low latency.


## 🎥 Helpful Video References  

- [Putting Rust into Production at Mozilla](https://www.youtube.com/watch?v=2RhbYpgVpg0)
- [Rust for Web Assembly](https://www.youtube.com/watch?v=7I4Z_MqvMxY)
- [Rust and WebAssembly - The complete guide](https://youtube.com/playlist?list=PLz0t90fOInA66qP_pjNQWZiBvqlZPQDUp&si=cejeJkrD84jpOK5D)



## 📚 Further Reading  

- [Rust and WebAssembly Book](https://rustwasm.github.io/book/)
- [Rust WebAssembly Examples](https://github.com/rustwasm)
- [WebAssembly Official Site](https://webassembly.org/)


## 📝 Day 26 Summary  

Today, we learned how to:  
- Set up Rust for WebAssembly.
- Write a basic WebAssembly function using Rust.
- Use tools like `wasm-pack` and `wasm-bindgen`.
- Understand key concepts such as imports, exports, and memory management in WebAssembly.  


Stay tuned for **Day 27**, where we will explore **Graphics Programming with Rust** in Rust! 🚀

🌟 _Great job on completing Day 26! Keep practicing, and get ready for Day 27!_

Thank you for joining **Day 26** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)


[<< Day 25](../25_Rust%20on%20Embedded%20Systems/25_rust_on_embedded_systems.md) | [Day 27 >>](../27_Graphics%20Programming%20with%20Rust/27_graphics_programming_with_rust.md)  

---
