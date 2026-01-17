#!/usr/bin/env python3
"""
GitHub Repository Information
"""

import subprocess
import os

def get_git_info():
    """Get Git repository information"""
    try:
        # Get remote URL
        remote_url = subprocess.check_output(['git', 'remote', 'get-url', 'origin'], 
                                           text=True).strip()
        
        # Get current branch
        branch = subprocess.check_output(['git', 'branch', '--show-current'], 
                                       text=True).strip()
        
        # Get last commit
        last_commit = subprocess.check_output(['git', 'log', '-1', '--oneline'], 
                                            text=True).strip()
        
        # Get repository status
        status = subprocess.check_output(['git', 'status', '--porcelain'], 
                                       text=True).strip()
        
        return {
            'remote_url': remote_url,
            'branch': branch,
            'last_commit': last_commit,
            'status': status
        }
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

def count_files():
    """Count project files"""
    file_counts = {
        'Python files': 0,
        'Audio files': 0,
        'Notebook files': 0,
        'Model files': 0,
        'Total files': 0
    }
    
    for root, dirs, files in os.walk('.'):
        # Skip .git directory
        if '.git' in root:
            continue
            
        for file in files:
            file_counts['Total files'] += 1
            
            if file.endswith('.py'):
                file_counts['Python files'] += 1
            elif file.endswith(('.wav', '.mp3', '.flac')):
                file_counts['Audio files'] += 1
            elif file.endswith('.ipynb'):
                file_counts['Notebook files'] += 1
            elif file.endswith('.pkl'):
                file_counts['Model files'] += 1
    
    return file_counts

def main():
    print("🚀 GITHUB REPOSITORY INFORMATION")
    print("=" * 50)
    
    # Git information
    git_info = get_git_info()
    
    if 'error' in git_info:
        print(f"❌ Git error: {git_info['error']}")
        return
    
    print(f"📍 Repository URL: {git_info['remote_url']}")
    print(f"🌿 Current Branch: {git_info['branch']}")
    print(f"📝 Last Commit: {git_info['last_commit']}")
    
    if git_info['status']:
        print(f"⚠️  Uncommitted changes:")
        for line in git_info['status'].split('\n'):
            print(f"   {line}")
    else:
        print("✅ Working directory clean")
    
    # File statistics
    print(f"\n📊 PROJECT STATISTICS")
    print("-" * 30)
    
    file_counts = count_files()
    for category, count in file_counts.items():
        print(f"{category}: {count}")
    
    # Repository links
    repo_url = git_info['remote_url'].replace('.git', '')
    print(f"\n🔗 USEFUL LINKS")
    print("-" * 30)
    print(f"📂 Repository: {repo_url}")
    print(f"📋 Issues: {repo_url}/issues")
    print(f"🔀 Pull Requests: {repo_url}/pulls")
    print(f"📊 Insights: {repo_url}/pulse")
    print(f"⚙️  Settings: {repo_url}/settings")
    
    # Quick commands
    print(f"\n💻 QUICK COMMANDS")
    print("-" * 30)
    print("📥 Clone repository:")
    print(f"   git clone {git_info['remote_url']}")
    print()
    print("🔄 Update repository:")
    print("   git add .")
    print("   git commit -m 'Update message'")
    print("   git push")
    print()
    print("📦 Install and run:")
    print("   pip install -r requirements.txt")
    print("   python demo.py")
    
    print(f"\n🎉 SUCCESS!")
    print("Your Voice Emotion Recognition project is now live on GitHub! 🎤")

if __name__ == "__main__":
    main()