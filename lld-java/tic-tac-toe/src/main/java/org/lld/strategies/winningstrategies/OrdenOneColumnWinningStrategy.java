package org.lld.strategies.winningstrategies;

import org.lld.model.Board;
import org.lld.model.Move;
import org.lld.model.Player;
import org.lld.model.Symbol;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class OrdenOneColumnWinningStrategy implements WinningStrategy {
    private List<Map<Symbol, Integer>> colMaps;

    public OrdenOneColumnWinningStrategy(int size, List<Player> players){
        colMaps = new ArrayList<>();
        for(int i=0; i < size; i++){
            colMaps.add(new HashMap<>());
            for(Player player: players){
                colMaps.get(i).put(player.getSymbol(), 0);
            }
        }
    }
    @Override
    public boolean checkWinner(Board board, Move move) {
        int row =move.getCell().getCol();
        Symbol symbol = move.getPlayer().getSymbol();
        colMaps.get(row).put(symbol, 1 + colMaps.get(row).get(symbol));

        if(colMaps.get(row).get(symbol) == board.getSize()){
            return true;
        }
        return false;
    }

    @Override
    public void handleUndo(Board board, Move move) {
        int col = move.getCell().getCol();
        Symbol symbol = move.getPlayer().getSymbol();

        colMaps.get(col).put(
                symbol,
                colMaps.get(col).get(symbol) - 1
        );

    }
}
