# Session 4: Transformers - The Architecture Behind Modern AI

Transformers are the breakthrough architecture that powers ChatGPT, Claude, Gemini, and virtually all modern AI language models. This session explains how transformers work and why they're so effective.

## What You'll Learn

- The transformer architecture and its key components
- How self-attention helps AI understand relationships
- Why positional encoding matters
- How feed-forward networks process information
- The complete flow from input to output

## The Transformer Revolution

Before transformers (pre-2017), AI struggled with:

- Understanding long-range dependencies in text
- Processing text in parallel (it was sequential and slow)
- Capturing complex relationships between words

**The Transformer paper** ("Attention Is All You Need", 2017) changed everything.

**Impact:**

- GPT models (ChatGPT)
- BERT (Google search)
- T5, BART (text generation)
- Claude (Anthropic)
- LLaMA (Meta)
- All modern LLMs

## The Three Core Components

Based on the architecture diagram, transformers have three essential mechanisms:

```
Input Text
    ↓
1. POSITIONAL ENCODING
    ↓
2. SELF-ATTENTION
    ↓
3. FEED FORWARD NETWORK
    ↓
Output
```

Let's explore each component with the Persian example from the diagram:
**"من در خانه در را بستم"** (I closed the door at home)

## 1. Positional Encoding

### The Problem

Unlike humans, neural networks don't inherently understand word order:

**To a basic neural network:**

- "The dog chased the cat"
- "The cat chased the dog"

...look identical (same words, just rearranged).

But these sentences mean completely different things!

### The Solution: Positional Encoding

Add position information to each word's embedding.

**How it works:**

```
Original embeddings (meaning only):
من (I):      [0.2, 0.8, 0.3, ...]
در (at/in):  [0.5, 0.2, 0.7, ...]
خانه (house): [0.1, 0.9, 0.4, ...]

Positional encodings (position info):
Position 1:  [0.0, 1.0, 0.0, ...]
Position 2:  [0.84, 0.54, 0.0, ...]
Position 3:  [0.91, -0.42, 0.0, ...]

Combined (meaning + position):
من at position 1:   [0.2+0.0, 0.8+1.0, 0.3+0.0, ...]
در at position 2:   [0.5+0.84, 0.2+0.54, 0.7+0.0, ...]
خانه at position 3: [0.1+0.91, 0.9-0.42, 0.4+0.0, ...]
```

Now the model knows both:

- **What** each word means (from embedding)
- **Where** it appears in the sentence (from position)

### Why This Matters

**Example: Ambiguous Word "در" (dar)**

In Persian, "در" can mean:

- "door" (noun)
- "at/in" (preposition)

In "من در خانه در را بستم":

- First "در" (position 2) = "at/in" (preposition)
- Second "در" (position 4) = "door" (noun)

Positional encoding helps the model distinguish these identical words in different positions.

### Mathematical Detail (Optional)

Positional encodings use sine and cosine functions:

```
PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
```

**Benefits:**

- Consistent encoding for any position
- Model can learn relative positions
- Works for sequences of any length

## 2. Self-Attention

This is the revolutionary mechanism that makes transformers powerful.

### The Core Idea

**Self-attention lets each word "look at" all other words** to understand context.

### Persian Example: "من در خانه در را بستم"

Translation: "I closed the door at home"
Word-by-word: "I at house door [object marker] closed"

**When processing the word "بستم" (closed):**

The self-attention mechanism asks:

- "What did I close?" → looks at "در" (door)
- "Where?" → looks at "خانه" (house) and "در" (at/in)
- "Who closed it?" → looks at "من" (I)

**Attention weights might look like:**

```
Word: بستم (closed)
Pays attention to:
- در (door):      HIGH attention (0.8) - what was closed
- را (object):    MEDIUM attention (0.5) - grammatical marker
- خانه (house):   MEDIUM attention (0.4) - location context
- در (at):       MEDIUM attention (0.4) - location preposition
- من (I):        LOW attention (0.2) - subject
```

The model learns these attention patterns automatically during training!

### How Self-Attention Works

**Three Steps:**

**Step 1: Create Queries, Keys, and Values**

For each word, create three representations:

- **Query**: "What am I looking for?"
- **Key**: "What do I have to offer?"
- **Value**: "What information do I contain?"

```
Word "بستم" (closed):
Query: [0.3, 0.7, 0.2, ...] "I need info about what was closed"
Key: [0.8, 0.1, 0.6, ...] "I'm the action"
Value: [0.5, 0.4, 0.3, ...] "I represent closing action"

Word "در" (door):
Query: [0.1, 0.9, 0.3, ...]
Key: [0.7, 0.2, 0.8, ...] "I'm an object"
Value: [0.6, 0.5, 0.4, ...] "I represent a door"
```

