import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static class State {
        int row;
        int col;
        int dist;

        State(int row, int col, int dist) {
            this.row = row;
            this.col = col;
            this.dist = dist;
        }
    }

    private static boolean isValid(int r, int c, int M, int N, int[][] grid, boolean[][] visited) {
        if (r < 0 || r >= M || c < 0 || c >= N) {
            return false;
        }
        if (grid[r][c] == 1) {
            return false;
        }
        if (visited[r][c]) {
            return false;
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(reader.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        int[][] grid = new int[M][N];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(reader.readLine());
            for (int j = 0; j < N; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(reader.readLine());
        int startR = Integer.parseInt(st.nextToken());
        int startC = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(reader.readLine());
        int destR = Integer.parseInt(st.nextToken());
        int destC = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(reader.readLine());
        int dx = Integer.parseInt(st.nextToken());
        int dy = Integer.parseInt(st.nextToken());

        if (grid[startR][startC] == 1 || grid[destR][destC] == 1) {
             if (startR == destR && startC == destC && grid[startR][startC] == 0) {
                System.out.println(0);
            } else {
                System.out.println(-1);
            }
            return;
        }
        
        if (startR == destR && startC == destC) {
            System.out.println(0);
            return;
        }

        Queue<State> q = new LinkedList<>();
        q.add(new State(startR, startC, 0));

        boolean[][] visited = new boolean[M][N];
        visited[startR][startC] = true;

        int[][] moves = {
            {dx, dy},
            {dy, -dx},
            {-dy, dx},
            {-dx, -dy}
        };

        while (!q.isEmpty()) {
            State current = q.poll();

            for (int[] move : moves) {
                int newR = current.row + move[0];
                int newC = current.col + move[1];
                int newDist = current.dist + 1;

                if (newR == destR && newC == destC) {
                    System.out.println(newDist);
                    return;
                }

                if (isValid(newR, newC, M, N, grid, visited)) {
                    visited[newR][newC] = true;
                    q.add(new State(newR, newC, newDist));
                }
            }
        }

        System.out.println(-1);
    }
}
