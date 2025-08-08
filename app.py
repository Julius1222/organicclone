from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    html_content = """
    <html>
    <head>
        <title>OrganicClone AI</title>
        <style>
            body { 
                background: linear-gradient(135deg, #0a0a0a, #1a1a1a); 
                color: white; 
                font-family: Arial; 
                padding: 50px; 
                text-align: center; 
            }
            h1 { 
                color: #ff6b35; 
                font-size: 3rem; 
                margin-bottom: 20px; 
            }
            p { 
                font-size: 1.3rem; 
                color: #ccc; 
                margin: 20px 0; 
            }
            .success { 
                color: #4ade80; 
                font-weight: bold; 
                font-size: 1.5rem; 
                margin: 30px 0; 
            }
            input { 
                padding: 15px; 
                margin: 10px; 
                border-radius: 10px; 
                border: none; 
                width: 300px; 
                background: rgba(255,255,255,0.1); 
                color: white; 
            }
            button { 
                padding: 15px 30px; 
                background: #ff6b35; 
                color: white; 
                border: none; 
                border-radius: 25px; 
                font-size: 1.1rem; 
                cursor: pointer; 
                margin: 20px; 
            }
        </style>
    </head>
    <body>
        <h1>🚀 OrganicClone AI</h1>
        <p>Turn Any Viral Video Into Your Next Hit</p>
        <div class="success">✅ Platform is Working!</div>
        
        <div>
            <input type="url" placeholder="Viral Video URL (TikTok/Instagram)" style="display: block; margin: 20px auto;">
            <input type="url" placeholder="Your YouTube Video URL" style="display: block; margin: 20px auto;">
            <button onclick="alert('Analysis feature coming soon!')">🎯 Analyze Videos</button>
        </div>
        
        <p>Ready to build amazing AI features!</p>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
