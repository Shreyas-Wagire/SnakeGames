# Snake Game with Hand Tracking

This project is an **interactive Snake Game** built using Python, OpenCV, and CVZone. Instead of traditional keyboard controls, the game uses **real-time hand tracking** to control the snake, creating a fun, gesture-based gaming experience.

## 🚀 Features

- **Gesture-Based Controls:** Use your hand to guide the snake in real time.
- **Dynamic Gameplay:** The snake grows longer and the difficulty increases as you score points.
- **Interactive UI:** Displays the score, animations for game over, and restart functionality.
- **Food Mechanics:** Randomly placed food items for the snake to "eat."
- **AI-Powered Hand Tracking:** Powered by CVZone and OpenCV for accurate and responsive controls.

---

## 🛠 Technologies Used

- **Python**: Core programming language.
- **OpenCV**: For video capture and image processing.
- **CVZone**: Simplifies hand tracking and image overlays.
- **NumPy**: Used for efficient mathematical calculations.

---

## 📋 Requirements

1. Python 3.7 or above
2. Required Python libraries:
   - OpenCV
   - CVZone
   - NumPy

To install the dependencies, run:
```bash
pip install opencv-python cvzone numpy
```

---

## ▶ How to Run the Game

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/hand-tracking-snake-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hand-tracking-snake-game
   ```
3. Add your food image file (e.g., `Donut.png`) to the project directory.
4. Run the Python script:
   ```bash
   python snake_game.py
   ```
5. Use your hand in front of your webcam to control the snake!

---

## 🎮 Controls

- Use your **index finger** to guide the snake.
- Press **`r`** to restart the game.
- Press **`q`** to quit the game.

---

## 📂 Project Structure

```
hand-tracking-snake-game/
├── Donut.png              # Food image
├── snake_game.py          # Main game script
├── README.md              # Project documentation
```

---

## 🖼 Preview

![Game Screenshot](./screenshots/game_preview.png)

---

## 📈 Future Improvements

- Add multiple difficulty levels.
- Introduce obstacles for added challenge.
- Multiplayer mode using additional hand tracking.
- Improve visual effects and animations.

---

## 🤝 Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request to enhance the game.

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE).

---

## 🙌 Acknowledgements

- [OpenCV](https://opencv.org/) for real-time image processing.
- [CVZone](https://github.com/cvzone/cvzone) for simplifying hand tracking and overlays.

