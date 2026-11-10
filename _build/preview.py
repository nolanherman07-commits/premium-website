# Bundles every page + photo into one self-contained preview file.
import base64, re, json, os, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")
def uri(p):
    mime = 'image/png' if p.endswith('.png') else 'image/jpeg'
    return f"data:{mime};base64," + base64.b64encode(open(p,'rb').read()).decode()
pages = ['index','about','buy','sell','listings','areas','hickory','newton','granite-falls','contact']
css = open('styles.css').read(); js = open('script.js').read()
bodies = {pg: re.search(r'<body>\n(.*)<script src="script.js"></script>', open(f'{pg}.html').read(), re.S).group(1) for pg in pages}
sections = ''.join(f'<div class="pgview" id="pg-{pg}"{"" if pg=="index" else " hidden"}>{b}</div>' for pg, b in bodies.items())
for pg in pages: sections = sections.replace(f'href="{pg}.html', f'href="#pg-{pg}')
sections = sections.replace('href="#pg-listings#sold"', 'href="#pg-listings"').replace(' loading="lazy"', '')
sections = sections.replace('data-guide="Hickory-Area-Home-Buyers-Guide.pdf"', 'data-guide="https://nolanherman07-commits.github.io/nolan-herman-premium/Hickory-Area-Home-Buyers-Guide.pdf"')
imgs = {p: uri(p) for p in glob.glob('images/*.*') + glob.glob('images/listings/*.*')}
loader = '<script>const IMG=' + json.dumps(imgs) + ''';
document.querySelectorAll("img").forEach(i=>{const s=i.getAttribute("src"); if(IMG[s]) i.src=IMG[s];});
document.querySelectorAll("[style*='images/']").forEach(el=>{let s=el.getAttribute("style"); for(const k in IMG) s=s.split(k).join(IMG[k]); el.setAttribute("style",s);});
</script>'''
router = '''<script>
function route(){ const id=(location.hash||"#pg-index").slice(1); const t=document.getElementById(id);
  if(!t||!t.classList.contains("pgview")) return; document.querySelectorAll(".pgview").forEach(v=>v.hidden=v!==t); scrollTo(0,0);
  t.querySelectorAll(".rev").forEach(el=>el.classList.add("in")); }
addEventListener("hashchange", route); route();
</script>'''
doc = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Nolan Herman, REALTOR® | Nestlewood Realty</title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Open+Sans:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet" />
<style>{css}</style></head><body>{sections}{loader}<script>{js}</script>{router}</body></html>'''
open('nolan-herman-premium-preview.html','w').write(doc)
print(len(doc)//1024, 'KB')
