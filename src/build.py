# Builds the repo's index.html: the original page's CSS and head, the new CSS, the logo symbol, the new body, the Firebase
# scripts and the app. Chunks of the original are found by content, not line numbers, so editing them can't shift the slices.
import os
SP = os.path.dirname(os.path.abspath(__file__)) + "/"   # this folder: the sources
ROOT = os.path.dirname(SP.rstrip("/")) + "/"          # the repo: index.html is written here
orig = open(SP + "index.orig.html").read()
css_end = orig.index("</style>")                                      # original CSS ends here; new CSS goes right before it
logo_end = orig.index("</symbol></svg>", css_end) + len("</symbol></svg>")
fb0 = orig.index('<script src="https://www.gstatic.com/firebasejs/'); fb1 = orig.index('<script src="firebase-config.js"></script>') + len('<script src="firebase-config.js"></script>')
app = open(SP + "app.js").read()
css = open(SP + "new.css").read()
body = open(SP + "body.html").read()
out = orig[:css_end] + "\n" + css + "\n" + orig[css_end:logo_end] + "\n" + body + "\n" + orig[fb0:fb1] + "\n<script>\n" + app + "</script>\n</body>\n</html>\n"
assert out.count('<header class="mast">') == 1 and out.count("<main>") == 1 and out.count('id="gg-logo"') == 1
open(ROOT + "index.html", "w").write(out)
print("built", len(out), "bytes,", out.count("\n"), "lines")
