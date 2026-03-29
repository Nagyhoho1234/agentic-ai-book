# Chapter 6: AI Agents in Offensive Security

**Authors:** Jerry Huang, Ken Huang, and Chris Hughes

## Comprehensive Summary

This chapter examines the dual-edged nature of AI agents in offensive security -- how they are used both to proactively uncover vulnerabilities (defensive red teaming) and how they can be exploited by malicious actors. The chapter covers five major areas: red team operations, social engineering, software supply chain attacks, bug bounty programs, and vulnerability/zero-day discovery, with extensive code examples.

### 6.1 AI Agent in Red Team Operations

Red teaming emulates adversary tactics to holistically challenge an organization's defenses. Figure 6.1 provides a mind map of AI agents in offensive security (Red Teaming, Social Engineering, Supply Chain Attacks, Vulnerability Discovery, Code Examples). Figure 6.2 shows the AI-driven red teaming process flow.

**Four major red teaming frameworks:**

1. **Meta's GOAT (Generative Offensive Agent Tester):** Automated system using a general-purpose "attacker" agent for multi-turn adversarial conversations with target models. Dynamically selects adversarial prompting techniques (output manipulation, safe response distractors, fictional scenarios). Achieved 97% attack success rate against Llama 3.1 and 88% against GPT-4-Turbo on JailbreakBench.

2. **Google's AART (AI-Assisted Red Teaming):** Creates adversarial datasets using customizable "recipes" for context-aware testing. Multi-agent system with attack agents and evaluation agents. Integrated with Google's Secure AI Framework (SAIF) for continuous testing.

3. **OpenAI's Red Teaming Using AI Agents:** Two-step process: (1) generate diverse attacker goals via few-shot generation and reward generation from data, (2) train attacker agent using reinforcement learning with multi-objective rewards (attack success, few-shot similarity, diversity, length penalty). Uses rule-based rewards (RBRs) as yes/no questions, cosine similarity for few-shot similarity, sigmoid normalization, and discount factor gamma=0.

4. **Microsoft's PyRIT (Python Risk Identification Tool):** Open-source agentic framework with five components: targets, datasets, scoring engine, attack strategies, and memory. Supports both single-turn and multi-turn adversarial strategies. Integrates with Azure OpenAI Service, Hugging Face, Azure ML.

5. **Burpference for Dreadnode:** Extension of Burp Suite integrating LLM capabilities for offensive web application testing. Captures HTTP requests, forwards to LLM endpoints for analysis. Can host models locally.

### 6.2 AI Agent-Driven Social Engineering

Social engineering exploits human psychology; AI makes these attacks more personalized, automated, and difficult to detect. Figure 6.3 shows the workflow: Reconnaissance -> Analyze Target Data -> Craft Personalized Attack -> Send Attack -> Interaction -> Capture Information -> Adjust Tactics.

1. **Deepfake Video Calls:** Arup (Hong Kong) lost HK$200M ($25.6M) to a deepfake video conference where all participants except the victim were AI-generated. First known instance of deepfakes for an entire group meeting.

2. **AI-Powered Phishing Emails:** Nearly indistinguishable from genuine emails. Abnormal Security documented cases impersonating insurance representatives and Netflix customer service with polished language lacking typical phishing indicators.

3. **Voice Cloning for Vishing:** Only 3 seconds of audio needed. In 2021, attackers cloned a company director's voice to steal $35M via phone call. MGM Resorts 2023 attack (~$100M loss) potentially initiated through AI voice impersonation.

**Countermeasures:** Education and training, AI-powered email filters, MFA (with awareness of MitM limitations), verification procedures via secondary channels, regular security audits.

### 6.3 AI Agent in Software Supply Chain Attacks

1. **False Code Package Generation:** AI creates convincing malicious packages mimicking legitimate libraries, using obfuscation and polymorphic code.
2. **False API Endpoint Creation:** MitM attacks via DNS/IP spoofing to redirect to malicious endpoints.
3. **CI/CD Pipeline Attacks:** Automated injection of malicious code into build processes.
4. **Runtime Environment Attacks:** Code injection, buffer overflows, self-healing malware.
5. **AI-Driven Software Composition Analysis:** Vulnerability discovery, exploit generation, zero-day prediction, attack surface expansion.
6. **Intelligent Trojan Injection:** BlankBot (July 2024) -- Android banking trojan using AI agent technology, custom injection attacks, keylogging, screen recording, largely undetected by antivirus.

