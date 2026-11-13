"""共通ヘッダー・フッターを各ページに差し込んで HTML を書き出す。
使い方: python3 build.py   （pages/*.html → ./*.html）
"""
import pathlib, re

ROOT = pathlib.Path(__file__).parent
SITE_URL = "https://marais.co.jp/"

NAV = [
    ("index.html#about", "GOATについて", "about"),
    ("index.html#work", "お仕事", None),
    ("index.html#flow", "ご利用の流れ", None),
    ("index.html#faq", "よくある質問", None),
    ("index.html#office", "事業所情報", None),
    ("ec.html", "企業の方へ", "ec"),
]

HEAD = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{site}img/ogp.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="google-site-verification" content="R8UAGRc12L2dRGkrX6KynYFcTC_PrOb49aAnZQQxa30">
<link rel="icon" href="img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New:wght@400;500;700&family=Zen+Maru+Gothic:wght@700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css">
</head>
<body>
<a class="skip" href="#main">本文へ移動</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="img/logo.png" alt="" width="44" height="44"><span>就労継続支援A型事業所 GOAT<small>福岡市東区</small></span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="gnav"><i></i><i></i><i></i>メニュー</button>
    <nav class="gnav" id="gnav" aria-label="メインメニュー">
      <ul>
{nav}
        <li><a class="nav-cta" href="contact.html">見学・お問い合わせ</a></li>
      </ul>
    </nav>
  </div>
</header>
<main id="main">
"""

FOOT = """</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-brand">
      <img src="img/logo.png" alt="GOAT" width="64" height="64">
      <p>就労継続支援A型事業所 GOAT<br>運営：Marais株式会社<br>〒812-0063 福岡県福岡市東区原田4-25-1<br>TEL 092-214-2786</p>
    </div>
    <div class="foot-cols">
      <div>
        <h3>働きたい方へ</h3>
        <ul>
          <li><a href="about.html">GOATについて</a></li>
          <li><a href="index.html#work">お仕事</a></li>
          <li><a href="index.html#flow">ご利用の流れ</a></li>
          <li><a href="index.html#faq">よくある質問</a></li>
        </ul>
      </div>
      <div>
        <h3>企業の方へ</h3>
        <ul>
          <li><a href="ec.html">EC向け物流サービス</a></li>
          <li><a href="ec.html#price">料金</a></li>
          <li><a href="ec.html#flow">ご利用の流れ</a></li>
        </ul>
      </div>
      <div>
        <h3>GOAT</h3>
        <ul>
          <li><a href="contact.html">お問い合わせ</a></li>
          <li><a href="privacy.html">プライバシーポリシー</a></li>
          <li><a href="https://www.instagram.com/syurou.goat/">Instagram</a></li>
          <li><a href="https://www.tiktok.com/@syurou.goat0901">TikTok</a></li>
        </ul>
      </div>
    </div>
    <p class="copyright">© 2025 Marais株式会社</p>
  </div>
</footer>
<script src="js/site.js"></script>
</body>
</html>
"""


def render(src: pathlib.Path):
    text = src.read_text(encoding="utf-8")
    m = re.match(r"<!--\s*title:(.*?)\n\s*desc:(.*?)\n\s*current:(.*?)\s*-->\n", text, re.S)
    title, desc, current = (s.strip() for s in m.groups())
    body = text[m.end():]
    nav = "\n".join(
        f'        <li><a href="{href}"{" aria-current=\"page\"" if key and key == current else ""}>{label}</a></li>'
        for href, label, key in NAV
    )
    url = SITE_URL + ("" if src.name == "index.html" else src.name)
    out = HEAD.format(title=title, desc=desc, url=url, site=SITE_URL, nav=nav) + body + FOOT
    (ROOT / src.name).write_text(out, encoding="utf-8")
    print("built", src.name)


for p in sorted((ROOT / "pages").glob("*.html")):
    render(p)
