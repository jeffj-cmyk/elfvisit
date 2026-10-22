"""Wrap page.html (the preview source) into a standalone docs/index.html for hosting."""
import pathlib, urllib.parse

root = pathlib.Path(__file__).parent
src = (root / "page.html").read_text()
head, body = src.split("<!--BODY-->", 1)

icon = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="10" fill="#0C1733"/>'
        '<path d="M8 34c6-18 14-26 26-28 4 6 2 12-2 16" fill="#C8283A"/><path d="M6 33h30a4 4 0 0 1 0 8H6a4 4 0 0 1 0-8z" fill="#FFF6E6"/>'
        '<circle cx="35" cy="7" r="5" fill="#E9B949"/></svg>')
desc = ("Elf Visit: a North Pole elf comes to your home in Gilbert, Chandler, Queen Creek, Mesa or Scottsdale, "
        "reads two Christmas stories and delivers a gift from Santa. November 1 to Christmas Eve.")

doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0C1733">
<meta property="og:title" content="Elf Visit">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://elfvisit.com/">
<link rel="canonical" href="https://elfvisit.com/">
<link rel="icon" href="data:image/svg+xml,{urllib.parse.quote(icon)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{head.strip().replace("<title>Elf Visit</title>", "<title>Elf Visit | An elf at your door, East Valley Arizona</title>")}
</head>
<body>
{body.strip()}
</body>
</html>
"""
out = root / "docs"
out.mkdir(exist_ok=True)
(out / "index.html").write_text(doc)
(out / ".nojekyll").write_text("")
print("wrote", out / "index.html", len(doc), "bytes")
