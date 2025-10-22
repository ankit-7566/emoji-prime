#!/usr/bin/env python3
"""
Web interface for Discord Bot Emoji Updater
"""

from flask import Flask, render_template_string, request, jsonify
from update_emoji_ids import find_all_emojis, update_emoji_id
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Discord Bot Emoji Updater</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #5865F2 0%, #7289DA 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        .header h1 { font-size: 2.5em; margin-bottom: 10px; }
        .header p { font-size: 1.1em; opacity: 0.9; }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
            border-bottom: 2px solid #e9ecef;
        }
        .stat-card {
            background: white;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .stat-number {
            font-size: 2.5em;
            font-weight: bold;
            color: #5865F2;
            margin-bottom: 5px;
        }
        .stat-label {
            color: #6c757d;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .content {
            padding: 30px;
        }
        .section {
            margin-bottom: 40px;
        }
        .section h2 {
            color: #5865F2;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #e9ecef;
        }
        .emoji-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 15px;
            max-height: 500px;
            overflow-y: auto;
            padding: 10px;
        }
        .emoji-item {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.2s;
        }
        .emoji-item:hover {
            background: #e9ecef;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .emoji-code {
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            color: #495057;
            flex: 1;
        }
        .emoji-count {
            background: #5865F2;
            color: white;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.85em;
            margin-left: 10px;
        }
        .update-form {
            background: #f8f9fa;
            padding: 25px;
            border-radius: 12px;
            margin-top: 20px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #495057;
        }
        .form-group input, .form-group select {
            width: 100%;
            padding: 12px;
            border: 2px solid #dee2e6;
            border-radius: 8px;
            font-size: 1em;
            transition: border-color 0.2s;
        }
        .form-group input:focus, .form-group select:focus {
            outline: none;
            border-color: #5865F2;
        }
        .btn {
            background: #5865F2;
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 8px;
            font-size: 1em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
        }
        .btn:hover {
            background: #4752C4;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(88, 101, 242, 0.4);
        }
        .message {
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
            display: none;
        }
        .message.success {
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        .message.error {
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        .guide-section {
            background: #e7f3ff;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #5865F2;
        }
        .guide-section h3 {
            color: #5865F2;
            margin-bottom: 10px;
        }
        .guide-section ul {
            margin-left: 20px;
            line-height: 1.8;
        }
        .top-emojis {
            background: #fff3cd;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #ffc107;
            margin-bottom: 20px;
        }
        .top-emojis h3 {
            color: #856404;
            margin-bottom: 15px;
        }
        .top-emoji-item {
            font-family: 'Courier New', monospace;
            padding: 8px;
            margin: 5px 0;
            background: white;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎨 Discord Bot Emoji Updater</h1>
            <p>Easily update all emoji IDs in your Discord bot</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">{{ total_emojis }}</div>
                <div class="stat-label">Total Emojis</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{{ total_files }}</div>
                <div class="stat-label">Files with Emojis</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{{ total_uses }}</div>
                <div class="stat-label">Total Uses</div>
            </div>
        </div>
        
        <div class="content">
            <div class="top-emojis">
                <h3>🔥 Top 5 Most Used Emojis</h3>
                {% for emoji, count in top_emojis %}
                <div class="top-emoji-item">{{ emoji }} - used {{ count }} times</div>
                {% endfor %}
            </div>
            
            <div class="section">
                <h2>Update Emoji ID</h2>
                <div class="update-form">
                    <form id="updateForm">
                        <div class="form-group">
                            <label for="emojiSelect">Select Emoji to Update:</label>
                            <select id="emojiSelect" name="emoji" required>
                                <option value="">-- Choose an emoji --</option>
                                {% for emoji in emojis %}
                                <option value="{{ emoji }}">{{ emoji }}</option>
                                {% endfor %}
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="newId">New Emoji ID (17-19 digits):</label>
                            <input type="text" id="newId" name="new_id" pattern="[0-9]{17,19}" placeholder="1234567890123456789" required>
                        </div>
                        <button type="submit" class="btn">Update Emoji ID</button>
                    </form>
                    <div id="message" class="message"></div>
                </div>
            </div>
            
            <div class="section">
                <h2>All Emojis ({{ total_emojis }})</h2>
                <div class="emoji-list">
                    {% for emoji, count in emoji_list %}
                    <div class="emoji-item">
                        <span class="emoji-code">{{ emoji }}</span>
                        <span class="emoji-count">{{ count }} uses</span>
                    </div>
                    {% endfor %}
                </div>
            </div>
            
            <div class="section">
                <div class="guide-section">
                    <h3>📚 How to Get New Emoji IDs</h3>
                    <ul>
                        <li>In Discord, type <code>\\:emoji_name:</code> and send it</li>
                        <li>Discord will show the full emoji code with ID</li>
                        <li>Copy just the ID number (17-19 digits)</li>
                        <li>Paste it in the form above</li>
                        <li>Or enable Developer Mode in Discord, right-click emoji, and "Copy ID"</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        document.getElementById('updateForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const data = {
                emoji: formData.get('emoji'),
                new_id: formData.get('new_id')
            };
            
            const messageDiv = document.getElementById('message');
            messageDiv.style.display = 'none';
            
            try {
                const response = await fetch('/update', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                
                const result = await response.json();
                
                messageDiv.className = 'message ' + (result.success ? 'success' : 'error');
                messageDiv.textContent = result.message;
                messageDiv.style.display = 'block';
                
                if (result.success) {
                    setTimeout(() => location.reload(), 2000);
                }
            } catch (error) {
                messageDiv.className = 'message error';
                messageDiv.textContent = 'Error: ' + error.message;
                messageDiv.style.display = 'block';
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    emoji_locations = find_all_emojis()
    
    emoji_list = sorted(emoji_locations.items(), key=lambda x: len(x[1]), reverse=True)
    total_uses = sum(len(locations) for locations in emoji_locations.values())
    
    # Count unique files
    all_files = set()
    for locations in emoji_locations.values():
        for file_path, _ in locations:
            all_files.add(file_path)
    
    top_emojis = emoji_list[:5]
    
    return render_template_string(
        HTML_TEMPLATE,
        emojis=sorted(emoji_locations.keys()),
        emoji_list=emoji_list,
        total_emojis=len(emoji_locations),
        total_files=len(all_files),
        total_uses=total_uses,
        top_emojis=[(emoji, len(locs)) for emoji, locs in top_emojis]
    )

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    emoji = data.get('emoji')
    new_id = data.get('new_id')
    
    if not emoji or not new_id:
        return jsonify({'success': False, 'message': 'Missing emoji or new ID'})
    
    if not new_id.isdigit() or len(new_id) < 17 or len(new_id) > 19:
        return jsonify({'success': False, 'message': 'Invalid ID format. Must be 17-19 digits.'})
    
    try:
        files_updated = update_emoji_id(emoji, new_id)
        if files_updated > 0:
            return jsonify({
                'success': True,
                'message': f'✅ Successfully updated {emoji} in {files_updated} file(s)!'
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Emoji not found in any files'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
