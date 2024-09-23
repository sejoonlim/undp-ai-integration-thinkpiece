import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(page_title="UNDP AI Integration Think Piece", layout="wide")

# 제목
st.title("UNDP AI Integration Think Piece")

# 사이드바 메뉴
st.sidebar.title("섹션 선택")
sections = ["Executive Summary", "Current AI Landscape", "AI Recommendations", "Token Usage Projection"]
selection = st.sidebar.radio("보고 싶은 섹션을 선택하세요", sections)

# 데이터 (예시 데이터로 그래프 생성)
years = np.arange(1, 11)
token_usage = np.array([1.5, 2, 3, 4, 5.5, 7.5, 10, 15, 21, 28.5])
cost_per_million = np.array([9, 8, 7, 6.5, 6, 5.5, 5, 4.5, 4, 3.5])

# 각 섹션에 대한 콘텐츠 표시
if selection == "Executive Summary":
    st.header("Executive Summary")
    st.write("""
    This think piece critically examines the United Nations Development Programme's (UNDP) current approach to integrating 
    Artificial Intelligence (AI) into its operations. It argues for a shift towards decentralized innovation and 
    empowerment of local units.
    
    Key Points:
    1. AI advancements have reduced software development costs.
    2. UNDP must shift to local problem-solving and innovation.
    3. Bureaucratic challenges hinder rapid AI integration.
    4. Recommendations include decentralizing AI resources and fostering cross-unit collaboration.
    """)

elif selection == "Current AI Landscape":
    st.header("Current AI Landscape")
    st.write("""
    AI advancements are revolutionizing various sectors. The recent developments in models like GPT-4 and o1 have set 
    new benchmarks in language understanding, reasoning, and problem-solving. UNDP can leverage these tools to enhance 
    operational efficiency and empower local units.
    
    - GPT-4 achieved a score of 89.8 on the SuperGLUE benchmark.
    - AI tools are enabling rapid software development.
    - Edge AI is providing faster data processing closer to data sources.
    """)

elif selection == "AI Recommendations":
    st.header("Strategic Recommendations")
    st.write("""
    To fully harness the potential of AI, UNDP should focus on the following key areas:
    
    1. Establish a centralized AI resource hub for easier access to knowledge and tools.
    2. Improve transparency in resource allocation to enhance innovation.
    3. Empower local units with the tools and resources for rapid AI prototyping.
    4. Develop flexible guidelines that balance responsible AI use and innovation.
    """)

elif selection == "Token Usage Projection":
    st.header("Token Usage and Cost Projection Over 10 Years")

    # 그래프 그리기
    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.set_xlabel('Year')
    ax1.set_ylabel('Token Usage (Millions per Day)', color='tab:red')
    ax1.plot(years, token_usage, color='tab:red', label='Token Usage')
    ax1.tick_params(axis='y', labelcolor='tab:red')

    ax2 = ax1.twinx()  # 두 번째 y축
    ax2.set_ylabel('Cost per 1M Tokens (USD)', color='tab:blue')
    ax2.plot(years, cost_per_million, color='tab:blue', label='Cost per 1M Tokens')
    ax2.tick_params(axis='y', labelcolor='tab:blue')

    fig.tight_layout()  # 그래프 간 여백 조정
    st.pyplot(fig)
    
    # 추가 설명
    st.write("""
    This graph shows the projected increase in token usage and the corresponding decrease in cost per 1 million tokens over 
    the next 10 years. As AI technologies become more prevalent and efficient, token usage is expected to rise, while the 
    cost of processing decreases.
    """)

# 푸터
st.sidebar.write("Powered by Streamlit")
