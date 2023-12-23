package org.example.adapters;

import org.example.thirdParty.logger.LoggerAPI;

import java.nio.charset.StandardCharsets;

public class LoggerAdapter implements ILogger{
    private LoggerAPI logger = new LoggerAPI();
    @Override
    public void log(String message) {
        logger.printLog(message.getBytes());
    }
}
