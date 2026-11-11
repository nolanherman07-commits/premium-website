# Builds every page of the premium site. Run: python3 _build/build.py
import os, html
os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")
E = html.escape

A = dict(
  name="Nolan Herman", first="Nolan", title="REALTOR®", brokerage="Nestlewood Realty",
  phone="828-404-5335", tel="+18284045335", email="nolan@nestlewoodrealty.com",
  address="825 Highland Ave SE, Hickory, NC 28602",
  zillow="https://www.zillow.com/profile/Nolansellnc",
  homes="https://www.homes.com/real-estate-agents/nolan-herman/2672vt8/",
  instagram="https://www.instagram.com/nolansellsnc/", facebook="https://www.facebook.com/profile.php?id=61578346302536",
  calendly="",  # PLACEHOLDER: paste your Calendly link here
)
MAP = "https://www.google.com/maps/search/?api=1&query=" + A["address"].replace(" ", "+")

FEATURED = [
  ("5182 Corbin Ln", "Hickory, NC 28601", "https://www.zillow.com/homedetails/5182-Corbin-Ln-Hickory-NC-28601/92556701_zpid/", "images/listings/5182-corbin-ln.jpg"),
  ("1056 Old Hampton Rd", "Boone, NC 28607", "https://www.zillow.com/homedetails/1056-Old-Hampton-Rd-Boone-NC-28607/99379549_zpid/", "images/listings/1056-old-hampton-rd.jpg"),
  ("2137 Olde Farm Rd", "Hudson, NC 28638", "https://www.zillow.com/homedetails/2137-Olde-Farm-Rd-Hudson-NC-28638/70112964_zpid/", "images/listings/2137-olde-farm-rd.jpg"),
]
SOLD = [
  ("7107 Rolling Hills Dr", "Sherrills Ford, NC 28673", "https://www.zillow.com/homedetails/7107-Rolling-Hills-Dr-Sherrills-Ford-NC-28673/71910314_zpid/", "images/listings/7107-rolling-hills-dr.jpg"),
  ("350 14th Ave SW", "Hickory, NC 28602", "https://www.zillow.com/homedetails/350-14th-Ave-SW-Hickory-NC-28602/464120420_zpid/", "images/listings/350-14th-ave-sw.jpg"),
  ("1898 Henry Smith St", "Hickory, NC 28601", "https://www.zillow.com/homedetails/1898-Henry-Smith-St-Hickory-NC-28601/227261430_zpid/", ""),
]
# Action shots on the About page. To add your photo, upload it to images/action/ with the same file name.
ACTION_SHOTS = [
  ("closing", "Nolan at a closing"), ("showing", "Nolan showing a home"), ("clients", "Nolan with clients"),
  ("open-house", "Nolan at an open house"), ("around-town", "Nolan around town"),
]
REVIEWS = [
  ("Lorena & Martin", "Home Buyers", "Working with Nolan has been great! Throughout our home-buying process, he was incredibly communicative. He promptly answered calls and emails, keeping us informed about every development... He looked out for our best interests, getting us a fantastic deal. You feel like you're their only client."),
  ("Jacopo B.", "Home Buyer", "Working with Nolan has been an outstanding experience from start to finish. His professionalism, deep market knowledge, and ability to communicate clearly made the entire home-buying process significantly easier and far less stressful... He is exceptional at what he does, and I'm grateful to have worked with him."),
  ("Alfred & Rashonda Wingate", "First-Time Home Buyers", "As first-time homebuyers, we appreciated his professionalism, knowledge, and dedication throughout the entire process. We couldn't have asked for a better realtor than Nolan... We absolutely love our new home and highly recommend Nolan to anyone looking for a realtor who genuinely cares about their clients."),
]
HOODS = {
  "hickory": dict(name="Hickory", tag="City amenities, lake living", county="Catawba County",
    intro="Hickory is the largest city in the Catawba Valley, with a lively downtown, Lake Hickory on the Catawba River, and Lenoir-Rhyne University. You get city amenities, lake life, and an easy drive to Charlotte and the mountains.",
    facts=[("Catawba", "County"), ("~1 hr", "To Charlotte"), ("Lake Hickory", "On the water"), ("$XXX,XXX", "Median price*")],
    love=["Downtown restaurants, shops and events", "Lake Hickory for boating and waterfront homes", "Parks, greenways and youth sports", "Quick access to I-40 and US-321"]),
  "newton": dict(name="Newton", tag="Small-town charm, central location", county="Catawba County",
    intro="Newton is the county seat of Catawba County, known for its historic courthouse square and small-town feel. It sits just south of Hickory, so you're minutes from shopping, jobs and everything the area offers.",
    facts=[("County Seat", "Catawba County"), ("~15 min", "To Hickory"), ("Historic", "Downtown square"), ("$XXX,XXX", "Median price*")],
    love=["Historic downtown and local events", "More home for your money", "Quiet neighborhoods close to Hickory", "Easy commute in every direction"]),
  "granite-falls": dict(name="Granite Falls", tag="Quiet living near the lakes", county="Caldwell County",
    intro="Granite Falls is a friendly small town in Caldwell County along US-321, between Hickory and Lenoir. It's close to Lake Rhodhiss and Lake Hickory, and a great fit if you want more space and a slower pace without being far from town.",
    facts=[("Caldwell", "County"), ("~15 min", "To Hickory"), ("Lakes", "Rhodhiss & Hickory"), ("$XXX,XXX", "Median price*")],
    love=["Small-town community feel", "Close to lakes and the outdoors", "Larger lots and room to grow", "Quick drive to Hickory and Lenoir"]),
}

