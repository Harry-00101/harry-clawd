# Harry's CLI Assistant Aliases

# Quick weather
alias hkweather='curl -s "wttr.in/Hong+Kong?format=3"'

# Quick search
alias ddg='ddg-search'
alias websearch='web-search-exa'

# Quick summarize
alias tldr='tldr'

# File search
alias ff='fdfind'
alias rg='rg --color=always'

# Git shortcuts
alias gs='git status'
alias ga='git add'
alias gc='git commit -m'
alias gp='git push'
alias gpl='git pull'

# System shortcuts
alias ..='cd ..'
alias ...='cd ../..'
alias ll='ls -la'
alias la='ls -a'

# Quick notes
alias note='echo "$(date +%Y-%m-%d\ %H:%M) - " >> /root/clawd/memory/quick-notes.md && vim + /root/clawd/memory/quick-notes.md'

# Quick tasks
alias tasks='cat /root/clawd/memory/todo.md 2>/dev/null || echo "No tasks file"'

# Moltbook metaphysics posts (unique, non-repeating)
alias molt玄學='/root/clawd/scripts/moltbook-metaphysics-post.sh'
alias molt-metaphysics='/root/clawd/scripts/moltbook-metaphysics-post.sh'

# Moltbook auto-comment (continuous engagement)
alias moltcomment='/root/clawd/scripts/moltbook-autocomment.sh'
alias molt-engage='/root/clawd/scripts/moltbook-autocomment.sh'

# Check remaining metaphysics topics
alias molt玄學remaining='cat /root/clawd/.moltbook-metaphysics-tracker.json | jq ".topics[] | select(.posted == false) | .title"'
