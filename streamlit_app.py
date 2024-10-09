import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px  # Plotly 임포트
from utils import glossary_term

# =======================
# Set Page Configuration
# =======================
st.set_page_config(
    page_title="UNDP AI Integration Think Piece",  # 브라우저 탭 타이틀
    page_icon=":globe_with_meridians:", # 이모지 또는 이미지 URL
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================= 
# CSS for Tooltip Styling
# =======================

# UNDP 색상 코드
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

# 커스텀 CSS
custom_css = """
<style>
    @font-face {
        font-family: 'SohneBreit';
        src: url('path/to/SohneBreit.woff2') format('woff2'),
             url('path/to/SohneBreit.woff') format('woff');
    }

    @font-face {
        font-family: 'ProximaNova';
        src: url('path/to/ProximaNova-Regular.woff2') format('woff2'),
             url('path/to/ProximaNova-Regular.woff') format('woff');
    }
    
    .title {
        font-family: 'SohneBreit', sans-serif;
        font-size: 2.5em;
        color: #0a97d9;
        border-bottom: 2px solid #0a97d9;
        padding-bottom: 0.25em;
    }
    
    .header {
        font-family: 'ProximaNova', sans-serif;
        font-size: 2em;
        color: #0a97d9;
        border-bottom: 1px solid #e0e0e0;
        padding-bottom: 0.15em;
    }
    
    .subheader {
        font-family: 'ProximaNova', sans-serif;
        font-size: 1.5em;
        color: #333333;
    }

    body {
        font-family: 'ProximaNova', sans-serif;
    }

    /* Tooltip container */
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: pointer;
        border-bottom: 1px dotted black; /* If you want dots under the hoverable text */
    }

    /* Tooltip text */
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 300px;
        background-color: #555;
        color: #fff;
        text-align: left;
        border-radius: 6px;
        padding: 10px;
        position: absolute;
        z-index: 1;
        bottom: 125%; /* Position the tooltip above the text */
        left: 50%;
        margin-left: -150px;
        opacity: 0;
        transition: opacity 0.3s;
    }

    /* Tooltip arrow */
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

    /* Show the tooltip text when you mouse over the tooltip container */
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
</style>
"""

# Inject CSS
st.markdown(custom_css, unsafe_allow_html=True)

# =======================
# Page Content
# =======================

st.title("UNDP AI Integration Think Piece")
st.markdown("**8 October 2024**")

st.header("Executive Summary")
st.markdown("""
This think piece critically examines UNDP’s current approach to integrating {glossary_term('Artificial Intelligence (AI)', 'Artificial Intelligence (AI) refers to the capability of machines to perform tasks that typically require human intelligence, such as understanding language, recognizing patterns, and making decisions.')} into its operations, viewed from the perspective of an office located outside of New York. This paper proposes a fundamental shift in how UNDP engages with AI technologies, emphasizing the need for decentralized innovation and empowerment of local units.
""", unsafe_allow_html=True)

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
{glossary_term('Artificial Intelligence (AI)', 'Artificial Intelligence (AI) refers to the capability of machines to perform tasks that typically require human intelligence, such as understanding language, recognizing patterns, and making decisions.')} is reshaping how organizations operate, and UNDP is no exception. However, the current approach to AI integration within UNDP has not allowed it yet to meet its full potential. This think piece, written from the perspective of an office located outside of New York, proposes a new way forward.
""", unsafe_allow_html=True)

ai_def = "Artificial Intelligence (AI) refers to the capability of machines to perform tasks that typically require human intelligence, such as understanding language, recognizing patterns, and making decisions."
st.markdown(f"""
Recent developments in {glossary_term('AI', ai_def)} technology have significant implications for UNDP:
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
This document is not a general commentary on society’s AI technology adoption, including the pace of AI developments, the possibilities of {glossary_term('Artificial General Intelligence (AGI)', 'Artificial General Intelligence (AGI) refers to a machine with the ability to understand, learn, and apply knowledge in a general, flexible manner similar to a human being.')} or other wider socio-technological conversations. Instead, its primary purpose is to emphasize that amidst these broader developments, UNDP should be at the forefront of adoption. Adoption should go beyond our IT systems and tools, to every level of the organization, from general strategic planning to enhancing digital agility for all individuals.
""", unsafe_allow_html=True)

st.markdown("""
The Strategic Plan 2022-2025 identifies digitalisation and strategic innovation as critical enablers to maximize impact in country partners. AI adoption stands as one of the most prevailing areas in this context, necessitating UNDP’s immediate action. To support the AI adoption for country partners, UNDP itself must become a proactive adopter of these technologies. Thus, technological expertise should not be concentrated in a few dedicated units but be distributed and integrated at every level of the organization. 
The need to become a digitally native UNDP is also expressed in the Digital Strategy 2022-2025. In the same way principles such as environmental sustainability and gender awareness are mainstreamed into every action, technology and innovation should also become an integral part of our work. Technology is not a silver bullet, but it is an invaluable tool in achieving the Sustainable Development Goals. Transformation within UNDP is necessary to build the expertise to act as a key development partner and share valuable insight to inform policy and programmes as countries undergo their own transformations.
UNDP leadership has already expressed a strong intent to get ahead of the emergent challenges in the digital age. Against this backdrop, this piece aims to spark a conversation about how the organization can better leverage AI to enhance its impact. The goal is not just to advocate for broad adoption of new technologies, but to better cultivate an organization-wide culture of innovation that keeps UNDP at the forefront of development work in an increasingly AI-driven world.
""")

st.header("II. The Current State of AI (September 2024)")
st.subheader("Advanced AI Capabilities and Real-World Applications")
st.markdown("""
The field of {glossary_term('Artificial Intelligence (AI)', 'Artificial Intelligence (AI) refers to the capability of machines to perform tasks that typically require human intelligence, such as understanding language, recognizing patterns, and making decisions.')} has seen remarkable advancements in recent years, with AI models now demonstrating capabilities that rival or even surpass human performance in various domains. These capabilities are translating into significant real-world applications across multiple sectors. The recent release of OpenAI's o1 model, marks another leap forward, showcasing unprecedented reasoning abilities that further blur the line between human and artificial intelligence.
""", unsafe_allow_html=True)

st.subheader("Language Understanding and Generation")
st.markdown("""
AI models like {glossary_term('GPT-4', 'GPT-4 is the fourth generation of the Generative Pre-trained Transformer model developed by OpenAI.')} have achieved scores of 89.8 on the {glossary_term('SuperGLUE Benchmark', 'The SuperGLUE benchmark is a set of challenging tasks used to evaluate the performance of natural language understanding models.')} , a series of challenging language understanding tasks designed to test the most sophisticated language AI, surpassing the human baseline. This proficiency extends to professional domains, with AI systems passing medical licensing exams with scores of 82%, well above the 60% passing threshold for human doctors. These exams include multiple choice questions and clinical case studies, demonstrating the AI's ability to handle complex medical scenarios.
In content creation, AI can generate first drafts of articles, reports, or marketing copy that require only minor edits 70% of the time, potentially doubling the productivity of writers and marketers. The legal sector has seen AI models draft legal documents that pass expert review 94% of the time, potentially saving hundreds of billable hours.
""", unsafe_allow_html=True)

st.subheader("Complex Reasoning and Problem Solving")
st.markdown("""
AI models have demonstrated remarkable complex reasoning abilities, with OpenAI's o1 setting new benchmarks. In competitive programming, o1 ranks in the 89th percentile, showcasing its ability to solve intricate algorithmic problems. It has also placed among the top 500 students in a qualifier for the USA Math Olympiad, demonstrating advanced mathematical reasoning capabilities.
In a recent study by MIT, AI models automatically solved 81% of randomly selected university-level mathematics problems. The o1 model has pushed this further, exceeding human PhD-level accuracy on benchmarks covering physics, biology, and chemistry problems ({glossary_term('GPQA', 'General Purpose Question Answering (GPQA) refers to AI systems designed to answer a wide range of questions across different domains.')} ). In the legal field, {glossary_term('GPT-4', 'GPT-4 is the fourth generation of the Generative Pre-trained Transformer model developed by OpenAI.')} scored in the 90th percentile on the {glossary_term('Uniform Bar Exam', 'The Uniform Bar Exam is a standardized test for admission to the bar in the United States.')} , showcasing law school graduate-level reasoning.
AI is increasingly bridging the gap between specialized knowledge and practical application, enabling individuals to tackle complex technical tasks that were once the domain of experts. One notable example is a student who built a DIY nuclear fusion reactor at home with AI assistance ({glossary_term('DIY nuclear fusion reactor at home', 'A do-it-yourself project where an individual builds a nuclear fusion reactor with the help of AI tools.')} ). While this case is unusual, it illustrates AI's potential to make highly complex tasks more accessible.
More commonly, AI is helping individuals and small teams develop software of medium complexity, such as custom data analysis tools, mobile apps, or {glossary_term('IoT', 'The Internet of Things (IoT) refers to a network of physical devices connected to the internet, allowing them to collect and share data.')} device controllers. In the realm of hardware, AI-assisted design and simulation tools are enabling enthusiasts to create sophisticated electronics projects, 3D-printed prototypes, and even small-scale robotics.
These examples demonstrate how AI is democratizing access to advanced technical knowledge and capabilities, allowing non-experts to engage with complex fields in unprecedented ways.
""", unsafe_allow_html=True)

st.subheader("Code Generation and Analysis")
st.markdown("""
Code generation and analysis capabilities have made significant strides. {glossary_term('GitHub Copilot', 'GitHub Copilot is an AI-powered tool that assists software developers by suggesting code snippets and functions as they write.')} can generate up to 40% of new code in supported languages. In controlled studies, developers using AI coding assistants completed tasks 55% faster than those without AI help, marking a substantial increase in productivity. The impact varies by language, with productivity increases of 55% for Java and 61% for Python.
The o1 model has further advanced this field, achieving an {glossary_term('Elo Rating', 'The Elo rating system is a method for calculating the relative skill levels of players in two-player games such as chess.')} of 1807 in simulated Codeforces competitions, outperforming 93% of human competitors. This demonstrates AI's growing ability to not just assist in coding tasks, but to independently solve complex programming challenges.
""", unsafe_allow_html=True)

st.subheader("Multimodal Understanding")
st.markdown("""
Visual language models like {glossary_term('GPT-4V', 'GPT-4V refers to the visual capabilities of GPT-4, enabling it to analyze and understand images.')} can analyze images and provide detailed descriptions, answer questions about image content, and even identify potential safety hazards or OSHA violations in workplace photos with over 90% accuracy. These models can generate image captions that are indistinguishable from human-written ones in 85% of cases, as judged by human evaluators. Notably, these models can generate captions in multiple languages, further expanding their utility.
""", unsafe_allow_html=True)

st.subheader("Adaptive Learning")
st.markdown("""
Recent AI models, such as o1-preview and o1-mini, show impressive abilities to adapt to new tasks quickly. For example, when tested on complex questions about biological risks, o1-preview performed remarkably well, achieving a 72% success rate compared to expert human responses. This means it accurately addressed critical safety questions more often than not, demonstrating its capability to learn and apply information effectively.
In another example, o1-mini was tested in a simulated scenario where it needed to persuade a user to donate money. It successfully convinced the user to donate about 25.8% of the time. This indicates that the model can navigate tricky social interactions and adapt its approach based on the situation, similar to how a human might adapt their persuasion techniques in conversation.
These examples highlight not just the models' ability to learn from a few examples but also their potential to quickly adjust to specific challenges, making them valuable tools in various real-world applications.
""", unsafe_allow_html=True)

st.subheader("Customer Service Applications")
st.markdown("""
Customer service has experienced a transformation, with AI chatbots resolving approximately 70-80% of routine inquiries without human intervention, leading to a reported 30-50% reduction in operational costs and significantly shorter wait times. These chatbots utilize natural language processing and machine learning algorithms to understand and respond to customer queries in a human-like manner.
""", unsafe_allow_html=True)

st.subheader("Democratization of AI: Open-Source Models and Affordable Computing")
st.markdown("""
While closed-source models like {glossary_term('GPT-4', 'GPT-4 is the fourth generation of the Generative Pre-trained Transformer model developed by OpenAI.')} and Claude 3.5 represent the cutting edge of AI capabilities, open-source alternatives and affordable computing options are rapidly democratizing access to AI technologies.
""", unsafe_allow_html=True)

st.subheader("Open-Source Models")
st.markdown("""
Open-source models are closing the gap with proprietary alternatives. Meta's {glossary_term('LLaMA 3', 'LLaMA 3 is the third generation of the LLaMA series developed by Meta, designed for efficiency and high performance in language tasks.')} , released in July 2024, includes models with 8B, 70B, and 405B parameters, making it the largest in the series. It outperforms many proprietary models on several benchmarks while being freely available for research and commercial use. These models are trained on diverse datasets including web pages, books, and scientific papers, enabling tasks like advanced language translation, content generation, and complex reasoning.
""", unsafe_allow_html=True)

st.subheader("Affordable Hardware")
st.markdown("""
The accessibility of AI computing power has increased dramatically. Advanced models can now run on more affordable hardware. Some examples:
- {glossary_term('Raspberry Pi 5', 'Raspberry Pi 5 is a low-cost, high-performance single-board computer suitable for various AI applications.')} : Released in October 2023, it offers substantial improvements in speed and performance at a low cost. The 2GB variant is priced at just $50, while the 4GB and 8GB models cost $60 and $80 respectively. This makes powerful AI-capable hardware accessible to a wide range of users and projects, allowing for tasks such as real-time image recognition, natural language processing, and even running small-scale language models locally.
- {glossary_term('Edge AI deployments', 'Edge AI deployments involve running AI algorithms on local devices rather than centralized servers, enabling faster processing and real-time decision-making.')} : The Raspberry Pi AI Kit, which includes a Hailo AI module containing a {glossary_term('NPU', 'A Neural Processing Unit (NPU) is specialized hardware designed to accelerate the processing of machine learning tasks.')}, can boost AI capabilities to 13 {glossary_term('TOPS', 'Tera Operations Per Second (TOPS) is a measure of a computer\'s performance, particularly in AI and machine learning.'))} with low power consumption. This enables complex computer vision tasks, real-time object detection, and efficient natural language processing at the edge. Google's {glossary_term('Coral USB Accelerator', 'Coral USB Accelerator is a device that provides high-performance machine learning inference on edge devices.')}, priced at around $60, when paired with a Raspberry Pi, can run complex object detection models in real-time, further expanding the possibilities for IoT projects such as smart home devices, autonomous robots, and industrial monitoring systems.
- {glossary_term('TinyML', 'TinyML refers to machine learning technologies and applications that are capable of performing on-device analytics at extremely low power.')}: Frameworks continue to allow AI models to run on microcontrollers, with ongoing improvements in efficiency and accuracy. For example, the {glossary_term('MAX78002 AI microcontroller', 'MAX78002 is a microcontroller designed for ultra-low-power AI applications.')}, from Analog Devices, enables battery-powered applications to execute AI inferences while expending only millijoules of energy. This makes it possible to implement AI in even the most power-constrained edge devices, enabling applications like smart sensors, wearable health monitors, and ultra-low-power IoT devices capable of local decision-making and data processing.
""", unsafe_allow_html=True)

st.subheader("Cost-Effective AI Services")
st.markdown("""
The cost of using advanced AI tools has decreased dramatically. {glossary_term('GPT-4o mini', 'GPT-4o mini is a cost-efficient variant of the GPT-4 model, designed for large-scale text processing at reduced costs.')}, available through APIs, processes text at a rate of 15 cents per million input tokens and 60 cents per million output tokens. This translates to processing 2,500 pages of text for 60 cents, making large-scale AI applications financially viable for organizations with limited budgets.
""", unsafe_allow_html=True)

st.subheader("Diversity in AI Models and Approaches")
st.markdown("""
While large language models ({glossary_term('LLMs', 'Large Language Models (LLMs) are advanced AI models trained on extensive text data to understand and generate human-like text.')}) like GPT-4 and Claude 3.5 have captured significant attention, the AI landscape is increasingly diverse, offering a range of solutions suited to different tasks and contexts:
1. **Large Language Models (LLMs)**: These models excel at complex, general-purpose tasks requiring broad knowledge and reasoning capabilities. They power many of the advanced applications described earlier, from passing medical licensing exams to solving graduate-level math problems.
2. **Small Language Models (SLMs)**: Often more efficient and cost-effective for specific, narrowly defined tasks, {glossary_term('SLMs', 'Small Language Models (SLMs) are compact AI models designed for specific tasks, often requiring fewer resources than LLMs.')} are gaining traction in resource-constrained environments. They can run on edge devices or with minimal cloud resources, making them suitable for localized applications.
3. **Specialized AI Models**: Designed for particular domains (e.g., image recognition, speech processing), these models can outperform general models in their areas of expertise. For instance, specialized computer vision models can achieve high accuracy in specific industrial or medical imaging tasks.
4. **Hybrid Approaches**: An emerging trend involves combining different model types. For example, an LLM might orchestrate multiple smaller, specialized models, leveraging the strengths of each to create more robust and efficient systems.
5. **Open Source vs. Proprietary Models**: The AI ecosystem now offers a choice between open-source solutions like Meta's {glossary_term('LLaMA 3', 'LLaMA 3 is the third generation of the LLaMA series developed by Meta, designed for efficiency and high performance in language tasks.')}} and proprietary models.
""", unsafe_allow_html=True)

st.markdown("""
The optimal AI "infrastructure" for a given project may thus involve:
1. **Single Model Approaches**: Using either a large, general-purpose model or a smaller, specialized model, depending on the task complexity and resource constraints.
2. **Multi-Model Systems**: Combining multiple models, which could include large models coordinating smaller ones, ensembles of models, or multi-modal systems integrating language, vision, and/or audio capabilities.
3. **Hybrid AI Architectures**: Integrating AI models with other technologies such as retrieval systems ({glossary_term('RAG', 'Retrieval-Augmented Generation (RAG) is a model architecture that combines retrieving information from a database with generating new content.')}}, symbolic AI, or human-in-the-loop approaches.
4. **Distributed AI Solutions**: Implementing federated learning, {glossary_term('Edge AI', 'Edge AI refers to the deployment of AI algorithms on local devices rather than in a centralized cloud.')}, cloud-based services, or hybrid edge-cloud architectures to balance computational needs with data locality and privacy concerns.
5. **Customized AI Development**: Adapting pre-trained models through transfer learning, fine-tuning on domain-specific data, or developing custom models from scratch.
""", unsafe_allow_html=True)

st.markdown("""
This diversity in AI solutions allows for more tailored approaches to specific problems and contexts, a crucial consideration for organizations operating in varied environments.
""")

st.subheader("Implications for UNDP")
st.markdown("""
The advancements in AI capabilities, increased accessibility, and diversity of AI solutions discussed above have significant implications for UNDP's operations and strategies:

