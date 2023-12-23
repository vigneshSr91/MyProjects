package org.example.adapters;

import org.example.thirdParty.slo4j.LoggingAPI4J;

public class Slo4jAdapter implements ILogger{
    private LoggingAPI4J slo4j = new LoggingAPI4J();
    @Override
    public void log(String message) {
        slo4j.out(message);
    }
}
