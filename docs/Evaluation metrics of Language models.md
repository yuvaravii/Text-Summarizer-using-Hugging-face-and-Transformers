These are text evaluation metrics. Each answers a different question. Simple examples below.

---

## 1. BLEU

**Question:** How close is the generated text to a reference translation word by word.

**How it works:** Counts matching n-grams. Precision-focused.

**Example:**

* Reference: `"The cat is on the mat"`
* Output A: `"The cat is on the mat"`
* Output B: `"The cat sat on the mat"`

Output A gets higher BLEU. Exact word matches.

**Key point:**
Good for machine translation. Bad at synonyms and meaning.

---

## 2. ROUGE

**Question:** How much of the reference content is covered by the generated text.

**How it works:** Recall-focused n-gram overlap. Used for summarization.

**Variants:**

* **ROUGE-1:** word overlap
* **ROUGE-2:** two-word sequences
* **ROUGE-L:** longest common subsequence

**Example:**

* Reference summary: `"The company reported strong revenue growth"`
* Generated: `"The company reported revenue growth"`

High ROUGE. Most important words are present.

**Key point:**
Good for summaries. Doesn’t judge fluency or correctness.

---

## 3. BERTScore

**Question:** Do both texts mean the same thing.

**How it works:** Compares contextual embeddings from BERT. Semantic similarity.

**Example:**

* Reference: `"The boy is riding a bicycle"`
* Generated: `"A child is cycling"`

High BERTScore. Same meaning. Low BLEU.

**Key point:**
Best for meaning. Slower and model-dependent.

---

## 4. METEOR

**Question:** Are the words similar even if not exact.

**How it works:** Matches using synonyms, stemming, and word order.

**Example:**

* Reference: `"She is running fast"`
* Generated: `"She runs quickly"`

METEOR scores high. BLEU scores lower.

**Key point:**
More human-aligned than BLEU. Still reference-based.

---

## 5. Perplexity

**Question:** How surprised is the language model by the text.

**How it works:** Measures prediction uncertainty. Lower is better.

**Example:**

* Sentence A: `"I am going to the market"`
* Sentence B: `"I am going market to the"`

Sentence A has lower perplexity.

**Key point:**
Evaluates language models, not task correctness. No reference needed.

---

## Mental model (remember this)

```text
BLEU       → exact wording
ROUGE      → content coverage
METEOR     → wording flexibility
BERTScore  → meaning
Perplexity → language quality
```

---

## Truth

No single metric is enough.
BLEU alone is trash for modern LLMs.
Use **BERTScore + ROUGE** for generation tasks.
Use **Perplexity** only to compare language models, not outputs.

