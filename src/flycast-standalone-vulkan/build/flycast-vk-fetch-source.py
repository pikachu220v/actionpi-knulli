import pathlib,json,urllib.request,tarfile,concurrent.futures
root=pathlib.Path('work/flycast-vk');src=root/'source';src.mkdir(exist_ok=True)
def fetch(url):
    return urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'ActionPi-test'}),timeout=45).read()
def archive(repo,ref,dest):
    import io
    raw=fetch('https://codeload.github.com/'+repo+'/tar.gz/'+ref)
    with tarfile.open(fileobj=io.BytesIO(raw),mode='r:gz') as tf:
        for m in tf.getmembers():
            parts=pathlib.PurePosixPath(m.name).parts[1:]
            if not parts:continue
            if m.isfile():
                p=dest.joinpath(*parts);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(tf.extractfile(m).read())
    print('FETCH',repo,ref,flush=True)
if not (src/'CMakeLists.txt').exists():archive('flyinghead/flycast','v2.7',src)
tree=json.loads(fetch('https://api.github.com/repos/flyinghead/flycast/git/trees/v2.7?recursive=1'))
mods={}
for part in (src/'.gitmodules').read_text().split('[submodule ')[1:]:
    path=next((x.split('=',1)[1].strip() for x in part.splitlines() if x.strip().startswith('path =')),None)
    url=next((x.split('=',1)[1].strip() for x in part.splitlines() if x.strip().startswith('url =')),None)
    if path and url:mods[path]=url
def job(item):
    p=item['path'];url=mods.get(p)
    if not url:return
    repo=url.removeprefix('https://github.com/').removesuffix('.git')
    if '://' in repo:print('SKIP',p,url);return
    dest=src/p
    if any(dest.iterdir()) if dest.exists() else False:return
    archive(repo,item['sha'],dest)
items=[x for x in tree['tree'] if x['type']=='commit']
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:list(ex.map(job,items))
(root/'source-tree.json').write_text(json.dumps(tree),encoding='utf-8')
print('READY')
