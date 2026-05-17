import urllib.request
import re

icons = {
    'java': 'java',
    'pycharm': 'pycharm',
    'sql': 'postgresql',
    'mongodb': 'mongodb'
}

colors = {
    'java': '#ED8B00',
    'pycharm': '#000000',
    'sql': '#4169E1',
    'mongodb': '#47A248'
}

for name, slug in icons.items():
    url = f"https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/{slug}.svg"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            svg_data = response.read().decode('utf-8')
            
            # Replace fill color if there's no path fill, or we can just inject a fill attribute
            # Some SVGs might not have width/height or might be 24x24.
            # We will wrap the inner path in a group with animation.
            
            # Extract the path(s)
            paths = re.findall(r'(<path.*?>)', svg_data)
            path_str = " ".join(paths)
            
            # We'll create a nice bouncing animated SVG wrapper
            animated_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="50" height="50">
  <defs>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="{colors[name]}" flood-opacity="0.4"/>
    </filter>
  </defs>
  <g filter="url(#shadow)" fill="{colors[name]}">
    <animateTransform attributeName="transform" type="translate" values="0,0; 0,-8; 0,0" dur="2s" repeatCount="indefinite" />
    <g transform="translate(10, 10) scale(3.33)">
      {path_str}
    </g>
  </g>
</svg>"""
            
            with open(f"{name}-animated.svg", "w") as f:
                f.write(animated_svg)
            print(f"Generated {name}-animated.svg")
            
    except Exception as e:
        print(f"Failed to fetch {slug}: {e}")
