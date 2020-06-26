package com.yitianyigexiangfa.pythonchallenge;

import org.junit.Test;

import static org.junit.Assert.*;

public class Level2Test {

    @Test
    public void isAlphabetic() {
        boolean semicolonIsNotAlphabetic = Character.isAlphabetic(';');
        assertEquals(false, semicolonIsNotAlphabetic);
        boolean aIsAlphabetic = Character.isAlphabetic('a');
        assertEquals(true, aIsAlphabetic);
        boolean upperCaseAIsAlphabetic = Character.isAlphabetic('Z');
        assertEquals(true, upperCaseAIsAlphabetic);
        boolean spaceIsNotAlphabetic = Character.isAlphabetic(' ');
        assertEquals(false, spaceIsNotAlphabetic);
    }

    @Test
    public void bytesToString() {
        String s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        byte[] bytes = s.getBytes();
        for (int i = 0; i < bytes.length; i++) {
            System.out.println(bytes[i]);
        }
    }

}