from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>OrganicClone AI</title>
    <style>
        body { font-family: Arial; background: linear-gradient(135deg, #0a0a0a, #1a1a1a); color: white; margin: 0; padding: 40px; }
        .container { max-width: 1200px; margin: 0 auto; }
        h1 { font-size: 3rem; background: linear-gradient(45deg, #ff6b35, #f7931e); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; }
        .subtitle { text-align: center; font-size: 1.2rem; color: #ccc; margin-bottom: 40px; }
        .form-section { background: rgba(255,255,255,0.05); padding: 40px; border-radius: 20px; margin: 30px 0; }
        input, textarea { width: 100%; padding: 15px; background: rgba(0,0,0,0.3); border: 2px solid rgba(255,255,255,0.2); border-radius: 10px; color: white; font-size: 1rem; }
        .btn { background: linear-gradient(45deg, #ff6b35, #f7931e); border: none; padding: 18px 50px; border-radius: 50px; color: white; font-size: 1.1rem; cursor: pointer; margin: 20px 0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 OrganicClone AI</h1>
        <div class="subtitle">Turn Any Viral Video Into Your Next Hit</div>
        
        <div class="form-section">
            <h3 style="color: #ff6b35;">🔥 Paste Viral Video URL</h3>
            <input type="url" placeholder="https://www.tiktok.com/@username/video/1234567890">
        </div>
        
        <div class="form-section">
            <h3 style="color: #ff6b35;">📹 Describe Your Content</h3>
            <textarea rows="5" placeholder="Tell us about your video content..."></textarea>
        </div>
        
        <button class="btn">🎯 Analyze & Create Template</button>
    </div>
</body>
</html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
