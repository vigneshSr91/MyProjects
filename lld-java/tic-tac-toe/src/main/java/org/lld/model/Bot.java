package org.lld.model;

import org.lld.strategies.botplayingstrategies.BotPlayingStrategy;
import org.lld.strategies.botplayingstrategies.BotPlayingStrategyFactory;

public class Bot extends Player{
    private BotDifficultyLevel botDifficultyLevel;

    private BotPlayingStrategy botPlayingStrategy;

    public BotDifficultyLevel getBotDifficultyLevel() {
        return botDifficultyLevel;
    }

    public void setBotDifficultyLevel(BotDifficultyLevel botDifficultyLevel) {
        this.botDifficultyLevel = botDifficultyLevel;
    }

    public Bot(String name, BotDifficultyLevel botDifficultyLevel, Symbol symbol){
        super(name, symbol, PlayerType.BOT);
        this.botDifficultyLevel = botDifficultyLevel;
        this.botPlayingStrategy = BotPlayingStrategyFactory.getBotPlayingStrategyForDifficultyLevel(botDifficultyLevel);

    }

    @Override
    public Cell makeMove(Board board) {
        return botPlayingStrategy.makeMove(board);
    }
}
