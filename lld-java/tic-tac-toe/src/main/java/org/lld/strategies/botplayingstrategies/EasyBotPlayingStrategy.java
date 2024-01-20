package org.lld.strategies.botplayingstrategies;

import org.lld.model.Board;
import org.lld.model.Cell;
import org.lld.model.CellState;

import java.util.List;

public class EasyBotPlayingStrategy implements BotPlayingStrategy{
    @Override
    public Cell makeMove(Board board) {
        for(List<Cell> row: board.getBoard()){
            for(Cell cell: row){
                if(cell.getCellState().equals(CellState.EMPTY)){
                    return  cell;
                }
            }
        }
        return null; // ideally this is never reached
    }
}
