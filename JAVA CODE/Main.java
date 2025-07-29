import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    // A large number to represent infinity for our DP states.
    static final long INF = Long.MAX_VALUE;

    /**
     * Represents the result for a given prefix of X.
     * The primary goal is to minimize 'substrings'.
     * The secondary goal is to minimize 'factor'.
     * The compareTo method implements this priority.
     */
    static class Result implements Comparable<Result> {
        long substrings;
        long factor;

        Result(long substrings, long factor) {
            this.substrings = substrings;
            this.factor = factor;
        }

        @Override
        public int compareTo(Result other) {
            if (this.substrings != other.substrings) {
                return Long.compare(this.substrings, other.substrings);
            }
            return Long.compare(this.factor, other.factor);
        }
    }

    /**
     * Suffix Automaton (SA) is a powerful data structure for string processing.
     * Here, it's used to solve the "substring existence" problem efficiently.
     * After building it on a string (e.g., Y), we can find the longest suffix
     * of any prefix of another string (X) that is a substring of Y in linear time.
     */
    static class SuffixAutomaton {
        static class State {
            int len, link;
            Map<Character, Integer> next = new HashMap<>();
        }

        ArrayList<State> states = new ArrayList<>();
        int last;

        public SuffixAutomaton() {
            states.add(new State());
            states.get(0).len = 0;
            states.get(0).link = -1;
            last = 0;
        }

        public void extend(char c) {
            int newStateIdx = states.size();
            states.add(new State());
            states.get(newStateIdx).len = states.get(last).len + 1;
            int p = last;
            while (p != -1 && !states.get(p).next.containsKey(c)) {
                states.get(p).next.put(c, newStateIdx);
                p = states.get(p).link;
            }

            if (p == -1) {
                states.get(newStateIdx).link = 0;
            } else {
                int q = states.get(p).next.get(c);
                if (states.get(q).len == states.get(p).len + 1) {
                    states.get(newStateIdx).link = q;
                } else {
                    int cloneIdx = states.size();
                    states.add(new State());
                    State cloneState = states.get(cloneIdx);
                    State qState = states.get(q);

                    cloneState.len = states.get(p).len + 1;
                    cloneState.next = new HashMap<>(qState.next);
                    cloneState.link = qState.link;

                    while (p != -1 && states.get(p).next.get(c) == q) {
                        states.get(p).next.put(c, cloneIdx);
                        p = states.get(p).link;
                    }
                    qState.link = cloneIdx;
                    states.get(newStateIdx).link = cloneIdx;
                }
            }
            last = newStateIdx;
        }

        public int[] getMaxMatchLengths(String text) {
            int[] matchLengths = new int[text.length() + 1];
            int currentNode = 0;
            int currentLen = 0;
            for (int i = 0; i < text.length(); i++) {
                char c = text.charAt(i);
                while (currentNode != 0 && !states.get(currentNode).next.containsKey(c)) {
                    currentNode = states.get(currentNode).link;
                    currentLen = states.get(currentNode).len;
                }
                if (states.get(currentNode).next.containsKey(c)) {
                    currentNode = states.get(currentNode).next.get(c);
                    currentLen++;
                }
                matchLengths[i + 1] = currentLen;
            }
            return matchLengths;
        }
    }

    /**
     * A Segment Tree is used for efficient range queries.
     * In this problem, for each position `i` in X, we need to find the best
     * result from a range of previous positions `dp[j]`. This tree allows
     * us to find the minimum `Result` object in a given range in O(log N) time.
     */
    static class SegmentTree {
        Result[] tree;
        int size;

        public SegmentTree(int n) {
            this.size = n;
            tree = new Result[4 * size];
            build(1, 0, size - 1);
        }

        private void build(int v, int tl, int tr) {
            tree[v] = new Result(INF, INF);
            if (tl != tr) {
                int tm = (tl + tr) / 2;
                build(2 * v, tl, tm);
                build(2 * v + 1, tm + 1, tr);
            }
        }

        private Result min(Result r1, Result r2) {
            return r1.compareTo(r2) < 0 ? r1 : r2;
        }

        public void update(int v, int tl, int tr, int pos, Result newVal) {
            if (tl == tr) {
                tree[v] = newVal;
            } else {
                int tm = (tl + tr) / 2;
                if (pos <= tm) {
                    update(2 * v, tl, tm, pos, newVal);
                } else {
                    update(2 * v + 1, tm + 1, tr, pos, newVal);
                }
                tree[v] = min(tree[2 * v], tree[2 * v + 1]);
            }
        }

        public Result query(int v, int tl, int tr, int l, int r) {
            if (l > r) {
                return new Result(INF, INF);
            }
            if (l == tl && r == tr) {
                return tree[v];
            }
            int tm = (tl + tr) / 2;
            Result leftRes = query(2 * v, tl, tm, l, Math.min(r, tm));
            Result rightRes = query(2 * v + 1, tm + 1, tr, Math.max(l, tm + 1), r);
            return min(leftRes, rightRes);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String X, Y;
        int S, R;

        // --- Robust Input Reading Block ---
        try {
            X = br.readLine();
            Y = br.readLine();
            String lineForSR = br.readLine();

            if (X == null || Y == null || lineForSR == null) {
                System.err.println("Error: Input ended prematurely. Expected 3 lines of input.");
                return;
            }

            StringTokenizer st = new StringTokenizer(lineForSR);
            S = Integer.parseInt(st.nextToken());
            R = Integer.parseInt(st.nextToken());

        } catch (Exception e) {
            System.err.println(
                    "Error reading input. Please ensure the input format is correct: two strings followed by a line with two space-separated integers.");
            return;
        }

        /*
         * PROBLEM INTERPRETATION:
         * The problem asks to form string X by concatenating substrings of Y.
         * The phrase "select the sub strings from Y in reversed order" is ambiguous.
         * This solution uses the standard interpretation for such problems:
         * we can use substrings from EITHER string Y OR string reverse(Y).
         * This interpretation is supported by the provided examples.
         */

        int lenX = X.length();

        // 1. Build Suffix Automata for Y and its reverse.
        SuffixAutomaton saY = new SuffixAutomaton();
        for (char c : Y.toCharArray()) {
            saY.extend(c);
        }
        String revY = new StringBuilder(Y).reverse().toString();
        SuffixAutomaton saRevY = new SuffixAutomaton();
        for (char c : revY.toCharArray()) {
            saRevY.extend(c);
        }

        // 2. Pre-calculate max match lengths for all prefixes of X.
        int[] lY = saY.getMaxMatchLengths(X);
        int[] lR = saRevY.getMaxMatchLengths(X);

        // 3. DP Setup: dp[i] stores the best result for prefix X[0...i-1].
        Result[] dp = new Result[lenX + 1];
        dp[0] = new Result(0, 0); // Base case: empty string costs nothing.

        SegmentTree segTree = new SegmentTree(lenX + 1);
        segTree.update(1, 0, lenX, 0, dp[0]);

        // 4. Main DP Loop
        for (int i = 1; i <= lenX; i++) {
            // Find best option using a substring from Y
            Result candY = new Result(INF, INF);
            int lenMatchY = lY[i];
            if (lenMatchY > 0) {
                // Find the best previous state dp[j] where X[j...i-1] is a substring of Y
                Result minDpY = segTree.query(1, 0, lenX, i - lenMatchY, i - 1);
                if (minDpY.substrings != INF) {
                    candY = new Result(minDpY.substrings + 1, minDpY.factor + S);
                }
            }

            // Find best option using a substring from reverse(Y)
            Result candR = new Result(INF, INF);
            int lenMatchR = lR[i];
            if (lenMatchR > 0) {
                // Find the best previous state dp[j] where X[j...i-1] is a substring of
                // reverse(Y)
                Result minDpR = segTree.query(1, 0, lenX, i - lenMatchR, i - 1);
                if (minDpR.substrings != INF) {
                    candR = new Result(minDpR.substrings + 1, minDpR.factor + R);
                }
            }

            // Choose the better of the two candidates for dp[i]
            dp[i] = candY.compareTo(candR) < 0 ? candY : candR;

            // If we found a valid solution for dp[i], update the segment tree
            if (dp[i].substrings != INF) {
                segTree.update(1, 0, lenX, i, dp[i]);
            }
        }

        // 5. Final Result
        Result finalResult = dp[lenX];
        if (finalResult.substrings == INF) {
            System.out.println("Impossible");
        } else {
            System.out.println(finalResult.factor);
        }
    }
}