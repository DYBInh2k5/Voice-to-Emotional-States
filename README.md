# 🎤 Voice to Emotional States

A comprehensive machine learning project for recognizing emotional states from voice audio using advanced audio processing and classification techniques.

## 🌟 Features

- **Audio Feature Extraction**: MFCC, spectral features, chroma, zero-crossing rate
- **Multi-Emotion Classification**: 7 emotion categories (neutral, happy, sad, angry, fear, disgust, surprise)
- **Real-time Detection**: Live emotion recognition from microphone input
- **Command-Line Interface**: Easy-to-use CLI for training and prediction
- **Demo Mode**: Quick testing with synthetic data
- **Jupyter Integration**: Interactive notebooks for experimentation
- **Multiple Audio Formats**: Support for WAV, MP3, FLAC files

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/DYBInh2k5/Voice-to-Emotional-States.git
cd Voice-to-Emotional-States

# Install dependencies
pip install -r requirements.txt
```

### Run Demo

```bash
# Quick demo with synthetic data
python demo.py

# Create test audio files
python create_test_audio.py

# Test prediction
python main.py predict --audio test_audio/happy_test.wav --model models/demo_emotion_model.pkl
```

## 💻 Usage

### Command Line Interface

```bash
# Train a new model
python main.py train --data path/to/dataset --output models/my_model.pkl

# Predict emotion from audio file
python main.py predict --audio audio_file.wav --model models/trained_model.pkl

# Real-time emotion detection
python main.py realtime --model models/trained_model.pkl

# Show help
python main.py --help
```

### Python API

```python
from src.voice_emotion import VoiceEmotionAnalyzer

# Load trained model
analyzer = VoiceEmotionAnalyzer('models/demo_emotion_model.pkl')

# Predict emotion
result = analyzer.predict_emotion("audio_file.wav")
print(f"Emotion: {result['emotion']}")
print(f"Confidence: {result['confidence']:.2f}")
```

### Real-time Detection

```python
from src.real_time_detector import RealTimeEmotionDetector

# Start real-time detection
detector = RealTimeEmotionDetector('models/demo_emotion_model.pkl')
detector.start_recording()  # Press Ctrl+C to stop
```

## 📁 Project Structure

```
Voice-to-Emotional-States/
├── src/                          # Source code
│   ├── voice_emotion.py         # Core emotion analyzer
│   ├── data_processor.py        # Dataset processing utilities
│   ├── real_time_detector.py    # Real-time detection
│   └── __init__.py
├── models/                       # Trained models
│   └── demo_emotion_model.pkl   # Pre-trained demo model
├── test_audio/                   # Test audio files
│   ├── happy_test.wav
│   ├── sad_test.wav
│   ├── angry_test.wav
│   └── neutral_test.wav
├── notebooks/                    # Jupyter notebooks
│   └── emotion_analysis.ipynb   # Analysis and experimentation
├── main.py                      # CLI interface
├── demo.py                      # Demo script
├── create_test_audio.py         # Generate test audio
├── project_summary.py           # Project overview
├── requirements.txt             # Dependencies
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## 😊 Supported Emotions

| Emotion | Description |
|---------|-------------|
| 😐 Neutral | Calm, balanced emotional state |
| 😊 Happy | Joy, excitement, positive emotions |
| 😢 Sad | Sorrow, melancholy, low energy |
| 😠 Angry | Frustration, irritation, high energy |
| 😨 Fear | Anxiety, worry, nervousness |
| 🤢 Disgust | Aversion, repulsion |
| 😲 Surprise | Shock, amazement, unexpected |

## 🔧 Technical Details

### Audio Features
- **MFCC (Mel-Frequency Cepstral Coefficients)**: Captures spectral characteristics
- **Spectral Centroid**: Measures brightness of sound
- **Zero Crossing Rate**: Indicates voicing characteristics
- **Chroma Features**: Represents pitch class profiles
- **Mel Spectrogram**: Time-frequency representation

### Machine Learning
- **Algorithm**: Random Forest Classifier
- **Feature Scaling**: StandardScaler normalization
- **Training Data**: Synthetic data with emotion-specific patterns
- **Validation**: Cross-validation and confidence scoring

## 📊 Performance

The demo model achieves reasonable accuracy on synthetic data. For production use:
- Collect real audio datasets (RAVDESS, CREMA-D, etc.)
- Implement data augmentation techniques
- Experiment with deep learning models (CNN, RNN, Transformers)
- Fine-tune hyperparameters

## 🛠️ Development

### Running Tests
```bash
python test_all.py
```

### Jupyter Notebook
```bash
jupyter notebook notebooks/emotion_analysis.ipynb
```

### Project Summary
```bash
python project_summary.py
```

## 📦 Dependencies

- **numpy**: Numerical computing
- **pandas**: Data manipulation
- **scikit-learn**: Machine learning algorithms
- **librosa**: Audio processing
- **tensorflow**: Deep learning (optional)
- **matplotlib/seaborn**: Visualization
- **soundfile**: Audio I/O
- **pyaudio**: Real-time audio capture
- **jupyter**: Interactive notebooks

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **librosa** team for excellent audio processing tools
- **scikit-learn** for machine learning algorithms
- Audio dataset providers (RAVDESS, CREMA-D, etc.)
- Open source community for inspiration and tools

## 📞 Contact

- **Author**: DYBInh2k5
- **GitHub**: [@DYBInh2k5](https://github.com/DYBInh2k5)
- **Repository**: [Voice-to-Emotional-States](https://github.com/DYBInh2k5/Voice-to-Emotional-States)

---

⭐ **Star this repository if you found it helpful!** ⭐