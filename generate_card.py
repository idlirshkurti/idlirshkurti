import html,json,os,pathlib,subprocess,urllib.request
U='idlirshkurti';T=os.environ['PROFILE_STATS_TOKEN']
def api(x):return json.load(urllib.request.urlopen(urllib.request.Request(x,headers={'Authorization':'Bearer '+T,'User-Agent':'profile-card'})))
def sh(*x):return subprocess.run(x,text=True,capture_output=True,check=True).stdout
rs=[]
for n in range(1,100):
 x=api(f'https://api.github.com/user/repos?affiliation=owner,collaborator&per_page=100&page={n}')
 if not x:break
 rs += [r for r in x if not r['fork'] and not r['archived']]
root=pathlib.Path('/tmp/repos');root.mkdir(exist_ok=True);c=a=d=l=0
for r in rs:
 p=root/r['name'];url=r['clone_url'].replace('https://','https://x-access-token:'+T+'@');sh('git','clone','-q','--no-tags',url,str(p));log=sh('git','-C',str(p),'log','--all','--author',U,'--format=1','--numstat')
 for z in log.splitlines():
  if z=='1':c+=1
  elif len(z.split('\t'))==3 and z.split('\t')[0].isdigit():q=z.split('\t');a+=int(q[0]);d+=int(q[1])
 for f in p.rglob('*'):
  if f.is_file() and '.git' not in f.parts:
   try:l+=sum(1 for _ in f.open(errors='ignore'))
   except:pass
rows=[('Uptime','32 years'),('Host','jedox'),('Kernel','data scientist'),('Languages.Programming','python, r, sql'),('Tech.Stack','scikit-learn, tensorflow, kubernetes, docker, langgraph'),('Hobbies','football, running, scripting'),('Contact --------------------',''),('Linkedin','idlir-shkurti'),('Blog','idlirshkurti.github.io'),('Github stats ------------------',''),('Repos',len(rs)),('Contributed',c),('Code.Lines',l),('(+/-)',f'+{a:,} / -{d:,}')];art=open('ascii-art.txt').read().splitlines()
def card(o,b,f,m):
 y=110;s=''
 for k,v in rows:s+=f"<text x='42' y='{y}' fill='{f if not v else m}' font-family='monospace' font-size='17'>{k}</text>"+(f"<text x='610' y='{y}' text-anchor='end' fill='{f}' font-family='monospace' font-size='17'>{v}</text>" if v else '');y+=38
 a=''.join(f"<tspan x='680' y='{85+i*11}'>{html.escape(x)}</tspan>" for i,x in enumerate(art));pathlib.Path(o).write_text(f"<svg xmlns='http://www.w3.org/2000/svg' width='1400' height='700'><rect width='1400' height='700' fill='{b}'/>{s}<text fill='{f}' font-family='monospace' font-size='10'>{a}</text></svg>")
card('dark_mode.svg','#0d1117','#e6edf3','#8b949e');card('light_mode.svg','#fff','#1f2328','#59636e')