I = {
 'phone':'<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/>',
 'text':'<path d="M20 2H4a2 2 0 0 0-2 2v18l4-4h14a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2zM7 9h10v2H7zm6 5H7v-2h6zm4-6H7V6h10z"/>',
 'email':'<path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5z"/>',
 'cal':'<path d="M19 4h-1V2h-2v2H8V2H6v2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 16H5V9h14z"/>',
 'zillow':'<path d="M12 1 1 9.6v2.6l3-2.2V23h16V10l3 2.2V9.6zm4.6 17.4H7.4l5.9-6.6H8.1l1.3-3.2h7.2l-5.8 6.6h5.8z"/>',
 'instagram':'<path d="M12 2.2c3.2 0 3.6 0 4.8.1 3.3.1 4.8 1.7 4.9 4.9.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 3.2-1.7 4.8-4.9 4.9-1.3.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-3.3-.1-4.8-1.7-4.9-4.9C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8C2.4 3.9 3.9 2.4 7.2 2.3 8.4 2.2 8.8 2.2 12 2.2zM12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4zm5.2-9.6a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4z"/>',
 'facebook':'<path d="M24 12a12 12 0 1 0-13.9 11.9v-8.4h-3V12h3V9.4c0-3 1.8-4.7 4.5-4.7 1.3 0 2.7.2 2.7.2v3h-1.5c-1.5 0-2 .9-2 1.9V12h3.4l-.5 3.5h-2.9v8.4A12 12 0 0 0 24 12z"/>',
 'house':'<path d="M12 3 2 11h3v9h5v-6h4v6h5v-9h3z"/>',
}
def ic(k): return f'<svg viewBox="0 0 24 24" aria-hidden="true">{I[k]}</svg>'
EXT = 'target="_blank" rel="noopener"'
def ph(label, cls="ph"): return f'<div class="{cls}"><span>{E(label)}</span></div>'

