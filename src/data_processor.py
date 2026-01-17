import os
import pandas as pd
import numpy as np
from .voice_emotion import VoiceEmotionAnalyzer

class DataProcessor:
    def __init__(self):
        self.analyzer = VoiceEmotionAnalyzer()
    
    def process_dataset(self, data_dir, emotions_mapping=None):
        """Process audio dataset and extract features"""
        if emotions_mapping is None:
            emotions_mapping = {
                'neutral': 0, 'happy': 1, 'sad': 2, 'angry': 3,
                'fear': 4, 'disgust': 5, 'surprise': 6
            }
        
        features = []
        labels = []
        
        for emotion_folder in os.listdir(data_dir):
            emotion_path = os.path.join(data_dir, emotion_folder)
            
            if not os.path.isdir(emotion_path):
                continue
            
            if emotion_folder not in emotions_mapping:
                print(f"Skipping unknown emotion: {emotion_folder}")
                continue
            
            emotion_label = emotions_mapping[emotion_folder]
            
            for audio_file in os.listdir(emotion_path):
                if audio_file.endswith(('.wav', '.mp3', '.flac')):
                    audio_path = os.path.join(emotion_path, audio_file)
                    
                    # Extract features
                    feature_vector = self.analyzer.extract_features(audio_path)
                    
                    if feature_vector is not None:
                        features.append(feature_vector)
                        labels.append(emotion_label)
                        print(f"Processed: {audio_path}")
        
        return np.array(features), np.array(labels)
    
    def save_processed_data(self, features, labels, output_path):
        """Save processed features and labels"""
        data = {
            'features': features,
            'labels': labels
        }
        np.savez(output_path, **data)
        print(f"Data saved to: {output_path}")
    
    def load_processed_data(self, data_path):
        """Load processed features and labels"""
        data = np.load(data_path)
        return data['features'], data['labels']