**Defensive Countermeasures:** Anomaly detection (ML), graph analysis (GNNs), behavioral analysis, predictive patching.

### 6.4 AI Agent Used for Bug Bounty

**BountyAgent:** Designed AI agent with six capabilities: scope analysis (NLP), vulnerability pattern recognition, exploit crafting assistance, report generation, learning from historical data, cross-program insights. Full Python code example provided with data structures, initialization, scope analysis, pattern recognition, report generation, learning, and cross-program analysis.

### 6.5 AI Agent in Vulnerability Discovery and Zero-Day Discovery

1. **Google's Big Sleep Project:** Evolution of Project Naptime. Found stack buffer underflow vulnerability in SQLite database engine (October 2024). Analyzes code commits and simulates human-like vulnerability assessment. Can identify flaws that traditional fuzzing might miss.

2. **DeepFuzz Agent Design:** Comprehensive code example with seven capabilities: intelligent input generation (VAE neural network), adaptive fuzzing strategies, coverage-guided optimization, symbolic execution integration (Angr framework + Z3 solver), multidimensional analysis, automated exploit generation, continuous learning. Full multi-file Python implementation provided (utils.py, input_generator.py, symbolic_executor.py, coverage_tracker.py, vulnerability_detector.py, exploit_generator.py, fuzzing_worker.py using Ray for distributed computing, main DeepFuzz coordinator class).

### 6.6 Architectural Considerations for AI-Enhanced Offensive Platforms

Seven design considerations:
1. Distributed AI Processing for balancing load across attack infrastructure.
2. Secure Enclaves for protecting AI models and training data.
3. Modular AI Integration for rapid capability additions.
4. Edge AI for faster decision-making without central server dependency.
5. Federated Learning for improving models without centralizing sensitive data.
6. AI-Driven Resilience with self-healing and adaptation mechanisms.
7. Quantum-Resistant Designs for future-proofing against quantum threats.

## Key Definitions and Terminology

- **Red Teaming:** Advanced offensive security exercise emulating adversary tactics to challenge organizational defenses.
- **GOAT (Generative Offensive Agent Tester):** Meta's automated system for multi-turn adversarial testing of LLMs.
- **PyRIT (Python Risk Identification Tool):** Microsoft's open-source agentic framework for red teaming generative AI.
- **Vishing:** Voice phishing using AI voice cloning to impersonate trusted figures.
- **Zero-Day Discovery:** Finding vulnerabilities unknown to the software vendor, exploitable until patched.
- **DeepFuzz:** Proposed AI agent combining deep learning, symbolic execution, and distributed computing for intelligent fuzzing.

## Important Figures and Tables

- **Fig 6.1:** Mind map of AI agents in offensive security (5 branches: Red Teaming, Social Engineering, Supply Chain, Vulnerability Discovery, Code Examples).
- **Fig 6.2:** Process flow of AI-driven red teaming (Initiate -> Goals -> Generate Inputs -> Test -> Log/Refine -> Iterate).
- **Fig 6.3:** Workflow of AI Agent in social engineering attacks (sequence diagram).

## Practical Takeaways for Scientists

- The red teaming frameworks (GOAT, AART, PyRIT) can be used to test AI systems used in scientific research for safety and robustness.
- The BountyAgent code example provides a template for building automated security scanning tools for research software.
- Social engineering threats are relevant to scientists handling sensitive data -- awareness of deepfake and AI phishing capabilities is essential.
- The DeepFuzz architecture demonstrates how to combine multiple AI techniques (VAE, symbolic execution, reinforcement learning) in a single agent system.

## Notable References

- Meta (2024) -- Generative Offensive Agent Tester (GOAT)
- Google Project Zero (2024) -- Big Sleep / Naptime
- Radharapu et al. (2023) -- AI-assisted red teaming
- Intel 471 (2024) -- BlankBot Android banking trojan
- Magramo (2024) -- Arup deepfake scam ($25.6M)
- Brewster (2021) -- $35M voice cloning bank fraud
