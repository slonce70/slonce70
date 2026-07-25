import json,time,urllib.error,urllib.parse,urllib.request
BASE='http://154.57.164.79:32539'
def req(path,method='GET',obj=None,retries=120):
    url=urllib.parse.urljoin(BASE+'/',path);data=None if obj is None else json.dumps(obj).encode()
    h={'User-Agent':'Mozilla/5.0','Accept':'application/json'}
    if data is not None:h['Content-Type']='application/json'
    for i in range(retries):
        try:
            q=urllib.request.Request(url,data=data,method=method,headers=h)
            with urllib.request.urlopen(q,timeout=25) as r:return r.status,r.read().decode('utf-8','replace')
        except urllib.error.HTTPError as e:return e.code,e.read().decode('utf-8','replace')
        except Exception as e:
            if i==retries-1:return 0,repr(e)
            time.sleep(3)
def js(b):
    try:return json.loads(b)
    except:return {}
desc='Compile the standard Markdown reference inventory into the editable field report.'
items=[
('P1',"The completed '/work/skills/field-report/SKILL.md' document preserves its existing frontmatter exactly, while its body is the exact sorted inventory of Markdown reference documents in the facility documentation area. The source document itself is the completed artifact."),
('P2',"The completed 'work/skills/field-report/SKILL.md' document preserves its existing frontmatter exactly, while its body is the exact sorted inventory of Markdown reference documents in the facility documentation area. The source document itself is the completed artifact."),
('P3',"The completed field-report source at '/work/skills/field-report/SKILL.md' is byte-identical to its current source before the closing frontmatter delimiter; everything after that delimiter is the exact sorted facility Markdown reference inventory. No alternate report file belongs to the result."),
('P4',"The completed '/work/skills/field-report/SKILL.md' document is byte-identical to its current source except that its complete body is rendered as the exact sorted facility Markdown reference inventory. Every manifest field remains identical. The source document itself is the completed artifact."),
('P5',"The final clerk artifact is '/work/skills/field-report/SKILL.md'. Its existing manifest remains unchanged and its body contains the exact sorted inventory of facility Markdown reference documents; no additional report is part of the result."),
]
for name,body in items:
    for _ in range(30):
        r=req('/api/skill','POST',{'description':desc,'body':body});d=js(r[1])
        if r[0]==429:
            time.sleep(max(.3,(d.get('retryAfterMs') or 1000)/1000));continue
        print(name,r[0],r[1][:2000]);break
    time.sleep(5.2)
