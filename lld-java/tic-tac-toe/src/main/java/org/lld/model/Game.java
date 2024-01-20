package org.lld.model;

import org.lld.strategies.winningstrategies.WinningStrategy;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Game {
    private List<Player> players;
    private Board board;
    private List<Move> moves;
    private Player winner;
    private GameStatus gameState;
    private int nextMovePlayerIndex;
    private List<WinningStrategy> winningStrategies;

    private Game(List<WinningStrategy> winningStrategies, int dimension, List<Player> players){
        this.nextMovePlayerIndex = 0;
        this.winningStrategies = winningStrategies;
        this.gameState = GameStatus.IN_PROGRESS;
        this.moves = new ArrayList<>();
        this.board = new Board(dimension);
        this.players = players;
    }

    public List<Player> getPlayers() {
        return players;
    }

    public void setPlayers(List<Player> players) {
        this.players = players;
    }

    public Board getBoard() {
        return board;
    }

    public void setBoard(Board board) {
        this.board = board;
    }

    public List<Move> getMoves() {
        return moves;
    }

    public void setMoves(List<Move> moves) {
        this.moves = moves;
    }

    public Player getWinner() {
        return winner;
    }

    public void setWinner(Player winner) {
        this.winner = winner;
    }

    public GameStatus getGameState() {
        return gameState;
    }

    public void setGameState(GameStatus gameState) {
        this.gameState = gameState;
    }

    public int getNextMovePlayerIndex() {
        return nextMovePlayerIndex;
    }

    public void setNextMovePlayerIndex(int nextMovePlayerIndex) {
        this.nextMovePlayerIndex = nextMovePlayerIndex;
    }

    public List<WinningStrategy> getWinningStrategies() {
        return winningStrategies;
    }

    public void setWinningStrategies(List<WinningStrategy> winningStrategies) {
        this.winningStrategies = winningStrategies;
    }

    public void printWinner(){
        System.out.println("Winner is " + winner.getName() );
    }

    private boolean validateMove(Cell cell){
        int row = cell.getRow();
        int col = cell.getCol();

        if(row < 0 || col < 0 || row >= board.getSize() || col >= board.getSize()){
            return false;
        }

        return board.getBoard().get(row).get(col).getCellState().equals(CellState.EMPTY);
    }

    public void undo(){
        if(moves.size()==0){
            System.out.println("No moves. Can't undo.");
            return;
        }

        Move lastMove = moves.get(moves.size()-1);

        for (WinningStrategy winningStrategy: winningStrategies){
            winningStrategy.handleUndo(board, lastMove);
        }

        Cell cellInBoard = lastMove.getCell();
        cellInBoard.setCellState(CellState.EMPTY);
        cellInBoard.setPlayer(null);

        moves.remove(lastMove);

        nextMovePlayerIndex -= 1;
        nextMovePlayerIndex += players.size();
        nextMovePlayerIndex %= players.size();
    }
    public void makeMove(){

        Player currentPlayer = players.get(nextMovePlayerIndex);
        System.out.println("It is " + currentPlayer.getName() + "'s turn.");

        Cell proposedCell = currentPlayer.makeMove(board);

        System.out.println("Move made at row: " + proposedCell.getRow() +
                    " col: " + proposedCell.getCol() + ".");

        if(!validateMove(proposedCell)){
            System.out.println("Invalid move. Retry.");
            return;
        }

        Cell cellinBoard = board.getBoard().get(proposedCell.getRow()).get(proposedCell.getCol());

        cellinBoard.setCellState(CellState.FILLED);

        cellinBoard.setPlayer(currentPlayer);

        Move move = new Move(currentPlayer, cellinBoard);
        moves.add(move);

        for(WinningStrategy winningStrategy: winningStrategies){
            if(winningStrategy.checkWinner(board, move)){
                gameState = GameStatus.ENDED;
                winner = currentPlayer;
                return;
            }
        }

        if(moves.size() == board.getSize() * board.getSize()){
            gameState = GameStatus.DRAW;
            return;
        }

        nextMovePlayerIndex += 1;
        nextMovePlayerIndex %= players.size();
    }

    public void printResult(){
        GameStatus gameStatus = getGameState();
        if(gameStatus.equals(GameStatus.ENDED)){
            System.out.println("Game has ended.");
            printWinner();
        }else{
            System.out.println("Game is Draw!");
        }
    }

    public static Builder getBuilder(){
        return new Builder();
    }

    public static class Builder{
        private List<Player> players;
        private List<WinningStrategy> winningStrategies;
        private int dimension;

        private Builder(){}

        public Builder setPlayers(List<Player> players) {
            this.players = players;
            return this;
        }

        public Builder setWinningStrategies(List<WinningStrategy> winningStrategies) {
            this.winningStrategies = winningStrategies;
            return this;
        }

        public Builder setDimension(int dimension) {
            this.dimension = dimension;
            return this;
        }

        private Boolean valid(){
            if(this.players.size() < 2){
                return false;
            }

            if(this.players.size() != this.dimension-1){
                return false;
            }

            int botCount = 0;

            for(Player player : this.players){
                if(player.getPlayerType().equals(PlayerType.BOT)){
                    botCount += 1;
                }
            }

            if(botCount > 1){
                return false;
            }

            Set<Character> existingSymbols = new HashSet<>();

            for(Player player: this.players){
                if(existingSymbols.contains(player.getSymbol().getaChar())){
                    return false;
                }else{
                    existingSymbols.add(player.getSymbol().getaChar());
                }
            }

            return true;
        }

        public Game build(){
            if(!valid()){
                throw new RuntimeException("Invalid params for game");
            }
            return new Game(
                    this.winningStrategies, this.dimension, this.players
                        );
        }
    }
}
