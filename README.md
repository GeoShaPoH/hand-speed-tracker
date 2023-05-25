# hand-speed-tracker
Hand-Speed is an application that tracks the real-time speed of your pointer. It provides a visual representation of the speed and allows you to monitor the movement of the pointer on your screen.

# Installation
To run the Hand-Speed application, follow these steps:
1. Clone the repository:
```bash
git clone https://github.com/GeoShaPoH/hand-speed-tracker
```
2. Install the required dependencies:
```python
pip install pyautogui pillow
```

3. Run the application:
```python
python hand_speed_tracker.py
```
# Usage
1. Launch the application by running the script.
2. A window titled "Hand-Speed" will appear on your screen.
3. The current speed of the pointer will be displayed in millimeters per second.
4. Move the pointer around the screen, and the speed will be updated accordingly.
# Notes
1. The application uses the pyautogui library to track the pointer's position on the screen.
2. The speed is calculated based on the distance traveled by the pointer between two consecutive measurements.
3. The application updates the speed every 0.165 seconds.
4. The color of the neon border surrounding the speed display changes gradually to create a visually appealing effect.
5. The application window has a fixed size and cannot be maximized to ensure consistent display and user experience.
Feel free to explore and customize the code to suit your specific needs.

## License

[MIT](https://choosealicense.com/licenses/mit/)
