# Chapter 8: Recurrent Neural Networks and the Temporal Component

**Authors:** Marco Koerner and Marc Russwurm

## Summary

This chapter provides a comprehensive treatment of recurrent neural networks (RNNs) for processing temporal Earth observation data. Earth system processes are inherently dynamic, and satellite time series (e.g., MODIS NDVI, Sentinel-2 multitemporal imagery) require models that can capture temporal dependencies. The chapter covers vanilla RNNs, the vanishing/exploding gradient problem, LSTM and GRU gated variants, various network topologies, and demonstrates the superiority of LSTMs over feed-forward CNNs for crop classification from Sentinel-2 time series.

The central message is that LSTMs' gated architecture allows them to maintain stable gradients over long temporal windows, enabling them to capture long-term phenological patterns (seasonal crop cycles, multi-year trends) that vanilla RNNs and feed-forward networks cannot.

## Key Concepts and Methods

### Why RNNs for Earth Sciences
- Earth observation data is sequential (satellite revisits over time)
- Regular DNNs process single observations or fixed-length concatenations
- RNNs dynamically incorporate temporal context of variable length
- Historically, HMMs were used for EO time series but require manual state-space design

### Vanilla RNNs
- Hidden state update: h_t = sigma(W_in * x_t + W_rec * h_{t-1} + b_rec)
- Trained via Back-Propagation Through Time (BPTT)
- **Critical problem**: Vanishing/exploding gradients -- gradient magnitudes depend on (W_rec)^T, causing exponential decay or growth over time steps

### Countermeasures for Gradient Problems
- **Truncated BPTT (tBPTT)**: Limit backpropagation to k time steps
- **Temporal skip connections**: Add time delays to reduce vanishing rate
- **Gradient clipping**: Cap gradient norms at threshold c
- **Regularization**: Norm-preserving error updates (Pascanu et al., 2013)
- **Weight initialization**: Identity matrix initialization for W_rec (Le et al., 2015)

### Long Short-Term Memory (LSTM)
- Four gates controlling information flow:
  - **Forget gate f_t**: Controls how much of previous cell state to retain (sigmoid)
  - **Input gate i_t**: Controls how much new information enters (sigmoid)
  - **Modulation gate v_t**: Extracts new candidate values (tanh)
  - **Output gate o_t**: Controls what information is output (sigmoid)
- Cell state c_t = f_t * c_{t-1} + i_t * v_t (additive, not multiplicative -- avoids gradient decay)
- Hidden state h_t = o_t * tanh(c_t)
- **Peephole connections**: Allow gates to peek at current cell state (more stable training)
- 4x parameters compared to vanilla RNN

### Gated Recurrent Unit (GRU)
- Simplified LSTM: Combines input and forget gates into single "update gate"
- Adds "reset gate" instead
- Fewer parameters but loses ability to detect context-free languages
- **Minimal Gated Unit (MGU)**: Further reduces to single forget gate

### Network Topologies
- **One-to-one**: Single input to single output (standard)
- **Many-to-one**: Sequence input to single prediction (e.g., full season to crop type)
- **One-to-many**: Single input to sequence prediction (forecasting)
- **Many-to-many**: Sequence to sequence (concurrent or consecutive)
- **Bidirectional RNNs**: Process sequence both forward and backward (offline settings)
- **Multi-dimensional RNNs**: Augment with spatial dimensions (ConvLSTMs)

### Application: NDVI Prediction and Crop Classification
- **NDVI prediction**: LSTM maintains near-constant gradient magnitudes over 10 years of MODIS data; vanilla RNN gradients decay exponentially
- **Crop classification**: LSTM on Sentinel-2 time series outperforms CNN baseline
  - LSTM classification accuracy increases with each new observation during growing season
  - CNN shows uncorrelated accuracy fluctuations
  - LSTM converges faster and more reliably across initializations

## Practical Takeaways for Scientists

1. **Use LSTMs over vanilla RNNs** for any EO time series longer than ~10 time steps -- vanishing gradients make vanilla RNNs unreliable for longer sequences.
2. **LSTMs capture phenological patterns**: Growth onset, harvesting events, seasonal cycles are automatically learned without explicit feature engineering.
3. **LSTMs improve with more observations**: Classification accuracy increases monotonically as the growing season progresses, unlike feed-forward approaches.
4. **GRUs are a lighter alternative** when computational resources are limited, but may miss longer-term dependencies.
5. **ConvLSTMs** combine spatial and temporal processing for spatio-temporal EO data.
6. **Initialize forget gate bias to large values** to prevent early "forgetting" of temporal context during training.

## Notable References

- Hochreiter and Schmidhuber (1997) -- Original LSTM paper
- Cho et al. (2014) -- GRU
- Russwurm and Koerner (2017a, 2018) -- LSTM for crop type classification
- Gers et al. (2000) -- Forget gate and peephole connections
- Kraft et al. (2020, 2019) -- RNNs for climate system analysis
- Sainath et al. (2015) -- ConvLSTMs
