# Flowcharts

Flowcharts are visual diagrams that use symbols, arrows, and shapes to represent steps in a process or algorithm.

---

## Why use them?

- Make complex processes easier to understand  
- Help plan algorithms before coding  
- Show step-by-step workflows clearly  
- Useful for decision-making systems (e.g., choosing between options)  

**Key idea:**  
Instead of only using words or code, flowcharts use visual representation to explain logic.

**Example use:**  
A program can decide to run Program A or Program B based on a condition, and a flowchart shows this clearly with branches.

---

## Flowchart Symbols (5 main symbols)

🟢 **Oval (Start/End)**  
- Shows the beginning or end of a process  
- Example: START, STOP  

🟦 **Rectangle (Process/Action)**  
- Represents an action or step  
- Example: calculate, turn on light  

🔷 **Diamond (Decision)**  
- Represents a question or condition  
- Has two outcomes: YES / NO  
- Example: “Is it dark?”  

🔼 **Arrows (Flowlines)**  
- Show the direction of the process  
- Connect all steps together  

📥 **Parallelogram (Input/Output)**  
- Used for input or output of data  
- Example: enter data, display result  

---

## Q1: What is a flowchart used for?

It is a visual diagram that uses symbols, arrows, and shapes to represent steps in a process or algorithm.  
It helps make complex processes easier, helps plan algorithms, shows clear workflows, and supports decision-making.

---

## Q2: What does a diamond shape represent?

It represents decisions or conditions.

---

## Q3: In the “room light” example: What happens if it is dark?

If it is dark (YES) → the system will turn on the light.

---

## Q4: In Heron’s method: Why do we repeat the steps again and again?

We repeat the steps to get a more accurate answer.

---

## Q5: What do arrows represent in a flowchart?

They connect steps together and show direction.

---

# Core Idea

Every flowchart (and every program) follows the same structure:

👉 **INPUT → PROCESS → OUTPUT**

This is the foundation of all programming logic.

---

## What each part means

### 📥 INPUT
What the system receives.

Examples:
- User input (age, number, name)
- Sensor data
- File data  

---

### ⚙️ PROCESS
What the system does with the input.

Examples:
- Calculations  
- Comparisons (decisions)  
- Loops (repetition)  
- Transformations  

---

### 📤 OUTPUT
Final result shown to the user/system.

Examples:
- “Access granted”  
- Result of calculation  
- Message on screen  

---

## Connection to Flowcharts

Flowcharts are just a visual version of this:

- Input → Parallelogram  
- Process → Rectangle  
- Decision → Diamond (inside process step)  
- Output → Parallelogram or End  

---

## Why decisions exist (VERY IMPORTANT)

A decision (diamond) exists because programs must choose different paths.

Example:
- If dark → turn light on  
- If not dark → do nothing  

So decision = branching logic.

---

## Why loops exist (Heron’s method link)

Loops exist because sometimes one pass is not enough.

Example:
- First guess is wrong  
- Second guess is better  
- Repeat until accurate  

So loop = improving result step-by-step.

---

## Full example (Room light system)

**INPUT:**
- Check light status  

**PROCESS:**
- Evaluate: is it dark?  

**DECISION:**
- YES → turn light on  
- NO → do nothing  

**OUTPUT:**
- Correct lighting state achieved  

---

## Key thinking rule (developer mindset)

Every problem can be broken into:

- What do I receive? (Input)  
- What do I do with it? (Process)  
- What do I produce? (Output)  

---

## Q1: What is the purpose of the process step?

The process step shows the work being done in the algorithm or system.

---

## Q2: Why do programs need decisions (diamonds)?

Programs can choose different paths based on correct decisions.

---

## Q3: What does INPUT → PROCESS → OUTPUT help you understand?

It helps you understand how a program changes input into output through processing.

---

## Final idea

Programming is just:
**taking input, processing it step-by-step, and producing output**