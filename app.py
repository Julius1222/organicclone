from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OrganicClone AI</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0a0a0a, #1a1a1a); 
            color: white; 
            min-height: 100vh;
            padding: 20px;
        }
        .container { 
            max-width: 1200px; 
            margin: 0 auto; 
            padding: 40px 20px;
        }
        .header {
            text-align: center;
            margin-bottom: 60px;
        }
        h1 { 
            font-size: 3.5rem; 
            background: linear-gradient(45deg, #ff6b35, #f7931e); 
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 20px;
            font-weight: 700;
        }
        .subtitle { 
            font-size: 1.3rem; 
            color: #ccc; 
            margin-bottom: 40px; 
        }
        .stats {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-bottom: 60px;
            flex-wrap: wrap;
        }
        .stat {
            text-align: center;
            padding: 20px;
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
            border: 1px solid rgba(255,107,53,0.3);
        }
        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #ff6b35;
            display: block;
        }
        .stat-label {
            color: #ccc;
            font-size: 0.9rem;
            margin-top: 5px;
        }
        .form-section { 
            background: rgba(255,255,255,0.05); 
            padding: 40px; 
            border-radius: 20px; 
            margin: 30px 0;
            border: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
        }
        .section-title {
            color: #ff6b35;
            font-size: 1.4rem;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        input, textarea { 
            width: 100%; 
            padding: 18px; 
            background: rgba(0,0,0,0.4); 
            border: 2px solid rgba(255,255,255,0.2); 
            border-radius: 12px; 
            color: white; 
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        input:focus, textarea:focus {
            outline: none;
            border-color: #ff6b35;
            box-shadow: 0 0 0 3px rgba(255,107,53,0.1);
        }
        input::placeholder, textarea::placeholder {
            color: rgba(255,255,255,0.5);
        }
        .btn { 
            background: linear-gradient(45deg, #ff6b35, #f7931e); 
            border: none; 
            padding: 20px 50px; 
            border-radius: 50px; 
            color: white; 
            font-size: 1.2rem; 
            font-weight: 600;
            cursor: pointer; 
            display: block;
            margin: 40px auto;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(255,107,53,0.3);
        }
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(255,107,53,0.4);
        }
        .btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }
        .results {
            display: none;
            margin-top: 40px;
            padding: 40px;
            background: rgba(255,255,255,0.05);
            border-radius: 20px;
            border: 1px solid rgba(255,107,53,0.3);
        }
        .loading {
            text-align: center;
            color: #ff6b35;
            font-size: 1.1rem;
        }
        .analysis-result {
            margin: 20px 0;
            padding: 25px;
            background: rgba(255,107,53,0.1);
            border-radius: 15px;
            border-left: 4px solid #ff6b35;
        }
        .result-title {
            color: #ff6b35;
            font-weight: bold;
            font-size: 1.2rem;
            margin-bottom: 10px;
        }
        @media (max-width: 768px) {
            h1 { font-size: 2.5rem; }
            .stats { flex-direction: column; gap: 20px; }
            .container { padding: 20px 10px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 OrganicClone AI</h1>
            <div class="subtitle">Turn Any Viral Video Into Your Next Hit</div>
            
            <div class="stats">
                <div class="stat">
                    <span class="stat-number">10K+</span>
                    <div class="stat-label">Creators Trust Us</div>
                </div>
                <div class="stat">
                    <span class="stat-number">300%</span>
                    <div class="stat-label">Avg Engagement Boost</div>
                </div>
                <div class="stat">
                    <span class="stat-number">30s</span>
                    <div class="stat-label">Analysis Time</div>
                </div>
            </div>
        </div>
        
        <form id="analysisForm">
            <div class="form-section">
                <h3 class="section-title">🔥 Viral Video URL</h3>
                <input type="url" id="viralUrl" name="viral_url" placeholder="https://www.tiktok.com/@username/video/1234567890" required>
                <small style="color: #ccc; margin-top: 10px; display: block;">Paste any TikTok, Instagram Reel, or YouTube Short URL</small>
            </div>
            
            <div class="form-section">
                <h3 class="section-title">📺 Your YouTube Video URL</h3>
                <input type="url" id="userUrl" name="user_url" placeholder="https://www.youtube.com/watch?v=your-video-id">
                <small style="color: #ccc; margin-top: 10px; display: block;">Your existing YouTube video that we'll recreate in viral format</small>
            </div>
            
            <div class="form-section">
                <h3 class="section-title">📝 Content Description</h3>
                <textarea id="content" name="content" rows="4" placeholder="Describe your brand, niche, or the message you want to convey..."></textarea>
            </div>
            
            <button type="submit" class="btn" id="analyzeBtn">
                🎯 Analyze & Create Viral Template
            </button>
        </form>
        
        <div id="results" class="results">
            <div id="loading" class="loading">
                🔄 Analyzing viral patterns and your content...
            </div>
            <div id="analysis-content" style="display: none;"></div>
        </div>
    </div>
    
    <script>
        document.getElementById('analysisForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const viralUrl = document.getElementById('viralUrl').value;
            const userUrl = document.getElementById('userUrl').value;
            const content = document.getElementById('content').value;
            
            if (!viralUrl || !userUrl) {
                alert('Please provide both viral video URL and your YouTube URL');
                return;
            }
            
            // Show loading
            document.getElementById('results').style.display = 'block';
            document.getElementById('loading').style.display = 'block';
            document.getElementById('analysis-content').style.display = 'none';
            document.getElementById('analyzeBtn').disabled = true;
            document.getElementById('analyzeBtn').textContent = '🔄 Analyzing...';
            
            // Simulate analysis (in production, this would call your AI backend)
            setTimeout(() => {
                showAnalysisResults(viralUrl, userUrl, content);
            }, 3000);
        });
        
        function showAnalysisResults(viralUrl, userUrl, content) {
            const platform = viralUrl.includes('tiktok') ? 'TikTok' : 
                           viralUrl.includes('instagram') ? 'Instagram' : 'YouTube Shorts';
            
            const analysisHTML = `
                <div class="analysis-result">
                    <div class="result-title">📊 Viral Video Analysis</div>
                    <ul style="line-height: 1.8; color: #ccc;">
                        <li><strong>Platform:</strong> ${platform}</li>
                        <li><strong>Format:</strong> Quick-cut lifestyle content</li>
                        <li><strong>Hook Strategy:</strong> Strong opening with text overlay</li>
                        <li><strong>Optimal Duration:</strong> 15-30 seconds</li>
                        <li><strong>Virality Score:</strong> 8.7/10</li>
                        <li><strong>Key Elements:</strong> Fast cuts, trending audio, bold text</li>
                    </ul>
                </div>
                
                <div class="analysis-result">
                    <div class="result-title">🎬 Your Recreation Template</div>
                    
                    <div style="background: rgba(255,107,53,0.15); padding: 20px; border-radius: 10px; margin: 15px 0;">
                        <strong>0-3s - Hook Section:</strong><br>
                        Start with attention-grabbing text overlay: "You won't believe this..."<br>
                        Use your best footage from the YouTube video intro.
                    </div>
                    
                    <div style="background: rgba(255,107,53,0.15); padding: 20px; border-radius: 10px; margin: 15px 0;">
                        <strong>3-12s - Main Content:</strong><br>
                        Quick cuts every 0.8 seconds matching the viral format.<br>
                        Extract key moments from: ${userUrl}<br>
                        Apply your content theme: "${content.substring(0, 100)}${content.length > 100 ? '...' : ''}"
                    </div>
                    
                    <div style="background: rgba(255,107,53,0.15); padding: 20px; border-radius: 10px; margin: 15px 0;">
                        <strong>12-15s - Call to Action:</strong><br>
                        Strong ending with clear next step for viewers.<br>
                        Drive traffic back to your full YouTube video.
                    </div>
                </div>
                
                <div class="analysis-result">
                    <div class="result-title">🎵 Audio & Effects Recommendations</div>
                    <ul style="line-height: 1.8; color: #ccc;">
                        <li>Use trending audio from the viral video</li>
                        <li>Add upbeat background music at 70% volume</li>
                        <li>Include sound effects for transitions</li>
                        <li>Maintain original voice-over from your YouTube content</li>
                    </ul>
                </div>
                
                <div style="text-align: center; margin-top: 30px;">
                    <button class="btn" onclick="downloadTemplate()" style="margin: 10px;">
                        📄 Download Full Template
                    </button>
                    <button class="btn" onclick="analyzeAnother()" style="margin: 10px; background: linear-gradient(45deg, #666, #888);">
                        🔄 Analyze Another Video
                    </button>
                </div>
            `;
            
            document.getElementById('loading').style.display = 'none';
            document.getElementById('analysis-content').innerHTML = analysisHTML;
            document.getElementById('analysis-content').style.display = 'block';
            document.getElementById('analyzeBtn').disabled = false;
            document.getElementById('analyzeBtn').textContent = '🎯 Analyze & Create Viral Template';
        }
        
        function downloadTemplate() {
            alert('Template download feature coming soon!');
        }
        
        function analyzeAnother() {
            document.getElementById('analysisForm').reset();
            document.getElementById('results').style.display = 'none';
        }
    </script>
</body>
</html>
'''

@app.route('/analyze', methods=['POST'])
def analyze():
    # This endpoint will handle the actual AI analysis
    viral_url = request.form.get('viral_url')
    user_url = request.form.get('user_url')
    content = request.form.get('content')
    
    # For now, return a simple response
    # Later we'll add real AI analysis here
    return jsonify({
        'status': 'success',
        'viral_url': viral_url,
        'user_url': user_url,
        'content': content
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
