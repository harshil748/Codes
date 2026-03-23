# LR(0) Parser - Test Cases

## Grammar Reference
```
0. S' -> S
1. S  -> A A
2. A  -> a A
3. A  -> b
```

## Language Definition
The grammar accepts strings with exactly **two 'b' characters**, where each 'b' can be preceded by zero or more 'a' characters.

Pattern: `a*b a*b`

---

## ✓ VALID TEST CASES (Should be ACCEPTED)

### Test Case 1: Minimal String
```
Input: ab$
Expected: ACCEPT
Derivation: S => AA => aAA => abA => abb
Description: One 'a' before first 'b', no 'a' before second 'b'
```

### Test Case 2: One 'a' before each 'b'
```
Input: aab$
Expected: ACCEPT
Derivation: S => AA => aAA => aaAA => aabA => aabb
Description: Two 'a's before first 'b', no 'a' before second 'b'
```

### Test Case 3: No 'a' before second 'b'
```
Input: abb$
Expected: ACCEPT
Derivation: S => AA => aAA => abA => abb
Description: One 'a' before first 'b', immediate second 'b'
```

### Test Case 4: Multiple 'a's before both 'b's
```
Input: aabb$
Expected: ACCEPT
Derivation: S => AA => aAA => aaAA => aabA => aabxB => aabb
Description: Two 'a's then 'b', one 'a' then 'b'
```

### Test Case 5: Many 'a's before first 'b'
```
Input: aaab$
Expected: ACCEPT
Derivation: S => AA => aAA => aaAA => aaaAA => aaabA => aaabb
Description: Three 'a's before first 'b'
```

### Test Case 6: Longer string variant
```
Input: aaaabb$
Expected: ACCEPT
Description: Four 'a's before first 'b', one 'a' before second 'b'
```

### Test Case 7: Maximum 'a's test
```
Input: aaaaaabb$
Expected: ACCEPT
Description: Six 'a's before first 'b', one 'a' before second 'b'
```

### Test Case 8: Both 'b's adjacent
```
Input: bb$
Expected: ACCEPT
Derivation: S => AA => bA => bb
Description: No 'a's, just two 'b's
```

### Test Case 9: Second part has more 'a's
```
Input: baaa$
Expected: REJECT (wait, this should be 'baaab' to be valid)
Corrected Input: baaab$
Expected: ACCEPT
Description: No 'a' before first 'b', three 'a's before second 'b'
```

### Test Case 10: Symmetric pattern
```
Input: aaaabbbb$
Wait, this has four b's - INVALID
Corrected: aaabaaab$
Expected: ACCEPT
Description: Three 'a's before each 'b'
```

---

## ✗ INVALID TEST CASES (Should be REJECTED)

### Test Case 11: Single 'a'
```
Input: a$
Expected: REJECT
Reason: No 'b' characters (need exactly 2)
```

### Test Case 12: Single 'b'
```
Input: b$
Expected: REJECT
Reason: Only one 'b' (need exactly 2)
```

### Test Case 13: Only 'a's
```
Input: aa$
Expected: REJECT
Reason: No 'b' characters
```

### Test Case 14: Three 'b's
```
Input: bbb$
Expected: REJECT
Reason: Three 'b's instead of two
```

### Test Case 15: Alternating pattern
```
Input: abab$
Expected: REJECT
Reason: Grammar requires form A A where each A ends with 'b'
Analysis: This would need S -> AAAA or different structure
```

### Test Case 16: Reverse pattern
```
Input: ba$
Expected: REJECT
Reason: 'a' after 'b' in second A (A must be a*b form)
```

### Test Case 17: Too many 'b's with 'a's
```
Input: aabbb$
Expected: REJECT
Reason: Three 'b's total
```

### Test Case 18: Empty string
```
Input: $
Expected: REJECT
Reason: Need exactly two 'b's
```

