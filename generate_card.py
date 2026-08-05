import html,json,urllib.request,datetime
u='idlirshkurti'
def get(url): return json.load(urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'profile-card'})))
p=get(f'https://api.github.com/users/{u}');r=get(f'https://api.github.com/users/{u}/repos?per_page=100&type=owner')
rows=[('role','Data Scientist'),('location','Germany'),('languages','Python · SQL · R · TypeScript'),('data','DuckDB · PostgreSQL · pandas'),('ml/ai','Forecasting · LLM systems · evals'),('platform','Kubernetes · Azure · FastAPI · Temporal'),('repos',p['public_repos']),('stars',sum(x['stargazers_count'] for x in r)),('followers',p['followers']),('updated',datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%d'))]
art=open('ascii-art.txt').read().splitlines()
def card(path,bg,fg,muted,accent):
 stats=''.join(f"<text x='42' y='{135+i*43}' class='l'>{k}</text><text x='560' y='{135+i*43}' text-anchor='end' class='v'>{v}</text>" for i,(k,v) in enumerate(rows))
 portrait=''.join(f"<tspan x='660' y='{80+i*11}'>{html.escape(line)}</tspan>" for i,line in enumerate(art))
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1350" height="700" viewBox="0 0 1350 700"><style>.t{{font:700 34px monospace;fill:{fg}}}.s,.l{{font:18px monospace;fill:{muted}}}.v{{font:700 18px monospace;fill:{fg}}}.a{{font:10px monospace;fill:{accent}}}</style><rect width="1350" height="700" rx="22" fill="{bg}"/><rect x="24" y="24" width="1302" height="652" rx="15" fill="none" stroke="{muted}" stroke-opacity=".5"/><line x1="620" y1="48" x2="620" y2="652" stroke="{muted}" stroke-opacity=".5"/><text x="42" y="85" class="t">idlirshkurti@github</text>{stats}<text class="a" xml:space="preserve">{portrait}</text><text x="660" y="650" class="s">ASCII profile portrait</text></svg>'''
 open(path,'w').write(svg)
card('dark_mode.svg','#0d1117','#e6edf3','#8b949e','#58a6ff')
card('light_mode.svg','#ffffff','#1f2328','#59636e','#0969da')
