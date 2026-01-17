#!/usr/bin/env python3
"""
Voice Emotion Recognition - Main Application
"""

import argparse
import os
from src.voice_emotion import VoiceEmotionAnalyzer
from src.data_processor import DataProcessor
from src.real_time_detector import RealTimeEmotionDetector

def train_model(data_dir, model_output):
    """Train emotion recognition model"""
    print("Training emotion recognition model...")
    
    # Process dataset
    processor = DataProcessor()
    features, labels = processor.process_dataset(data_dir)
    
    if len(features) == 0:
        print("No valid audio files found in dataset!")
        return
    
    # Train model
    analyzer = VoiceEmotionAnalyzer()
    analyzer.train_model(features, labels)
    
    # Save model
    os.makedirs(os.path.dirname(model_output), exist_ok=True)
    analyzer.save_model(model_output)
    
    print(f"Model trained and saved to: {model_output}")

def predict_emotion(audio_file, model_path):
    """Predict emotion from audio file"""
    if not os.path.exists(model_path):
        print(f"Model not found: {model_path}")
        return
    
    analyzer = VoiceEmotionAnalyzer(model_path)
    result = analyzer.predict_emotion(audio_file)
    
    if result:
        print(f"Audio file: {audio_file}")
        print(f"Predicted emotion: {result['emotion']}")
        print(f"Confidence: {result['confidence']:.2f}")
    else:
        print("Failed to analyze audio file")

def real_time_detection(model_path):
    """Start real-time emotion detection"""
    if not os.path.exists(model_path):
        print(f"Model not found: {model_path}")
        return
    
    detector = RealTimeEmotionDetector(model_path)
    detector.start_recording()

def main():
    parser = argparse.ArgumentParser(description="Voice Emotion Recognition")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Train command
    train_parser = subparsers.add_parser('train', help='Train emotion recognition model')
    train_parser.add_argument('--data', required=True, help='Path to training data directory')
    train_parser.add_argument('--output', default='models/emotion_model.pkl', help='Output model path')
    
    # Predict command
    predict_parser = subparsers.add_parser('predict', help='Predict emotion from audio file')
    predict_parser.add_argument('--audio', required=True, help='Path to audio file')
    predict_parser.add_argument('--model', default='models/emotion_model.pkl', help='Path to trained model')
    
    # Real-time command
    realtime_parser = subparsers.add_parser('realtime', help='Start real-time emotion detection')
    realtime_parser.add_argument('--model', default='models/emotion_model.pkl', help='Path to trained model')
    
    args = parser.parse_args()
    
    if args.command == 'train':
        train_model(args.data, args.output)
    elif args.command == 'predict':
        predict_emotion(args.audio, args.model)
    elif args.command == 'realtime':
        real_time_detection(args.model)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()