# Spartan: Voice-Activated Gesture Control System

An integrated Python application that combines a voice assistant (“Spartan”) with a dynamic hand-gesture controller for seamless, hands-free human–computer interaction. Users can issue voice commands to perform common tasks and, on demand, switch to real-time hand gestures (via webcam) for cursor control, clicks, scrolling, volume/brightness adjustment, and more.

---

## 🚀 Features

- **Voice Assistant**  
  - Text-to-speech responses (pyttsx3)  
  - Speech recognition (speech_recognition + Google API)  
  - Wikipedia lookups, web searches, opening URLs  
  - Time & date queries, location search  
  - Customizable greetings (“Good Morning/Afternoon/Evening”)  

- **Gesture Controller**  
  - Real-time hand tracking (MediaPipe + OpenCV)  
  - Gesture encoding (fist, palm, V-sign, pinch, two-finger close)  
  - Mouse control: move, left/right click, double-click, drag  
  - Pinch-based scroll, volume & brightness adjustment (PyAutoGUI + Pycaw + screen_brightness_control)  
  - Noise-resilient gesture stabilization  

- **Dynamic Mode Switching**  
  - Voice-first operation by default  
  - “Open/Stop gesture controller” voice commands spawn or terminate a separate multiprocessing gesture process  
  - Seamless transition between voice and gesture inputs  

---

## 🛠️ Tech Stack & Libraries

- **Python 3.8+**  
- **Voice**: `pyttsx3`, `speech_recognition`, `wikipedia`  
- **Vision & Gestures**: `opencv-python`, `mediapipe`, `pyautogui`  
- **Audio & Brightness**: `pycaw`, `screen_brightness_control`  
- **Process Management**: `multiprocessing`  

---

## ⚙️ Installation

1. Clone the repo:  
   ```bash
   git clone https://github.com/your-username/spartan-gesture-voice.git
   cd spartan-gesture-voice
