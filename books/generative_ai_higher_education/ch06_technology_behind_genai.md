# Chapter 6: Technology Behind GenAI

## Summary

This is the most technical chapter of the book, authored primarily by Tom Colloton. It provides a comprehensive, accessible introduction to the technology underlying Generative AI. While the book is aimed at educators rather than engineers, this chapter ensures readers understand enough about how GenAI works to make informed decisions about its educational use. The chapter covers the history of AI, the process of creating a model, model ecosystems, and state-of-the-art models.

### AI Categorisation

The chapter opens with a nested hierarchy (Figure 6.1):
- **Artificial Intelligence** (broadest)
  - **Machine Learning**
    - **Artificial Neural Networks**
      - **Deep Learning**
        - **GenAI** (includes LLMs and text-to-image models)

### Two Camps in AI History

- **Symbolists** -- Believed intelligence comes from manipulating symbols and rules (logic-based systems, expert systems). Key figures: John McCarthy, Marvin Minsky, Herbert Simon
- **Connectionists** -- Believed intelligence emerges from interconnected networks of simple units (neural networks). Key figures: Frank Rosenblatt, Geoffrey Hinton, Yann LeCun, James Rumelhart

### Three Historical Phases

#### The Genesis Phase (1940s-1980s)
- McCulloch & Pitts (1943) -- logical calculus of nervous activity
- Hebb (1949) -- Hebbian Learning
- The 1956 Dartmouth Workshop -- birth of "artificial intelligence" as a term
- Rosenblatt's Perceptron (1958) -- first trainable neural network
- ELIZA (1966) -- early chatbot
- Minsky & Papert's "Perceptrons" (1969) -- highlighted limitations, contributing to the first AI winter
- Backpropagation discovered by Werbos (1974), later popularised by Rumelhart et al. (1985)

**Philosophical considerations from this era:**
- **Alan Turing** (1950) -- The Turing Test / Imitation Game
- **Isaac Asimov** (1942) -- Three Laws of Robotics
- **Joseph Weizenbaum** -- Warned against machines handling tasks needing genuine compassion
- **Norbert Wiener** -- Cautioned about automation's unintended consequences

#### The Maturing Phase (1980s-2010s)
- Backpropagation (Rumelhart, Hinton, Williams, 1986)
- Hopfield networks (1982)
- Boltzmann Machines (Hinton & Sejnowski, 1985)
- LSTMs -- Long Short-Term Memory networks (Hochreiter & Schmidhuber, 1997)
- CNNs for document recognition (LeCun et al., 1998)
- Support Vector Machines (Wahba et al., 2002)
- Random Forests (Breiman, 2001)

#### The Acceleration Phase (2010s-2030s)
- AlexNet and the "ImageNet moment" (Krizhevsky et al., 2012)
- GANs -- Generative Adversarial Networks (Goodfellow et al., 2014)
- **"Attention Is All You Need"** -- The Transformer paper (Vaswani et al., 2017) -- foundational for all modern LLMs
- BERT (2018) -- Bidirectional Transformers
- GPT-3 (2020) -- Few-shot learning demonstrated
- Stable Diffusion (2022) -- Open-source image generation
- ChatGPT (November 2022) -- Mass consumer adoption
- GPT-4 (March 2023) -- Multimodal capabilities
- LLaMA, PaLM-2, Claude, Mistral (2023) -- Proliferation of LLMs

### Creating a Model -- The Big Picture

The chapter describes the full model creation pipeline:

1. **Training Data**
   - Data gathering and preparation
   - Dataset customisation
   - Key data sources: Common Crawl (120 TB compressed web data), C4 (Colossal Clean Crawled Corpus), LAION-5B (5.85 billion image-text pairs), LabelMe, GitHub, Wikipedia, Project Gutenberg

2. **Foundation Model**
   - Model design and structuring
   - Model training (unsupervised learning)
   - Model testing

3. **Fine-Tuning**
   - Fine-tuning dataset customisation
   - Fine-tuning training (supervised or semi-supervised)
   - Model testing

4. **Deployment and Use**
   - Model deployment
   - Model monitoring
   - Model use (inference)

### Key Technical Concepts Explained

#### Artificial Neurons
- **Weights** -- Numbers that are multiplied with inputs; adjusted during training
- **Bias** -- A number added to the weighted sum; adjusted during training
- **Activation functions** -- Mathematical functions that determine the neuron's output (sigmoid, ReLU, SwiGLU, etc.)

#### Cell Types
- **Feed-forward cells** -- Process inputs in one direction
- **Recurrent cells** -- Incorporate output from the previous step as input (used in RNNs)

#### Deep Neural Networks
- Input layer, hidden layers (at least 3 for "deep"), output layer
- Connections between layers (synapses)
- Flexibility in number of nodes per layer

#### Text Processing Pipeline
1. **Tokenisation** -- Breaking text into tokens (words, sub-words, or characters)
2. **Encoding** -- Mapping tokens to numerical representations (one-hot encoding)
3. **Embedding** -- Learning vector representations that capture semantic relationships
4. **Attention** -- The mechanism that allows the model to focus on relevant parts of the input (query, key, value matrices; multiple attention heads)
5. **Next word prediction** -- The core learning goal of LLMs

#### Image Processing Pipeline
1. **Pre-processing** -- Normalising images to standard format and size
2. **Encoding** -- Converting pixels to tensors (RGB values)
3. **Convolutional layers** -- Learning relationships between image regions
4. **Diffusion learning** -- Forward diffusion (adding noise) and reverse diffusion (removing noise) teach the model to generate images