NAV = [("index.html","Home"),("about.html","About"),("buy.html","Buy"),("sell.html","Sell")]
def header(active):
    links = "".join(f'<a href="{h}" class="{"active" if h==active else ""}">{t}</a>' for h,t in NAV)
    return f'''<div class="topbar"><div class="wrap">
  <span><a href="tel:{A["tel"]}">{A["phone"]}</a> &nbsp;·&nbsp; <a href="mailto:{A["email"]}">{A["email"]}</a></span>
  <span class="tsoc"><a href="{A["instagram"]}" {EXT} aria-label="Instagram">{ic("instagram")}</a><a href="{A["facebook"]}" {EXT} aria-label="Facebook">{ic("facebook")}</a><a href="{A["zillow"]}" {EXT} aria-label="Zillow">{ic("zillow")}</a></span>
</div></div>
<header class="header"><div class="wrap">
  <a href="index.html"><img class="logo" src="images/logo.png" alt="Nestlewood Realty" /></a>
  <nav class="nav">{links}<a href="contact.html" class="btn">Contact Me</a></nav>
  <button class="menu-btn" aria-label="Menu"><span></span><span></span><span></span></button>
</div></header>'''

FOOTER = f'''<footer class="footer"><div class="wrap">
  <div class="f-grid">
    <div><img class="flogo" src="images/logo.png" alt="Nestlewood Realty" />
      <p>{A["name"]}, {A["title"]}<br />{A["brokerage"]}<br />{A["address"]}</p>
      <div class="fsoc"><a href="{A["instagram"]}" {EXT} aria-label="Instagram">{ic("instagram")}</a><a href="{A["facebook"]}" {EXT} aria-label="Facebook">{ic("facebook")}</a><a href="{A["zillow"]}" {EXT} aria-label="Zillow">{ic("zillow")}</a><a href="{A["homes"]}" {EXT} aria-label="Homes.com">{ic("house")}</a></div></div>
    <div><h4>Explore</h4><a href="buy.html">Buy a Home</a><a href="sell.html">Sell Your Home</a><a href="about.html">About Nolan</a><a href="contact.html">Contact</a></div>
    <div><h4>Contact</h4><a href="tel:{A["tel"]}">{A["phone"]}</a><a href="mailto:{A["email"]}">{A["email"]}</a><a href="contact.html">Send a Message</a><a href="{MAP}" {EXT}>Get Directions</a></div>
  </div>
  <div class="f-bottom"><span>© 2026 {A["brokerage"]}. All rights reserved.</span><span>Equal Housing Opportunity · {A["title"]}</span></div>
</div></footer>'''

def page(fname, title, active, body):
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{E(title)}</title>
<meta name="description" content="Nolan Herman, REALTOR® with Nestlewood Realty. Helping buyers and sellers in Hickory, Newton, Granite Falls and the Charlotte area." />
<link rel="icon" href="images/tree-icon.png" />
<link rel="preconnect" href="https://fonts.googleapis.com" /><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Open+Sans:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="styles.css" />
</head>
<body>
{header(active)}
{body}
{FOOTER}
<script src="script.js"></script>
</body>
</html>'''
    open(fname, "w").write(doc)

def listing_card(addr, city, url, photo="", sold=False):
    pic = f'<img src="{photo}" alt="{E(addr)}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover" loading="lazy" />' if photo else ph("Listing photo")
    return f'''<a class="listing rev" href="{url}" {EXT}>
  <div class="pic"><span class="tag {"sold" if sold else ""}">{"Sold" if sold else "Featured"}</span>{pic}</div>
  <div class="body"><div class="price">{"Sold · $XXX,XXX" if sold else "$XXX,XXX"}</div><p class="addr">{E(addr)}</p><p class="city">{E(city)}</p>
  <div class="specs"><span><b>X</b> bd</span><span><b>X</b> ba</span><span><b>X,XXX</b> sqft</span></div>
  <div class="zl">View on Zillow →</div></div></a>'''

def hood_card(key):
    h = HOODS[key]
    return f'<a class="hood rev" href="{key}.html">{ph(h["name"] + " photo")}<div class="cap"><h3>{h["name"]}</h3><p>{h["tag"]}</p></div></a>'

REVIEW_SLIDER = f'''<section class="section dark" id="reviews"><div class="wrap center">
  <p class="eyebrow">Client Reviews</p><h2>What my clients say</h2>
  <div class="slider">{"".join(f'<div class="rv{" on" if i==0 else ""}"><div class="stars">★★★★★</div><blockquote>“{E(t)}”</blockquote><cite>{E(n)}<span>{E(ty)}</span></cite></div>' for i,(n,ty,t) in enumerate(REVIEWS))}
    <div class="rv-nav"><button class="rv-prev" aria-label="Previous review">←</button><span class="rv-count">1 / {len(REVIEWS)}</span><button class="rv-next" aria-label="Next review">→</button></div>
  </div>
  <a class="zillow-badge" href="{A["zillow"]}" {EXT}>{ic("zillow").replace("<svg", '<svg style="width:18px;height:18px;fill:currentColor"')} Read all my reviews on Zillow</a>