**Reduction in Software Development Costs**  
Some of the most well-used developer tools such as {glossary_term('GitHub', 'GitHub is a platform for version control and collaboration, allowing developers to work together on projects.')}} and Replit now host AI features that meaningfully reduce development time and expenses. For UNDP, this could mean faster development of tailored applications and reduced reliance on external contractors.

**Democratization of Advanced Technological Capabilities**  
AI models now serve as accessible repositories of specialized knowledge across various fields. They provide step-by-step guidance for complex tasks, enabling individuals without extensive training to undertake sophisticated projects. The DIY nuclear fusion reactor example, while extreme, illustrates how AI can bridge the gap between specialized knowledge and practical application. For UNDP, this democratization could empower local teams to catalyze their existing local knowledge and develop context-specific solutions without extensive external support, potentially accelerating project implementation and increasing local ownership.

**Increased Accessibility of AI Tools and Platforms**  
The reduced costs and increased accessibility of AI tools open new possibilities for UNDP to implement sophisticated technological solutions across its programs, even in resource-constrained environments. 
These advancements enable UNDP to foster rapid experimentation, local problem-solving, and grassroots innovation across its global network. By leveraging these technologies, UNDP can enhance its impact and efficiency in addressing complex development challenges worldwide. The ability to perform advanced language translation, content generation, and complex reasoning using open-source models could significantly boost UNDP's capacity to operate effectively across diverse linguistic and cultural contexts.

