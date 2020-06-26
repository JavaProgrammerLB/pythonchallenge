package com.yitianyigexiangfa.pythonchallenge;

import java.text.NumberFormat;

public class Level1 {

    public static void main(String[] args) {
        Double result = Math.pow(2, 38);
        System.out.println(result);
        NumberFormat numberFormat = NumberFormat.getInstance();
        numberFormat.setGroupingUsed(false);
        String resultVal = numberFormat.format(result);
        System.out.println(resultVal);
    }


}
