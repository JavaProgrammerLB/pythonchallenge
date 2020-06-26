package com.yitianyigexiangfa.pythonchallenge;

import org.junit.Test;

import static org.junit.Assert.*;

public class Level2Test {

    @Test
    public void charToInteger() {
        byte[] bytes = "a".getBytes();
        int digit = bytes[0];
        assertEquals(digit, 97);
        System.out.println(digit);
    }
}