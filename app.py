from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>OrganicClone AI</title>
    <style>
        body { 
            background: linear-gradient(135deg, #0a0a0a, #1a1a1a); 
            color: white; 
            font-family: Arial, sans-serif; 
            margin: 0; 
            padding: 40px;
        }
        .container { max-width: 800px; margin: 0 auto; text-align: center; }
        h1 { 
            font-size: 3rem; 
            background: linear-gradient(45deg, #ff6b35, #f7931e); 
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent; 
            margin-bottom: 20px;
        }
        p { font-size: 1.2rem; color: #ccc; margin-bottom: 30px; }
        .working { color: #4ade80; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 OrganicClone AI</h1>
        <p>Turn Any Viral Video Into Your Next Hit</p>
        <p class="working">✅ Website is now working!</p>
        <p>Ready to build amazing AI features.</p>
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
