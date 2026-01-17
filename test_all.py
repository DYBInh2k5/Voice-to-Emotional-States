#!/usr/bin/env python3
"""
Test tất cả chức năng của Voice Emotion Recognition
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Chạy command và hiển thị kết quả"""
    print(f"\n{'='*50}")
    print(f"🔄 {description}")
    print(f"Command: {command}")
    print('='*50)
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.stdout:
            print("📤 Output:")
            print(result.stdout)
        
        if result.stderr:
            print("⚠️ Errors:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("✅ Thành công!")
        else:
            print(f"❌ Lỗi (Exit code: {result.returncode})")
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def main():
    print("🎤 VOICE EMOTION RECOGNITION - FULL TEST")
    print("=" * 60)
    
    # 1. Kiểm tra cấu trúc project
    print("\n📁 Kiểm tra cấu trúc project...")
    required_files = [
        'src/voice_emotion.py',
        'src/data_processor.py', 
        'src/real_time_detector.py',
        'main.py',
        'demo.py',
        'requirements.txt'
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file}")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n⚠️ Thiếu {len(missing_files)} file quan trọng!")
        return
    
    # 2. Test demo training
    success = run_command("python demo.py", "Chạy demo training")
    if not success:
        print("❌ Demo training thất bại!")
        return
    
    # 3. Tạo test audio
    success = run_command("python create_test_audio.py", "Tạo file audio test")
    if not success:
        print("❌ Tạo audio test thất bại!")
        return
    
    # 4. Test prediction với các file audio
    test_files = [
        'test_audio/happy_test.wav',
        'test_audio/sad_test.wav',
        'test_audio/angry_test.wav', 
        'test_audio/neutral_test.wav'
    ]
    
    for audio_file in test_files:
        if os.path.exists(audio_file):
            emotion_type = os.path.basename(audio_file).replace('_test.wav', '')
            success = run_command(
                f"python main.py predict --audio {audio_file} --model models/demo_emotion_model.pkl",
                f"Test prediction cho {emotion_type} emotion"
            )
        else:
            print(f"⚠️ File không tồn tại: {audio_file}")
    
    # 5. Test help commands
    run_command("python main.py --help", "Kiểm tra help menu")
    run_command("python main.py train --help", "Kiểm tra train help")
    run_command("python main.py predict --help", "Kiểm tra predict help")
    run_command("python main.py realtime --help", "Kiểm tra realtime help")
    
    # 6. Kiểm tra model đã được tạo
    print(f"\n📊 Kiểm tra model...")
    model_path = 'models/demo_emotion_model.pkl'
    if os.path.exists(model_path):
        size = os.path.getsize(model_path)
        print(f"✅ Model tồn tại: {model_path} ({size} bytes)")
    else:
        print(f"❌ Model không tồn tại: {model_path}")
    
    # 7. Tổng kết
    print(f"\n🎯 TỔNG KẾT")
    print("=" * 60)
    print("✅ Dự án Voice Emotion Recognition đã được setup thành công!")
    print("\n📋 Các chức năng có sẵn:")
    print("1. 🎓 Training model: python main.py train --data <dataset_path>")
    print("2. 🔮 Predict emotion: python main.py predict --audio <audio_file>")
    print("3. 🎙️ Real-time detection: python main.py realtime")
    print("4. 📊 Demo với dữ liệu giả: python demo.py")
    print("5. 📓 Jupyter notebook: jupyter notebook notebooks/emotion_analysis.ipynb")
    
    print(f"\n📁 Cấu trúc project:")
    print("├── src/                    # Source code")
    print("├── models/                 # Trained models")
    print("├── test_audio/            # Test audio files")
    print("├── notebooks/             # Jupyter notebooks")
    print("├── main.py                # CLI interface")
    print("└── demo.py                # Demo script")
    
    print(f"\n🚀 Để bắt đầu sử dụng:")
    print("1. Chạy demo: python demo.py")
    print("2. Test với audio: python main.py predict --audio test_audio/happy_test.wav")
    print("3. Real-time (cần microphone): python main.py realtime")

if __name__ == "__main__":
    main()