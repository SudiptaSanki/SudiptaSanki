def make_header_svg():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="80" height="80">
    <!-- Dark Background -->
    <rect width="200" height="200" fill="transparent" rx="20"/>

    <!-- Glowing Definitions -->
    <defs>
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="6" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <linearGradient id="cyberGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#8B5CF6"/>
            <stop offset="100%" stop-color="#3B82F6"/>
        </linearGradient>
    </defs>

    <!-- Outer Rotating Ring -->
    <circle cx="100" cy="100" r="70" fill="none" stroke="url(#cyberGradient)" stroke-width="6" stroke-dasharray="80 30" filter="url(#glow)">
        <animateTransform attributeName="transform" type="rotate" from="0 100 100" to="360 100 100" dur="4s" repeatCount="indefinite" />
    </circle>

    <!-- Inner Counter-Rotating Ring -->
    <circle cx="100" cy="100" r="50" fill="none" stroke="#F43F5E" stroke-width="4" stroke-dasharray="40 20" filter="url(#glow)" opacity="0.8">
        <animateTransform attributeName="transform" type="rotate" from="360 100 100" to="0 100 100" dur="3s" repeatCount="indefinite" />
    </circle>

    <!-- Center Tech Symbol -->
    <path d="M 80,75 L 60,100 L 80,125 M 120,75 L 140,100 L 120,125" fill="none" stroke="#10B981" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" filter="url(#glow)">
        <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite" />
    </path>
    <line x1="110" y1="70" x2="90" y2="130" stroke="#10B981" stroke-width="8" stroke-linecap="round" filter="url(#glow)">
        <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite" />
    </line>

    <!-- Floating Particles -->
    <circle cx="100" cy="20" r="4" fill="#60A5FA" filter="url(#glow)">
        <animate attributeName="cy" values="20;180" dur="3s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0;1;0" dur="3s" repeatCount="indefinite" />
    </circle>
    <circle cx="40" cy="140" r="3" fill="#F472B6" filter="url(#glow)">
        <animate attributeName="cy" values="140;30" dur="4s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0;1;0" dur="4s" repeatCount="indefinite" />
    </circle>
    <circle cx="160" cy="60" r="5" fill="#34D399" filter="url(#glow)">
        <animate attributeName="cx" values="160;40" dur="5s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0;1;0" dur="5s" repeatCount="indefinite" />
    </circle>
</svg>"""
    with open("top-header-animated.svg", "w") as f:
        f.write(svg_content)
    print("Created top-header-animated.svg")

if __name__ == "__main__":
    make_header_svg()