#### Hyperparameters
- Learning rate, batch size, number of epochs, dropout rate
- **Temperature** -- Controls randomness of predictions (low = more deterministic, high = more random)

### Learning Types

1. **Supervised learning** -- Training data includes labels; model learns from correct answers
2. **Self-supervised learning** -- Model uses unlabelled data to supervise its own learning (e.g., predicting the next word); most common for LLMs
3. **Unsupervised learning** -- No labels; model discovers patterns (e.g., clustering)
4. **Reinforcement Learning with Human Feedback (RLHF)** -- Human evaluators rate model outputs; model learns from these preferences

### The Training Process

For each batch of training data:
1. **Forward pass** -- Model makes predictions
2. **Loss calculation** -- Compares predictions to actual values (cross-entropy for LLMs, adversarial loss for image models)
3. **Backward pass (backpropagation)** -- Computes gradients of loss with respect to each parameter
4. **Adjustment** -- Updates weights and biases based on gradients

### Model Testing and Benchmarks

The chapter provides detailed coverage of major benchmarks:

**Common Sense Reasoning:** BoolQ, PIQA, SIQA, SWAG, HellaSwag, WinoGrande, ARC (Easy and Challenge)

**Question Answering:** OpenBookQA, Natural Questions, TriviaQA, SQuAD 1.1 and 2.0

**Reading Comprehension:** RACE

**Mathematical Reasoning:** MATH, GSM8K

**Code Generation:** HumanEval, MBPP

**Multi-task Language Understanding:** GLUE (9 NLU tasks), SuperGLUE (8 harder tasks), MMLU (57 tasks across domains)

**Toxicity:** RealToxicityPrompts

**Bias:** CrowS-Pairs, WinoGender

**Truthfulness:** TruthfulQA

### Model Deployment

The chapter covers deployment considerations:
- **Model optimisation** -- Pruning, quantisation, ablation studies
- **Model conversion** -- ONNX, TensorFlow SavedModel, PyTorch formats
- **Additional testing** -- Inference speed, resource consumption, scale testing
- **API wrapper** -- User authentication, interface design
- **Monitoring and logging** -- Performance tracking, error detection
- **Filtering for safety** -- Input and output filters to prevent harmful content
- **Continuous improvement** -- Updates, new versions, addressing hallucinations

### Runtime Concepts

- **Prompt engineering** -- Designing effective inputs for desired outputs
- **Prompt injection** -- Adversarial manipulation of prompts
- **Jailbreaking** -- Circumventing safety filters (e.g., DAN mode for ChatGPT)
- **Prompt leaking** -- Extracting internal system prompts

### Model Ecosystems

The chapter describes the broader ecosystem around models:
- **Custom interfaces and chat** -- User-facing applications
- **APIs and functions** -- Developer access to models
- **Plugins and agents** -- Extensions that give models access to external tools
- **Custom fine-tuning** -- Users creating specialised model versions
- **Custom models** -- Purpose-built models (e.g., OpenAI's Advanced Data Analysis / Code Interpreter)
- **Vector databases and RAG** -- Retrieval Augmented Generation combining search with generation

### State-of-the-Art Models (as of late 2023)

**LLMs:**
- **OpenAI ChatGPT/GPT-4** -- ~1.8T parameters, ~120 layers, MoE architecture, multimodal
- **Meta LLaMA-2** -- 7B/13B/70B parameters, open source, uses SFT and RLHF
- **Google Bard/PaLM-2** -- Three sizes (S/M/L), multilingual, multiple configurations (Gecko, Otter, Bison, Unicorn)
- **Anthropic Claude** -- Transformer-based, >52B parameters, Constitutional AI approach, 100k context window
- **Mistral AI Mistral-7B** -- Open source (Apache 2), uses GQA and sliding window attention

**Diffusion Models:**
- **Stable Diffusion** (Stability AI) -- Open source, trained on 5B+ images, Latent Diffusion Model
- **DALL-E 3** (OpenAI) -- Integrated with ChatGPT, built natively on the platform
- **Midjourney** -- Transformer-based diffusion model, accessible through Discord

**Speech:**
- **Whisper** (OpenAI) -- Encoder-decoder transformer, 680K hours of training data, open source

## Practical Takeaways for University Faculty

1. **LLMs predict tokens, not truth** -- understanding this explains hallucinations and helps calibrate expectations
2. **Training data matters** -- models reflect the biases and limitations of their training data
3. **Temperature controls creativity vs. consistency** -- useful to know when directing student use
4. **Context windows are limited** -- models cannot read entire textbooks; they work within token limits
5. **Fine-tuning enables specialisation** -- the same base model can be adapted for different purposes
6. **RLHF shapes model behaviour** -- models are trained to be helpful, harmless, and honest through human feedback
7. **Benchmarks show capabilities but have limits** -- high benchmark scores do not equal real-world reliability
8. **The ecosystem is broader than chatbots** -- APIs, plugins, RAG, and agents extend model capabilities
9. **Open-source models are proliferating** -- LLaMA, Mistral, and others make AI more accessible
10. **The technology is advancing rapidly** -- what is state-of-the-art today will be surpassed within months

## Notable References

- Vaswani, A., et al. (2017). Attention is all you need. *NeurIPS*
- Goodfellow, I., et al. (2014). Generative adversarial networks
- Brown, T. B., et al. (2020). Language models are few-shot learners (GPT-3)
- OpenAI. (2023). GPT-4 technical report
- Touvron, H., et al. (2023). LLaMA: Open and efficient foundation language models
- McCulloch, W. S., & Pitts, W. (1943). A logical calculus of the ideas immanent in nervous activity
- Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by backpropagating errors