</div></section>'''

VALUATION = '''<section class="valuation" id="value"><div class="wrap val-grid">
  <div><h2>What's your home worth?</h2><p>Get a free, personalized home value report from Nolan, not an algorithm.</p></div>
  <form class="val-form lead-form" data-subject="Home value request"><input name="address" placeholder="Enter your home address" required /><button class="btn btn-dark" type="submit">Get My Value</button></form>
</div></section>'''

GUIDE = '''<section class="section soft" id="guide"><div class="wrap guide">
  <div class="book rev"><small>FREE GUIDE</small><h3>The Hickory Area Home Buyer's Guide</h3><span class="by">By Nolan Herman, REALTOR®</span><img src="images/logo.png" alt="" /></div>
  <div class="rev"><p class="eyebrow">Free Download</p><h2>Buying a home? Start here.</h2>
    <p class="lead">My step-by-step guide to buying in Hickory, Newton, Granite Falls and the Charlotte area, written in plain English.</p>
    <ul class="checks"><li>How much home you can really afford</li><li>Getting pre-approved (and why it wins offers)</li><li>How to make an offer that stands out</li><li>Inspections, appraisals and closing day, explained</li><li>A checklist for your first home tour</li></ul>
    <form class="inline-form lead-form" data-subject="Free buyer's guide request" data-guide="Hickory-Area-Home-Buyers-Guide.pdf"><input name="name" placeholder="First name" required /><input name="email" type="email" placeholder="Email address" required /><button class="btn" type="submit">Send My Guide</button></form>
    <p class="fine">I'll email you the guide. No spam, ever.</p></div>
</div></section>'''

BOOKING = f'''<section class="section" id="book"><div class="wrap booking">
  <div class="rev"><p class="eyebrow">Book a Call</p><h2>Pick a time that works for you.</h2>
    <p class="lead">Grab a free 15-minute call to talk about buying, selling, or what your home is worth. No pressure, just answers.</p>
    <div class="hero-actions"><a class="btn" href="tel:{A["tel"]}">{ic("phone")} Call {A["first"]}</a><a class="btn btn-line" href="sms:{A["tel"]}">{ic("text")} Text {A["first"]}</a></div></div>
  <div class="calendar-ph rev"><div>{ic("cal").replace("<svg", '<svg style="width:40px;height:40px;fill:#f78d2d;margin:0 auto"')}
    <div style="font:1.6rem var(--head);color:var(--brown);margin-top:.5rem">Calendly Booking</div>
    <div class="cal">{"".join(f'<i class="{"sel" if d==14 else "av" if d in (9,10,15,16,17,21,22) else ""}">{d}</i>' for d in range(5,26))}</div>
    <small>PLACEHOLDER: your Calendly calendar goes here</small></div></div>
</div></section>'''

CTA = f'''<section class="cta"><div class="wrap"><p class="eyebrow">Ready when you are</p><h2>Let's go home.</h2>
  <p>Buying, selling, or just curious? I'm a call or text away.</p>
  <div class="cta-actions"><a class="btn" href="tel:{A["tel"]}">{ic("phone")} Call {A["first"]}</a><a class="btn btn-ghost" href="sms:{A["tel"]}">{ic("text")} Text {A["first"]}</a><a class="btn btn-ghost" href="contact.html">{ic("email")} Message Me</a></div>
