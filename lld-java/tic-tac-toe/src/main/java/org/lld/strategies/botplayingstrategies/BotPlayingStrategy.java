package org.lld.strategies.botplayingstrategies;

import org.lld.model.Board;
import org.lld.model.Cell;

public interface BotPlayingStrategy {
    Cell makeMove(Board board);
}
