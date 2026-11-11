# Nolan Herman, REALTOR® | Nestlewood Realty (Premium site)

Pages: Home (`index.html`), About, Buy, Sell, Listings, Areas (Hickory, Newton, Granite Falls), Contact.

## Files
- `*.html`: the pages.
- `styles.css` / `script.js`: the design and the interactive parts (slideshow, reviews slider, mortgage calculator, forms).
- `images/`: logo, headshot, cover photo. Upload a new photo with the same file name to swap it.
- `Hickory-Area-Home-Buyers-Guide.pdf`: the free guide visitors get after signing up.
- `guide-source/guide.html`: the guide's source, used to make the PDF.
- `_build/build.py`: all of the site's text, listings, reviews and links live at the top of this file.
  After editing it, run `python3 _build/build.py` to rebuild every page.

## Still placeholders
- Listing prices, beds/baths/sq ft, and photos
- Area photos (striped boxes)
- Action shots on the About page: a stock photo shows until you upload your own to `images/action/` (create the folder) using the file names (closing, showing, clients, open-house, around-town)
- Calendly booking calendar (paste the link into `calendly` in `_build/build.py`)
- Market numbers on area pages and the Sell page stats marked with *

## Forms
Forms open the visitor's email app addressed to nolan@nestlewoodrealty.com.
For leads straight to your inbox, create a free form at formspree.io and paste its URL into
`FORM_ENDPOINT` at the top of `script.js`.
