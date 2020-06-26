package com.yitianyigexiangfa.pythonchallenge;

import org.junit.Test;

import java.text.NumberFormat;

import static org.junit.Assert.*;

public class Level1Test {

    @Test
    public void pow(){
        Double result = Math.pow(2, 3);
        assertEquals(new Double(8), result);
    }

    @Test
    public void numberFormatTest(){
        Double d = 123456789123D;
        System.out.println(d);
        NumberFormat numberFormat = NumberFormat.getInstance();
        String dStr = numberFormat.format(d);
        assertEquals("123,456,789,123", dStr);
        numberFormat.setGroupingUsed(false);
        String dStr2 = numberFormat.format(d);
        assertEquals("123456789123", dStr2);
    }

    @Test
    public void doubleToString(){
        Double d = Math.pow(2, 38);
        System.out.println(d);
        NumberFormat numberFormat = NumberFormat.getInstance();
        numberFormat.setGroupingUsed(false);
        String numStr = numberFormat.format(d);
        System.out.println(numStr);
        assertEquals("2.74877906944E11", d.toString());
    }
}