</div></section>'''

STATS = '''<section class="stats"><div class="wrap stats-grid">
  <div class="stat"><strong>$10M+</strong><span>Total sales volume</span></div>
  <div class="stat"><strong>$8M+</strong><span>Sold in 2026</span></div>
  <div class="stat"><strong>100%</strong><span>Of my listings sold</span></div>
  <div class="stat"><strong>2 Years</strong><span>In real estate</span></div>
  <div class="stat"><strong>600+</strong><span>Families helped by Nestlewood</span></div>
</div></section>'''

# ---------------- HOME ----------------
page("index.html", "Nolan Herman, REALTOR® | Nestlewood Realty | Hickory, NC", "index.html", f'''
<section class="hero">
  <div class="slides"><div class="slide on" style="background-image:url('images/cover.jpg')"></div><div class="slide ph-slide"></div><div class="slide ph-slide"></div></div>
  <div class="wrap"><div class="hero-copy">
    <p class="eyebrow">Hickory · Charlotte · and surrounding areas</p>
    <h1>Let's go <em>home.</em></h1>
    <p>I'm Nolan Herman, a REALTOR® with Nestlewood Realty. I make buying and selling simple, fast, and stress-free.</p>
    <div class="hero-actions"><a class="btn" href="contact.html">Contact Me</a><a class="btn btn-ghost" href="#value">What's My Home Worth?</a></div>
  </div></div>
  <div class="dots"><i class="on"></i><i></i><i></i></div>
</section>
{STATS}
<section class="section"><div class="wrap split">
  <div class="portrait rev"><img src="images/headshot.jpg" alt="Nolan Herman" />
    <div class="badge-float"><img src="images/tree-icon.png" alt="" /><div><strong>$10M+</strong><span>Sold in 2 years</span></div></div></div>
  <div class="rev"><p class="eyebrow">Meet Nolan</p><h2>I carved my own path into real estate.</h2>
    <p class="lead">After realizing the traditional school path wasn't for me, I decided to carve out my own path in real estate, even though no one in my family had experience in the industry. My passion comes from my own experience with how stressful moving can be, and I want to make that process easier, smoother, and more enjoyable for others.</p>
    <ul class="checks"><li>Fast answers by call, text, or email</li><li>Local know-how across the Catawba Valley</li><li>Social media marketing that gets your home seen</li></ul>
    <a class="btn btn-dark" href="about.html">My Story</a></div>
</div></section>
<section class="section soft"><div class="wrap">
  <div class="head-row"><div><p class="eyebrow">Featured &amp; Recently Sold</p><h2>Homes I'm proud to represent</h2></div><a class="link" href="{A["zillow"]}" {EXT}>More on Zillow →</a></div>
  <div class="cards5">{"".join(listing_card(*l) for l in FEATURED)}{"".join(listing_card(*l, sold=True) for l in SOLD[:2])}</div>
