package com.yitianyigexiangfa.pythonchallenge;

public class Level2 {

    public static void main(String[] args) {
        String result = makeTrans(str);
        System.out.println(result);
        String urlBase = "map";
        String url = makeTrans(urlBase);
        System.out.println(url);
    }

    public static String makeTrans(String base){
        byte[] bytes = base.getBytes();
        int len = bytes.length;
        byte[] bytes2 = new byte[len];
        for (int i = 0; i < len; i++) {
            byte b = bytes[i];
            if(!Character.isAlphabetic(b)){
                bytes2[i] = b;
            } else if(b == 'y'){
                bytes2[i] = (byte)'a';
            } else if(b == 'z'){
                bytes2[i] = (byte)'b';
            }else {
                bytes2[i] = (byte) (b + 2);
            }
        }
        String result = new String(bytes2);
        return result;
    }


    private static String str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq " +
            "ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. " +
            "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.";
}
