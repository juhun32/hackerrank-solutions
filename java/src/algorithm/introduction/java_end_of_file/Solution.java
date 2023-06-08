package algorithm.introduction.java_end_of_file;

import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            int i = 1;
            while (scanner.hasNextLine()) {
                System.out.println(String.format("%d %s", i++, scanner.nextLine()));
            }
        }
    }
}