#!/usr/bin/env python3
"""
Demo script cho Voice Emotion Recognition
"""

import numpy as np
import os
from src.voice_emotion import VoiceEmotionAnalyzer
from src.data_processor import DataProcessor

def create_demo_data():
    """Create demo data for testing"""
    print("Creating demo data...")
    
    # Tạo thư mục models nếu chưa có
    os.makedirs('models', exist_ok=True)
    
    # Tạo dữ liệu giả lập (thay thế cho audio thật)
    np.random.seed(42)
    n_samples = 500
    n_features = 10
    
    # Tạo features giả lập với các pattern khác nhau cho mỗi emotion
    features = []
    labels = []
    
    emotions = ['neutral', 'happy', 'sad', 'angry', 'fear', 'disgust', 'surprise']
    
    for i, emotion in enumerate(emotions):
        # Tạo 70-80 samples cho mỗi emotion
        n_emotion_samples = np.random.randint(70, 81)
        
        for _ in range(n_emotion_samples):
            # Tạo features với pattern đặc trưng cho từng emotion
            base_features = np.random.randn(n_features)
            
            # Thêm pattern đặc trưng
            if emotion == 'happy':
                base_features[0] += 1.5  # MFCC cao hơn
                base_features[2] += 1.0  # Spectral centroid cao
            elif emotion == 'sad':
                base_features[0] -= 1.0  # MFCC thấp hơn
                base_features[4] -= 0.5  # ZCR thấp
            elif emotion == 'angry':
                base_features[1] += 2.0  # Std cao
                base_features[3] += 1.5  # Spectral features cao
            elif emotion == 'fear':
                base_features[4] += 1.0  # ZCR cao
                base_features[5] += 0.8  # Chroma features
            
            features.append(base_features)
            labels.append(i)
    
    return np.array(features), np.array(labels)

def train_demo_model():
    """Train model with demo data"""
    print("Training model with demo data...")
    
    # Create demo data
    features, labels = create_demo_data()
    
    print(f"Total samples: {len(features)}")
    print(f"Number of features: {features.shape[1]}")
    
    # Count samples for each emotion
    emotions = ['neutral', 'happy', 'sad', 'angry', 'fear', 'disgust', 'surprise']
    for i, emotion in enumerate(emotions):
        count = np.sum(labels == i)
        print(f"  {emotion}: {count} samples")
    
    # Train model
    analyzer = VoiceEmotionAnalyzer()
    model = analyzer.train_model(features, labels)
    
    # Save model
    model_path = 'models/demo_emotion_model.pkl'
    analyzer.save_model(model_path)
    
    print(f"Model saved at: {model_path}")
    
    # Test model
    print("\nTesting model...")
    test_features = features[:10]  # Lấy 10 samples đầu để test
    test_labels = labels[:10]
    
    for i in range(len(test_features)):
        # Predict
        features_scaled = analyzer.scaler.transform(test_features[i].reshape(1, -1))
        prediction = model.predict(features_scaled)[0]
        confidence = np.max(model.predict_proba(features_scaled))
        
        actual_emotion = emotions[test_labels[i]]
        predicted_emotion = emotions[prediction]
        
        print(f"Sample {i+1}: Actual={actual_emotion}, Predicted={predicted_emotion}, Confidence={confidence:.2f}")
    
    return model_path

def demo_prediction(model_path):
    """Demo prediction with trained model"""
    print(f"\nDemo prediction with model: {model_path}")
    
    # Load model
    analyzer = VoiceEmotionAnalyzer(model_path)
    
    # Create test samples
    print("Creating test samples...")
    test_samples = []
    expected_emotions = []
    
    # Happy sample
    happy_features = np.random.randn(10)
    happy_features[0] += 1.5
    happy_features[2] += 1.0
    test_samples.append(happy_features)
    expected_emotions.append('happy')
    
    # Sad sample
    sad_features = np.random.randn(10)
    sad_features[0] -= 1.0
    sad_features[4] -= 0.5
    test_samples.append(sad_features)
    expected_emotions.append('sad')
    
    # Angry sample
    angry_features = np.random.randn(10)
    angry_features[1] += 2.0
    angry_features[3] += 1.5
    test_samples.append(angry_features)
    expected_emotions.append('angry')
    
    # Test predictions
    print("\nPrediction results:")
    for i, (features, expected) in enumerate(zip(test_samples, expected_emotions)):
        features_scaled = analyzer.scaler.transform(features.reshape(1, -1))
        prediction = analyzer.model.predict(features_scaled)[0]
        confidence = np.max(analyzer.model.predict_proba(features_scaled))
        
        predicted_emotion = analyzer.emotions[prediction]
        
        print(f"Test {i+1}:")
        print(f"  Expected: {expected}")
        print(f"  Predicted: {predicted_emotion}")
        print(f"  Confidence: {confidence:.2f}")
        print(f"  Result: {'OK' if predicted_emotion == expected else 'FAIL'}")
        print()

def main():
    print("=== DEMO VOICE EMOTION RECOGNITION ===\n")
    
    try:
        # Train model với dữ liệu demo
        model_path = train_demo_model()
        
        # Demo prediction
        demo_prediction(model_path)
        
        print("=== DEMO COMPLETED ===")
        print(f"Model saved at: {model_path}")
        print("You can use this model to:")
        print("1. Run real-time detection: python main.py realtime --model models/demo_emotion_model.pkl")
        print("2. Predict from audio file: python main.py predict --audio your_audio.wav --model models/demo_emotion_model.pkl")
        
    except Exception as e:
        print(f"Error during demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()