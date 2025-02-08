# Fibonacci Wave Explorer

## Description
The **Fibonacci Wave Explorer** is an interactive Python tool that visualizes Fibonacci-based waveforms. Made for fun. It features:

- **Fibonacci Wave Generation**: Uses Fibonacci numbers to generate waveforms.
- **Harmonic Decomposition**: Applies Hann, Hamming, and Blackman window functions to analyze harmonics.
- **Spectral Density Analysis**: Uses FFT to visualize the frequency spectrum.
- **Interactive UI**: Sliders allow real-time adjustments to Fibonacci iterations, frequency scaling, and wave complexity.
- **Reset Function**: Restores default settings with user confirmation.

## Demo

![Image](resources/Play.gif)

## Installation
Ensure Python 3.x is installed along with the necessary dependencies.

### Install System-Wide (Ubuntu/WSL)
```bash
$ sudo apt update
$ sudo apt install python3-numpy python3-matplotlib python3-scipy python3-tk
```

### Using a Virtual Environment (Recommended)
```bassh
$ python3 -m venv ~/wave-venv
$ source ~/wave-venv/bin/activate
$ pip install numpy matplotlib scipy
```

## Running the Application
Run the script:
```sh
python /home/xian/local/wave-explorer/main.py
```
If using a virtual environment:
```sh
source ~/wave-venv/bin/activate
python /home/xian/local/wave-explorer/main.py
```

## Controls
- **Iterations Slider**: Adjusts the number of Fibonacci iterations.
- **Frequency Scale Slider**: Modifies the wave frequency scaling.
- **Wave Complexity Slider**: Controls wave amplitude complexity.
- **Reset Button**: Restores default settings after confirmation.

## Notes
- Requires `python3-tk` for GUI functionality on Ubuntu.
- Uses logarithmic scaling in spectral density plots.
- Default values: **Iterations = 20**, **Frequency Scale = 1.0**, **Complexity = 1.0**.

## License
MIT License - Free for use and modification.
