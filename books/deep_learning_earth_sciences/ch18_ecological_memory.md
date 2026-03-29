# Chapter 18: Emulating Ecological Memory with Recurrent Neural Networks

**Authors:** Basil Kraft, Simon Besnard, and Sujan Koirala

## Summary

This chapter explores the use of recurrent neural networks (RNNs) to capture "ecological memory" -- the phenomenon whereby past environmental conditions influence current ecosystem responses. The key innovation is using RNN hidden states as proxies for unobserved state variables (such as soil moisture) that encode memory effects. The authors demonstrate through controlled experiments on MATSIRO land surface model simulations that LSTMs can emulate evapotranspiration (ET) dynamics, capture seasonal patterns, and quantify the contribution of ecological memory under both normal and extreme climate conditions.

## Key Concepts and Methods

### Ecological Memory Concepts
- **Ecological memory**: Encoding of past environmental conditions in the current ecosystem state that affects its future trajectory
- **Memory effects**: Direct influence of ecological memory on current ecosystem functions
- **Types**: Direct (e.g., drought reduces productivity) vs. indirect (drought causes fire, which alters species composition)
- **Concurrent vs. lagged**: Effects can be immediate or delayed by months to years
- **Key state variable**: Soil moisture is the primary memory-encoding variable in terrestrial ecosystems

### Mathematical Framework
- System state: S_t = f(S_{t-1}, X_t) -- state depends on previous state and current forcing
- Response: Y_t = g(S_t) -- ecosystem response is a function of state
- With observations: S_t = f(S_{t-1}, X_t, O_t) -- observed state variables reduce reliance on memory
- RNN hidden state h_t acts as a learned analog of the system state S_t

### Data-driven Methods for Memory Effects
- **Traditional**: Hand-designed lag features, cumulative variables, random forests (sequence-agnostic)
- **RNNs**: Naturally capture temporal dependencies through hidden states without requiring explicit feature engineering
- **Advantage**: RNNs can learn memory effects that depend on complex interactions among variables over varying time scales

### Case Study: Emulating MATSIRO Land Surface Model
- **MATSIRO**: Physically-based global land surface model simulating water/energy budget (runoff, ET, soil moisture, groundwater)
- **Test design**: Train RNN on MATSIRO simulations to isolate the ability to learn memory effects in a controlled setting
- **Data**: Global, daily, 1979-2010 at 1-degree resolution; 6 forcing variables (precipitation, temperature, humidity, wind, radiation, surface pressure)
- **Two experiments**:
  1. With soil moisture as input (memory information provided)
  2. Without soil moisture (RNN must learn memory internally)

### Network Architecture and Training
- LSTM with 256 hidden units, 365-day input sequences
- Single FC layer maps LSTM output to ET prediction
- Dropout regularization, Adam optimizer
- Trained globally across all grid cells

### Key Results

**Experiment 1 (with soil moisture):**
- LSTM achieves median NSE = 0.99 globally -- nearly perfect emulation
- Captures seasonal ET dynamics, including differences between energy-limited and water-limited regimes
- Works well across all climate zones

**Experiment 2 (without soil moisture):**
- LSTM still achieves median NSE = 0.94 -- strong performance despite missing state variable
- LSTM hidden state implicitly learns soil moisture dynamics
- Largest errors in transition/semi-arid regions where soil moisture is most important
- Under drought conditions, LSTM captures reduced ET response even without explicit soil moisture input

**Memory effect quantification:**
- Difference between LSTM (with memory) and a static FC baseline (no memory) quantifies memory contribution
- Largest memory effects in semi-arid regions where soil moisture strongly modulates ET
- LSTM captures both seasonal cycles and anomalous events (droughts)

## Practical Takeaways for Scientists

1. **RNN hidden states learn unobserved state variables**: LSTMs can internally reconstruct soil moisture dynamics even when not provided as input.
2. **365-day sequences are sufficient** for capturing seasonal ecological memory in ET prediction.
3. **Use physical model simulations** as controlled test beds to evaluate DL capabilities before applying to noisy observational data.
4. **Memory effects are largest in semi-arid regions** where water availability modulates ecosystem responses.
5. **LSTM vs. static model comparison** provides a principled way to quantify memory contributions.
6. **Global training works**: A single LSTM trained across all grid cells and climate zones produces strong results.

## Notable References

- Kraft et al. (2019) -- RNNs for ecological memory in ET prediction
- Besnard et al. (2019) -- Dynamic vs. static methods for carbon flux prediction
- Reichstein et al. (2018, 2019) -- DL for Earth system science
- Ogle et al. (2015) -- Ecological memory framework
- Koirala et al. (2014) -- MATSIRO land surface model
- Hochreiter and Schmidhuber (1997) -- LSTM
