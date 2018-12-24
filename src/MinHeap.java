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
 * @Time : 12/24/2018 20:34
 * @Author : Zhang, Chen (chansonzhang)
 * @Email : ZhangChen.Shaanxi@gmail.com
 * @FileName: MinHeap.java
 */
public class MinHeap {
    private int[] elements;
    private int heapSize;

    public int[] getElements() {
        return elements;
    }

    public MinHeap(int heapSize) {
        this.heapSize = heapSize;
        elements = new int[heapSize];
    }

    public int insert(int x) {
        if (x <= elements[0]) {
            return -1; //insert failure
        }
        elements[0] = x;
        return adjustDown(0);
    }

    public int adjustDown(int currentIndex) {
        int leftIndex = leftChildIndex(currentIndex);
        int rightIndex = rightChildIndex(currentIndex);
        int minElementIndex = currentIndex;
        if (leftIndex < this.heapSize && elements[leftIndex] < elements[minElementIndex])
            minElementIndex = leftIndex;
        if (rightIndex < this.heapSize && elements[rightIndex] < elements[minElementIndex]) {
            minElementIndex = rightIndex;
        }

        if (minElementIndex != currentIndex) {
            swap(currentIndex, minElementIndex);
            return adjustDown(minElementIndex);
        } else {
            return currentIndex;
        }
    }

    private int leftChildIndex(int i) {
        return 2 * i + 1;
    }

    private int rightChildIndex(int i) {
        return 2 * i + 2;
    }

    private void swap(int i, int j) {
        int tmp = elements[i];
        elements[i] = elements[j];
        elements[j] = tmp;
    }

    public static void main(String[] args){
        int[] a={0,1,2,3,5,6,4,9,7,8};
        int k=3;
        MinHeap minHeap=new MinHeap(3);
        for(int x:a){
            minHeap.insert(x);
        }
        System.out.println("The max k numbers:");
        for(int x:minHeap.getElements()){
            System.out.print(x+" ");
        }
        System.out.println("\nThe k-th largest Number "+minHeap.getElements()[0]);

    }
}


