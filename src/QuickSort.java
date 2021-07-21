/**
 * Copyright 2021 Zhang, Chen. All Rights Reserved.
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
 * @author Zhang Chen(ChansonZhang)
 * @since 2021/7/21 12:12
 */
public class QuickSort {
    public static void main(String[] args) {
        int[] a = new int[]{1, 8, 2, 4, 6, 5, 3, 9, 0, 7};
        print(a);
        quickSort(a, 0, a.length);
        print(a);
    }

    private static void quickSort(int[] arr, int start, int end) {
        //empty
        if (end - start <= 1) {
            return;
        }

        //end - start >= 2
        int pivot = arr[start];
        int i = start;
        int j = end - 1;
        while (j > i) {
            if (arr[j] >= pivot) {
                j--;
            } else {
                //arr[j] < pivot
                i++;
                int tmp = arr[j];
                arr[j] = arr[i];
                arr[i] = tmp;
            }
        }

        //j==i
        arr[start] = arr[i];
        arr[i] = pivot;
        quickSort(arr, start, i + 1);
        quickSort(arr, i + 1, end);
    }

    private static void print(int[] a) {
        for (int j : a) {
            System.out.print(j + " ");
        }
        System.out.println();
    }
}
