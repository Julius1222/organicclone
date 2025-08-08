import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = b'''
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
                h1 { color: #ff6b35; font-size: 3rem; }
                p { font-size: 1.3rem; color: #ccc; margin: 20px; }
                .success { color: #4ade80; font-weight: bold; font-size: 1.5rem; }
            </style>
        </head>
        <body>
            <h1>🚀 OrganicClone AI</h1>
            <p>Turn Any Viral Video Into Your Next Hit</p>
            <div class="success">✅ Platform is Working!</div>
            <p>Basic version is live - ready to build features!</p>
        </body>
        </html>
        '''
        
        self.wfile.write(html)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    print(f'Server running on port {port}')
    server.serve_forever()
