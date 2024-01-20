package org.lld.strategies.winningstrategies;

import org.lld.model.Board;
import org.lld.model.Move;

public interface WinningStrategy {
    boolean checkWinner(Board board, Move move);

    void handleUndo(Board board,Move move);
}
