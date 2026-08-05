import os,json,urllib.request,html
u='idlirshkurti';t=os.environ['PROFILE_STATS_TOKEN']
def api(url):
 r=urllib.request.Request(url,headers={'Authorization':'Bearer '+t,'User-Agent':'profile-card'});return json.load(urllib.request.urlopen(r))
repos=[]
for p in range(1,100):
 x=api(f'https://api.github.com/user/repos?affiliation=owner,collaborator&per_page=100&page={p}')
 if not x:break
 repos += [r for r in x if not r['fork'] and not r['archived']]
commits=0
for r in repos:
 try: commits += len(api(r['commits_url'].replace('{/sha}','')+'?author='+u+'&per_page=100'))
 except Exception: pass
art=open('ascii-art.txt').read().splitlines()
rows=[('Uptime','32 years'),('Host','jedox'),('Kernel','data scientist'),('Languages.Programming','python, r, sql'),('Tech.Stack','scikit-learn, tensorflow, kubernetes, docker, langgraph'),('Hobbies','football, running, scripting'),('Contact',''),('Linkedin','idlir-shkurti'),('Blog','idlirshkurti.github.io'),('Github stats',''),('Repos',str(len(repos))),('Contributed',str(commits))]
def make(fn,bg,fg,muted):
 a=''.join(f"<text x='45' y='{90+i*36}' fill='{muted}' font-family='monospace' font-size='17'>{html.escape(k)}</text><text x='625' y='{90+i*36}' text-anchor='end' fill='{fg}' font-family='monospace' font-size='17'>{html.escape(v)}</text>" for i,(k,v) in enumerate(rows));b=''.join(f"<tspan x='700' y='{70+i*11}'>{html.escape(z)}</tspan>" for i,z in enumerate(art));open(fn,'w').write(f"<svg xmlns='http://www.w3.org/2000/svg' width='1400' height='620'><rect width='100%' height='100%' fill='{bg}'/>{a}<text fill='{fg}' font-family='monospace' font-size='10'>{b}</text></svg>")
make('dark_mode.svg','#0d1117','#e6edf3','#8b949e');make('light_mode.svg','#fff','#1f2328','#59636e')
