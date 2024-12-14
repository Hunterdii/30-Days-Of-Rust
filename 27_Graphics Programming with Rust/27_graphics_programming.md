<div align="center">
  <h1>🦀 30 Days of Rust: Day 27 - Graphics Programming with Rust 🎨 </h1>
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

[<< Day 26](../26_Rust%20and%20WebAssembly/26_rust_and_webassembly.md) | [Day 28 >>](../28_Game%20Development%20with%20Rust/28_game_development_with_rust.md)  


![30DaysOfRust](https://github.com/user-attachments/assets/a1083fb3-3eec-4d1e-b93a-fa4d7a99f180)

- [📘 Day 27 - Graphics Programming with Rust 🎨](#-day-27graphics-programming-with-rust-)
  - [👋 Welcome](#-welcome)  
  - [🎨 What is Graphics Programming?](#-what-is-graphics-programming)
  - [🛠 Tools and Libraries for Graphics in Rust](#-tools-and-libraries-for-graphics-in-rust)  
  - [🛠️ Why Use Rust for Graphics Programming?](#️-why-use-rust-for-graphics-programming)  
  - [🔧 Setting Up a Rust Graphics Project](#-setting-up-a-rust-graphics-project)
  - [📦 Adding Graphics Libraries](#-adding-graphics-libraries)  
  - [🎬 Your First Rust Graphics Program](#-your-first-rust-graphics-program)  
    - [1. Drawing a Window with `winit`](#1-drawing-a-window-with-winit)  
    - [2. Adding Shapes with `pixels`](#2-adding-shapes-with-pixels)  
  - [🖌 Key Concepts in Rust Graphics](#-key-concepts-in-rust-graphics)  
    - [💡 Game Loops and Rendering](#-game-loops-and-rendering)  
    - [📊 Framebuffers](#-framebuffers)
  - [📦 Libraries and Frameworks for Graphics in Rust](#-libraries-and-frameworks-for-graphics-in-rust)  
    - [1. WGPU ⚙️](#1-wgpu)  
    - [2. SDL2 🎮](#2-sdl2)  
    - [3. OpenGL with Glium 💻](#3-opengl-with-glium)  
  - [🖌️ Creating a Basic Graphics Application](#️-creating-a-basic-graphics-application)  
    - [1. Using WGPU 🎨](#1-using-wgpu)  
    - [2. Using Glium 🖼️](#2-using-glium)
  - [🎮 Working with 2D Graphics in Rust](#-working-with-2d-graphics-in-rust)
  - [⚡ Advanced Graphics Topics](#-advanced-graphics-topics)  
    - [1. Shaders ✨](#1-shaders)  
    - [2. Textures 🖼️](#2-textures)  
    - [3. 3D Rendering 🏞️](#3-3d-rendering)  
  - [🚀 Hands-On Challenge](#-hands-on-challenge)
  - [💻 Exercises - Day 27](#-exercises---day-27)
    - [✅ Exercise: Level 1](#-exercise-level-1)
    - [🚀 Exercise: Level 2](#-exercise-level-2)
    - [🏆 Exercise: Level 3 (Advanced)](#-exercise-level-3-advanced)
  - [🎥 Helpful Video References](#-helpful-video-references)
  - [📚 Further Reading](#-further-reading)
  - [📝 Day 27 Summary](#day-27-summary)  




# 📘 Day 27 - Graphics Programming with Rust 🎨

Welcome to **Day 27** of the **30 Days of Rust Challenge**! 🎉  

Today, we explore **Graphics Programming with Rust**, combining performance, control, and expressive code to create visual experiences. Whether you're building a game, a simulation, or a visualizer, Rust has a growing ecosystem of tools and libraries for graphics programming.  


## 👋 Welcome  

Welcome to **Day 27** of the **30 Days of Rust Challenge**! 🎉  

By the end of today, you will:  
- Learn why Rust is a fantastic choice for graphics programming.  
- Explore libraries like `winit`, `pixels`, `wgpu`, and `bevy`.  
- Set up a simple Rust environment for graphics development.  
- Write a basic program that opens a window and renders shapes.  


## 🎨 What is Graphics Programming?  

Rust is an excellent choice for graphics programming because:

| **Feature**                | **Rust**                                  | **C/C++**                      |
|----------------------------|-------------------------------------------|--------------------------------|
| **Memory Safety**           | No null pointer dereferencing, no data races | Manual memory management       |
| **Concurrency**             | Fearless concurrency with ownership model  | Prone to race conditions       |
| **Performance**             | Zero-cost abstractions for minimal overhead | High, but requires manual optimization |
| **Tooling**                 | Cargo, Clippy, Rustfmt                    | Less standardized              |

Rust offers the performance of low-level languages with the safety of modern tools. The language’s memory safety ensures there are no unexpected crashes or memory leaks, making it ideal for graphics programming.

Graphics programming involves:  
- Drawing shapes, images, or animations on a screen.  
- Using specialized hardware like GPUs to render visual content.  
- Managing resources like textures, shaders, and framebuffers.  

It’s widely used in:  
- Game development.  
- Data visualization.  
- User interface design.  

## 🛠 Tools and Libraries for Graphics in Rust  

Here are the most popular tools and libraries for graphics programming:  

| **Library**      | **Description**                                               |  
|-|-|  
| **`winit`**       | Cross-platform window creation and input handling.            |  
| **`pixels`**      | Hardware-accelerated 2D graphics in Rust.                     |  
| **`wgpu`**        | Native cross-platform graphics API for high-performance 3D.   |  
| **`bevy`**        | Modern game engine with ECS architecture.                     |  
| **`glium`**       | Safe OpenGL bindings for Rust.                                |  



## 🛠️ Why Use Rust for Graphics Programming?  

Rust is an excellent choice for graphics programming because:  

1. **Performance**: Rust’s memory safety and zero-cost abstractions allow efficient GPU utilization.  
2. **Concurrency**: Rust’s ownership model simplifies multi-threaded rendering.  
3. **Cross-Platform Support**: Many Rust graphics libraries support Windows, macOS, Linux, and even WebAssembly.  
4. **Thriving Ecosystem**: Libraries like `wgpu`, `glium`, and `sdl2` make graphics development accessible.  

Rust's powerful features like memory safety, performance, and low-level control make it an excellent choice for graphics programming.  

### Key Advantages:  
1. **High Performance**: Ideal for rendering graphics in real-time.  
2. **Memory Safety**: Prevents crashes and unsafe memory access during rendering.  
3. **Cross-Platform**: Write once, run anywhere with libraries like `wgpu`.  
4. **Modern Tools**: Use libraries like `winit` for window management and `pixels` for pixel-level control.  

Rust's growing community and active ecosystem make it easier than ever to get started with graphics programming.  



## 🔧 Setting Up a Rust Graphics Project  

Before diving into graphics programming, make sure your environment is ready. Here's how to set up Rust for graphics:

- **Install Rust**: Install Rust via [rust-lang.org](https://www.rust-lang.org/tools/install).
- **Configure Dependencies**: You'll need to configure the necessary libraries, such as `wgpu` (WebGPU), `glium` (OpenGL bindings), or `piston_window` (2D library).
- **Create a New Project**: Initialize a new project with `cargo new graphics_project --bin`.
  
1. **Install Rust**: Ensure you have the latest Rust version:  
   ```bash
   rustup update
   ```

2. **Create a New Project**:  
   ```bash
   cargo new graphics_example --bin
   cd graphics_example
   ```

3. **Choose a Graphics Library**: Add your preferred library as a dependency in `Cargo.toml`.  


## 📦 Adding Graphics Libraries  

To get started with graphics programming in Rust, we’ll use a few essential libraries. The main libraries you’ll need are:

1. **winit**: A cross-platform window creation library that handles input events.
2. **pixels**: A simple 2D rendering library that allows you to manipulate pixels directly on the screen.

### Steps to Add Libraries to Your Project:

1. First, create a new Rust project if you haven’t already:
    ```bash
    cargo new rust_graphics --bin
    cd rust_graphics
    ```

2. Then, open your `Cargo.toml` file and add the dependencies:
    ```toml
    [dependencies]
    winit = "0.27"
    pixels = "0.11"
    ```

Now, your project is ready to start rendering graphics with these two libraries!


## 🎬 Your First Rust Graphics Program

### 1. Drawing a Window with `winit`

The first step in creating a graphical program is setting up a window. `winit` is a Rust crate that helps you create a window on your system. Here’s how to set up a basic window.

#### Step-by-Step Code:
```rust
use winit::{
    event::{Event, WindowEvent},
    event_loop::{ControlFlow, EventLoop},
    window::WindowBuilder,
};

fn main() {
    // Create an event loop
    let event_loop = EventLoop::new();
    
    // Build the window
    let window = WindowBuilder::new()
        .with_title("Rust Graphics Window")
        .build(&event_loop)
        .unwrap();

    // Run the event loop to listen for window events
    event_loop.run(move |event, _, control_flow| {
        // Set the control flow to wait for events
        *control_flow = ControlFlow::Wait;

        // Handle the window close event
        match event {
            Event::WindowEvent {
                event: WindowEvent::CloseRequested,
                ..
            } => *control_flow = ControlFlow::Exit,
            _ => (),
        }
    });
}
```

#### Explanation:
- **`winit::EventLoop`**: This handles events like mouse clicks or keyboard presses.
- **`WindowBuilder::new()`**: Creates a new window with the specified properties, such as the title.
- **`Event::WindowEvent::CloseRequested`**: Listens for the window close event, which will exit the event loop.



### 2. Adding Shapes with `pixels`

Now that we have a window, let’s render some basic shapes. The `pixels` crate provides an easy way to directly manipulate the pixel data of the window.

#### Step-by-Step Code:
```rust
use pixels::{Pixels, SurfaceTexture};
use winit::{
    dpi::LogicalSize,
    event::{Event, WindowEvent},
    event_loop::{ControlFlow, EventLoop},
    window::WindowBuilder,
};

fn main() {
    // Set up the event loop and window
    let event_loop = EventLoop::new();
    let window = WindowBuilder::new()
        .with_inner_size(LogicalSize::new(800, 600)) // Set window size
        .with_title("Rust Graphics with Pixels") // Set window title
        .build(&event_loop)
        .unwrap();

    // Create a texture for the window surface
    let window_size = window.inner_size();
    let surface_texture = SurfaceTexture::new(window_size.width, window_size.height, &window);
    
    // Initialize pixels rendering
    let mut pixels = Pixels::new(800, 600, surface_texture).unwrap();

    event_loop.run(move |event, _, control_flow| {
        // Set the control flow to wait for events
        *control_flow = ControlFlow::Wait;
        
        match event {
            // Redraw the window
            Event::RedrawRequested(_) => {
                let frame = pixels.get_frame();
                // Fill the frame with a solid color (RGBA)
                for pixel in frame.chunks_exact_mut(4) {
                    pixel.copy_from_slice(&[0x00, 0x80, 0x80, 0xFF]); // Teal color (R, G, B, A)
                }
                // Render the frame to the window
                pixels.render().unwrap();
            }
            // Handle the close event
            Event::WindowEvent {
                event: WindowEvent::CloseRequested,
                ..
            } => *control_flow = ControlFlow::Exit,
            _ => (),
        }
    });
}
```

#### Explanation:
- **`SurfaceTexture`**: This handles the pixel buffer that will be rendered onto the window.
- **`pixels.get_frame()`**: Fetches the frame where pixel data is written.
- **`pixels.render()`**: Renders the frame to the window.

In this example, we're rendering a solid teal color. You can modify the pixel array to draw shapes or create more complex visuals.


## 🖌 Key Concepts in Rust Graphics

## 💡 Game Loops and Rendering

A **game loop** is a core concept in graphics programming. It’s responsible for updating the state of the application (e.g., animations, movements) and rendering the new state to the screen.

- **Rendering** is the process of converting data (like shapes, textures, etc.) into visual images.
- Rust makes it efficient to implement game loops by providing low-level access to performance-critical areas such as memory and concurrency.

## 📊 Framebuffers

A **framebuffer** is a block of memory that holds the pixel data of the screen. This is where the graphics are stored before they’re displayed. In the `pixels` library, the framebuffer is automatically managed, but you can manipulate it directly for custom effects.


## 📦 Libraries and Frameworks for Graphics in Rust

Rust has a rich ecosystem of libraries and frameworks for graphics programming. Here are some of the most commonly used ones:

## 1. WGPU ⚙️

**WGPU** is a high-performance, low-level graphics API designed for Rust. It is the Rust binding for the WebGPU API, which provides access to modern graphics hardware. WGPU is great for both 2D and 3D rendering, and is widely used in game development, simulations, and GPU-intensive applications.

#### Features:
- Cross-platform (supports Windows, macOS, Linux, and WebAssembly)
- Rust-native bindings, designed for modern GPUs
- Suitable for 2D and 3D rendering

## 2. SDL2 🎮

**SDL2** (Simple DirectMedia Layer) is a popular multimedia library. It provides a simple API for video, audio, and input. In Rust, `sdl2` crate provides bindings to the SDL2 library, making it easy to create 2D games or multimedia applications.

#### Features:
- Handles graphics, sound, and input
- Cross-platform support
- Popular in game development for its simplicity and performance

## 3. OpenGL with Glium 💻

**Glium** is a safe and modern OpenGL wrapper in Rust. It simplifies the process of using OpenGL in Rust and provides a high-level API to interact with OpenGL. Glium is best used for 3D graphics programming and rendering.

#### Features:
- Provides access to OpenGL through a Rust-safe API
- Suitable for complex 3D graphics applications
- Allows fine-grained control over rendering pipelines

### <div align="center">_*or*_</div>

Rust has several libraries to help with graphics programming:

- **wgpu**: A modern graphics API in Rust for high-performance 3D graphics.
- **glium**: Safe OpenGL bindings for Rust, great for 3D rendering.
- **piston_window**: Easy-to-use 2D graphics library.
- **ash**: Low-level Vulkan bindings for Rust.
- **glutin**: A library for managing windows and OpenGL contexts.

For more details, check out their [documentation](https://docs.rs/).


## 🖌️ Creating a Basic Graphics Application

Here, we’ll explore how to create a basic graphics application using some of the libraries mentioned above, focusing on **WGPU** and **Glium**.

## 1. Using WGPU 🎨

WGPU is a modern choice for creating graphics applications in Rust. Let’s walk through creating a basic application using WGPU.

#### Steps:
1. Add the WGPU crate to your `Cargo.toml`:
    ```toml
    [dependencies]
    wgpu = "0.12"
    winit = "0.27"
    ```

2. Set up the application to create a window and initialize WGPU for rendering:
    ```rust
    use winit::{
        event::{Event, WindowEvent},
        event_loop::{ControlFlow, EventLoop},
        window::WindowBuilder,
    };
    use wgpu::util::DeviceExt;

    fn main() {
        let event_loop = EventLoop::new();
        let window = WindowBuilder::new()
            .with_title("WGPU Graphics App")
            .build(&event_loop)
            .unwrap();

        let instance = wgpu::Instance::new(wgpu::Backends::all());
        let surface = unsafe { instance.create_surface(&window) };
        let adapter = block_on(instance.request_adapter(&wgpu::RequestAdapterOptions {
            power_preference: wgpu::PowerPreference::HighPerformance,
            compatible_surface: Some(&surface),
        }))
        .unwrap();
        
        let (device, queue) = block_on(adapter.request_device(&wgpu::DeviceDescriptor {
            features: wgpu::Features::empty(),
            limits: wgpu::Limits::default(),
            shader_validation: true,
        }))
        .unwrap();
        
        // Continue with setup for shaders, pipelines, and rendering loops...
    }
    ```

This basic setup initializes WGPU for rendering, but you can extend it by adding shaders and pipelines for more complex graphics rendering.

## 2. Using Glium 🖼️

If you prefer to use OpenGL, Glium is a great choice. Here’s how to set up a basic application:

1. Add the Glium crate to your `Cargo.toml`:
    ```toml
    [dependencies]
    glium = "0.32"
    ```

2. Set up the window and OpenGL context:
    ```rust
    use glium::{Display, Surface};
    use glium::glutin::event_loop::EventLoop;
    use glium::glutin::window::WindowBuilder;

    fn main() {
        let event_loop = EventLoop::new();
        let window_builder = WindowBuilder::new().with_title("Glium Graphics App");
        let display = Display::new(window_builder, event_loop).unwrap();

        let mut target = display.draw();
        target.clear_color(0.0, 0.0, 1.0, 1.0); // Clear to blue
        target.finish().unwrap();
    }
    ```

This creates a window and clears the screen with a blue color. From here, you can add more advanced OpenGL features like shaders, textures, and more complex rendering.

### <div align="center">_*or*_</div>

### 1. Using WGPU  

**`src/main.rs`:**  
```rust
use winit::{event::*, event_loop::EventLoop, window::WindowBuilder};

fn main() {
    // Create a window
    let event_loop = EventLoop::new();
    let window = WindowBuilder::new().build(&event_loop).unwrap();

    event_loop.run(move |event, _, control_flow| {
        *control_flow = winit::event_loop::ControlFlow::Wait;
        match event {
            Event::WindowEvent { event, .. } => match event {
                WindowEvent::CloseRequested => *control_flow = ControlFlow::Exit,
                _ => (),
            },
            _ => (),
        }
    });
}
```

This creates a simple window using `winit`, a library compatible with `wgpu`.  

### 2. Using Glium  

**`src/main.rs`:**  
```rust
use glium::{glutin, Surface};

fn main() {
    // Create a display
    let event_loop = glutin::event_loop::EventLoop::new();
    let wb = glutin::window::WindowBuilder::new();
    let cb = glutin::ContextBuilder::new();
    let display = glium::Display::new(wb, cb, &event_loop).unwrap();

    event_loop.run(move |event, _, control_flow| {
        *control_flow = glutin::event_loop::ControlFlow::Wait;

        match event {
            glutin::event::Event::WindowEvent { event, .. } => match event {
                glutin::event::WindowEvent::CloseRequested => *control_flow = glutin::event_loop::ControlFlow::Exit,
                _ => (),
            },
            _ => (),
        }

        // Clear the screen
        let mut target = display.draw();
        target.clear_color(0.0, 0.0, 1.0, 1.0); // Blue background
        target.finish().unwrap();
    });
}
```

This creates a blue window using `glium` and OpenGL.  

## **🎮 Working with 2D Graphics in Rust**

2D graphics form the foundation of many games and interactive applications. Here’s how to get started with 2D graphics in Rust:

- **piston_window**: A simple library for 2D games. It handles window management, input, and graphics rendering.
- **Basic Setup**: Load an image, set up a window, and draw simple shapes like rectangles and circles.
- **Example Code**:
  ```rust
  use piston_window::*;
  
  fn main() {
      let mut window: PistonWindow = WindowSettings::new("2D Graphics", [800, 600])
          .exit_on_esc(true)
          .build()
          .unwrap();
  
      while let Some(event) = window.next() {
          window.draw_2d(&event, |c, g, _| {
              clear([1.0, 1.0, 1.0, 1.0], g);
              rectangle([0.0, 0.0, 1.0, 1.0], [200.0, 150.0, 100.0, 100.0], c.transform, g);
          });
      }
  }
  ```
- **Resources**: [Piston Window Docs](https://docs.rs/piston_window/).



## ⚡ Advanced Graphics Topics

Once you are comfortable with the basics, you can dive into more advanced topics like **Shaders**, **Textures**, and **3D Rendering**.

### 1. Shaders ✨

**Shaders** are small programs that run on the GPU. They control the way vertices and pixels are processed, allowing you to create effects like lighting, shadows, and other visual effects.

- **Vertex Shaders**: Handle the transformation of vertex data (position, color, texture coordinates).
- **Fragment Shaders**: Handle the color of each pixel, allowing for custom coloring, lighting effects, and textures.

Example of a simple shader in GLSL (used with OpenGL or WGPU):
```glsl
#version 450

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec4 a_color;

out vec4 fragColor;

void main() {
    fragColor = a_color;
    gl_Position = vec4(a_position, 1.0);
}
```

### <div align="center">_*or*_</div>

### 1. Shaders  

Shaders are small programs that run on the GPU to control rendering.  

Example of a simple vertex and fragment shader:  

**Vertex Shader (`vertex_shader.glsl`):**  
```glsl
#version 450
layout(location = 0) in vec2 position;
void main() {
    gl_Position = vec4(position, 0.0, 1.0);
}
```

**Fragment Shader (`fragment_shader.glsl`):**  
```glsl
#version 450
out vec4 color;
void main() {
    color = vec4(1.0, 0.0, 0.0, 1.0); // Red
}
```


### 2. Textures 🖼️

**Textures** are images applied to surfaces in graphics applications. In Rust, libraries like WGPU and Glium allow you to load and display textures on shapes.

#### Example:
In WGPU, you load textures like this:
```rust
use wgpu::util::DeviceExt;
use image::open;

let img = open("path/to/texture.png").unwrap().to_rgba8();
let texture = device.create_texture_with_data(
    &queue,
    &wgpu::TextureDescriptor {
        size: wgpu::Extent3d {
            width: img.width(),
            height: img.height(),
            depth_or_array_layers: 1,
        },
        mip_level_count: 1,
        sample_count: 1,
        dimension: wgpu::TextureDimension::D2,
        format: wgpu::TextureFormat::Rgba8Unorm,
        usage: wgpu::TextureUsage::SAMPLED | wgpu::TextureUsage::COPY_DST,
        label: Some("texture"),
    },
    &img,
);
```

### 3. 3D Rendering 🏞️

For **3D rendering**, you'll work with matrices, 3D shapes, camera transformations, and shaders to create realistic 3D worlds.

To get started, you’ll need to understand basic concepts like:
- **Projection Matrices**: Define the view of the 3D scene.
- **View Matrices**: Define the camera’s position and orientation.
- **Model Matrices**: Define the position, rotation, and scale of objects.

Using libraries like WGPU and Glium, you can implement these concepts in your application to create complex 3D scenes with lighting, textures, and animations.

Once you have a basic understanding of graphics programming with Rust, you can dive into more advanced topics:

1. **3D Rendering with `wgpu`**: Rust provides powerful libraries for 3D rendering, with `wgpu` being one of the most popular.
2. **Shaders**: Shaders are programs that run on the GPU to compute the color and effects of pixels in the frame. Writing custom shaders can help you create unique effects such as lighting, shadows, and textures.
3. **Physics Engines**: When building games or simulations, you might need to integrate a physics engine. Libraries like `rapier` can help you with collision detection, gravity, and movement in a 2D or 3D space.

## 🚀 Hands-On Challenge  

### Beginner:  
1. Create a 2D application that draws a triangle using `wgpu` or `glium`.  

### Intermediate:  
1. Add a texture to a 2D shape.  
2. Implement basic keyboard controls for interaction.  

### Advanced:  
1. Build a 3D cube that can rotate using a vertex and fragment shader.  
2. Add lighting effects using shaders.  

## 💻 Exercises - Day 27

## ✅ Exercise: Level 1
- Create a program that renders a rectangle on the screen.

## 🚀 Exercise: Level 2
- Experiment with **shaders** to color your shapes.

## 🏆 Exercise: Level 3 (Advanced)
- Implement **camera controls** to move through a 3D scene.

## 🎥 Helpful Video References
- [Rust Graphics Programming - YouTube](https://www.youtube.com/watch?v=example)
- [Rust Shaders - YouTube](https://www.youtube.com/watch?v=example)

## 📚 Further Reading
- [Rust and Graphics Programming](https://www.rust-lang.org/)
- [wgpu Documentation](https://wgpu.rs/)
- [The Book of Shaders](https://thebookofshaders.com/)


## 📝 Day 27 Summary  

Today, you explored:  
- The basics of graphics programming with Rust.  
- Libraries like `wgpu`, `sdl2`, and `glium`.  
- How to create 2D and 3D graphics applications.  

Graphics programming is both challenging and rewarding. Practice the hands-on challenges to deepen your understanding of rendering concepts.  

Stay tuned for **Day 28**, where we will explore **Game Development with Rust** in Rust! 🚀

🌟 _Great job on completing Day 27! Keep practicing, and get ready for Day 28!_

Thank you for joining **Day 27** of the 30 Days of Rust challenge! If you found this helpful, don’t forget to <img src="https://github.com/user-attachments/assets/35f6838c-52f5-4e48-8a98-c5203f8c57e3" style="width:20px; color: #FFD700" alt="Star GIF"> star this repository, share it with your friends, and stay tuned for more exciting lessons ahead!

**Stay Connected**  
📧 **Email**: [Hunterdii](mailto:hunterdii9879@gmail.com)  
🐦 **Twitter**: [@HetPate94938685](https://twitter.com/HetPate94938685)  
🌐 **Website**: [Working On It(Temporary)](https://hunterdii.github.io/Portfolio-Temporary/)

[<< Day 26](../26_Rust%20and%20WebAssembly/26_rust_and_webassembly.md) | [Day 28 >>](../28_Game%20Development%20with%20Rust/28_game_development_with_rust.md)  

---
