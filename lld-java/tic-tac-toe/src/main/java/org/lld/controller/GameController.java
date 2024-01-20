package org.lld.controller;

import org.lld.model.Game;
import org.lld.model.GameStatus;
import org.lld.model.Player;
import org.lld.strategies.winningstrategies.WinningStrategy;

import java.util.List;

public class GameController {
    public Game createGame(int dimension,
                           List<Player> players,
                           List<WinningStrategy> winningStrategies){
        return Game.getBuilder()
                    .setDimension(dimension)
                    .setPlayers(players)
                    .setWinningStrategies(winningStrategies)
                    .build();
    }

    public void displayBoard(Game game){
        game.getBoard().print();
    }

    public void undo(Game game){
        game.undo();
    }

    public void makeMove(Game game){
        game.makeMove();
    }

    public GameStatus getGameStatus(Game game){
        return game.getGameState();
    }

    public void printResult(Game game){
        game.printResult();
    }
}
