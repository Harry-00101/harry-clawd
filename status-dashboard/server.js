const http = require('http');
const fs = require('fs');
const { execSync } = require('child_process');

const html = fs.readFileSync('/root/clawd/status-dashboard/index.html', 'utf8');

const STATUS_FILE = '/tmp/harry001-status.json';

const server = http.createServer((req, res) => {
    if (req.url === '/api/status') {
        try {
            const uptime = execSync('uptime -p 2>/dev/null || uptime | cut -d"," -f1 | cut -d" " -f4-').toString().trim();
            
            let statusData = { emoji: '🤖', text: '🤖 Harry-001' };
            try {
                statusData = JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
            } catch (e) {}
            
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({
                uptime: uptime || 'Active',
                emoji: statusData.emoji,
                text: statusData.text
            }));
        } catch (e) {
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ uptime: 'Active', emoji: '🤖', text: '🤖 Harry-001' }));
        }
    } else {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(html);
    }
});

server.listen(3000, () => console.log('Status: http://localhost:3000'));
