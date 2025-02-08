import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from scipy.fft import fft, fftfreq
from scipy.signal import windows
from tkinter import messagebox, Tk

class AdvancedFibonacciWaveExplorer:
    def __init__(self):
        # Create main figure with subplots
        self.fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(3, 1, figsize=(15, 15))
        plt.subplots_adjust(left=0.1, bottom=0.3, right=0.9, top=0.95, hspace=0.3)
        
        # Initial parameters
        self.iterations = 20
        self.frequency_scale = 1.0
        self.wave_complexity = 1.0
        
        # Generate initial Fibonacci sequence
        self.fibonacci_sequence = self.generate_fibonacci_sequence()
        
        # Prepare x values
        self.x = np.linspace(0, 10, 1000)
        
        # First plot: Raw Fibonacci Wave
        self.wave_line, = self.ax1.plot(self.x, self.generate_wave(), label='Fibonacci Wave')
        self.ax1.set_title('Fibonacci Wave')
        self.ax1.set_xlabel('Time')
        self.ax1.set_ylabel('Amplitude')
        
        # Second plot: Harmonic Decomposition
        self.harmonic_line, = self.ax2.plot(self.x, self.generate_harmonic_decomposition(), label='Harmonic Decomposition')
        self.ax2.set_title('Harmonic Decomposition')
        self.ax2.set_xlabel('Time')
        self.ax2.set_ylabel('Amplitude')
        
        # Third plot: Spectral Density
        frequencies, spectral_density = self.compute_spectral_density()
        self.spectral_line, = self.ax3.plot(frequencies, spectral_density, label='Spectral Density')
        self.ax3.set_title('Spectral Density')
        self.ax3.set_xlabel('Frequency')
        self.ax3.set_ylabel('Density')
        self.ax3.set_xscale('log')
        self.ax3.set_yscale('log')
        
        # Create sliders
        slider_color = 'lightgoldenrodyellow'
        
        ax_iterations = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor=slider_color)
        self.slider_iterations = Slider(ax_iterations, 'Iterations', 5, 50, valinit=self.iterations, valstep=1)
        self.slider_iterations.on_changed(self.update_iterations)
        
        ax_freq = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor=slider_color)
        self.slider_freq = Slider(ax_freq, 'Frequency Scale', 0.1, 5.0, valinit=self.frequency_scale, valstep=0.1)
        self.slider_freq.on_changed(self.update_frequency_scale)
        
        ax_complexity = plt.axes([0.1, 0.05, 0.65, 0.03], facecolor=slider_color)
        self.slider_complexity = Slider(ax_complexity, 'Complexity', 0.1, 5.0, valinit=self.wave_complexity, valstep=0.1)
        self.slider_complexity.on_changed(self.update_wave_complexity)
        
        # Reset Button with Confirmation
        ax_reset = plt.axes([0.8, 0.05, 0.1, 0.04])
        self.reset_button = Button(ax_reset, 'Reset')
        self.reset_button.on_clicked(self.reset)
        
        plt.show()
    
    def generate_fibonacci_sequence(self):
        """Generate Fibonacci sequence using safe numerical limits"""
        sequence = [0, 1]
        while len(sequence) < self.iterations:
            sequence.append(sequence[-1] + sequence[-2])
        return np.array(sequence, dtype=np.int64)
    
    def generate_wave(self):
        """Optimized wave generation using numpy vectorization"""
        wave = np.zeros_like(self.x, dtype=float)
        frequencies = np.arange(len(self.fibonacci_sequence)) * self.frequency_scale
        sin_values = np.sin(2 * np.pi * np.outer(frequencies, self.x))
        np.add.at(wave, np.arange(len(self.x)), (self.fibonacci_sequence[:, None] * self.wave_complexity * sin_values).sum(axis=0))
        return wave
    
    def generate_harmonic_decomposition(self):
        wave = self.generate_wave()
        windowed_waves = [wave * w for w in [windows.hann(len(wave)), windows.hamming(len(wave)), windows.blackman(len(wave))]]
        return np.mean(windowed_waves, axis=0)
    
    def compute_spectral_density(self):
        wave = self.generate_wave()
        fft_values = np.abs(fft(wave)) / len(wave)
        spectral_density = np.log1p(fft_values ** 2)  # Log scaling for visualization
        frequencies = fftfreq(len(wave), d=1.0)
        mask = frequencies > 0
        return frequencies[mask], spectral_density[mask]
    
    def update_iterations(self, val):
        self.iterations = int(val)
        self.fibonacci_sequence = self.generate_fibonacci_sequence()
        self.update_plots()
    
    def update_frequency_scale(self, val):
        self.frequency_scale = val
        self.update_plots()
    
    def update_wave_complexity(self, val):
        self.wave_complexity = val
        self.update_plots()
    
    def update_plots(self):
        wave = self.generate_wave()
        self.wave_line.set_ydata(wave)
        self.ax1.relim()
        self.ax1.autoscale_view()
        
        harmonic_wave = self.generate_harmonic_decomposition()
        self.harmonic_line.set_ydata(harmonic_wave)
        self.ax2.relim()
        self.ax2.autoscale_view()
        
        frequencies, spectral_density = self.compute_spectral_density()
        self.spectral_line.set_xdata(frequencies)
        self.spectral_line.set_ydata(spectral_density)
        self.ax3.set_xlim(1e-2, np.max(frequencies))
        self.ax3.relim()
        self.ax3.autoscale_view()
        
        self.fig.canvas.draw_idle()
    
    def reset(self, event):
        root = Tk()
        root.withdraw()
        if messagebox.askyesno('Confirm Reset', 'Are you sure you want to reset all values?'):
            self.slider_iterations.reset()
            self.slider_freq.reset()
            self.slider_complexity.reset()
        root.destroy()

def main():
    AdvancedFibonacciWaveExplorer()

if __name__ == "__main__":
    main()

# Relative Path: /home/xian/local/wave-explorer/main.py