**Step 2: Calculate Attention Scores**

Compare each word's query with every other word's key:

```
بستم's Query · در's Key = attention score
(how much should "closed" pay attention to "door")
```

High score = strong relationship
Low score = weak relationship

**Step 3: Use Attention to Combine Information**

Weighted combination of values based on attention scores:

```
بستم's output =
  0.8 × (door's value) +
  0.5 × (object marker's value) +
  0.4 × (house's value) +
  0.4 × (at's value) +
  0.2 × (I's value)
```

The result: "بستم" now has rich context about the entire sentence!

### Multi-Head Attention

Transformers don't use just one attention mechanism - they use **many in parallel** (typically 8-16 "heads").

**Why?**

Different heads learn different relationships:

- **Head 1**: Grammatical relationships (subject-verb-object)
- **Head 2**: Semantic relationships (door-house-close)
- **Head 3**: Long-distance dependencies
- **Head 4**: Nearby word relationships

**Example: "The bank on the river"**

- Head 1: "bank" attends to "river" (geographical context)
- Head 2: "on" attends to "bank" and "river" (spatial relationship)
- Head 3: "The" attends to "bank" (determiner-noun)

Each head captures different aspects, then results are combined.

### Visual Representation

```
Sentence: I    at   house  door  [obj]  closed
Position: 1    2     3      4      5      6

Self-Attention for word "closed" (position 6):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
I      →  0.2  ▓▓
at     →  0.4  ▓▓▓▓
house  →  0.4  ▓▓▓▓
door   →  0.8  ▓▓▓▓▓▓▓▓
[obj]  →  0.5  ▓▓▓▓▓
closed →  0.9  ▓▓▓▓▓▓▓▓▓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

(Darker = stronger attention)
```

## 3. Feed Forward Network

After self-attention, each word's representation goes through a **feed-forward network**.

### What It Does

**Purpose**: Transform and enhance the information gathered by attention.

**Architecture:**

```
Input (from attention)
    ↓
Dense Layer 1 (expand) - typically 4× larger
    ↓
Activation (ReLU/GELU)
    ↓
Dense Layer 2 (compress) - back to original size
    ↓
Output
```

### Why It's Important

1. **Non-linear transformation**: Captures complex patterns
2. **Enhancement**: Refines the context understanding
3. **Position-specific**: Each position processed independently

### Example Process

```
Word "door" after attention: [0.3, 0.7, 0.2, 0.8, ...]
                               ↓
Feed Forward Network:
  Layer 1 → [0.5, 0.2, 0.9, 0.1, 0.7, 0.3, 0.8, 0.4, ...]
  (expanded to more dimensions)
                               ↓
  Activation → [0.5, 0.0, 0.9, 0.0, 0.7, 0.0, 0.8, 0.0, ...]
  (negative values set to 0)
                               ↓
  Layer 2 → [0.4, 0.8, 0.3, 0.9, ...]
  (compressed back to original size)
```

The result: Enhanced representation of "door" with its full context.

## Complete Transformer Flow

Let's walk through the full process with our Persian example:

### Step-by-Step

**Input:** "من در خانه در را بستم"

**1. Tokenization**

```
Tokens: [من, در, خانه, در, را, بستم]
```

**2. Embedding**

```
من    → [0.2, 0.8, 0.3, ...]
در    → [0.5, 0.2, 0.7, ...]
خانه  → [0.1, 0.9, 0.4, ...]
... (each word becomes a vector)
```

**3. Positional Encoding**

```
من + position 1    → [0.2+0.0, 0.8+1.0, ...]
در + position 2    → [0.5+0.84, 0.2+0.54, ...]
خانه + position 3  → [0.1+0.91, 0.9-0.42, ...]
```

**4. Self-Attention (repeated for each word)**

```
For "بستم":
- Query what information is needed
- Check relevance with all other words
- Gather context from related words
Result: "بستم" now knows about "door", "house", etc.
```

**5. Feed Forward**

```
Enhanced representation for each word with full context
```

**6. Repeat** (typically 12-96 times)

```
Stack multiple transformer layers
Each layer refines understanding further
```

**7. Output**

```
Final representations ready for:
- Next token prediction (language models)
- Classification (sentiment analysis)
- Translation (sequence-to-sequence)
```

## Why Transformers Are Powerful

### 1. Parallel Processing

**Old models (RNNs):**

```
Process word 1 → then word 2 → then word 3 → ... (sequential)
Slow for long sequences
```

**Transformers:**

```
Process ALL words simultaneously
Much faster training and inference
```

### 2. Long-Range Dependencies

**Example:** Understanding references across long text

