import pyaudio
import numpy as np
import librosa
import threading
import time
from .voice_emotion import VoiceEmotionAnalyzer

class RealTimeEmotionDetector:
    def __init__(self, model_path, chunk_size=1024, sample_rate=22050):
        self.analyzer = VoiceEmotionAnalyzer(model_path)
        self.chunk_size = chunk_size
        self.sample_rate = sample_rate
        self.is_recording = False
        self.audio_buffer = []
        
        # Initialize PyAudio
        self.audio = pyaudio.PyAudio()
        
    def start_recording(self):
        """Start real-time emotion detection"""
        self.is_recording = True
        
        # Open audio stream
        stream = self.audio.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk_size
        )
        
        print("Starting real-time emotion detection...")
        print("Press Ctrl+C to stop")
        
        try:
            while self.is_recording:
                # Read audio data
                data = stream.read(self.chunk_size)
                audio_data = np.frombuffer(data, dtype=np.float32)
                
                # Add to buffer
                self.audio_buffer.extend(audio_data)
                
                # Process every 2 seconds of audio
                if len(self.audio_buffer) >= self.sample_rate * 2:
                    self.process_audio_chunk()
                    
        except KeyboardInterrupt:
            print("\nStopping emotion detection...")
            
        finally:
            stream.stop_stream()
            stream.close()
            self.is_recording = False
    
    def process_audio_chunk(self):
        """Process audio chunk and detect emotion"""
        if len(self.audio_buffer) < self.sample_rate:
            return
        
        # Get audio chunk
        audio_chunk = np.array(self.audio_buffer[:self.sample_rate * 2])
        self.audio_buffer = self.audio_buffer[self.sample_rate:]
        
        # Extract features directly from audio data
        features = self.extract_features_from_audio(audio_chunk)
        
        if features is not None:
            # Predict emotion
            features = features.reshape(1, -1)
            
            if self.analyzer.scaler:
                features = self.analyzer.scaler.transform(features)
            
            prediction = self.analyzer.model.predict(features)[0]
            confidence = np.max(self.analyzer.model.predict_proba(features))
            
            emotion = self.analyzer.emotions[prediction]
            
            print(f"Detected emotion: {emotion} (confidence: {confidence:.2f})")
    
    def extract_features_from_audio(self, audio_data):
        """Extract features from raw audio data"""
        try:
            # Extract features similar to VoiceEmotionAnalyzer
            features = []
            
            # MFCC features
            mfccs = librosa.feature.mfcc(y=audio_data, sr=self.sample_rate, n_mfcc=13)
            features.extend([np.mean(mfccs), np.std(mfccs)])
            
            # Spectral features
            spectral_centroids = librosa.feature.spectral_centroid(y=audio_data, sr=self.sample_rate)[0]
            features.extend([np.mean(spectral_centroids), np.std(spectral_centroids)])
            
            # Zero crossing rate
            zcr = librosa.feature.zero_crossing_rate(audio_data)[0]
            features.extend([np.mean(zcr), np.std(zcr)])
            
            # Chroma features
            chroma = librosa.feature.chroma_stft(y=audio_data, sr=self.sample_rate)
            features.extend([np.mean(chroma), np.std(chroma)])
            
            # Mel spectrogram
            mel = librosa.feature.melspectrogram(y=audio_data, sr=self.sample_rate)
            features.extend([np.mean(mel), np.std(mel)])
            
            return np.array(features)
            
        except Exception as e:
            print(f"Error extracting features: {e}")
            return None
    
    def stop_recording(self):
        """Stop real-time detection"""
        self.is_recording = False
    
    def __del__(self):
        """Cleanup PyAudio"""
        if hasattr(self, 'audio'):
            self.audio.terminate()