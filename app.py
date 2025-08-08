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
        body { 
            background: linear-gradient(135deg, #0a0a0a, #1a1a1a); 
            color: white; 
            font-family: Arial, sans-serif; 
            margin: 0; 
            padding: 40px;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        h1 { 
            font-size: 3rem; 
            background: linear-gradient(45deg, #ff6b35, #f7931e); 
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent; 
            text-align: center; 
            margin-bottom: 20px;
        }
        .subtitle { 
            text-align: center; 
            font-size: 1.3rem; 
            color: #ccc; 
            margin-bottom: 40px; 
        }
        .section { 
            background: rgba(255,255,255,0.05); 
            padding: 30px; 
            border-radius: 15px; 
            margin: 25px 0; 
            border: 1px solid rgba(255,255,255,0.1);
        }
        .section h3 {
            color: #ff6b35;
            margin-top: 0;
            font-size: 1.3rem;
        }
        input, textarea { 
            width: 100%; 
            padding: 15px; 
            background: rgba(0,0,0,0.3); 
            border: 2px solid rgba(255,255,255,0.2); 
            border-radius: 10px; 
            color: white; 
            font-size: 1rem; 
            box-sizing: border-box;
            margin-top: 10px;
        }
        input::placeholder, textarea::placeholder {
            color: #888;
        }
        .btn { 
            background: linear-gradient(45deg, #ff6b35, #f7931e); 
            border: none; 
            padding: 18px 50px; 
            border-radius: 30px; 
            color: white; 
            font-size: 1.2rem; 
            font-weight: bold;
            cursor: pointer; 
            display: block;
            margin: 30px auto;
            transition: transform 0.2s;
        }
        .btn:hover {
            transform: translateY(-2px);
        }
        .status {
            text-align: center;
            padding: 20px;
            color: #4ade80;
            font-weight: bold;
            font-size: 1.1rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 OrganicClone AI</h1>
        <div class="subtitle">Turn Any Viral Video Into Your Next Hit</div>
        
        <div class="status">✅ Platform is Live & Working!</div>
        
        <div class="section">
            <h3>🔥 Paste Viral Video URL</h3>
            <p style="color: #aaa; margin: 10px 0;">TikTok, Instagram Reel, or YouTube Short you want to recreate</p>
            <input type="url" id="viralUrl" placeholder="https://www.tiktok.com/@username/video/1234567890">
        </div>
        
        <div class="section">
            <h3>📺 Your YouTube Video URL</h3>
            <p style="color: #aaa; margin: 10px 0;">Your existing content that we'll transform into viral format</p>
            <input type="url" id="userUrl" placeholder="https://www.youtube.com/watch?v=your_video_id">
        </div>
        
        <div class="section">
            <h3>📝 Content Description</h3>
            <p style="color: #aaa; margin: 10px 0;">Tell us about your brand, message, or content style</p>
            <textarea id="content" rows="4" placeholder="Describe your content, target audience, and what message you want to convey..."></textarea>
        </div>
        
        <button class="btn" onclick="analyzeVideos()">🎯 Analyze & Create Viral Template</button>
        
        <div id="results" style="display: none; margin-top: 30px;">
            <div class="section">
                <h3>🎬 Analysis Results</h3>
                <div id="analysis-content"></div>
            </div>
        </div>
        
        <div style="text-align: center; margin-top: 50px; color: #666; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 30px;">
            <p>AI-powered viral video recreation platform</p>
            <p style="font-size: 0.9rem;">Transform your content using proven viral formulas</p>
        </div>
    </div>

    <script>
        function analyzeVideos() {
            const viralUrl = document.getElementById('viralUrl').value;
            const userUrl = document.getElementById('userUrl').value;
            const content = document.getElementById('content').value;
            
            if (!viralUrl || !userUrl || !content) {
                alert('Please fill in all fields to analyze your videos');
                return;
            }
            
            // Show results section
            document.getElementById('results').style.display = 'block';
            document.getElementById('analysis-content').innerHTML = '<p style="color: #ff6b35;">🔄 Analyzing viral patterns and your content...</p>';
            
            // Scroll to results
            document.getElementById('results').scrollIntoView({ behavior: 'smooth' });
            
            // Simulate analysis (replace with real API call later)
            setTimeout(() => {
                const platform = viralUrl.includes('tiktok') ? 'TikTok' : 
                                viralUrl.includes('instagram') ? 'Instagram' : 'YouTube';
                                
                document.getElementById('analysis-content').innerHTML = `
                    <div style="background: rgba(255,107,53,0.1); padding: 20px; border-radius: 10px; margin: 15px 0;">
                        <h4 style="color: #ff6b35; margin-top: 0;">📊 Viral Video Analysis</h4>
                        <ul style="line-height: 1.8; color: #ddd;">
                            <li><strong>Platform:</strong> ${platform}</li>
                            <li><strong>Format:</strong> Quick-cut engagement style</li>
                            <li><strong>Hook Strategy:</strong> Strong opening with text overlay</li>
                            <li><strong>Optimal Duration:</strong> 15-30 seconds</li>
                            <li><strong>Virality Score:</strong> 8.5/10</li>
                        </ul>
                    </div>
                    
                    <div style="background: rgba(255,107,53,0.1); padding: 20px; border-radius: 10px; margin: 15px 0;">
                        <h4 style="color: #ff6b35; margin-top: 0;">🎬 Your Recreation Template</h4>
                        
                        <div style="background: rgba(0,0,0,0.3); padding: 15px; border-radius: 8px; margin: 10px 0;">
                            <strong>0-3s - Hook Section:</strong><br>
                            Start with attention-grabbing text: "You won't believe this..." <br>
                            Use your strongest footage from: <em>${userUrl}</em>
                        </div>
                        
                        <div style="background: rgba(0,0,0,0.3); padding: 15px; border-radius: 8px; margin: 10px 0;">
                            <strong>3-12s - Main Content:</strong><br>
                            Quick cuts every 0.8 seconds matching viral pacing<br>
                            Content focus: <em>${content.substring(0, 100)}${content.length > 100 ? '...' : ''}</em>
                        </div>
                        
                        <div style="background: rgba(0,0,0,0.3); padding: 15px; border-radius: 8px; margin: 10px 0;">
                            <strong>12-15s - Call to Action:</strong><br>
                            Strong ending: "Follow for more tips like this!"<br>
                            Use trending audio overlay
                        </div>
                        
                        <div style="text-align: center; margin-top: 20px;">
                            <button style="background: linear-gradient(45deg, #4ade80, #22c55e); border: none; padding: 12px 30px; border-radius: 20px; color: white; font-weight: bold; cursor: pointer;">
                                📥 Download Full Template
                            </button>
                        </div>
                    </div>
                `;
            }, 2500);
        }
    </script>
</body>
</html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
