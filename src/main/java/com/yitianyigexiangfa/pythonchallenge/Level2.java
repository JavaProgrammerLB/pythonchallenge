package com.yitianyigexiangfa.pythonchallenge;

public class Level2 {

    public static void main(String[] args) {
        char[] chars = str.toCharArray();
        for (char charElment: chars) {
//             char newChar = charElment + 2;
            System.out.print(Character.toString(charElment));
            System.out.println();
            int value = Character.getNumericValue(charElment);
            System.out.print(value);
        }
    }



    private static String str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq " +
            "ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. " +
            "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.";
}