```
"The trophy didn't fit in the suitcase because it was too large."
```

What is "it"? The trophy or the suitcase?

**Self-attention can look back** to "trophy" and "suitcase," considering:

- "too large" suggests "trophy"
- Physical constraints suggest checking both

Transformers handle these connections naturally.

### 3. Context-Aware Representations

Every word's final representation includes information from the entire sentence.

**"Bank" in different contexts:**

```
"I went to the bank" → "bank" attends to "went" (action → financial)
"The river bank" → "bank" attends to "river" (location → geographical)
```

Each instance of "bank" gets a different representation based on context.

## Practical Implications

### For Language Models

**GPT (Generative Pre-trained Transformer)**

- Uses transformer decoder
- Generates text left-to-right
- Each token can only attend to previous tokens
- Powers ChatGPT, GPT-4

**BERT (Bidirectional Encoder)**

- Uses transformer encoder
- Can attend to entire context (both directions)
- Great for understanding tasks
- Powers Google search improvements

### For Your Applications

**Understanding these mechanisms helps you:**

1. **Choose the right model**

   - Need bidirectional context? → BERT-style
   - Need generation? → GPT-style

2. **Optimize prompts**

   - Relevant context near the question
   - Clear relationships between concepts

3. **Debug issues**

   - Model confused? Might be ambiguous attention
   - Poor results? Check if context is too far apart

4. **Estimate costs**
   - Self-attention is O(n²) in sequence length
   - Longer sequences = much more expensive

## Advanced Topics

### Layer Normalization

Keeps values stable as they flow through many layers:

```
After each attention/feed-forward:
Normalize → prevents explosion/vanishing
```

### Residual Connections

Skip connections that preserve information:

```
Input → [Attention] → + Input → Output
```

**Why?** Prevents information loss in deep networks.

### The Full Architecture

```
Input Embedding + Positional Encoding
    ↓
┌──────────────────┐
│ Transformer Layer│ ×N (repeat many times)
│                  │
│ • Multi-Head     │
│   Self-Attention │
│ • Add & Norm     │
│ • Feed Forward   │
│ • Add & Norm     │
└──────────────────┘
    ↓
Output Projection
    ↓
Final Output
```

**Typical sizes:**

- **GPT-3**: 96 layers, 96 attention heads
- **GPT-4**: Estimated 120+ layers
- **BERT-base**: 12 layers, 12 attention heads

## Key Takeaways

1. **Three core components**: Positional encoding, self-attention, feed-forward networks
2. **Positional encoding** teaches models about word order
3. **Self-attention** lets words understand their relationships
4. **Multi-head attention** captures different types of relationships
5. **Feed-forward networks** enhance and transform representations
6. **Parallel processing** makes transformers fast
7. **Context-aware** representations understand word meaning in context
8. **Stacking layers** creates deep understanding

## Hands-On Understanding

Try these mental exercises:

**Exercise 1: Attention Prediction**

Sentence: "The chef cooked the meal in the kitchen"

What should "cooked" pay attention to?

- High: "chef" (who cooked?), "meal" (what was cooked?)
- Medium: "kitchen" (where?)
- Low: "The", "the", "in" (grammatical words)

**Exercise 2: Position Importance**

Compare:

- "The dog bit the man"
- "The man bit the dog"

Same words, different positions → different meanings
Positional encoding is crucial!

**Exercise 3: Context Changes Meaning**

Word: "light"

- "Please turn on the light" → noun (lamp)
- "This bag is light" → adjective (not heavy)
- "Light the candle" → verb (ignite)

Self-attention helps distinguish these by looking at surrounding words.

## Connection to Next Session

Now you understand the architecture behind AI. In Session 5, we'll explore **RAG (Retrieval-Augmented Generation)** and **Agents** - how to combine transformers with external knowledge and tools to build powerful applications that go beyond just chat.

## Resources

- [The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (original paper)
- [The Annotated Transformer](http://nlp.seas.harvard.edu/annotated-transformer/)
- [3Blue1Brown: Attention in Transformers](https://www.youtube.com/watch?v=eMlx5fFNoYc)

## Technical Terms Glossary

- **Attention**: Mechanism for weighing importance of different inputs
- **Query/Key/Value**: Three representations used in attention calculation
- **Multi-head**: Multiple parallel attention mechanisms
- **Positional Encoding**: Adding position information to embeddings
- **Feed-Forward**: Simple neural network layer
- **Layer Normalization**: Technique to stabilize training
- **Residual Connection**: Skip connection that preserves information

## Discussion Questions

1. How does understanding self-attention help you write better prompts?
2. Why might longer contexts be slower to process?
3. How could positional encoding affect different languages?
4. What types of relationships in your field would benefit from attention mechanisms?
