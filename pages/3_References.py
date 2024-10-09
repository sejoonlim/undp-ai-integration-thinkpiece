# pages/References.py
import streamlit as st

st.title("References")

references = [
    "Alford, A. (2022, September 13). MIT researchers develop AI model to solve university-level mathematics problems. InfoQ. https://www.infoq.com/news/2022/09/mit-math-solving-ai/",
    "Betker, J., Goh, G., Jing, L., Brooks, T., Wang, J., Li, L., Ouyang, L., Zhuang, J., Lee, J., Guo, Y., Manassra, W., Dhariwal, P., Chu, C., Jiao, Y., & Ramesh, A. (n.d.). Improving image generation with better captions. OpenAI. https://openai.com/research/dall-e-3",
    "Chen, Z., Chen, H., Imani, M., Chen, R., & Imani, F. (2024). Vision language model for interpretable and fine-grained detection of safety compliance in diverse workplaces. arXiv. https://arxiv.org/abs/2408.07146",
    "Deniz Karaci, B., Gnanasambandan, C., Harrysson, M., Hussin, A., & Srivastava, S. (2023, June 27). Unleashing developer productivity with generative AI. McKinsey Digital. https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/unleashing-developer-productivity-with-generative-ai",
    "Dhingra, S., Singh, M., Vaisakh, S. B., Malviya, N., & Gill, S. S. (2023). Mind meets machine: Unravelling GPT-4's cognitive psychology. BenchCouncil Transactions on Benchmarks, Standards and Evaluations, 3(3), 1-5. https://doi.org/10.1016/j.tbench.2023.100139",
    "Drori, I., Zhang, S., Shuttleworth, R., Tang, L., Lu, A., Ke, E., Liu, K., Chen, L., Tran, S., Cheng, N., Wang, R., Singh, N., Patti, T. L., Lynch, J., Shporer, A., Verma, N., Wu, E., & Strang, G. (2022). A neural network solves, explains, and generates university math problems by program synthesis and few-shot learning at human level. Proceedings of the National Academy of Sciences, 119(32). https://doi.org/10.1073/pnas.2123433119",
    "Guthrie, S. (2023, March 7). Morgan Stanley TMT Conference. Microsoft. https://www.microsoft.com/en-us/Investor/events/FY-2023/Morgan-Stanley-TMT-Conference",
    "Haleem, A., Javaid, M., Qadri, A. M., Singh, R. P., & Suman, R. (2022). Artificial intelligence (AI) applications for marketing: A literature-based study. International Journal of Intelligent Networks, 3, 119-132. https://doi.org/10.1016/j.ijin.2022.08.005",
    "Katz, D. M., Bommarito, M. J., Gao, S., & Arredondo, P. D. (2023). GPT-4 passes the bar exam. Philosophical Transactions of the Royal Society A, 382, 1-35. http://dx.doi.org/10.2139/ssrn.4389233",
    "Kung, T. H., Cheatham, M., Medenilla, A., Sillos, C., De Leon, L., Elepaño, C., Madriaga, M., Aggabao, R., Diaz-Candido, G., Maningo, J., & Tseng, V. (2023). Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models. PLOS Digital Health, 2(2), 1-12. https://doi.org/10.1371/journal.pdig.0000198",
    "Liu, X., Jing, X., Zhu, Q., Du, W., & Wang, X. (2023). Automatic construction hazard identification integrating on-site scene graphs with information extraction in outfield test. Buildings, 13(2), 377. https://doi.org/10.3390/buildings13020377",
    "Mann, C. (2024, March 28). Long-term Token Usage and Costs Trends Insights from Martian's Founder. LinkedIn. https://www.linkedin.com/pulse/long-term-token-usage-costs-trends-insights-from-martians-chris-mann-sv1te",
    "Matias, Y., & Corrado, G. (2023, March 14). Our latest health AI research updates. Google Blog. https://blog.google/technology/health/ai-llm-medpalm-research-thecheckup/",
    "OpenAI. (2024, July 18). GPT-4o mini: Advancing cost-efficient intelligence. OpenAI. https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/",
    "OpenAI. (2024, September 12). Learning to reason with LLMs. OpenAI. https://openai.com/index/learning-to-reason-with-llms/",
    "Prior, S. (2024, August 2). How GitHub Copilot boosted developer productivity. UC San Diego. https://blink.ucsd.edu/technology/about/news/posts/2024-08-01-github-copilot.html"
]

for ref in references:
    st.markdown(f"- {ref}")
