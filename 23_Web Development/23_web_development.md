<div align="center">
  <h1>🦀 30 Days of Rust: Day 23 - Web Development with Rust 🌐</h1>
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

[<< Day 22](../22_Building%20CLI%20Applications/22_building_cli_applications.md) | [Day 24 >>](../24_Integrating_with_C_C%2B%2B/24_integrating_with_c_c%2B%2B.md)  

![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)


- [📘 Day 23 - Web Development with Rust](#-day-23---web-development-with-rust)
  - [👋 Welcome](#-welcome)
  - [🔍 Overview](#-overview)
  - [🛠 Environment Setup](#-environment-setup)  
  - [🕸 Introduction to Web Development with Rust](#-introduction-to-web-development-with-rust)  
    - [🌟 Why Choose Rust for Web Development?](#-why-choose-rust-for-web-development)
  - [🚀 Setting Up a Rust Web Server](#-setting-up-a-rust-web-server)  
    - [⚙ Basic Web Server with `axum`](#-basic-web-server-with-axum)
    - [🔧 Adding Routes](#-adding-routes)
    - [🛠 Handling Requests and Responses](#-handling-requests-and-responses)
  - [🔒 Handling Authentication and Security](#-handling-authentication-and-security)  
    - [🔑 Adding Middleware](#-adding-middleware)
    - [📲 Adding Authentication](#-adding-authentication)
    - [🔐 Securing the Server](#-securing-the-server)
  - [📦 Working with JSON and APIs](#-working-with-json-and-apis)  
    - [📤 Building REST APIs](#-building-rest-apis)
    - [📥 Handling JSON Payloads](#-handling-json-payloads)
  - [🌐 Building a Simple Full-Stack Application](#-building-a-simple-full-stack-application)
  - [📚 Popular Web Frameworks](#-popular-web-frameworks)  
    - [1️⃣ Actix Web](#1%EF%B8%8F⃣-actix-web)  
    - [2️⃣ Rocket](#2%EF%B8%8F⃣-rocket)  
    - [3️⃣ Warp](#3%EF%B8%8F⃣-warp)  
    - [4️⃣ Axum](#4%EF%B8%8F⃣-axum)
  - [🛠️ Building a Simple Web Server](#️-building-a-simple-web-server)  
  - [🌟 Exploring APIs and Routes](#-exploring-apis-and-routes)  
  - [🗄️ Database Integration](#️-database-integration)  
  - [🚀 Deploying Rust Web Applications](#-deploying-rust-web-applications)
  - [🎯 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 23](#-exercises---day-23)
     - [✅ Exercise: Level 1](#-exercise-level-1)
     - [🚀 Exercise: Level 2](#-exercise-level-2)
     - [🏆 Exercise: Level 3 (Advanced)](#-exercise-level-3-advanced)
  - [🎥 Helpful Video References](#-helpful-video-references)
  - [📚 Further Reading](#-further-reading)
 - [📝 Day 23 Summary](#-day-23-summary)  

---

# 📘 Day 23 - Web Development with Rust

## 👋 Welcome  

Welcome to **Day 23** of the **30 Days of Rust Challenge**! 🎉  

Today, we dive into **web development** with Rust. While Rust isn’t traditionally associated with web development like JavaScript or Python, it has grown into a compelling choice for building **high-performance**, **secure**, and **scalable** web applications.  

Whether you're building APIs, microservices, or complete web applications, Rust's ecosystem offers powerful tools to craft performant, secure, and scalable web solutions.

By the end of this lesson, you will:  
- Understand Rust’s web development ecosystem.  
- Learn about popular web frameworks like Actix Web, Rocket, and Warp.  
- Build a simple web server with routes and APIs.  
- Integrate a database for persistent storage.  
- Explore authentication, security, and deployment strategies.
- Build a **basic web server** with Rust.  
- Explore the `axum` crate for handling routes and middleware.  
- Learn to handle **JSON payloads** and develop REST APIs.  
- Create a **simple full-stack web application**.  
 
Let’s get started! 🚀  

## 🔍 Overview  

Welcome to **Day 23** of your Rust journey! Today, we’ll dive into the exciting world of **web development with Rust**. 🚀  

Rust is gaining traction as a go-to language for building fast, reliable, and secure web applications. From crafting robust backends to implementing high-performance APIs, Rust's ecosystem has everything you need to excel.  

In this session, we’ll:  
1. Explore **popular frameworks** like `axum` and `actix-web`.  
2. Build our first **REST API**.  
3. Learn to integrate Rust backends with modern frontend frameworks like React or Vue.js.  

**Why Rust for Web Development?**  
- ⚡ **High Performance**: Built for speed and concurrency.  
- 🔒 **Safety First**: No more null pointer exceptions or data races!  
- 🌐 **Growing Ecosystem**: Powerful libraries like `axum`, `warp`, and `actix-web` to streamline web development.  

By the end of this day, you’ll be equipped to create your first full-stack app with Rust at its core.  


## 🛠 Environment Setup  

Let’s ensure you’re ready to code! Follow these steps to set up a complete environment for web development with Rust:  

#### 1. **Install Rust**  
Ensure Rust is installed on your system:  
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```  
Verify installation:  
```bash
rustc --version
```  

#### 2. **Install Cargo Tools**  
Cargo is Rust's package manager and build system. It's essential for managing dependencies and projects.  
Update Cargo for the latest features:  
```bash
cargo install-update -a
```  

#### 3. **Set Up a Web Framework**  
We’ll use `axum` for this day. Add it to your project dependencies:  
```bash
cargo new rust_web_project
cd rust_web_project
cargo add axum tokio serde serde_json
```  
This command includes:  
- `axum`: For building web servers.  
- `tokio`: For async runtime.  
- `serde` & `serde_json`: For JSON serialization and deserialization.  

#### 4. **Add a Database Library (Optional)**  
To include database support, install a library like `sqlx` for PostgreSQL:  
```bash
cargo add sqlx --features postgres
```  

#### 5. **Set Up Development Tools**  
- **IDE**: Use **VS Code** or **IntelliJ IDEA** with the Rust plugin for syntax highlighting and autocompletion.  
- **Linting**: Install `clippy` to catch common mistakes:  
    ```bash
    rustup component add clippy
    ```  
- **Formatting**: Ensure consistent code style with `rustfmt`:  
    ```bash
    rustup component add rustfmt
    ```  

#### 6. **Run Your First Server**  
Test your setup with a simple `Hello, World!` server:  
```rust
use axum::{handler::get, Router};

#[tokio::main]
async fn main() {
    let app = Router::new().route("/", get(|| async { "Hello, World!" }));
    axum::Server::bind(&([127, 0, 0, 1], 3000).into())
        .serve(app.into_make_service())
        .await
        .unwrap();
}
```  
Start the server:  
```bash
cargo run
```  
Visit `http://127.0.0.1:3000` in your browser, and you’re ready to go! 🎉  


## 🕸 Introduction to Web Development with Rust  

Rust's emphasis on performance, type safety, and memory safety makes it an excellent choice for web applications that demand:  
- **Speed**: Comparable to C and C++ for high-performance backends.  
- **Concurrency**: Powerful async capabilities with `tokio` and `async-std`.  
- **Security**: Strong guarantees to prevent common bugs like data races and memory corruption.  

## 🌟 Why Choose Rust for Web Development?  

1. **Efficiency**: Rust’s zero-cost abstractions allow developers to write high-performance web servers.  
2. **Reliability**: Memory safety features reduce bugs, crashes, and vulnerabilities.  
3. **Async Support**: Rust’s async runtime makes handling thousands of connections easy.  
4. **Ecosystem**: Libraries like `axum`, `warp`, and `actix-web` simplify the development process.  

### Key Advantages  

1. **Performance**  
   Rust delivers low-level performance, making it ideal for web applications with high throughput and low latency requirements.  

2. **Safety**  
   Rust’s memory safety guarantees ensure fewer bugs and vulnerabilities compared to languages like C++ or PHP.  

3. **Concurrency**  
   With its async runtime and modern concurrency model, Rust is well-suited for handling multiple simultaneous connections.  

4. **Rich Ecosystem**  
   Tools like `axum`, `warp`, and `actix-web` make web development simple and expressive.  

5. **Cross-platform Deployments**  
   Rust's portability allows seamless deployment across different platforms and environments.  

## 🚀 Setting Up a Rust Web Server  

We’ll use the `axum` framework to build our server. It’s lightweight, async-native, and easy to use for both beginners and experts.  

### Step 1: Create a New Rust Project  

Start by creating a new Rust project:  

```bash
$ cargo new rust-web-server
$ cd rust-web-server
```

### Step 2: Add Dependencies  

Add the following dependencies to your `Cargo.toml`:  

```toml
[dependencies]
axum = "0.6"
tokio = { version = "1", features = ["full"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
tower = "0.4"
```

### Step 3: Write Your First Web Server  

```rust
use axum::{routing::get, Router};
use std::net::SocketAddr;

#[tokio::main]
async fn main() {
    // Define a basic route
    let app = Router::new().route("/", get(|| async { "Hello, Rustacean!" }));

    // Bind to an address and start the server
    let addr = SocketAddr::from(([127, 0, 0, 1], 3000));
    println!("Server running at http://{}", addr);

    axum::Server::bind(&addr)
        .serve(app.into_make_service())
        .await
        .unwrap();
}
```

Run the server with:  

```bash
$ cargo run
```

Visit `http://127.0.0.1:3000` in your browser. You’ll see `Hello, Rustacean!`.


## ⚙ Basic Web Server with `axum`  

Here’s a minimal example:  

```rust
use axum::{routing::get, Router};
use std::net::SocketAddr;

#[tokio::main]
async fn main() {
    // Define a basic route
    let app = Router::new().route("/", get(|| async { "Hello, World!" }));

    // Bind to an address and start the server
    let addr = SocketAddr::from(([127, 0, 0, 1], 3000));
    println!("Server running at http://{}", addr);
    axum::Server::bind(&addr)
        .serve(app.into_make_service())
        .await
        .unwrap();
}
```

Run the server with:  

```sh
$ cargo run
```

Visit `http://127.0.0.1:3000` to see `Hello, World!`.



## 🔧 Adding Routes  

Define additional routes for different endpoints:  

```rust
let app = Router::new()
    .route("/", get(|| async { "Welcome to Rust Web Development!" }))
    .route("/hello", get(|| async { "Hello, Rustacean!" }))
    .route("/json", get(|| async { axum::Json(serde_json::json!({"message": "Hello, JSON!"})) }));
```


## 🛠 Handling Requests and Responses  

Use `axum`’s request extractors to handle data:  

```rust
use axum::{extract::Query, routing::get, Router};
use serde::Deserialize;

#[derive(Deserialize)]
struct GreetParams {
    name: String,
}

#[tokio::main]
async fn main() {
    let app = Router::new().route(
        "/greet",
        get(|Query(params): Query<GreetParams>| async move {
            format!("Hello, {}!", params.name)
        }),
    );

    axum::Server::bind(&([127, 0, 0, 1], 3000).into())
        .serve(app.into_make_service())
        .await
        .unwrap();
}
```

Test it with:  
```sh
$ curl "http://127.0.0.1:3000/greet?name=Het"
```



## 🔒 Handling Authentication and Security 

- **JWT (JSON Web Tokens)**: For user authentication.  
- **OAuth**: Integrate with third-party services like Google or GitHub.  
- **HTTPS**: Use TLS to encrypt communication.  

### Example: Middleware for Authentication  

```rust
use actix_web::{dev::ServiceRequest, Error, HttpMessage};
use actix

_web_httpauth::middleware::HttpAuthentication;

async fn validator(req: ServiceRequest, _: actix_web::dev::Payload) -> Result<ServiceRequest, Error> {
    if let Some(auth_header) = req.headers().get("Authorization") {
        if auth_header == "Bearer secret-token" {
            return Ok(req);
        }
    }
    Err(actix_web::error::ErrorUnauthorized("Unauthorized"))
}

App::new().wrap(HttpAuthentication::with_fn(validator));
```

Middleware allows you to intercept requests or responses to add extra behavior like logging or authentication.  

### <div align="center">_*or*_</div>


Middleware allows us to apply transformations, authentication, or logging.  

## 🔑 Adding Middleware  

```rust
use axum::{middleware, routing::get, Router};

async fn log_middleware<B>(req: axum::http::Request<B>) -> axum::http::Request<B> {
    println!("Request: {:?}", req);
    req
}

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/", get(|| async { "Home Page" }))
        .layer(middleware::from_fn(log_middleware));

    axum::Server::bind(&([127, 0, 0, 1], 3000).into())
        .serve(app.into_make_service())
        .await
        .unwrap();
}
```


## 🔑 Adding Middleware  

```rust
use axum::{middleware, routing::get, Router};
use tower_http::trace::TraceLayer;

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/", get(|| async { "Hello, Middleware!" }))
        .layer(TraceLayer::new_for_http());

    axum::Server::bind(&([127, 0, 0, 1], 3000).into())
        .serve(app.into_make_service())
        .await
        .unwrap();
}
```

## 📲 Adding Authentication  

You can handle token-based authentication using extractors:  

```rust
use axum::{extract::Extension, middleware, routing::get, Router};

async fn check_auth<B>(
    req: axum::http::Request<B>,
) -> Result<axum::http::Request<B>, axum::http::Response<axum::body::Body>> {
    if let Some(auth) = req.headers().get("Authorization") {
        if auth == "Bearer mysecrettoken" {
            return Ok(req);
        }
    }
    Err(axum::http::Response::builder()
        .status(401)
        .body("Unauthorized".into())
        .unwrap())
}

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/", get(|| async { "Secure Zone!" }))
        .layer(middleware::from_fn(check_auth));

    axum::Server::bind(&([127, 0, 0, 1], 3000).into())
        .serve(app.into_make_service())
        .await
        .unwrap();
}
```


## 🔐 Securing the Server  

Securing your server involves implementing HTTPS and robust authentication mechanisms. Here's a detailed guide with examples:

#### **1. Using HTTPS with TLS**  
HTTPS ensures that the communication between your server and clients is encrypted, preventing data interception and tampering. In Rust, you can use libraries like `hyper-rustls` or `rustls` to add TLS (Transport Layer Security) support.

##### **Steps to Add HTTPS:**
1. **Install Dependencies**  
   Add the required crates to your `Cargo.toml` file:
   ```toml
   [dependencies]
   hyper = "0.14"
   hyper-rustls = "0.23"
   tokio = { version = "1", features = ["full"] }
   ```
2. **Generate SSL Certificates**  
   Use tools like **Let's Encrypt** or **OpenSSL** to create certificates.  
   For development purposes, generate self-signed certificates:  
   ```bash
   openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
   ```
   This creates `key.pem` (private key) and `cert.pem` (certificate).

3. **Set Up the TLS Configuration**  
   Here's an example of a basic HTTPS server using `hyper` and `hyper-rustls`:
   ```rust
   use hyper::service::{make_service_fn, service_fn};
   use hyper::{Body, Request, Response, Server};
   use hyper_rustls::{HttpsConnectorBuilder, ServerConfig};
   use std::sync::Arc;
   use tokio::fs::read;

   async fn handle_request(_req: Request<Body>) -> Result<Response<Body>, hyper::Error> {
       Ok(Response::new(Body::from("Hello, HTTPS World!")))
   }

   #[tokio::main]
   async fn main() -> Result<(), Box<dyn std::error::Error>> {
       // Load SSL certificates
       let certs = read("cert.pem").await?;
       let key = read("key.pem").await?;

       let tls_config = ServerConfig::builder()
           .with_safe_defaults()
           .with_no_client_auth()
           .with_single_cert(certs, key)?;

       let tls_acceptor = Arc::new(tls_config);

       let addr = ([127, 0, 0, 1], 443).into();

       let make_svc = make_service_fn(|_conn| async { Ok::<_, hyper::Error>(service_fn(handle_request)) });

       let server = Server::builder(HttpsConnectorBuilder::new(tls_acceptor).build())
           .serve(make_svc);

       println!("HTTPS Server running on https://{}", addr);
       server.await?;

       Ok(())
   }
   ```
   This server listens on port 443 and serves encrypted content using HTTPS.


#### **2. Adding Authentication**  
Authentication ensures only authorized users can access certain parts of your application.

##### **Option 1: Basic Authentication**  
Basic Authentication sends a username and password with each request (over HTTPS).  
Example:
```rust
use hyper::{header, Body, Request, Response, StatusCode};

async fn handle_request(req: Request<Body>) -> Result<Response<Body>, hyper::Error> {
    if let Some(auth) = req.headers().get(header::AUTHORIZATION) {
        if auth == "Basic dXNlcjpwYXNzd29yZA==" { // user:password base64
            return Ok(Response::new(Body::from("Welcome, authenticated user!")));
        }
    }
    let mut response = Response::new(Body::from("Unauthorized"));
    *response.status_mut() = StatusCode::UNAUTHORIZED;
    Ok(response)
}
```

##### **Option 2: Token-Based Authentication (JWT)**  
JWT (JSON Web Tokens) are a more secure and scalable way to handle authentication.

1. **Add Dependencies**:  
   ```toml
   [dependencies]
   jsonwebtoken = "8"
   serde = { version = "1.0", features = ["derive"] }
   ```
2. **Generate and Verify Tokens**:  
   Example:
   ```rust
   use jsonwebtoken::{encode, decode, Header, Algorithm, Validation, EncodingKey, DecodingKey};
   use serde::{Serialize, Deserialize};

   #[derive(Debug, Serialize, Deserialize)]
   struct Claims {
       sub: String,
       exp: usize,
   }

   fn generate_jwt() -> String {
       let my_claims = Claims { sub: "user1".to_owned(), exp: 10000000000 };
       encode(&Header::default(), &my_claims, &EncodingKey::from_secret("secret".as_ref())).unwrap()
   }

   fn verify_jwt(token: &str) -> bool {
       decode::<Claims>(token, &DecodingKey::from_secret("secret".as_ref()), &Validation::new(Algorithm::HS256)).is_ok()
   }

   fn main() {
       let token = generate_jwt();
       println!("Generated JWT: {}", token);

       let is_valid = verify_jwt(&token);
       println!("Token is valid: {}", is_valid);
   }
   ```
3. Use JWT in Headers for Secure Communication.

#### **Practices for Security**  
- Always use HTTPS in production.  
- Store secrets securely (e.g., use environment variables).  
- Use well-tested libraries for authentication.  
- Regularly update dependencies to patch vulnerabilities.  

## 📦 Working with JSON and APIs  

## 📤 Building REST APIs  

Develop endpoints for CRUD operations:  

```rust
use axum::{routing::get, Router, Json};
use serde::{Deserialize, Serialize};

#[derive(Serialize)]
struct User {
    id: u32,
    name: String,
}

async fn get_user() -> Json<User> {
    Json(User {
        id: 1,
        name: "Het Patel".to_string(),
    })
}

#[tokio::main]
async fn main() {
    let app = Router::new().route("/user", get(get_user));

    axum::Server::bind(&([127, 0, 0, 1], 3000).into())
        .serve(app.into_make_service())
        .await
        .unwrap();
}
```

## 📡 REST APIs  

REST APIs are integral to web development. Use `serde` for JSON serialization/deserialization.  

### Creating a REST API  

```rust
use axum::{extract::Json, routing::post, Router};
use serde::Deserialize;

#[derive(Deserialize)]
struct CreateUser {
    name: String,
}

async fn create_user(Json(payload): Json<CreateUser>) -> String {
    format!("User {} created", payload.name)
}

#[tokio::main]
async fn main() {
    let app = Router::new().route("/user", post(create_user));

    axum::Server::bind(&([127, 0, 0, 1], 3000).into())
        .serve(app.into_make_service())
        .await
        .unwrap();
}
```

## 📥 Handling JSON Payloads  

```rust
#[derive(Deserialize)]


struct CreateUser {
    name: String,
}

async fn create_user(Json(payload): Json<CreateUser>) -> String {
    format!("User {} created", payload.name)
}
```

## 🌐 Building a Simple Full-Stack Application  

Let’s take it up a notch! 🚀 Here's how to integrate **Rust** for your backend and use **React** or **Vue.js** for the frontend. We'll create a **TODO App** as an example.  

### Backend: REST API with Rust  
We'll use `axum` for routing and `serde` for JSON serialization.  

1. **Setup a POST endpoint to add a task:**  
    ```rust
    use axum::{extract::Json, routing::post, Router};
    use serde::{Deserialize, Serialize};

    #[derive(Deserialize, Serialize)]
    struct Task {
        id: usize,
        title: String,
        completed: bool,
    }

    async fn add_task(Json(task): Json<Task>) -> Json<Task> {
        // Ideally, store tasks in a database; here, we'll just return it.
        Json(task)
    }

    #[tokio::main]
    async fn main() {
        let app = Router::new().route("/add_task", post(add_task));

        axum::Server::bind(&([127, 0, 0, 1], 3000).into())
            .serve(app.into_make_service())
            .await
            .unwrap();
    }
    ```

2. **Frontend: Call the API**  
    Using `fetch` or `axios` in React:  
    ```javascript
    async function addTask(task) {
        const response = await fetch("http://127.0.0.1:3000/add_task", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(task),
        });
        const data = await response.json();
        console.log(data);
    }
    ```

3. **Test the Integration:**  
    Use `Postman` or the browser console to ensure the backend and frontend are talking smoothly.  


## 📚 Popular Web Frameworks  

Rust has several web frameworks to choose from, each with its unique strengths.  



### **1️⃣ Actix Web**  

- **Features**:  
  - Highly performant and scalable.  
  - Built on the powerful `actix` actor framework.  
  - Supports middleware, websockets, and async operations.  

- **Use Case**:  
  - Ideal for building large-scale, production-grade APIs.  

```rust
use actix_web::{web, App, HttpServer, Responder};

async fn greet() -> impl Responder {
    "Hello, World!"
}

#[tokio::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new().route("/", web::get().to(greet))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
```



### **2️⃣ Rocket**  

- **Features**:  
  - Simple, intuitive, and batteries-included.  
  - Focuses on developer productivity.  
  - Built-in support for templating and JSON.  

- **Use Case**:  
  - Quick prototyping or building RESTful APIs.  

```rust
#[macro_use] extern crate rocket;

#[get("/")]
fn index() -> &'static str {
    "Welcome to Rocket!"
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![index])
}
```



### **3️⃣ Warp**  

- **Features**:  
  - Lightweight, functional-style framework.  
  - Built on `hyper` for speed and async capabilities.  
  - Powerful composability with filters.  

- **Use Case**:  
  - Microservices and serverless APIs.  

```rust
use warp::Filter;

#[tokio::main]
async fn main() {
    let route = warp::path!("hello" / String)
        .map(|name| format!("Hello, {}!", name));

    warp::serve(route)
        .run(([127, 0, 0, 1], 3030))
        .await;
}
```


### **4️⃣ Axum**  

- **Features**:  
  - Designed for ergonomics and performance.  
  - Leverages `tokio` and `tower` for async and middleware.  

- **Use Case**:  
  - A balance between simplicity and scalability.  

```rust
use axum::{Router, routing::get};

async fn handler() -> &'static str {
    "Welcome to Axum!"
}

#[tokio::main]
async fn main() {
    let app = Router::new().route("/", get(handler));
    axum::Server::bind(&"127.0.0.1:4000".parse().unwrap())
        .serve(app.into_make_service())
        .await
        .unwrap();
}
```


## 🛠️ Building a Simple Web Server  

Let’s build a **basic REST API** with Actix Web.  

### Steps:  

1. **Setup Project**:  
   Add dependencies to `Cargo.toml`:  
   ```toml
   [dependencies]
   actix-web = "4.0"
   serde = { version = "1.0", features = ["derive"] }
   ```

2. **Define API Endpoints**:  

```rust
use actix_web::{web, App, HttpServer, Responder};
use serde::Serialize;

#[derive(Serialize)]
struct Message {
    text: String,
}

async fn hello() -> impl Responder {
    web::Json(Message { text: "Hello, Actix!".to_string() })
}

#[tokio::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new().route("/hello", web::get().to(hello))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
```

3. **Run and Test**:  
   Start the server and access the endpoint at `http://127.0.0.1:8080/hello`.  



## 🌟 Exploring APIs and Routes  

1. **Dynamic Routing**:  

```rust
async fn greet(name: web::Path<String>) -> impl Responder {
    format!("Hello, {}!", name)
}

App::new().route("/greet/{name}", web::get().to(greet));
```

2. **Middleware**:  
   Add logging, authentication, or custom behavior.  

```rust
use actix_web::middleware::Logger;

App::new()
    .wrap(Logger::default())
    .route("/", web::get().to(index));
```



## 🗄️ Database Integration  

Rust provides great database support through libraries like:  
- **Diesel**: Strongly-typed ORM.  
- **SQLx**: Async and lightweight.  

### Example with SQLx:  

```rust
use sqlx::sqlite::SqlitePool;

#[tokio::main]
async fn main() -> Result<(), sqlx::Error> {
    let pool = SqlitePool::connect("sqlite::memory:").await?;

    sqlx::query("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
        .execute(&pool)
        .await?;

    sqlx::query("INSERT INTO users (name) VALUES ('Alice')")
        .execute(&pool)
        .await?;

    let row: (i64, String) = sqlx::query_as("SELECT id, name FROM users WHERE name = 'Alice'")
        .fetch_one(&pool)
        .await?;

    println!("User: {} with ID {}", row.1, row.0);
    Ok(())
}
```


## 🚀 Deploying Rust Web Applications  

1. **Containerization**: Use Docker to package your application.  
2. **Hosting**:  
   - Cloud services like AWS, Azure, or DigitalOcean.  
   - Serverless platforms like Fly.io or Vercel.  

### Example Dockerfile:  

```dockerfile
FROM rust:1.72 as builder
WORKDIR /app
COPY . .
RUN cargo build --release

FROM debian:buster
WORKDIR /app
COPY --from=builder /app/target/release/my-app .
CMD ["./my-app"]
```



## 🎯 Hands-On Challenge  

Put your skills to the test with these hands-on challenges for **Day 23**!  

### Challenge: Blog Backend 📝  
Build a simple blog backend that supports:  
1. Adding blog posts (POST).  
2. Viewing all posts (GET).  
3. Deleting posts by ID (DELETE).  

**Bonus:** Implement an in-memory database (e.g., `HashMap`) to store the posts temporarily.  

Build a simple blog backend with Rust:  
- Define routes for **post creation**, **retrieval**, and **deletion**.  
- Use **JSON** to manage posts.  
1. Build a RESTful API that includes CRUD operations for a `Book` resource.  
2. Integrate an SQLite database for storing books.  
3. Secure your API with basic JWT authentication.  


## 💻 Exercises - Day 23  

### ✅ Exercise: Level 1
- Set up a basic Rust web server with `axum`.  
- Add routes for `/` and `/hello`.  
- Display a JSON response on a `/data` route.  



### 🚀 Exercise: Level 2
- Build a REST API to manage a **User Registry**:  
  - Add a user (POST).  
  - List all users (GET).  
  - Update a user's details (PUT).  
  - Delete a user (DELETE).  



### 🏆 Exercise: Level 3 (Advanced)
- Build a **secure full-stack application**:  
  - Backend: Use Rust to create a CRUD API for tasks with authentication middleware.  
  - Frontend: Use **React** or **Vue.js** for a responsive UI.  
  - Use Docker to containerize the application.  

**Bonus Challenge:** Implement OAuth2 login (e.g., Google Sign-In) for your application.  



## 🎥 Helpful Video References  

Boost your learning with these handpicked video tutorials:  

1. **[Rust Web Development with Axum](https://www.youtube.com/watch?v=XZtlD_m59sM)** - A beginner-friendly introduction to building web apps with Axum.  
2. **[Building REST APIs in Rust](https://www.youtube.com/watch?v=vhNoiBOuW94)** - Covers advanced REST API concepts.  
3. **[Rust Async Programming Demystified](https://youtube.com/playlist?list=PLJEZDlUEtOf4zr5cBDdt3DP7QLEd55S38&si=zgo3_VWemLca7JBW)** - Learn async programming in Rust to handle concurrent requests.  
4. **[Integrating Rust with React Frontend](https://youtube.com/playlist?list=PLmWYh0f8jKSjt9VC5sq2T3mFETasG2p2L&si=ZE-Mx2H3jGo_a2G3)** - Full-stack development using Rust and React.  



## 📚 Further Reading  

For those eager to dive deeper, here are some valuable resources:  

1. **[Official Axum Documentation](https://docs.rs/axum/latest/axum/)**  
   Comprehensive guide on building apps with Axum.  
2. **[Rust Web Development Handbook]([https://rustwebdev.com/](https://github.com/PacktPublishing/Rust-Web-Programming-2nd-Edition))**  
   A comprehensive guide to building scalable and efficient web applications with Rust development.
3. **[The Tower Library](https://github.com/tower-rs/tower)**  
   Middleware library for building scalable web services.  
4. **[Tokio Async Runtime](https://tokio.rs/)**  
   Master Rust's async ecosystem with Tokio.  
5. **[Understanding Actix Web](https://actix.rs/)**  
   Learn another popular Rust web framework.  



## 📝 Day 23 Summary  

Today, we explored the fascinating world of **web development with Rust**:  
- Learned about popular frameworks like Actix Web, Rocket, Warp, and Axum.  
- Built a simple REST API.  
- Integrated a database using SQLx.  
- Explored authentication and security best practices.  
- Discussed deployment strategies for Rust web applications.  

Rust empowers developers to build fast, secure, and scalable web apps. Practice the hands-on challenges to solidify your knowledge!  

Stay tuned for **Day 24**, where we will explore **Integrating with C/C++ in Rust** in Rust! 🚀

🌟 _Great job on completing Day 23! Keep practicing, and get ready for Day 24!_

Thank you for joining **Day 23** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 22](../22_Building%20CLI%20Applications/22_building_cli_applications.md) | [Day 24 >>](../24_Integrating_with_C_C%2B%2B/24_integrating_with_c_c%2B%2B.md)  

---
