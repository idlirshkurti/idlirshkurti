import html,json,urllib.request,datetime
u='idlirshkurti'
def get(url):
 return json.load(urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'profile-card'})))
p=get(f'https://api.github.com/users/{u}')
r=get(f'https://api.github.com/users/{u}/repos?per_page=100&type=owner')
stats=[('repos',p['public_repos']),('stars',sum(x['stargazers_count'] for x in r)),('followers',p['followers']),('following',p['following']),('updated',datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%d'))]
art=open('ascii-art.txt').read().splitlines()[:26]
def card(path,bg,fg,muted,accent):
 rows=''.join(f"<text x='36' y='{112+i*34}' class='l'>{k}</text><text x='340' y='{112+i*34}' text-anchor='end' class='v'>{v}</text>" for i,(k,v) in enumerate(stats))
 portrait=''.join(f"<tspan x='450' y='{52+i*11}'>{html.escape(line)}</tspan>" for i,line in enumerate(art))
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="720" height="360" viewBox="0 0 720 360"><style>.t{{font:700 25px monospace;fill:{fg}}}.s,.l{{font:14px monospace;fill:{muted}}}.v{{font:700 15px monospace;fill:{fg}}}.a{{font:8px monospace;fill:{accent}}}</style><rect width="720" height="360" rx="16" fill="{bg}"/><rect x="18" y="18" width="684" height="324" rx="11" fill="none" stroke="{muted}"/><line x1="404" y1="39" x2="404" y2="321" stroke="{muted}"/><text x="36" y="61" class="t">idlirshkurti@github</text><text x="36" y="84" class="s">data engineer · Germany</text>{rows}<text class="a" xml:space="preserve">{portrait}</text><text x="450" y="323" class="s">ASCII profile portrait</text></svg>'''
 open(path,'w').write(svg)
card('dark_mode.svg','#0d1117','#e6edf3','#8b949e','#58a6ff')
card('light_mode.svg','#ffffff','#1f2328','#59636e','#0969da')