</div></section>
{REVIEW_SLIDER}
{VALUATION}
{CTA}''')

# ---------------- ABOUT ----------------
page("about.html", "About Nolan Herman | Nestlewood Realty", "about.html", f'''
<section class="page-hero" style="--bg:url('images/cover.jpg')"><div class="wrap"><div class="crumbs">Home / About</div><h1>Meet Nolan Herman</h1><p>Licensed REALTOR® with Nestlewood Realty, serving Hickory, Newton, Granite Falls and the Charlotte area.</p></div></section>
<section class="section"><div class="wrap split">
  <div class="portrait rev"><img src="images/headshot.jpg" alt="Nolan Herman" /></div>
  <div class="rev"><p class="eyebrow">My Story</p><h2>I didn't wait for an invitation.</h2>
    <p class="lead">Real estate wasn't a family business, and I didn't have a traditional path into the industry. School wasn't for me, and after experiencing firsthand how stressful moving can be, I knew I wanted to build a career where I could make that experience easier for others.</p>
    <p>I took a chance on myself, reached out for an opportunity, and turned that first yes into a career built on hard work, determination, and helping people find a place to call home.</p>
    <p>Two years later, I'm a licensed REALTOR® with Nestlewood Realty. I've helped clients buy and sell over $10 million in homes, including more than $8 million in 2026 alone, and every one of my listings has sold. I bring that same hustle to every client: fast answers, honest advice, and marketing that gets results.</p>
    <div class="hero-actions"><a class="btn" href="contact.html">Work With Me</a><a class="btn btn-line" href="{A["zillow"]}" {EXT}>{ic("zillow")} Zillow Profile</a><a class="btn btn-line" href="{A["homes"]}" {EXT}>{ic("house")} Homes.com</a></div></div>
</div></section>
<section class="section soft"><div class="wrap center"><p class="eyebrow">How I Got Here</p><h2>From emails to $10M+</h2>
  <div class="timeline">
    <div class="tl rev"><i>1</i><h3>Growing Up</h3><p>Saw firsthand how stressful moving can be for a family.</p></div>
    <div class="tl rev"><i>2</i><h3>The Emails</h3><p>Out of high school, I emailed brokers asking for a shot.</p></div>
    <div class="tl rev"><i>3</i><h3>The Internship</h3><p>One broker said yes. I learned every part of the business.</p></div>
    <div class="tl rev"><i>4</i><h3>Licensed REALTOR®</h3><p>2 years in, $10M+ sold and 100% of my listings sold.</p></div>
  </div></div></section>
<section class="section"><div class="wrap"><div class="head-row"><div><p class="eyebrow">Behind the Scenes</p><h2>On the job</h2></div></div>
  <div class="gallery">{"".join(f'<div class="shot"><img src="images/action/{f}.jpg" alt="{E(t)}" loading="lazy" /></div>' for f, t in ACTION_SHOTS)}</div></div></section>
{STATS}
{REVIEW_SLIDER}
{CTA}''')

# ---------------- BUY ----------------
page("buy.html", "Buy a Home | Nolan Herman, REALTOR®", "buy.html", f'''
<section class="page-hero" style="--bg:url('images/cover.jpg')"><div class="wrap"><div class="crumbs">Home / Buy</div><h1>Buy a Home</h1><p>From your first showing to closing day, I'll help you find the right home and negotiate the best deal.</p></div></section>
<section class="section"><div class="wrap center"><p class="eyebrow">How It Works</p><h2>Your path to the keys</h2>
  <div class="steps" style="text-align:left;margin-top:2rem">
    <div class="step rev"><h3>Talk</h3><p>A quick call about what you want, where, and your budget.</p></div>
    <div class="step rev"><h3>Get Pre-Approved</h3><p>I'll connect you with trusted lenders so you can shop with confidence.</p></div>
    <div class="step rev"><h3>Tour & Offer</h3><p>We tour homes together, then write a strong offer that stands out.</p></div>
    <div class="step rev"><h3>Close</h3><p>I handle inspections, appraisal, and paperwork right up to closing day.</p></div>
  </div></div></section>
