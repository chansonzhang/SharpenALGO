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
 * @since 2021/7/21 10:49
 */
public class MergeSort {
    public static void main(String[] args) {
        int[] a = new int[]{1, 8, 2, 4, 6, 5, 3, 9, 0, 7};
        print(a);
        mergeSort(a, 0, a.length);
        print(a);
    }

    private static void mergeSort(int[] arr, int start, int end) {
        //empty
        if (end - start <= 1) {
            return;
        }

        //end - start >= 2
        int mid = start + (end - start) / 2;
        mergeSort(arr, start, mid);
        mergeSort(arr, mid, end);
        merge(arr, start, mid, end);
    }

    //first and second are all sorted list
    private static void merge(int[] arr, int start1, int start2, int end) {
        int pos1 = start1;
        int pos2 = start2;
        int[] tmp = new int[end - start1];
        int i = 0;
        while (pos1 < start2 && pos2 < end) {
            if (arr[pos1] <= arr[pos2]) {
                tmp[i++] = arr[pos1++];
            } else {
                //swap
                tmp[i++] = arr[pos2++];
            }
        }
        while (pos1 < start2) {
            tmp[i++] = arr[pos1++];
        }

        while (pos2 < end) {
            tmp[i++] = arr[pos2++];
        }

        int pos_t=0;
        for (int k=start1;k<end;){
            arr[k++]=tmp[pos_t++];
        }
    }

    private static void print(int[] a) {
        for (int j : a) {
            System.out.print(j + " ");
        }
        System.out.println();
    }
}
