import numpy as np
import librosa
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import soundfile as sf

class VoiceEmotionAnalyzer:
    def __init__(self, model_path=None):
        self.model = None
        self.scaler = None
        self.emotions = ['neutral', 'happy', 'sad', 'angry', 'fear', 'disgust', 'surprise']
        
        if model_path:
            self.load_model(model_path)
    
    def extract_features(self, audio_path, sr=22050):
        """Extract audio features for emotion recognition"""
        try:
            # Load audio file
            y, sr = librosa.load(audio_path, sr=sr)
            
            # Extract features
            features = []
            
            # MFCC features
            mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
            features.extend([np.mean(mfccs), np.std(mfccs)])
            
            # Spectral features
            spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
            features.extend([np.mean(spectral_centroids), np.std(spectral_centroids)])
            
            # Zero crossing rate
            zcr = librosa.feature.zero_crossing_rate(y)[0]
            features.extend([np.mean(zcr), np.std(zcr)])
            
            # Chroma features
            chroma = librosa.feature.chroma_stft(y=y, sr=sr)
            features.extend([np.mean(chroma), np.std(chroma)])
            
            # Mel spectrogram
            mel = librosa.feature.melspectrogram(y=y, sr=sr)
            features.extend([np.mean(mel), np.std(mel)])
            
            return np.array(features)
            
        except Exception as e:
            print(f"Error extracting features: {e}")
            return None
    
    def predict_emotion(self, audio_path):
        """Predict emotion from audio file"""
        if not self.model:
            raise ValueError("Model not loaded. Please train or load a model first.")
        
        features = self.extract_features(audio_path)
        if features is None:
            return None
        
        # Reshape for single prediction
        features = features.reshape(1, -1)
        
        # Scale features
        if self.scaler:
            features = self.scaler.transform(features)
        
        # Predict
        prediction = self.model.predict(features)[0]
        confidence = np.max(self.model.predict_proba(features))
        
        return {
            'emotion': self.emotions[prediction],
            'confidence': confidence
        }
    
    def train_model(self, X, y):
        """Train the emotion recognition model"""
        # Scale features
        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X)
        
        # Train model
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_scaled, y)
        
        return self.model
    
    def save_model(self, model_path):
        """Save trained model and scaler"""
        model_data = {
            'model': self.model,
            'scaler': self.scaler,
            'emotions': self.emotions
        }
        
        with open(model_path, 'wb') as f:
            pickle.dump(model_data, f)
    
    def load_model(self, model_path):
        """Load trained model and scaler"""
        with open(model_path, 'rb') as f:
            model_data = pickle.load(f)
        
        self.model = model_data['model']
        self.scaler = model_data['scaler']
        self.emotions = model_data['emotions']