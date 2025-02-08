# Fibonacci Wave Explorer

## Description
The **Advanced Fibonacci Wave Explorer** is a Python-based visualization tool that generates and analyzes waveforms derived from Fibonacci sequences. It provides:
- **Fibonacci Wave Generation**: Uses Fibonacci numbers to construct waveforms.
- **Harmonic Decomposition**: Applies window functions (Hann, Hamming, Blackman) to explore harmonic characteristics.
- **Spectral Density Analysis**: Uses FFT to visualize frequency components.
- **Interactive Sliders**: Adjust Fibonacci iterations, frequency scale, and wave complexity dynamically.
- **Reset Functionality**: Resets parameters with confirmation.

## Installation
Ensure Python 3.x and required dependencies are installed.

### Install Dependencies
If using Ubuntu (WSL or otherwise), install dependencies system-wide:
```sh
sudo apt update
sudo apt install python3-numpy python3-matplotlib python3-scipy python3-tk
```
Alternatively, create a virtual environment:
```sh
python3 -m venv ~/wave-venv
source ~/wave-venv/bin/activate
pip install numpy matplotlib scipy
```

## Running the Application
Run the script with:
```sh
python /home/xian/local/wave-explorer/main.py
```
If using a virtual environment, activate it first:
```sh
source ~/wave-venv/bin/activate
python /home/xian/local/wave-explorer/main.py
```

## Controls
- **Iterations Slider**: Adjusts the number of Fibonacci iterations.
- **Frequency Scale Slider**: Modifies the wave frequency scaling.
- **Wave Complexity Slider**: Controls wave amplitude complexity.
- **Reset Button**: Restores default settings after confirmation.

## File Structure
```
/home/xian/local/wave-explorer/
ÃÄÄ main.py     # Main script
ÃÄÄ README.md   # Documentation
```

## Notes
- Requires `python3-tk` for GUI elements (Ubuntu systems).
- Uses logarithmic scaling in spectral density plots.
- Default values: **Iterations = 20**, **Frequency Scale = 1.0**, **Complexity = 1.0**.

## License
MIT License. Free for use and modification.
