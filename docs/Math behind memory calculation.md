* **Model parameters:** The numbers the model learns and stores as its knowledge.
* **Optimizers:** The rulebook that decides how those numbers should be updated after mistakes.
* **Gradient descent:** The step-by-step process of moving the parameters in the direction that reduces error.
* **Activations:** The temporary intermediate values created while the model processes an input.

```
Total memory ≈
params
+ gradients
+ optimizer
+ activations × batch_size
```

# Analogy
Memory math is about **packing a school bag**. If you don’t know what goes inside, the bag tears. Simple analogies. No jargon first.


## Imagine you are studying for exams

Your **GPU / RAM = your school bag capacity**
Your **model = books and notes**

If the bag capacity is 10 kg and you carry 14 kg, it breaks.
Computer says OOM.

## What goes into the bag (4 things)

### 1. Model parameters = Textbook

This is the main book.

* Big book → heavy
* Small book → light

**Example**

```text
Big book = 2 kg
```

### 2. Gradients = Pencil notes on the book

Every time you study, you write notes on the book pages.

Same size as the book.

**Example**

```text
Book = 2 kg
Notes = 2 kg
```

### 3. Optimizer = Teacher’s correction notebook

Teacher keeps extra notebooks to track:

* your mistakes
* your improvement history

For Adam optimizer, teacher needs **two notebooks**.

**Example**

```text
Teacher notebooks = 4 kg
```


### 4. Activations = Rough work pages

This is the rough work you do while solving problems.

This depends on:

* how many questions (batch size)
* how long the question is (sequence length)

This is usually the **heaviest**.

**Example**

```text
Rough work = 6 kg
```

## Total weight in the bag

```text
Textbook       2 kg
Notes          2 kg
Teacher notes  4 kg
Rough work     6 kg
------------------
Total         14 kg
```

If your bag capacity is **10 kg**, it breaks.

That is **out of memory**.


## Why “half precision” helps (mixed precision)

Instead of thick paper, you use **thin paper**.

Everything weighs half.

```text
Book        1 kg
Notes       1 kg
Teacher     2 kg
Rough work  3 kg
------------
Total       7 kg
```

Same study. Lighter bag.


## Why more bags (GPUs) don’t automatically help

You bring **4 bags**, but you put **the same book in all bags**.

That is stupid but that’s how default training works.

Each bag still carries:

```text
14 kg
```

More bags ≠ less weight per bag.

## ZeRO optimizer = smart sharing between friends

You and 3 friends study together.

Instead of everyone carrying **all books**:

* You carry chapter 1
* Friend 1 carries chapter 2
* Friend 2 carries chapter 3
* Friend 3 carries chapter 4

When needed, you share.


### ZeRO-1 (share teacher notebooks)

Only teacher notes are split.

```text
Teacher notes 4 kg → 1 kg each
```

Bag weight now:

```text
2 + 2 + 1 + 6 = 11 kg
```

Still heavy.


### ZeRO-2 (share teacher + notes)

```text
Notes       2 kg → 0.5 kg
Teacher     4 kg → 1 kg
```

Bag:

```text
2 + 0.5 + 1 + 6 = 9.5 kg
```

Almost fits.

### ZeRO-3 (share everything except rough work)

```text
Book        2 kg → 0.5 kg
Notes       2 kg → 0.5 kg
Teacher     4 kg → 1 kg
Rough work  stays 6 kg
```

Bag:

```text
0.5 + 0.5 + 1 + 6 = 8 kg
```

Now it fits.



## Why batch size kills memory

Batch size = number of questions you solve at once.

More questions → more rough work.

```text
10 questions → 6 kg rough work
20 questions → 12 kg rough work
```

Bag explodes.

That is why reducing batch size always works.



## One golden rule (remember this)

```text
Books are fixed.
Notes are same size as books.
Teacher notes are double.
Rough work explodes with batch size.
```


## Reality check for you

* CPU-only = small bag, slow walking
* Good for learning and testing
* Not for carrying truckloads of books

---

# Real world use case

Concrete case study. Real numbers. Real math. No abstraction.



## Case study

**Task:** Fine-tune BERT-base for text classification
**Hardware:** 1 GPU with **16 GB VRAM**
**Model:** BERT-base
**Optimizer:** Adam
**Precision:** FP16
**Batch size:** 8
**Sequence length:** 512

This is a very common real-world setup.

## Step 1. Model parameters (FACT)

BERT-base has **110 million parameters**.

Memory per parameter in FP16:

```text
2 bytes
```

### Parameter memory

```text
110M × 2 bytes = 220 MB ≈ 0.22 GB
```


## Step 2. Gradients

Each parameter has one gradient.

```text
Gradients = same as parameters
```

```text
= 0.22 GB
```

## Step 3. Optimizer memory (Adam)

Adam stores:

* first moment
* second moment

That is **2 copies of parameters**, usually in FP32.

```text
110M × 4 bytes × 2 = 880 MB ≈ 0.88 GB
```


## Step 4. Activations (this is real math)

For transformers, activation memory is roughly:

```text
batch_size × seq_len × hidden_size × layers × bytes
```

### BERT-base specs

```text
hidden_size = 768
layers = 12
batch_size = 8
seq_len = 512
bytes = 2 (FP16)
```

### Activation calculation

```text
8 × 512 × 768 × 12 × 2 bytes
```

Step by step:

```text
512 × 768 = 393,216
393,216 × 12 = 4,718,592
4,718,592 × 8 = 37,748,736
37,748,736 × 2 bytes ≈ 75 MB
```

Backward pass stores more tensors. Multiply by ~3.

```text
Activations ≈ 225 MB ≈ 0.22 GB
```


## Step 5. Total memory usage

Now add everything.

```text
Parameters   = 0.22 GB
Gradients    = 0.22 GB
Optimizer    = 0.88 GB
Activations  = 0.22 GB
-------------------------
Total        = 1.54 GB
```

## Step 6. Reality correction (framework overhead)

PyTorch + CUDA buffers + fragmentation ≈ **2× safety factor**

```text
1.54 GB × 2 ≈ 3.1 GB
```

This comfortably fits in **16 GB GPU**.

## Step 7. What breaks it in real life

### Increase batch size from 8 → 32

Activations scale linearly.

```text
Activations = 0.22 × 4 = 0.88 GB
```

New total:

```text
0.22 + 0.22 + 0.88 + 0.88 = 2.2 GB
× 2 overhead ≈ 4.4 GB
```

Still fits.


### Switch to FP32

Everything doubles except optimizer moments which are already FP32.

```text
Parameters   = 0.44 GB
Gradients    = 0.44 GB
Optimizer    = 0.88 GB
Activations  = 0.44 GB
-------------------------
Total        = 2.2 GB
× 2 overhead ≈ 4.4 GB
```

Still fine.


## Step 8. Now a real failure case

**Model:** LLaMA-7B
**Params:** 7 billion
**FP16**

### Parameters

```text
7B × 2 bytes = 14 GB
```

Already almost fills the GPU.

Add:

```text
Gradients  = 14 GB
Optimizer  = 28 GB
Activations ≈ 20+ GB
```

Total:

```text
> 70 GB
```

On a **24 GB GPU**.

Impossible without:

* ZeRO-2 / ZeRO-3
* gradient checkpointing
* offloading

This is not a bug. This is math.


## Final takeaway (burn this in brain)

```text
Small model → activations dominate
Large model → parameters + optimizer dominate
OOM is predictable
Memory failure is not mysterious
```