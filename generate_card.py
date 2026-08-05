import html,json,os,pathlib,subprocess,urllib.request
U='idlirshkurti';T=os.environ['PROFILE_STATS_TOKEN']
def api(x):return json.load(urllib.request.urlopen(urllib.request.Request(x,headers={'Authorization':'Bearer '+T,'User-Agent':'profile-card'})))
def run(*x):return subprocess.run(x,text=True,capture_output=True,check=True).stdout
repos=[]
for page in range(1,100):
 batch=api(f'https://api.github.com/user/repos?affiliation=owner,collaborator&per_page=100&page={page}')
 if not batch:break
 repos += [r for r in batch if not r['fork'] and not r['archived']]
commits=adds=dels=lines=0;root=pathlib.Path('/tmp/profile-repos');root.mkdir(exist_ok=True)
for r in repos:
 p=root/r['name'];url=r['clone_url'].replace('https://','https://x-access-token:'+T+'@')
 try:run('git','clone','-q','--no-tags',url,str(p))
 except subprocess.CalledProcessError:continue
 try:log=run('git','-C',str(p),'log','--all','--author',U,'--format=1','--numstat')
 except subprocess.CalledProcessError:log=''
 for row in log.splitlines():
  x=row.split('\t')
  if row=='1':commits+=1
  elif len(x)==3 and x[0].isdigit():adds+=int(x[0]);dels+=int(x[1])
 for f in p.rglob('*'):
  if f.is_file() and '.git' not in f.parts:
   try:lines+=sum(1 for _ in f.open(errors='ignore'))
   except OSError:pass
rows=[('Uptime','32 years'),('Host','jedox'),('Kernel','data scientist'),('Languages.Programming','python, r, sql'),('Tech.Stack','scikit-learn, tensorflow, kubernetes, docker, langgraph'),('Hobbies','football, running, scripting'),('Contact --------------------',''),('Linkedin','idlir-shkurti'),('Blog','idlirshkurti.github.io'),('Github stats ------------------',''),('Repos',len(repos)),('Contributed',commits),('Code.Lines',lines),('(+/-)',f'+{adds:,} / -{dels:,}')];art=open('ascii-art.txt').read().splitlines()
def card(out,bg,fg,muted):
 left=''.join(f"<text x='42' y='{110+i*38}' fill='{fg if not v else muted}' font-family='monospace' font-size='17'>{k}</text>"+(f"<text x='610' y='{110+i*38}' text-anchor='end' fill='{fg}' font-family='monospace' font-size='17'>{v}</text>" if v else '') for i,(k,v) in enumerate(rows));portrait=''.join(f"<tspan x='680' y='{85+i*11}'>{html.escape(x)}</tspan>" for i,x in enumerate(art));pathlib.Path(out).write_text(f"<svg xmlns='http://www.w3.org/2000/svg' width='1400' height='700'><rect width='1400' height='700' fill='{bg}'/>{left}<text fill='{fg}' font-family='monospace' font-size='10'>{portrait}</text></svg>")
card('dark_mode.svg','#0d1117','#e6edf3','#8b949e');card('light_mode.svg','#ffffff','#1f2328','#59636e')
