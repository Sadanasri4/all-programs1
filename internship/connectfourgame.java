 import java.util.*;
 public class connectfourgame {
    private static final int ROWS = 6;
    private static final int COLS = 7;
    private static final char EMPTY_SLOT = ' ';
    private static final char PLAYER1 = 'X';
    private static final char PLAYER2 = 'O';

    private static char[][] board = new char[ROWS][COLS];
    
    public static void main(String[] args) {
        initializeBoard();
        printBoard();
        char currentPlayer = PLAYER1;
        
        while (true) {
            int col = getPlayerMove(currentPlayer);
            if (dropDisc(currentPlayer, col)) {
                printBoard();
                if (checkWin(currentPlayer)) {
                    System.out.println("Player " + currentPlayer + " wins!");
                    break;
                }
                currentPlayer = (currentPlayer == PLAYER1) ? PLAYER2 : PLAYER1;
            } else {
                System.out.println("Column is full! Choose another column.");
            }
        }
    }

    private static void initializeBoard() {
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                board[row][col] = EMPTY_SLOT;
            }
        }
    }

    private static void printBoard() {
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                System.out.print("|" + board[row][col]);
            }
            System.out.println("|");
        }
        System.out.println("---------------------");
    }

    private static int getPlayerMove(char player) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Player " + player + ", enter your column (0-6): ");
        return scanner.nextInt();
    }

    private static boolean dropDisc(char player, int col) {
        if (col < 0 || col >= COLS) {
            return false;
        }

        for (int row = ROWS - 1; row >= 0; row--) {
            if (board[row][col] == EMPTY_SLOT) {
                board[row][col] = player;
                return true;
            }
        }
        return false;
    }

    private static boolean checkWin(char player) {
        // Check horizontal win
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS - 3; col++) {
                if (board[row][col] == player && board[row][col + 1] == player
                        && board[row][col + 2] == player && board[row][col + 3] == player) {
                    return true;
                }
            }
        }

        // Check vertical win
        for (int col = 0; col < COLS; col++) {
            for (int row = 0; row < ROWS - 3; row++) {
                if (board[row][col] == player && board[row + 1][col] == player
                        && board[row + 2][col] == player && board[row + 3][col] == player) {
                    return true;
                }
            }
        }

        // Check ascending diagonal win
        for (int row = 3; row < ROWS; row++) {
            for (int col = 0; col < COLS - 3; col++) {
                if (board[row][col] == player && board[row - 1][col + 1] == player
                        && board[row - 2][col + 2] == player && board[row - 3][col + 3] == player) {
                    return true;
                }
            }
        }

        // Check descending diagonal win
        for (int row = 0; row < ROWS - 3; row++) {
            for (int col = 0; col < COLS - 3; col++) {
                if (board[row][col] == player && board[row + 1][col + 1] == player
                        && board[row + 2][col + 2] == player && board[row + 3][col + 3] == player) {
                    return true;
                }
            }
        }

        return false;
    }
}
