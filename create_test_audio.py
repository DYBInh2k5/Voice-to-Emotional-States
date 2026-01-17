#!/usr/bin/env python3
"""
Tạo file audio test để demo
"""

import numpy as np
import soundfile as sf
import os

def create_test_audio():
    """Create simple test audio files"""
    print("Creating test audio files...")
    
    # Create test_audio directory if not exists
    os.makedirs('test_audio', exist_ok=True)
    
    # Audio parameters
    sample_rate = 22050
    duration = 3  # 3 seconds
    
    # Create different types of sounds
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # 1. Happy sound - high frequency, fast changes
    happy_freq = 440 + 100 * np.sin(2 * np.pi * 5 * t)  # Variable frequency
    happy_audio = 0.3 * np.sin(2 * np.pi * happy_freq * t)
    happy_audio += 0.1 * np.random.randn(len(t))  # Add noise
    sf.write('test_audio/happy_test.wav', happy_audio, sample_rate)
    
    # 2. Sad sound - low frequency, less variation
    sad_freq = 200 + 20 * np.sin(2 * np.pi * 0.5 * t)  # Low freq, slow changes
    sad_audio = 0.2 * np.sin(2 * np.pi * sad_freq * t)
    sad_audio += 0.05 * np.random.randn(len(t))  # Less noise
    sf.write('test_audio/sad_test.wav', sad_audio, sample_rate)
    
    # 3. Angry sound - high frequency, lots of noise
    angry_freq = 300 + 200 * np.sin(2 * np.pi * 10 * t)  # Fast changes
    angry_audio = 0.4 * np.sin(2 * np.pi * angry_freq * t)
    angry_audio += 0.2 * np.random.randn(len(t))  # Lots of noise
    sf.write('test_audio/angry_test.wav', angry_audio, sample_rate)
    
    # 4. Neutral sound - medium frequency, stable
    neutral_freq = 330  # Fixed frequency
    neutral_audio = 0.25 * np.sin(2 * np.pi * neutral_freq * t)
    neutral_audio += 0.08 * np.random.randn(len(t))  # Medium noise
    sf.write('test_audio/neutral_test.wav', neutral_audio, sample_rate)
    
    print("Created test audio files:")
    print("  - test_audio/happy_test.wav")
    print("  - test_audio/sad_test.wav") 
    print("  - test_audio/angry_test.wav")
    print("  - test_audio/neutral_test.wav")

if __name__ == "__main__":
    create_test_audio()