**Tailored Solutions**  
The range of AI models allows UNDP to select or develop solutions that are precisely tailored to specific project needs and resource constraints.

**Cost-Effective Innovation**  
Smaller, specialized models and open-source alternatives can enable innovation even in resource-constrained environments, including places with low technology and internet access, aligning with UNDP's global reach and diverse operational contexts.

**Scalability and Flexibility**  
The ability to combine different model types (e.g., using an LLM to orchestrate smaller, specialized models) offers scalable and flexible solutions that can adapt to varying project requirements and local conditions.

**Capacity Building**  
Engaging with a diverse AI ecosystem can foster the development of AI expertise within UNDP, enhancing the organization's ability to leverage these technologies effectively across its global operations. As stated earlier, AI knowledge and resources should not be confined to specific units or individuals. Access to learning materials and tools should be made available at every level of the organization. Innovation can emerge from any unit, and capacity building is not an end in itself but a crucial step to unlock potential innovation wherever it may arise.
""", unsafe_allow_html=True)

st.header("III. Potential Applications for UNDP")
st.markdown("""
Recent advancements in AI technology present opportunities for UNDP to enhance its operations and impact. This section explores concrete examples of how AI can be leveraged across various aspects of UNDP's work, from local problem-solving to organization-wide efficiency gains. 
""")