### Test Case 19: Missing end marker
```
Input: aabb
Expected: ERROR
Reason: No $ end marker (implementation specific)
```

### Test Case 20: 'b' in middle with 'a' after
```
Input: aba$
Expected: REJECT
Reason: Only one 'b' total
```

### Test Case 21: Four 'b's
```
Input: bbbb$
Expected: REJECT
Reason: Too many 'b's
```

### Test Case 22: Random pattern
```
Input: aababa$
Expected: REJECT
Reason: Three 'b's and wrong structure
```

---

## Parsing Trace Examples

### Example 1: Input `aab$`

```
Step  Stack                          Input          Action
──────────────────────────────────────────────────────────────
1     [0]                            aab$           Shift 2
2     [0 2a]                         ab$            Shift 2
3     [0 2a 2a]                      b$             Shift 4
4     [0 2a 2a 4b]                   $              Reduce by 3: A -> b
5     [0 2a 2a 3A]                   $              Reduce by 2: A -> a A
6     [0 2a 3A]                      $              Reduce by 2: A -> a A
7     [0 3A]                         $              Shift 5
8     [0 3A 5a]                      $              ERROR (or continue based on grammar)
```

### Example 2: Input `bb$`

```
Step  Stack                          Input          Action
──────────────────────────────────────────────────────────────
1     [0]                            bb$            Shift 4
2     [0 4b]                         b$             Reduce by 3: A -> b
3     [0 3A]                         b$             Shift 5
4     [0 3A 5A]                      $              Reduce by 1: S -> A A
5     [0 1S]                         $              Accept ✓
```

---

## Conflict Analysis

### This grammar is LR(0) compatible (NO CONFLICTS)

**Why?**
1. No state has both shift and reduce actions simultaneously
2. No state has multiple reduce actions
3. The grammar structure ensures deterministic parsing decisions

### Potential Conflict Scenarios in Other Grammars

**Shift-Reduce Conflict Example:**
```
E -> E + E
E -> id
```
In state with items `E -> E + •E` and some reduction item, both shift and reduce are possible.

**Reduce-Reduce Conflict Example:**
```
A -> x
B -> x
```
Multiple reductions possible in same state with same lookahead.

---

## Post-Laboratory Test Cases

### Extended Test 1: Very long string
```
Input: aaaaaaaaaaaab$
Expected: ACCEPT
Purpose: Test parser with extended derivations
```

### Extended Test 2: Boundary case
```
Input: aaaaaaaaabbbbbbbb$
Expected: REJECT
Purpose: Test error detection with many extra 'b's
```

### Extended Test 3: Performance test
```
Input: (repeat 'a' 50 times)bb$
Expected: ACCEPT
Purpose: Test parser state management with deep recursion
```

---

## Grammar Transformation Exercise

**Non-LR(0) Grammar:**
```
S -> A a
S -> b A c
A -> A b
A -> d
```

**Suggested Transformation:**
1. Eliminate left recursion in A
2. Factor common prefixes
3. Test again with LR(0) parser

---

## Reflection Questions

1. **Why does LR(0) handle this grammar but would fail on ambiguous expression grammars?**
   - This grammar has clear reduce points (only when dot reaches end)
   - Expression grammars with multiple derivations cause conflicts

2. **How does the GOTO table enable non-terminal transitions?**
   - After reduction, GOTO determines next state based on LHS non-terminal
   - Maintains parse tree structure during bottom-up construction

3. **What makes bottom-up parsing more powerful than top-down?**
   - Handles left-recursive grammars naturally
   - Larger class of acceptable grammars (all LR languages)
   - Can delay decisions until more input is seen

---

**Testing Instructions:**
1. Compile: `gcc pr7.c -o pr7`
2. Run: `./pr7`
3. Test each case systematically
4. Record parsing traces for 5 valid and 5 invalid cases
5. Identify any unexpected behaviors
6. Document your observations

Good luck with your practical examination!
