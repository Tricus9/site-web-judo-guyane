from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
p=Path(__file__).resolve().parents[1]/'dist'
class Doc(HTMLParser):
 def __init__(self,s):
  super().__init__();self.refs=[];self.ids=set();self.h1=0;self.desc=False;self.feed(s)
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if 'id'in a:self.ids.add(a['id'])
  if t=='h1':self.h1+=1
  if t=='meta' and a.get('name')=='description':self.desc=True
  for k in ['href','src']:
   if k in a:self.refs.append(a[k])
docs={f.name:Doc(f.read_text())for f in p.glob('*.html')};errors=[]
for name,d in docs.items():
 if d.h1!=1 or not d.desc:errors.append(name+' headings/meta')
 for ref in d.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  target=unquote(u.path)or name
  if not(p/target).exists():errors.append(name+' -> '+ref)
  if u.fragment and target in docs and u.fragment not in docs[target].ids:errors.append(name+' missing anchor '+ref)
print(f'{len(docs)} pages checked; {len(errors)} errors');print('\n'.join(errors));assert not errors
