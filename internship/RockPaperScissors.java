import java.util.Random;
import java.util.Scanner;

public class RockPaperScissors {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        
        String[] rps = {"rock", "paper", "scissors"};
        String computerMove;
        String playerMove;
        
        while (true) {
            System.out.println("Enter move (rock, paper, scissors). To exit the game, type \"exit\": ");
            playerMove = scanner.nextLine();
            
            if (playerMove.equals("exit")) {
                break;
            }

            if (!playerMove.equals("rock") && !playerMove.equals("paper") && !playerMove.equals("scissors")) {
                System.out.println("Invalid move, please try again.");
                continue;
            }

            int rand = random.nextInt(3);
            computerMove = rps[rand];

            System.out.println("Computer move: " + computerMove);

            if (playerMove.equals(computerMove)) {
                System.out.println("It's a tie!");
            } else if (playerMove.equals("rock")) {
                if (computerMove.equals("scissors")) {
                    System.out.println("You win!");
                } else if (computerMove.equals("paper")) {
                    System.out.println("You lose!");
                }
            } else if (playerMove.equals("paper")) {
                if (computerMove.equals("rock")) {
                    System.out.println("You win!");
                } else if (computerMove.equals("scissors")) {
                    System.out.println("You lose!");
                }
            } else if (playerMove.equals("scissors")) {
                if (computerMove.equals("paper")) {
                    System.out.println("You win!");
                } else if (computerMove.equals("rock")) {
                    System.out.println("You lose!");
                }
            }
        }
        
        scanner.close();
    }
}