<section class="section soft" id="calculator"><div class="wrap"><div class="head-row"><div><p class="eyebrow">Mortgage Calculator</p><h2>What will my payment be?</h2></div></div>
  <div class="calc rev">
    <div class="inputs">
      <label>Home price ($)<input id="c-price" type="number" value="350000" min="0" step="1000" /></label>
      <div class="row"><label>Down payment (%)<input id="c-down" type="number" value="10" min="0" max="100" step="1" /></label><label>Interest rate (%)<input id="c-rate" type="number" value="6.5" min="0" step="0.05" /></label></div>
      <div class="row"><label>Loan term (years)<input id="c-term" type="number" value="30" min="1" step="1" /></label><label>Taxes + insurance / mo ($)<input id="c-extra" type="number" value="350" min="0" step="10" /></label></div>
      <p class="fine">Estimate only. Talk to a lender for your exact numbers.</p>
    </div>
    <div class="result"><small>Estimated monthly payment</small><div class="pay" id="c-pay">$0</div>
      <div class="bd"><div><span>Principal & interest</span><b id="c-pi">$0</b></div><div><span>Taxes & insurance</span><b id="c-ti">$0</b></div><div><span>Loan amount</span><b id="c-loan">$0</b></div></div></div>
  </div></div></section>
{CTA}''')

# ---------------- SELL ----------------
page("sell.html", "Sell Your Home | Nolan Herman, REALTOR®", "sell.html", f'''
<section class="page-hero" style="--bg:url('images/cover.jpg')"><div class="wrap"><div class="crumbs">Home / Sell</div><h1>Sell Your Home</h1><p>Smart pricing, professional photos, and social media marketing that puts your home in front of the right buyers.</p></div></section>
<section class="stats"><div class="wrap stats-grid">
  <div class="stat"><strong>100%</strong><span>Of my listings sold</span></div><div class="stat"><strong>$10M+</strong><span>Total sales volume</span></div><div class="stat"><strong>$8M+</strong><span>Sold in 2026</span></div><div class="stat"><strong>XX</strong><span>Avg. days on market*</span></div><div class="stat"><strong>XX%</strong><span>Of asking price*</span></div>
</div></section>
<section class="section"><div class="wrap center"><p class="eyebrow">My Selling Plan</p><h2>How I get your home sold</h2>
  <div class="steps" style="text-align:left;margin-top:2rem">
    <div class="step rev"><h3>Price It Right</h3><p>A detailed look at recent sales so we list at the right number from day one.</p></div>
    <div class="step rev"><h3>Make It Shine</h3><p>Professional photos and video that make buyers stop scrolling.</p></div>
    <div class="step rev"><h3>Market Everywhere</h3><p>The MLS, Zillow, Homes.com, plus targeted Instagram and Facebook ads.</p></div>
    <div class="step rev"><h3>Negotiate & Close</h3><p>I screen offers, negotiate hard, and handle every detail to closing.</p></div>
  </div></div></section>
{VALUATION}
{REVIEW_SLIDER}
{CTA}''')

# ---------------- CONTACT ----------------
page("contact.html", "Contact Nolan Herman | Nestlewood Realty", "contact.html", f'''
<section class="page-hero" style="--bg:url('images/cover.jpg')"><div class="wrap"><div class="crumbs">Home / Contact</div><h1>Let's Talk</h1><p>Call, text, or email. I respond fast.</p></div></section>
<section class="section"><div class="wrap split" style="align-items:start">
  <div class="rev"><p class="eyebrow">Reach Me</p><h2>I'm here to help.</h2>
    <div class="hero-actions" style="flex-direction:column;align-items:stretch;max-width:380px">
      <a class="btn" href="tel:{A["tel"]}">{ic("phone")} Call {A["phone"]}</a><a class="btn" href="sms:{A["tel"]}">{ic("text")} Text {A["first"]}</a><a class="btn btn-dark" href="mailto:{A["email"]}">{ic("email")} {A["email"]}</a></div>
    <p style="margin-top:1.6rem"><strong>Office</strong><br /><a class="link" href="{MAP}" {EXT}>{A["address"]}</a></p></div>
  <form class="form rev lead-form" data-subject="Website contact form">
    <div class="row"><label>Name<input name="name" required /></label><label>Phone<input name="phone" type="tel" /></label></div>
    <label>Email<input name="email" type="email" required /></label>
    <label>I'm interested in<select name="topic"><option>Buying</option><option>Selling</option><option>Home value report</option><option>Something else</option></select></label>
    <label>Message<textarea name="message" rows="4"></textarea></label>
    <button class="btn" type="submit">Send Message</button>
  </form></div></section>
''')
print("built")
