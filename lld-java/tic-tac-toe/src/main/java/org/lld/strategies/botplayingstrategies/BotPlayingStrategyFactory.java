package org.lld.strategies.botplayingstrategies;

import org.lld.model.BotDifficultyLevel;

public class BotPlayingStrategyFactory {
    public static BotPlayingStrategy getBotPlayingStrategyForDifficultyLevel(BotDifficultyLevel difficultyLevel){
//        return switch (difficultyLevel){
//            case EASY -> new EasyBotPlayingStrategy();
//            case MEDIUM -> new MediumBotPlayingStrategy();
//            case HARD -> new HardBotPlayingStrategy();
//        };
        return new EasyBotPlayingStrategy();
    }
}
