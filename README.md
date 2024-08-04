# Hand Gesture Mouse

The Hand Gesture Mouse is an innovative project that allows users to control their computer mouse using hand gestures. This project leverages advanced computer vision techniques and the Mediapipe library for hand tracking, combined with PyAutoGUI for automating the mouse movements. It offers a hands-free interaction experience, enhancing accessibility and providing a novel way to interact with digital devices.

## Project Overview

This project was developed with the goal of exploring alternative input methods that go beyond traditional devices like the mouse and keyboard. By using a webcam, the system detects and tracks hand movements in real-time, converting them into corresponding cursor actions. The implementation is built with efficiency in mind, utilizing lightweight and optimized libraries to ensure real-time performance on standard hardware.

## Key Features

- **Hand Detection and Tracking**: 
  - Implemented using Mediapipe, which provides robust, real-time hand detection and tracking capabilities. The choice of Mediapipe was due to its highly optimized pre-built models that ensure low-latency and accurate tracking.
  - The HandTrackingModule.py script encapsulates the hand tracking functionality, providing easy integration and customization for further development.

- **Gesture Recognition for Mouse Control**:
  - Specific hand gestures are mapped to common mouse actions, such as moving the cursor, clicking, and scrolling. The AiVirtualMouseProject.py script processes the hand tracking data and triggers corresponding PyAutoGUI functions.
  - PyAutoGUI was chosen for its simplicity and versatility in automating GUI interactions across multiple platforms. It seamlessly integrates with the hand tracking data to perform mouse actions.

- **Real-Time Processing**:
  - The system processes video frames from the webcam in real-time, ensuring responsive cursor movements that mimic the user's hand gestures. OpenCV is used for video capture and pre-processing, chosen for its widespread use and efficiency in handling image processing tasks.
  - The combination of OpenCV with Mediapipe allows for efficient frame-by-frame analysis, maintaining high frame rates necessary for a smooth user experience.

## Technical Details

### Hand Detection

The hand detection is powered by Mediapipe's multi-hand tracking solution, which uses machine learning to infer 21 3D hand landmarks from a single frame. The reason for selecting Mediapipe over other hand tracking solutions is its balance of speed and accuracy. Unlike other deep learning models that might require powerful GPUs, Mediapipe is optimized to run on CPU, making it accessible for users with different hardware configurations.

### Cursor Control

Cursor control is achieved by mapping the position of the hand to the screen coordinates. This involves translating the 3D coordinates of the hand landmarks into 2D screen coordinates, a task handled by PyAutoGUI. The choice of PyAutoGUI was due to its cross-platform compatibility and ease of use. Additionally, it provides comprehensive control over the cursor, allowing for smooth movements and customizable gesture mappings.

### Efficiency Considerations

Efficiency was a key consideration in the development of this project. The choice of libraries and their configurations were aimed at minimizing processing overhead while maintaining accuracy. OpenCV's efficient image processing capabilities and Mediapipe's optimized inference models contribute to keeping the computational load low. This ensures that the system can run in real-time on a wide range of devices, from high-end desktops to more modest laptops.

## Installation

### Prerequisites

- Python 3.x
- Webcam

### Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone https://github.com/madhesh-hariharran/Hand-Gesture-Mouse.git
    ```

2. **Navigate to the project directory**:
    ```sh
    cd Hand-Gesture-Mouse
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

   The `requirements.txt` file includes all necessary dependencies, including OpenCV, Mediapipe, and PyAutoGUI, ensuring that the environment is correctly configured for running the project.

4. **Run the project**:
    ```sh
    python AiVirtualMouseProject.py
    ```

   This will start the webcam and the system will begin tracking your hand gestures to control the mouse.

## Files and Directories

- `AiVirtualMouseProject.py`: The main script that integrates hand tracking with cursor control.
- `HandTrackingModule.py`: A custom module encapsulating the hand detection and tracking logic using Mediapipe.
- `LICENSE`: This project is open-sourced under the MIT License, allowing for free use and modification.
- `README.md`: Documentation of the project.
- `__pycache__`: Contains Python bytecode files for faster loading times.

## Why This Approach?

The combination of OpenCV, Mediapipe, and PyAutoGUI was carefully selected to provide a balance of performance, accuracy, and ease of implementation. Mediapipe's ability to run efficiently on CPU means that the project is accessible to a wider audience without the need for specialized hardware. OpenCV's widespread adoption and robust support for video processing made it an ideal choice for handling the webcam input. Finally, PyAutoGUI's straightforward API simplifies the process of controlling the mouse, making the project easier to extend and modify.

## Potential Enhancements

- **Advanced Gesture Recognition**: Implementing machine learning models to recognize a wider range of hand gestures could expand the functionality beyond basic cursor control.
- **Customizable Gesture Mapping**: Allowing users to define their own gestures and corresponding actions could make the system more flexible and personalized.
- **Multi-Platform Support**: Expanding compatibility to include different operating systems and device types could broaden the application's use cases.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Mediapipe**: For providing the powerful hand tracking library that made this project possible.
- **OpenCV**: For its extensive image processing tools that facilitated video input handling.
- **PyAutoGUI**: For the simple and effective GUI automation tools.

---

