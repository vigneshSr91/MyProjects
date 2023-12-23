package org.example.adapters;

import org.example.thirdParty.log4j.Log4jSDK;

public class Log4jAdapter implements ILogger{
    private Log4jSDK log4j = new Log4jSDK();
    @Override
    public void log(String message) {
        log4j.sendStream(message);
    }
}
