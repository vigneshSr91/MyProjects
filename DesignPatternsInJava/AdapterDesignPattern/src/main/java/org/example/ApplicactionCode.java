package org.example;

import org.example.adapters.ILogger;

public class ApplicactionCode {
    ILogger logger;

    public void applicationLog(ILogger logger){
        logger.log("Hello World!");
    }
    public static void main(String[] args) {


        System.out.println("Hello world!");

        // Many logging libraries
        // Log4j    => sendStream( )
        // Slo4j    => printLog( )
        // Logger   => out( )
    }
}