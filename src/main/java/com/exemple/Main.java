package com.exemple;

public class Main {
    public static void main(String[] args) {
        Calculatrice c = new Calculatrice();
        System.out.println("2 + 3 = " + c.additionner(2, 3));
        System.out.println("4 x 5 = " + c.multiplier(4, 5));
        System.out.println("10 / 4 = " + c.diviser(10, 4));
    }
}
