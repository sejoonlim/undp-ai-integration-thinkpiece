# app.py
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px  # Plotly import
from utils import glossary_term

# =======================
# Set Page Configuration
# =======================
st.set_page_config(
    page_title="UNDP AI Integration Think Piece",  # Browser tab title
    page_icon=":globe_with_meridians:",  # Emoji or image URL
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================= 
# CSS for Tooltip Styling
# =======================

# UNDP color codes
UNDP_BLACK = "#000000"
UNDP_WHITE = "#ffffff"
UNDP_BLUE_100 = "#b5d5f5"
UNDP_BLUE_200 = "#94c4f5"
UNDP_BLUE_300 = "#6babeb"
UNDP_BLUE_400 = "#4f95dd"
UNDP_BLUE_500 = "#3288ce"
UNDP_BLUE_600 = "#006eb5"
UNDP_BLUE_700 = "#1f5a95"
UNDP_BLUE_800 = "#0468b1"
UNDP_GRAY_100 = "#fafafa"
UNDP_GRAY_200 = "#f7f7f7"
UNDP_GRAY_300 = "#edeff0"
UNDP_GRAY_400 = "#d4d6d8"
UNDP_GRAY_500 = "#a9b1b7"
UNDP_GRAY_600 = "#55606e"
UNDP_GRAY_700 = "#232e3d"
UNDP_LIGHT_YELLOW = "#ffe17e"
UNDP_YELLOW = "#ffeb00"
UNDP_DARK_YELLOW = "#fbc412"
UNDP_LIGHT_RED = "#ffbcb7"
UNDP_RED = "#ee402d"
UNDP_DARK_RED = "#d12800"
UNDP_LIGHT_GREEN = "#b8ecb6"
UNDP_GREEN = "#6de354"
UNDP_DARK_GREEN = "#59ba47"
UNDP_LIGHT_AZURE = "#a2daf3"
UNDP_AZURE = "#60d4f2"
UNDP_DARK_AZURE = "#00c1ff"
UNDP_LIGHT_PINK = "#ffb4ae"
UNDP_SILVERY_MOONLIGHT = "#ced0d3"
UNDP_SHUTTLE_GRAY = "#55606f"
UNDP_EBONY_CLAY = "#232e3e"
UNDP_SDG_RED = "#e5243b"
UNDP_SDG_MUSTARD = "#dda63a"
UNDP_SDG_KELLY_GREEN = "#4c9f38"
UNDP_SDG_DARK_RED = "#c5192d"
UNDP_SDG_RED_ORANGE = "#ff3a21"
UNDP_SDG_BRIGHT_BLUE = "#26bde2"
UNDP_SDG_YELLOW = "#fcc30b"
UNDP_SDG_BURGUNDY_RED = "#a21942"
UNDP_SDG_ORANGE = "#fd6925"
UNDP_SDG_MAGENTA = "#dd1367"
UNDP_SDG_GOLDEN_YELLOW = "#fd9d24"
UNDP_SDG_DARK_MUSTARD = "#bf8b2e"
UNDP_SDG_DARK_GREEN = "#3f7e44"
UNDP_SDG_BLUE = "#0a97d9"
UNDP_SDG_LIME_GREEN = "#56c02b"
UNDP_SDG_ROYAL_BLUE = "#00689d"
UNDP_SDG_NAVY_BLUE = "#19486a"

# Custom CSS including tooltip styles
custom_css = f"""
<style>
    @font-face {{
        font-family: 'SohneBreit';
        src: url('TestSohneBreit-Dreiviertelfett-BF663d89c955618.otf') format('opentype'),
    }}

    @font-face {{
        font-family: 'ProximaNova';
        src: url('path/to/ProximaNova-Regular.woff2') format('woff2'),
             url('path/to/ProximaNova-Regular.woff') format('woff');
    }}
    
    .title {{
        font-family: 'SohneBreit', sans-serif;
        font-size: 2.5em;
        color: {UNDP_BLACK};
        padding-bottom: 0.25em;
    }}
    
    .header {{
        font-family: 'ProximaNova', sans-serif;
        font-size: 2em;
        color: {UNDP_BLUE_800};
        padding-bottom: 0.15em;
    }}
    # border-bottom: 1px solid {UNDP_BLUE_800};
    
    .subheader {{
        font-family: 'ProximaNova', sans-serif;
        font-size: 1.5em;
        color: #333333;
    }}

    body {{
        font-family: 'ProximaNova', sans-serif;
    }}

    /* Tooltip styles */
    .tooltip {{
        position: relative;
        display: inline-block;
        cursor: pointer;
        border-bottom: 1px dotted {UNDP_BLACK}; /* Optional: underline with dotted line */
    }}

    .tooltip .tooltiptext {{
        visibility: hidden;
        width: 220px;
        background-color: #555;
        color: #fff;
        text-align: left;
        border-radius: 6px;
        padding: 5px 10px;
        position: absolute;
        z-index: 1;
        bottom: 125%; /* Position above the term */
        left: 50%;
        margin-left: -110px;
        opacity: 0;
        transition: opacity 0.3s;
    }}

    .tooltip:hover .tooltiptext {{
        visibility: visible;
        opacity: 1;
    }}

    /* Arrow below the tooltip */
    .tooltip .tooltiptext::after {{
        content: "";
        position: absolute;
        top: 100%; /* At the bottom of the tooltip */
        left: 50%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: #555 transparent transparent transparent;
    }}
</style>
"""

# Inject CSS
st.markdown(custom_css, unsafe_allow_html=True)

# =======================
# Sidebar Navigation
# =======================


# =======================
# Page Content
# =======================

st.markdown("<div class='title'>UNDP AI Integration Think Piece</div>", unsafe_allow_html=True)
st.markdown("**8 October 2024**")

st.markdown("<div class='header'>Executive Summary</div>", unsafe_allow_html=True)
st.markdown("""
This think piece critically examines UNDP’s current approach to integrating Artificial Intelligence (AI) into its operations, viewed from the perspective of an office located outside of New York. This paper proposes a fundamental shift in how UNDP engages with AI technologies, emphasizing the need for decentralized innovation and empowerment of local units.
""")

st.markdown("<div class='subheader'>Key Points</div>", unsafe_allow_html=True)
st.markdown("""
1. **Current AI Landscape**: Recent advancements in AI have led to dramatic reductions in software development costs, democratization of advanced technological capabilities, and increased accessibility of AI tools and platforms.
2. **Implications for UNDP**: These developments necessitate a shift towards rapid experimentation, local problem-solving, and grassroots innovation embedded within UNDP.
3. **Current Challenges**: UNDP's AI integration efforts are often delayed by administrative barriers, limited visibility, communication gaps, and a centralized approach to innovation.
4. **Strategic Recommendations**:
    - Streamline access to AI resources for all units and staff, enabling rapid prototyping and experimentation.
    - Foster a culture of peer-to-peer and cross-unit innovation and knowledge sharing across the organization.
    - Shift focus from centralized tool procurement to building AI capabilities among staff at all levels.
    - Implement flexible AI guidelines that balance responsible use with the need for innovation.
""")

st.markdown("<div class='header'>I. Introduction</div>", unsafe_allow_html=True)
st.markdown("""
Artificial Intelligence is reshaping how organizations operate, and UNDP is no exception. However, the current approach to AI integration within UNDP has not allowed it yet to meet its full potential. This think piece, written from the perspective of an office located outside of New York, proposes a new way forward.
""")

# Sample Glossary Term with Tooltip
ai_def = "Artificial Intelligence (AI) refers to the capability of machines to perform tasks that typically require human intelligence, such as understanding language, recognizing patterns, and making decisions."
st.markdown(f"""
Recent developments in {glossary_term('Artificial Intelligence (AI)', ai_def)} technology have significant implications for UNDP:
1. Software development costs have plummeted, making custom solutions more accessible.
2. Advanced AI capabilities are no longer confined to tech giants or specialized research labs.
3. User-friendly AI tools and platforms have proliferated, lowering barriers to entry.
""", unsafe_allow_html=True)

st.markdown("""
These changes open up new possibilities for UNDP, but to seize them, a rethinking of the current strategy is necessary. This document aims to:
1. Illustrate how the evolving AI landscape affects UNDP's work.
2. Identify roadblocks in the current approach to AI integration.
3. Propose practical steps to foster AI innovation across all levels of UNDP.
""")

st.markdown("""
This document is not a general commentary on society’s AI technology adoption, including the pace of AI developments, the possibilities of Artificial General Intelligence (AGI) or other wider socio-technological conversations. Instead, its primary purpose is to emphasize that amidst these broader developments, UNDP should be at the forefront of adoption. Adoption should go beyond our IT systems and tools, to every level of the organization, from general strategic planning to enhancing digital agility for all individuals.
""")

st.markdown("""
The Strategic Plan 2022-2025 identifies digitalisation and strategic innovation as critical enablers to maximize impact in country partners. AI adoption stands as one of the most prevailing areas in this context, necessitating UNDP’s immediate action. To support the AI adoption for country partners, UNDP itself must become a proactive adopter of these technologies. Thus, technological expertise should not be concentrated in a few dedicated units but be distributed and integrated at every level of the organization. 
""")

st.markdown("""
The need to become a digitally native UNDP is also expressed in the Digital Strategy 2022-2025. In the same way principles such as environmental sustainability and gender awareness are mainstreamed into every action, technology and innovation should also become an integral part of our work. Technology is not a silver bullet, but it is an invaluable tool in achieving the Sustainable Development Goals. Transformation within UNDP is necessary to build the expertise to act as a key development partner and share valuable insight to inform policy and programmes as countries undergo their own transformations.
""")

st.markdown("""
UNDP leadership has already expressed a strong intent to get ahead of the emergent challenges in the digital age. Against this backdrop, this piece aims to spark a conversation about how the organization can better leverage AI to enhance its impact. The goal is not just to advocate for broad adoption of new technologies, but to better cultivate an organization-wide culture of innovation that keeps UNDP at the forefront of development work in an increasingly AI-driven world.
""")

st.markdown("<div class='header'>II. The Current State of AI (September 2024)</div>", unsafe_allow_html=True)

# The rest of the think piece content goes here, with similar replacements for glossary terms.
# Due to the length of the content, only a portion is shown here as an example.

st.markdown("""
**Advanced AI Capabilities and Real-World Applications**

The field of {0} has seen remarkable advancements in recent years, with {0} models now demonstrating capabilities that rival or even surpass human performance in various domains. These capabilities are translating into significant real-world applications across multiple sectors. The recent release of OpenAI's o1 model marks another leap forward, showcasing unprecedented reasoning abilities that further blur the line between human and artificial intelligence.

**Language Understanding and Generation**

{0} models like {1} have achieved scores of 89.8 on the SuperGLUE benchmark, a series of challenging language understanding tasks designed to test the most sophisticated language AI, surpassing the human baseline. This proficiency extends to professional domains, with {0} systems passing medical licensing exams with scores of 82%, well above the 60% passing threshold for human doctors. These exams include multiple choice questions and clinical case studies, demonstrating the AI's ability to handle complex medical scenarios.
""".format(
    glossary_term('Artificial Intelligence (AI)', ai_def),
    glossary_term('GPT-4', "GPT-4 is the fourth generation of the Generative Pre-trained Transformer model developed by OpenAI.")
), unsafe_allow_html=True)

# Continue processing the think piece content similarly.

# =======================
# Sample Interactive Chart using Plotly
# =======================

st.markdown("<div class='header'>AI Cost and Token Usage Trends</div>", unsafe_allow_html=True)
years = np.arange(2021, 2031)
token_usage = np.array([1.5, 2, 3, 4, 5.5, 7.5, 10, 15, 21, 28.5])
cost_per_million = np.array([9, 8, 7, 6.5, 6, 5.5, 5, 4.5, 4, 3.5])

data = pd.DataFrame({
    'Year': years,
    'Token Usage (Millions per Day)': token_usage,
    'Cost per 1M Tokens (USD)': cost_per_million
})

# Create interactive chart using Plotly
fig = px.line(data, x='Year', y='Token Usage (Millions per Day)', title='AI Token Usage and Cost Trends (2021-2030)', markers=True, labels={
    'Token Usage (Millions per Day)': 'Token Usage (Millions per Day)',
    'Cost per 1M Tokens (USD)': 'Cost per 1M Tokens (USD)'
})

# Add secondary axis for Cost
fig.add_trace(
    px.line(data, x='Year', y='Cost per 1M Tokens (USD)', labels={'Cost per 1M Tokens (USD)': 'Cost per 1M Tokens (USD)'}).data[0]
)
fig.update_layout(
    yaxis2=dict(
        title='Cost per 1M Tokens (USD)',
        overlaying='y',
        side='right'
    ),
    legend=dict(x=0.1, y=1.1, orientation='h')
)

st.plotly_chart(fig, use_container_width=True)

# Continue adding the rest of the think piece content...
