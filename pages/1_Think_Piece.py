# Home.py
import streamlit as st

# CSS for Tooltip Styling
tooltip_css = """
<style>
.tooltip {
    position: relative;
    display: inline-block;
    border-bottom: 1px dotted #000;
}

.tooltip .tooltiptext {
    visibility: hidden;
    width: 220px;
    background-color: #555;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    padding: 5px 0;
    position: absolute;
    z-index: 1;
    bottom: 125%; /* Position above the text */
    left: 50%;
    margin-left: -110px;
    opacity: 0;
    transition: opacity 0.3s;
}

.tooltip .tooltiptext::after {
    content: "";
    position: absolute;
    top: 100%; /* At the bottom of the tooltip */
    left: 50%;
    margin-left: -5px;
    border-width: 5px;
    border-style: solid;
    border-color: #555 transparent transparent transparent;
}

.tooltip:hover .tooltiptext {
    visibility: visible;
    opacity: 1;
}
</style>
"""

# Inject CSS
st.markdown(tooltip_css, unsafe_allow_html=True)

# Page Content
st.title("UNDP AI Integration Think Piece")
st.markdown("**8 October 2024**")

st.header("Executive Summary")
st.markdown("""
This think piece critically examines UNDP’s current approach to integrating Artificial Intelligence (AI) into its operations, viewed from the perspective of an office located outside of New York. This paper proposes a fundamental shift in how UNDP engages with AI technologies, emphasizing the need for decentralized innovation and empowerment of local units.
""")

st.subheader("Key Points")
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

st.header("I. Introduction")
st.markdown("""
Artificial Intelligence is reshaping how organizations operate, and UNDP is no exception. However, the current approach to AI integration within UNDP has not allowed it yet to meet its full potential. This think piece, written from the perspective of an office located outside of New York, proposes a new way forward.
""")

# Sample Glossary Term with Tooltip
ai_def = "Artificial Intelligence (AI) refers to the capability of machines to perform tasks that typically require human intelligence, such as understanding language, recognizing patterns, and making decisions."
st.markdown(f"""
Recent developments in <span class="tooltip">Artificial Intelligence (AI)
    <span class="tooltiptext">{ai_def}</span>
</span> technology have significant implications for UNDP:
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

# Sample Chart
st.header("AI Cost and Token Usage Trends")
years = np.arange(2021, 2031)
token_usage = np.array([1.5, 2, 3, 4, 5.5, 7.5, 10, 15, 21, 28.5])
cost_per_million = np.array([9, 8, 7, 6.5, 6, 5.5, 5, 4.5, 4, 3.5])

data = pd.DataFrame({
    'Year': years,
    'Token Usage (Millions per Day)': token_usage,
    'Cost per 1M Tokens (USD)': cost_per_million
})

fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('Year')
ax1.set_ylabel('Token Usage (Millions per Day)', color=color)
ax1.plot(data['Year'], data['Token Usage (Millions per Day)'], marker='o', color=color, label='Token Usage')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color = 'tab:red'
ax2.set_ylabel('Cost per 1M Tokens (USD)', color=color)
ax2.plot(data['Year'], data['Cost per 1M Tokens (USD)'], marker='x', color=color, label='Cost per 1M Tokens')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
st.pyplot(fig)
