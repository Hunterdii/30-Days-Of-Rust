<div align="center">
  <h1>🦀 30 Days of Rust: Day 19 - Networking in Rust 🌐 </h1>
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

[<< Day 18](../18_Asynchronous%20Programming/18_asynchronous_programming.md) | [Day 20 >>](../20_Unsafe%20Rust/20_unsafe_rust.md)  

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)

- [📘 Day 19 - Networking in Rust](#-day-19---networking-in-rust)
  - [👋 Welcome](#-welcome)  
  - [🔍 Overview](#-overview)  
  - [🛠 Environment Setup](#-environment-setup)  
  - [🌐 Networking in Rust](#-networking-in-rust)  
    - [🔧 TCP Client and Server](#-tcp-client-and-server)  
    - [🔄 UDP Communication](#-udp-communication)  
    - [💬 HTTP Requests and Responses](#-http-requests-and-responses)  
    - [🛠 Asynchronous Networking](#-asynchronous-networking)  
  - [📖 Real-World Example: Chat Application](#-real-world-example-chat-application)  
  - [🚀 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 19](#-exercises---day-19)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [🚀 Exercise: Level 2](#-exercise-level-2)
  - [🎥 Additional Resources](#-additional-resources)
  - [📚 More Insights](#-more-insights)
  - [📝 Day 19 Summary](#-day-19-summary)  

---

# 📘 Day 19 - Networking in Rust

## 👋 Welcome  

Welcome to **Day 19** of the **30 Days of Rust Challenge**! 🎉  

Today’s topic is **Networking in Rust**, an essential skill for building distributed applications, web servers, APIs, and more. Rust provides powerful libraries and tools for networking, which are fast, safe, and efficient. We’ll cover core networking concepts, building a TCP server and client, handling UDP communication, and using `tokio` for asynchronous network operations.  

By the end of this day’s lesson, you will:  

- Understand how to work with TCP and UDP sockets in Rust.  
- Make HTTP requests and handle responses.  
- Build an asynchronous networking application using `tokio`.  

Let’s get started! 🚀



## 🔍 Overview  

Rust’s networking capabilities are robust, offering both synchronous and asynchronous ways to work with various protocols, including **TCP**, **UDP**, and **HTTP**. Networking in Rust is heavily based on libraries like **`std::net`** for basic functionality and **`tokio`** for asynchronous I/O.  

### Key Concepts in Networking:  

1. **TCP vs UDP**:  
   - **TCP (Transmission Control Protocol)**: Reliable, connection-based protocol. Ideal for applications requiring guaranteed delivery (e.g., web servers).  
   - **UDP (User Datagram Protocol)**: Unreliable, connectionless protocol. Suitable for real-time applications (e.g., video streaming, gaming).  

2. **HTTP**:  
   The foundation of the web, a request-response protocol that clients (browsers, apps) use to communicate with servers.  

3. **Asynchronous Networking**:  
   Handling multiple connections without blocking, allowing for highly scalable systems. This is often done using `tokio` and `async` in Rust.  



## 🛠 Environment Setup  

If you have already set up your Rust environment on **Day 1**, you’re good to go! Otherwise, check out the [Environment Setup](../README.md#-environment-setup) section for detailed instructions. Ensure you have **Cargo** installed by running:

```bash
$ cargo --version
```

If you see a version number, you’re all set! 🎉

Before diving into networking, let’s set up the required dependencies.  

### Step 1: Add Dependencies  

To perform asynchronous networking, we’ll use the `tokio` crate, which is the most popular async runtime in Rust. We’ll also use `reqwest` for making HTTP requests.  

Open your `Cargo.toml` and add the following dependencies:  

```toml
[dependencies]
tokio = { version = "1", features = ["full"] }
reqwest = { version = "0.11", features = ["json"] }
```

### Step 2: Install and Verify  

Run:  

```bash
cargo build
```

This will download and build all the necessary dependencies for networking. You’re ready to start working with networking in Rust!  



## 🌐 Networking in Rust  

### 🔧 TCP Client and Server  

Rust provides a simple API for working with TCP via the `std::net` module. Let’s look at how to create a basic TCP server and client.  

#### **TCP Server**  

```rust
use std::net::{TcpListener, TcpStream};
use std::io::{Read, Write};

fn handle_client(mut stream: TcpStream) {
    let mut buffer = [0; 512];
    stream.read(&mut buffer).unwrap();
    println!("Received: {}", String::from_utf8_lossy(&buffer));

    let response = "HTTP/1.1 200 OK\r\n\r\nHello, World!";
    stream.write(response.as_bytes()).unwrap();
    stream.flush().unwrap();
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    println!("Server listening on port 7878...");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                handle_client(stream);
            }
            Err(e) => {
                eprintln!("Failed to accept connection: {}", e);
            }
        }
    }
}
```

#### **TCP Client**  

```rust
use std::net::TcpStream;
use std::io::{Read, Write};

fn main() {
    let mut stream = TcpStream::connect("127.0.0.1:7878").unwrap();
    stream.write(b"GET / HTTP/1.1\r\n\r\n").unwrap();

    let mut response = String::new();
    stream.read_to_string(&mut response).unwrap();
    println!("Server response: {}", response);
}
```

In this example, we have a simple TCP server and client. The server listens on port 7878, while the client sends a simple HTTP request.  

### <div align="center">_*or*_</div>

#### **TCP Server**  

This implementation uses a function to handle each client and improves error handling with the `?` operator. It also demonstrates logging for debugging purposes.

```rust
use std::net::{TcpListener, TcpStream};
use std::io::{Read, Write};
use std::thread;

/// Handles communication with a single client.
fn handle_client(mut stream: TcpStream) -> std::io::Result<()> {
    let mut buffer = [0; 512];
    let bytes_read = stream.read(&mut buffer)?;

    println!("Received: {}", String::from_utf8_lossy(&buffer[..bytes_read]));

    let response = "HTTP/1.1 200 OK\r\n\r\nHello, Rusty World!";
    stream.write_all(response.as_bytes())?;
    stream.flush()?;
    Ok(())
}

fn main() -> std::io::Result<()> {
    let listener = TcpListener::bind("127.0.0.1:7878")?;
    println!("Server is running on 127.0.0.1:7878");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                // Spawn a new thread for each client connection.
                thread::spawn(|| {
                    if let Err(e) = handle_client(stream) {
                        eprintln!("Error handling client: {}", e);
                    }
                });
            }
            Err(e) => eprintln!("Failed to accept a connection: {}", e),
        }
    }

    Ok(())
}
```



#### **TCP Client**  

This implementation makes the client reusable by encapsulating the connection logic in a function. It also uses `Result` for better error handling.

```rust
use std::net::TcpStream;
use std::io::{Read, Write};

/// Connects to the server and sends a request.
fn connect_and_send_request() -> std::io::Result<()> {
    let mut stream = TcpStream::connect("127.0.0.1:7878")?;
    println!("Connected to the server!");

    // Send a request to the server.
    stream.write_all(b"GET / HTTP/1.1\r\n\r\n")?;

    // Read and display the response.
    let mut response = String::new();
    stream.read_to_string(&mut response)?;
    println!("Server response:\n{}", response);

    Ok(())
}

fn main() {
    if let Err(e) = connect_and_send_request() {
        eprintln!("Error connecting to the server: {}", e);
    }
}
```


## 🔄 UDP Communication  

Unlike TCP, **UDP** does not guarantee delivery, and the order of messages may not be preserved. However, UDP can be useful for real-time applications where speed is more important than reliability (e.g., gaming, video streaming).  

#### **UDP Server**  

```rust
use std::net::UdpSocket;

fn main() {
    let socket = UdpSocket::bind("127.0.0.1:8080").expect("Couldn't bind to address");
    let mut buf = [0; 100];

    loop {
        let (amt, src) = socket.recv_from(&mut buf).expect("Didn't receive data");
        println!("Received {} bytes from {}", amt, src);
        socket.send_to(&buf[..amt], &src).expect("Failed to send data");
    }
}
```

#### **UDP Client**  

```rust
use std::net::UdpSocket;

fn main() {
    let socket = UdpSocket::bind("127.0.0.1:0").expect("Couldn't bind to address");
    let server_addr = "127.0.0.1:8080";

    let message = b"Hello, UDP!";
    socket.send_to(message, server_addr).expect("Failed to send data");

    let mut buf = [0; 100];
    let (amt, _src) = socket.recv_from(&mut buf).expect("Didn't receive data");
    println!("Received response: {}", String::from_utf8_lossy(&buf[..amt]));
}
```

In this example, we have a simple UDP server that echoes back whatever message it receives from the client.  

### <div align="center">_*or*_</div>

#### **UDP Server**  

This version includes error handling and modularized code for clarity.

```rust
use std::net::UdpSocket;

fn main() -> std::io::Result<()> {
    // Bind the UDP server to an address and port
    let socket = UdpSocket::bind("127.0.0.1:8080")?;
    println!("Server is listening on 127.0.0.1:8080...");

    let mut buffer = [0; 512];

    loop {
        // Receive data from the client
        match socket.recv_from(&mut buffer) {
            Ok((bytes_received, source)) => {
                let message = String::from_utf8_lossy(&buffer[..bytes_received]);
                println!("Received '{}' from {}", message, source);

                // Echo the received data back to the client
                if let Err(e) = socket.send_to(message.as_bytes(), source) {
                    eprintln!("Error sending data: {}", e);
                }
            }
            Err(e) => eprintln!("Failed to receive data: {}", e),
        }
    }
}
```


#### **UDP Client**  

This version separates the logic into functions for better modularity and makes the server address configurable.

```rust
use std::net::UdpSocket;
use std::io::{self, Write};

fn main() -> std::io::Result<()> {
    // Bind the UDP client to an ephemeral port
    let socket = UdpSocket::bind("127.0.0.1:0")?;
    let server_address = "127.0.0.1:8080";

    loop {
        // Prompt the user for input
        print!("Enter message to send (or 'exit' to quit): ");
        io::stdout().flush()?; // Ensure the prompt is displayed

        let mut input = String::new();
        io::stdin().read_line(&mut input)?;
        let trimmed_input = input.trim();

        if trimmed_input.eq_ignore_ascii_case("exit") {
            println!("Exiting...");
            break;
        }

        // Send the input to the server
        socket.send_to(trimmed_input.as_bytes(), server_address)?;

        // Receive the response from the server
        let mut buffer = [0; 512];
        match socket.recv_from(&mut buffer) {
            Ok((bytes_received, _source)) => {
                let response = String::from_utf8_lossy(&buffer[..bytes_received]);
                println!("Response from server: {}", response);
            }
            Err(e) => eprintln!("Failed to receive response: {}", e),
        }
    }

    Ok(())
}
```


## 💬 HTTP Requests and Responses  

For HTTP communication, we use the `reqwest` crate, which makes it easy to send HTTP requests and handle responses.  

#### **Making HTTP Requests**  

Here’s an example of how to perform a GET request to fetch data from a URL:

```rust
use reqwest::Client;

#[tokio::main]
async fn main() {
    let client = Client::new();
    let res = client.get("https://jsonplaceholder.typicode.com/posts/1")
                    .send()
                    .await
                    .unwrap();

    let body = res.text().await.unwrap();
    println!("Response Body: {}", body);
}
```

In this example, we create a new HTTP client, send a GET request, and print the response body. The `await` keyword is used to make the asynchronous call non-blocking.  


## 🛠 Asynchronous Networking  

### 🛠 Working with `tokio` and `async-std`

Rust’s async runtimes, `tokio` and `async-std`, make asynchronous networking easy. While `tokio` is more feature-rich, `async-std` is designed to be simpler and easier to use. Both can be used for network I/O.

- **`tokio`**: A powerful, asynchronous runtime for Rust.
- **`async-std`**: A simpler alternative for asynchronous tasks.

Let’s look at an example using **`tokio`**:

```rust
use tokio::net::TcpListener;
use tokio::prelude::*;

#[tokio::main]
async fn main

() {
    let listener = TcpListener::bind("127.0.0.1:8080").await.unwrap();

    loop {
        let (mut socket, _) = listener.accept().await.unwrap();
        tokio::spawn(async move {
            let mut buffer = [0; 1024];
            socket.read(&mut buffer).await.unwrap();
            socket.write_all(b"Hello from Tokio!").await.unwrap();
        });
    }
}
```



## 📖 Real-World Example: Chat Application  

Now let’s build a simple **TCP-based chat application**. This will allow multiple clients to connect to a server, send messages, and receive messages from other clients.

### TCP Chat Server  

```rust
use std::net::{TcpListener, TcpStream};
use std::io::{Read, Write};
use std::thread;
use std::sync::{Arc, Mutex};

fn handle_client(stream: TcpStream, clients: Arc<Mutex<Vec<TcpStream>>>) {
    let mut buffer = [0; 512];
    loop {
        match stream.read(&mut buffer) {
            Ok(0) => break,
            Ok(_) => {
                let msg = String::from_utf8_lossy(&buffer);
                println!("Received: {}", msg);

                let clients = clients.lock().unwrap();
                for client in clients.iter() {
                    let _ = client.write_all(msg.as_bytes());
                }
            }
            Err(_) => break,
        }
    }
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    let clients = Arc::new(Mutex::new(Vec::new()));

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                let clients = Arc::clone(&clients);
                clients.lock().unwrap().push(stream.try_clone().unwrap());
                thread::spawn(move || {
                    handle_client(stream, clients);
                });
            }
            Err(_) => continue,
        }
    }
}
```

This example shows a chat server where multiple clients can connect and send messages to each other in real-time.  



## 🚀 Hands-On Challenge  

1. Create a **UDP-based chat application** where messages are broadcasted to all connected clients.
2. Build a **HTTP API client** that retrieves JSON data and parses it into Rust structs using `serde`.

### 1. **TCP Networking Challenge**  
Build a simple **Echo Server** and **Client**:
1. The server should listen for incoming connections and echo back any message received.
2. The client should connect to the server, send a message, and print the server's response.

**Extensions**:
- Modify the server to handle multiple clients simultaneously using threads.
- Add logging to record messages exchanged between the client and server.

### 2. **UDP Networking Challenge**  
Create a **Ping-Pong Application**:
1. A UDP server listens for "Ping" messages and responds with "Pong."
2. A UDP client sends "Ping" messages to the server and prints the "Pong" responses.

**Extensions**:
- Add a counter to track the number of "Pong" responses received.
- Implement a timeout mechanism for the client to handle server unresponsiveness.

### 3. **HTTP Networking Challenge**  
Write an HTTP server that:
1. Serves static HTML files from a directory (e.g., `index.html`).
2. Responds to unknown routes with a "404 Not Found" message.

**Extensions**:
- Implement routing for specific paths (e.g., `/about`, `/contact`).
- Add support for query parameters and parse them.

### 4. **Asynchronous Networking Challenge**  
Using the `tokio` crate, build an async TCP server and client:
1. The server accepts multiple client connections and handles each asynchronously.
2. The client connects to the server and sends a series of messages, receiving responses asynchronously.

**Extensions**:
- Create a chat application where multiple clients can send messages to each other through the server.
- Add a feature for private messaging between clients.
  

## 💻 Exercises - Day 19  

### ✅ **Exercise: Level 1**

1. **TCP Basics**:
   - Implement a TCP client that connects to a server and sends a "Hello, Server!" message.
   - Write a TCP server that listens for connections and responds with "Hello, Client!"

2. **UDP Basics**:
   - Create a UDP server that listens for "Hello" messages and replies with "World!"
   - Write a UDP client that sends "Hello" to the server and prints the response.

3. **Simple HTTP Client**:
   - Use the `reqwest` crate to fetch data from a public API (e.g., `https://api.github.com`) and print the response.


### 🚀 **Exercise: Level 2**

1. **Load Testing Server**:
   - Write a program to simulate multiple clients connecting to your TCP server concurrently and sending random messages.
   - Measure the server's response time for each client.

2. **Custom HTTP Server**:
   - Create a basic HTTP server that accepts `GET` and `POST` requests.
   - Respond to `GET` requests with a welcome message.
   - Log the body of `POST` requests to a file.

3. **File Transfer over TCP**:
   - Build a server that allows clients to upload files.
   - The client reads a file and sends it to the server over a TCP connection.

4. **Multicast Communication**:
   - Implement a simple multicast communication using UDP where one sender broadcasts a message to multiple receivers.

## 🎥 Additional Resources
- [Rust Networking with Tokio (Official Guide)](https://youtube.com/playlist?list=PL5E0b3rgRMdpDBdw56w7tNSZgVt2dysNF&si=CV0_gCJLfYu7NbZU)
- [Rust Async Book](https://www.youtube.com/watch?v=wBQ8KlX7glY)
- [Real-World Rust Networking Applications](https://youtube.com/playlist?list=PLrOQsSoS-V69jo82lPCIj8a1HLrmQLK2V&si=Aq5_-9n4a5eTRoc8)

## 📚 More Insights

| **Feature**               | **Synchronous Networking**          | **Asynchronous Networking**         | **Multithreading**                 |  
|---------------------------|-------------------------------------|-------------------------------------|------------------------------------|  
| **Performance**           | Blocks on I/O, can be slow for high concurrency | Efficient handling of many connections | High for CPU-bound tasks           |  
| **Best for**              | Simple use cases, low traffic       | High concurrency, I/O-bound tasks   | CPU-intensive tasks                |  
| **Complexity**            | Easier to write and debug           | Higher, requires async runtime      | Race conditions, manual safety     |  
| **Concurrency Handling**  | Single-threaded blocking I/O        | Non-blocking, event-driven          | Multi-threaded                     |  
| **Libraries/Crates**      | `std::net`                          | `tokio`, `async-std`, `hyper`       | `std::thread`, `rayon`             |  
| **Scalability**           | Limited by threads or processes     | Scales well with async runtimes     | Limited by thread count            |  
| **Example Use Cases**     | Simple TCP/UDP servers              | Web servers, chat applications      | Parallel data processing            |  
| **Ease of Learning**      | Beginner-friendly                   | Intermediate to advanced            | Intermediate, with sync primitives |  
| **Error Handling**        | Straightforward but runtime errors possible | Compile-time safety with `Future`  | Runtime errors and potential panics|  

### **1. Protocol Support**  
Rust's ecosystem supports various networking protocols through external crates:  
- **HTTP/HTTPS**: Use `reqwest`, `hyper`, or `surf` for building HTTP clients and servers.  
- **WebSocket**: Use `tungstenite` or `async-tungstenite` for WebSocket communication.  
- **FTP/SMTP**: Use crates like `rftp` for FTP and `lettre` for SMTP.  
- **DNS**: Use `trust-dns` for DNS querying and server implementation.  


### **2. Secure Networking**  
Rust provides tools to handle secure communication:  
- **TLS/SSL**: Use `native-tls` or `rustls` for encrypted connections.  
- **Certificate Management**: Manage X.509 certificates for secure communication.  
- **End-to-End Encryption**: Implement custom encryption with `ring` or `openssl` crates.  


### **3. Networking with Async Frameworks**  
Async programming in Rust is powered by runtime libraries:  
- **Tokio**: A high-performance async runtime for building scalable network applications.  
- **Async-std**: An alternative async runtime with simpler APIs for lightweight tasks.  
- **Actix**: A powerful actor-based framework for building concurrent web applications.  


### **4. UDP Communication**  
- **Unreliable Messaging**: Send and receive datagrams without maintaining a connection.  
- **Real-Time Applications**: Use UDP for low-latency applications like gaming or streaming.  
- **Example Crate**: `std::net::UdpSocket` provides basic support for UDP.  


### **5. Web Frameworks**  
- **Rocket**: A high-level framework for building web APIs.  
- **Warp**: A composable, flexible, and performant web framework.  
- **Axum**: Built on top of `tokio` and `hyper`, focusing on ergonomic APIs.  

### **6. Low-Level Networking**  
For more control over networking:  
- **Raw Sockets**: Use `socket2` crate for creating and handling raw sockets.  
- **Packet Crafting**: Use `pnet` to create custom network packets.  
- **Networking System Calls**: Use `nix` crate to interact with OS-level networking.  

### **7. Performance Optimization**  
- **Load Balancing**: Use tools like `haproxy` in combination with Rust servers.  
- **Connection Pooling**: Manage resource usage with libraries like `r2d2`.  
- **Caching**: Use crates like `cached` or `moka` to implement in-memory caches.  


### **8. Testing and Debugging**  
- **Mocking Servers**: Use crates like `mockito` to create mock HTTP servers for testing.  
- **Network Inspection**: Analyze traffic with tools like Wireshark or Tcpdump.  
- **Logging**: Use `env_logger` or `tracing` for detailed runtime logs.  


### **9. Real-Time Applications**  
Rust's concurrency model and async libraries make it suitable for:  
- **Chat Applications**: Build with WebSockets or TCP streams.  
- **Video Streaming**: Use crates like `gstreamer` for handling multimedia data.  
- **IoT Devices**: Build lightweight networking stacks with embedded-friendly crates like `smoltcp`.  


### **10. Common Crates**  
| **Crate**      | **Description**                                           |  
|-----------------|-----------------------------------------------------------|  
| `tokio`         | Async runtime for network programming.                    |  
| `hyper`         | HTTP library for client and server.                       |  
| `reqwest`       | HTTP client with an easy-to-use API.                      |  
| `actix-web`     | Web framework for building REST APIs and microservices.   |  
| `tungstenite`   | WebSocket library for both sync and async usage.          |  
| `trust-dns`     | DNS client and server library.                            |  
| `rustls`        | Modern TLS implementation for secure connections.         |  


## 📝 Day 19 Summary  

Today, you’ve learned how to work with **networking in Rust**, including:  

- **TCP and UDP communication**.  
- How to **make HTTP requests** using the `reqwest` crate.  
- How to build an asynchronous networking server using `tokio`.  
- A real-world example: **Building a TCP chat application**.  

Networking is a critical part of modern applications, and now you have the foundational knowledge to work with various networking protocols in Rust. Keep practicing and building!

Stay tuned for **Day 20**, where we will explore **Unsafe Rust in Rust** in Rust! 🚀

🌟 _Great job on completing Day 19! Keep practicing, and get ready for Day 20!_

Thank you for joining **Day 19** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 18](../18_Asynchronous%20Programming/18_asynchronous_programming.md) | [Day 20 >>](../20_Unsafe%20Rust/20_unsafe_rust.md)  

---
