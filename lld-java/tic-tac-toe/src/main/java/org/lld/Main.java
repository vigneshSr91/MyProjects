package org.lld;

import org.lld.controller.GameController;
import org.lld.model.*;
import org.lld.strategies.winningstrategies.OrdenOneColumnWinningStrategy;
import org.lld.strategies.winningstrategies.OrderOneDiagonalWinningStrategy;
import org.lld.strategies.winningstrategies.OrderOneRowWinningStrategy;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Game game;

        Scanner scanner = new Scanner(System.in);


        // create a game
        GameController gameController = new GameController();

        List<Player> players = List.of(
                new Player("Vignesh", new Symbol('X'), PlayerType.HUMAN),
                new Bot("Robo", BotDifficultyLevel.EASY, new Symbol('O'))
        );
        int size = 3;
        try {
            game = gameController.createGame(
                    size,
                    players,
                    List.of(
                            new OrderOneRowWinningStrategy(size, players),
                            new OrdenOneColumnWinningStrategy(size, players),
                            new OrderOneDiagonalWinningStrategy(size, players)
                    )
            );
        }catch(Exception e){
            System.out.println("Something went wrong");
            return;
        }

        System.out.println("------------Game is starting------------");


        while (game.getGameState().equals(GameStatus.IN_PROGRESS)){
            System.out.println("This is how the board looks like");
            gameController.displayBoard(game);

            System.out.println("Do you want to undo? (y/n)");

            String input = scanner.next();

            if(input.equalsIgnoreCase("y")){
                gameController.undo(game);
            }else{
                gameController.makeMove(game);
            }

        }

        gameController.printResult(game);
    }
}