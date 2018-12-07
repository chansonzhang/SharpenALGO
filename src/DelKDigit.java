/**
 * Copyright 2018 Zhang, Chen. All Rights Reserved.
 * <p>
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * <p>
 * http://www.apache.org/licenses/LICENSE-2.0
 * <p>
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ==============================================================================
 *
 * @Time : 12/5/2018 19:46
 * @Author : Zhang, Chen (chansonzhang)
 * @Email : ZhangChen.Shaanxi@gmail.com
 * @FileName: DelKDigit.java
 */
public class DelKDigit {
    public static int delKDigits(int number, int k, int max_or_min) {
        final int GET_MIN = 0;
        final int GET_MAX = 1;
        int[] digits = getDigits(number);
        for (int i = 0; i < k; i++) {
            int newLength = digits.length - 1;
            int[] digitsNew = new int[newLength];
            int j = 0;
            int delIndex = -1;
            switch (max_or_min) {
                case GET_MIN:
                    while (j < newLength - 1 && digits[j] <= digits[j + 1])
                        j++;
                    delIndex = j;
                    break;
                case GET_MAX:
                    while (j < newLength - 1 && digits[j] >= digits[j + 1])
                        j++;
                    delIndex = j;
                    break;
                default:
                    throw new IllegalArgumentException(
                            "max_or_in can only be either " + GET_MAX + "or " + GET_MIN + "!"
                    );
            }

            int n = 0;
            for (int m =0;m < digits.length;m++) {
                if (m != delIndex) {
                    digitsNew[n++] = digits[m];
                }
            }
            digits = digitsNew;
        }
        int result = getInt(digits);
        return result;
    }

    public static void testDelKDigits() {
        int number = 1593121212;
        int k = 3;
        int max_or_min = 0;
        int result = delKDigits(number, k, max_or_min);
        assert (result == 1121212);
        System.out.println("number: " + number);
        System.out.println("k: " + k);
        String description = "";
        if (1 == max_or_min) {
            description = "MAX";
        } else {
            description = "MIN";
        }
        System.out.print("find " + description + ": " + result);
    }

    public static int[] getDigits(int number) {
        String numberStr = String.valueOf(number);
        int len = numberStr.length();
        int[] digits = new int[len];
        for (int i = 0; i < len; i++) {
            digits[i] = Integer.parseInt(numberStr.substring(i, i + 1));
        }
        return digits;
    }

    public static int getInt(int[] digits) {
        int result = 0;
        for (int i = 0; i < digits.length; i++) {
            result = result * 10 + digits[i];
        }
        return result;
    }

    public static void testGetInt() {
        int number = 1121212;
        int[] digits = getDigits(number);
        int result = getInt(digits);
        assert (result == number);
    }

    public static void testGetDigits() {
        int number = 12345670;
        System.out.println("number: " + number);
        int[] digits = getDigits(number);
        for (int d : digits) {
            System.out.print(d + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        testDelKDigits();
    }
}
